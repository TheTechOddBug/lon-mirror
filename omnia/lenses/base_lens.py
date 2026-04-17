from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev
from typing import Any


@dataclass
class BaseProfile:
    base: int
    digit_length: int
    digit_sum: int
    digit_mean: float
    digit_std: float
    unique_digits: int
    transition_count: int
    transition_ratio: float
    max_run_length: int
    repeat_ratio: float


@dataclass
class BaseLensResult:
    input_value: int
    tested_bases: list[int]
    profiles: list[BaseProfile]
    cross_base_stability: float
    representation_drift: float
    base_sensitivity: float
    collapse_count: int
    collapse_threshold: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "input_value": self.input_value,
            "tested_bases": self.tested_bases,
            "profiles": [
                {
                    "base": p.base,
                    "digit_length": p.digit_length,
                    "digit_sum": p.digit_sum,
                    "digit_mean": p.digit_mean,
                    "digit_std": p.digit_std,
                    "unique_digits": p.unique_digits,
                    "transition_count": p.transition_count,
                    "transition_ratio": p.transition_ratio,
                    "max_run_length": p.max_run_length,
                    "repeat_ratio": p.repeat_ratio,
                }
                for p in self.profiles
            ],
            "cross_base_stability": self.cross_base_stability,
            "representation_drift": self.representation_drift,
            "base_sensitivity": self.base_sensitivity,
            "collapse_count": self.collapse_count,
            "collapse_threshold": self.collapse_threshold,
        }


class OmniabaseLens:
    """
    Minimal OMNIABASE lens for OMNIA.

    Scope:
    - deterministic
    - non-semantic
    - representation-focused
    - bounded diagnostics only

    Input:
    - positive integer

    Output:
    - cross_base_stability
    - representation_drift
    - base_sensitivity
    - collapse_count
    """

    def __init__(
        self,
        bases: list[int] | None = None,
        collapse_threshold: float = 0.20,
    ) -> None:
        self.bases = bases or list(range(2, 17))
        self.collapse_threshold = collapse_threshold

        if len(self.bases) < 2:
            raise ValueError("At least two bases are required.")

        if any(b < 2 for b in self.bases):
            raise ValueError("All bases must be >= 2.")

        if not (0.0 <= self.collapse_threshold <= 1.0):
            raise ValueError("collapse_threshold must be in [0, 1].")

    def evaluate(self, value: int) -> BaseLensResult:
        if not isinstance(value, int):
            raise TypeError("value must be an integer.")

        if value <= 0:
            raise ValueError("value must be a positive integer.")

        profiles = [self._profile_for_base(value, base) for base in self.bases]
        vectors = [self._profile_vector(profile) for profile in profiles]

        centroid = self._centroid(vectors)
        distances = [self._normalized_distance(vec, centroid) for vec in vectors]

        representation_drift = mean(distances)
        cross_base_stability = max(0.0, 1.0 - representation_drift)

        # Base sensitivity:
        # how unevenly the deviation is distributed across bases.
        #
        # Interpretation:
        # - higher value: instability is concentrated in a subset of bases
        # - lower value: drift is more evenly distributed across bases
        #
        # Implementation:
        # coefficient of variation over per-base distances,
        # then smoothly mapped into [0, 1).
        if len(distances) < 2:
            base_sensitivity = 0.0
        else:
            distance_mean = mean(distances)
            distance_std = pstdev(distances)

            if distance_mean == 0.0:
                base_sensitivity = 0.0
            else:
                cv = distance_std / (distance_mean + 1e-12)
                base_sensitivity = cv / (1.0 + cv)

        collapse_count = sum(1 for d in distances if d > self.collapse_threshold)

        return BaseLensResult(
            input_value=value,
            tested_bases=list(self.bases),
            profiles=profiles,
            cross_base_stability=round(cross_base_stability, 6),
            representation_drift=round(representation_drift, 6),
            base_sensitivity=round(base_sensitivity, 6),
            collapse_count=collapse_count,
            collapse_threshold=self.collapse_threshold,
        )

    def _profile_for_base(self, value: int, base: int) -> BaseProfile:
        digits = self._to_base_digits(value, base)

        digit_length = len(digits)
        digit_sum = sum(digits)
        digit_mean = mean(digits)
        digit_std = pstdev(digits) if len(digits) > 1 else 0.0
        unique_digits = len(set(digits))

        transitions = sum(1 for i in range(1, len(digits)) if digits[i] != digits[i - 1])
        transition_count = transitions
        transition_ratio = transitions / max(1, len(digits) - 1)

        max_run_length = self._max_run_length(digits)
        repeat_ratio = 1.0 - (unique_digits / max(1, digit_length))

        return BaseProfile(
            base=base,
            digit_length=digit_length,
            digit_sum=digit_sum,
            digit_mean=round(digit_mean, 6),
            digit_std=round(digit_std, 6),
            unique_digits=unique_digits,
            transition_count=transition_count,
            transition_ratio=round(transition_ratio, 6),
            max_run_length=max_run_length,
            repeat_ratio=round(repeat_ratio, 6),
        )

    @staticmethod
    def _to_base_digits(value: int, base: int) -> list[int]:
        if value == 0:
            return [0]

        digits: list[int] = []
        n = value
        while n > 0:
            digits.append(n % base)
            n //= base

        return list(reversed(digits))

    @staticmethod
    def _max_run_length(digits: list[int]) -> int:
        if not digits:
            return 0

        best = 1
        current = 1

        for i in range(1, len(digits)):
            if digits[i] == digits[i - 1]:
                current += 1
                if current > best:
                    best = current
            else:
                current = 1

        return best

    @staticmethod
    def _profile_vector(profile: BaseProfile) -> list[float]:
        return [
            float(profile.digit_length),
            float(profile.digit_sum),
            float(profile.digit_mean),
            float(profile.digit_std),
            float(profile.unique_digits),
            float(profile.transition_count),
            float(profile.transition_ratio),
            float(profile.max_run_length),
            float(profile.repeat_ratio),
        ]

    @staticmethod
    def _centroid(vectors: list[list[float]]) -> list[float]:
        if not vectors:
            raise ValueError("vectors must not be empty.")

        return [mean(values) for values in zip(*vectors)]

    @staticmethod
    def _normalized_distance(vec: list[float], centroid: list[float]) -> float:
        """
        Normalized mean relative distance from the cross-base centroid.

        Lower value:
        - more profile consistency across bases

        Higher value:
        - stronger representation drift across bases
        """
        parts: list[float] = []

        for x, c in zip(vec, centroid):
            denom = abs(c) + 1.0
            parts.append(abs(x - c) / denom)

        return mean(parts)