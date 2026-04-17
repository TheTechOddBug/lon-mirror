from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from omnia.lenses.base_lens import OmniabaseLens


@dataclass
class AdapterResult:
    input_text: str
    projection_mode: str
    projected_integer: int
    ob_cross_base_stability: float
    ob_representation_drift: float
    ob_base_sensitivity: float
    ob_collapse_count: int
    cross_base_fragility_warning: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "input_text": self.input_text,
            "projection_mode": self.projection_mode,
            "projected_integer": self.projected_integer,
            "ob_cross_base_stability": self.ob_cross_base_stability,
            "ob_representation_drift": self.ob_representation_drift,
            "ob_base_sensitivity": self.ob_base_sensitivity,
            "ob_collapse_count": self.ob_collapse_count,
            "cross_base_fragility_warning": self.cross_base_fragility_warning,
        }


class OmniabaseGateAdapter:
    """
    Minimal OMNIABASE -> OMNIA adapter demo.

    Purpose:
    - project candidate outputs into deterministic positive integers
    - run the OMNIABASE lens
    - emit prefixed auxiliary signals
    - raise a bounded warning flag when cross-base fragility is high

    This is a demo adapter only.
    It is not a production gate.
    """

    def __init__(
        self,
        bases: list[int] | None = None,
        collapse_threshold: float = 0.20,
        warning_stability_threshold: float = 0.72,
        warning_collapse_threshold: int = 12,
        warning_sensitivity_threshold: float = 0.40,
    ) -> None:
        self.lens = OmniabaseLens(
            bases=bases or list(range(2, 17)),
            collapse_threshold=collapse_threshold,
        )
        self.warning_stability_threshold = warning_stability_threshold
        self.warning_collapse_threshold = warning_collapse_threshold
        self.warning_sensitivity_threshold = warning_sensitivity_threshold

    def evaluate_text(self, text: str) -> AdapterResult:
        if not isinstance(text, str):
            raise TypeError("text must be a string.")

        stripped = text.strip()
        if not stripped:
            raise ValueError("text must not be empty.")

        projection_mode, projected_integer = self._project_text_to_integer(stripped)
        lens_result = self.lens.evaluate(projected_integer)

        warning = self._should_raise_warning(
            stability=lens_result.cross_base_stability,
            collapse_count=lens_result.collapse_count,
            sensitivity=lens_result.base_sensitivity,
        )

        return AdapterResult(
            input_text=text,
            projection_mode=projection_mode,
            projected_integer=projected_integer,
            ob_cross_base_stability=lens_result.cross_base_stability,
            ob_representation_drift=lens_result.representation_drift,
            ob_base_sensitivity=lens_result.base_sensitivity,
            ob_collapse_count=lens_result.collapse_count,
            cross_base_fragility_warning=warning,
        )

    def _project_text_to_integer(self, text: str) -> tuple[str, int]:
        numeric = self._extract_numeric_answer(text)
        if numeric is not None:
            return "direct_numeric", numeric

        return "weighted_char_sum", self._weighted_char_sum_projection(text)

    @staticmethod
    def _extract_numeric_answer(text: str) -> int | None:
        """
        Extract the last clean integer-like token from text.
        This is a bounded heuristic for demo purposes.
        """
        matches = re.findall(r"-?\d+", text)
        if not matches:
            return None

        value = abs(int(matches[-1]))
        if value == 0:
            value = 1
        return value

    @staticmethod
    def _weighted_char_sum_projection(text: str) -> int:
        """
        Deterministic fallback projection from text to positive integer.
        """
        total = 0
        for i, ch in enumerate(text, start=1):
            total += i * ord(ch)

        return max(1, total)

    def _should_raise_warning(
        self,
        stability: float,
        collapse_count: int,
        sensitivity: float,
    ) -> bool:
        return (
            stability < self.warning_stability_threshold
            or collapse_count >= self.warning_collapse_threshold
            or sensitivity >= self.warning_sensitivity_threshold
        )


def main() -> None:
    adapter = OmniabaseGateAdapter()

    candidates = [
        "The final answer is 42.",
        "111111",
        "The result appears consistent across all steps.",
        "After recomputing carefully, the answer is 104729.",
        "aaaaaaaaaaaaaaaa",
        "The system reports score 1024 with no visible issue.",
    ]

    results = [adapter.evaluate_text(text).to_dict() for text in candidates]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()