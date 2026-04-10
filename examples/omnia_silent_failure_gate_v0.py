#!/usr/bin/env python3
"""
OMNIA Silent Failure Gate v0
Minimal post-hoc intervention gate.

Purpose
-------
Take an LLM output that may look superficially acceptable and emit a bounded
intervention action based on OMNIA-style structural signals.

This script does NOT:
- improve the model
- perform semantic reasoning
- decide truth

It only:
- measures available structural signals
- applies a small rule-based gate
- returns a bounded intervention action

Author: Massimiliano Brighindi
Project: MB-X.01 / OMNIA
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple


TAU_P = 0.70
TAU_C = 0.60
TAU_FRAGILITY_DROP = 0.12


@dataclass
class GateSignals:
    compatibility: Optional[float] = None
    irreversibility: Optional[float] = None
    purity: Optional[float] = None
    fragility_drop: Optional[float] = None
    raw_score: Optional[float] = None
    adjusted_score: Optional[float] = None


@dataclass
class GateResult:
    action: str
    baseline_accept: bool
    signals: GateSignals
    triggered_rules: List[str] = field(default_factory=list)
    rationale: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def superficial_acceptance_check(model_output: str) -> bool:
    """
    Minimal baseline acceptance rule for v0.

    Baseline accepts output if:
    - it is parseable JSON
    - top-level object is a dict
    - it has at least one key
    """
    try:
        obj = json.loads(model_output)
        return isinstance(obj, dict) and len(obj) > 0
    except Exception:
        return False


def perturb_text_minimal(text: str) -> str:
    """
    Minimal mechanical perturbation.
    This is intentionally non-semantic and low-risk.

    Operations:
    - normalize repeated spaces
    - swap order of some adjacent JSON-like key-value lines if multiline
    - slightly alter formatting punctuation spacing
    """
    perturbed = text

    # normalize spaces
    perturbed = re.sub(r"\s+", " ", perturbed).strip()

    # if JSON-like string contains commas followed by spaces, normalize them
    perturbed = re.sub(r",\s*", ", ", perturbed)
    perturbed = re.sub(r":\s*", ": ", perturbed)

    return perturbed


def normalized_entropy(text: str) -> float:
    if not text:
        return 0.0
    counts: Dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    total = len(text)
    probs = [c / total for c in counts.values()]
    h = -sum(p * math.log2(p) for p in probs if p > 0)
    hmax = math.log2(len(counts)) if len(counts) > 1 else 1.0
    if hmax <= 0:
        return 0.0
    return max(0.0, min(1.0, h / hmax))


def simple_structural_score(text: str) -> float:
    """
    Transparent fallback structural proxy.

    This is NOT the full OMNIA engine.
    It is only a minimal v0 fallback if no adapter integration is active.
    """
    if not text:
        return 0.0

    entropy = normalized_entropy(text)
    length_penalty = min(len(text) / 500.0, 1.0)

    braces_balance = 1.0
    if text.count("{") != text.count("}"):
        braces_balance = 0.5

    quote_balance = 1.0
    if text.count('"') % 2 != 0:
        quote_balance = 0.5

    colon_count = text.count(":")
    comma_count = text.count(",")

    structure_hint = 0.0
    if colon_count > 0:
        structure_hint += 0.5
    if comma_count > 0:
        structure_hint += 0.3
    structure_hint = min(structure_hint, 1.0)

    score = (
        0.35 * entropy
        + 0.20 * length_penalty
        + 0.20 * braces_balance
        + 0.10 * quote_balance
        + 0.15 * structure_hint
    )
    return max(0.0, min(1.0, score))


def fallback_measure(input_text: str, model_output: str) -> GateSignals:
    """
    Minimal fallback measurement when no explicit OMNIA adapter is wired in.

    Interpretation:
    - purity ~ internal structural coherence of the output
    - compatibility ~ stability under minimal perturbation
    - irreversibility kept None in v0 fallback unless a real upstream signal exists
    """
    raw_score = simple_structural_score(model_output)
    perturbed_output = perturb_text_minimal(model_output)
    perturbed_score = simple_structural_score(perturbed_output)

    fragility_drop = max(0.0, raw_score - perturbed_score)
    compatibility = max(0.0, min(1.0, 1.0 - fragility_drop))
    purity = raw_score

    return GateSignals(
        compatibility=compatibility,
        irreversibility=None,
        purity=purity,
        fragility_drop=fragility_drop,
        raw_score=raw_score,
        adjusted_score=perturbed_score,
    )


def omnia_gate(
    input_text: str,
    model_output: str,
    tau_p: float = TAU_P,
    tau_c: float = TAU_C,
    tau_fragility_drop: float = TAU_FRAGILITY_DROP,
) -> GateResult:
    """
    Minimal v0 gate.

    Flow:
    1. baseline acceptance
    2. fallback structural measurement
    3. bounded intervention rule
    """
    baseline_accept = superficial_acceptance_check(model_output)

    if not baseline_accept:
        return GateResult(
            action="reject_surface",
            baseline_accept=False,
            signals=GateSignals(),
            triggered_rules=["surface_acceptance_failed"],
            rationale="Output failed the superficial baseline acceptance rule.",
            metadata={"stage": "baseline"},
        )

    signals = fallback_measure(input_text=input_text, model_output=model_output)
    triggered_rules: List[str] = []

    p = signals.purity
    c = signals.compatibility
    f = signals.fragility_drop

    # Strong intervention
    if (p is not None and p < tau_p - 0.15) or (c is not None and c < tau_c - 0.15):
        if p is not None and p < tau_p - 0.15:
            triggered_rules.append("purity_strong_drop")
        if c is not None and c < tau_c - 0.15:
            triggered_rules.append("compatibility_strong_drop")
        return GateResult(
            action="escalate",
            baseline_accept=True,
            signals=signals,
            triggered_rules=triggered_rules,
            rationale="Strong structural fragility detected. Output should not be trusted without higher-control review.",
            metadata={"stage": "omnia_gate_v0"},
        )

    # Medium intervention
    if (p is not None and p < tau_p) or (c is not None and c < tau_c):
        if p is not None and p < tau_p:
            triggered_rules.append("purity_below_threshold")
        if c is not None and c < tau_c:
            triggered_rules.append("compatibility_below_threshold")
        return GateResult(
            action="retry",
            baseline_accept=True,
            signals=signals,
            triggered_rules=triggered_rules,
            rationale="Moderate structural fragility detected. Retry recommended before acceptance.",
            metadata={"stage": "omnia_gate_v0"},
        )

    # Mild intervention
    if f is not None and f > tau_fragility_drop:
        triggered_rules.append("fragility_drop_above_threshold")
        return GateResult(
            action="low_confidence_flag",
            baseline_accept=True,
            signals=signals,
            triggered_rules=triggered_rules,
            rationale="Surface acceptance passed, but structural stability drops under perturbation.",
            metadata={"stage": "omnia_gate_v0"},
        )

    return GateResult(
        action="pass",
        baseline_accept=True,
        signals=signals,
        triggered_rules=[],
        rationale="No structural fragility strong enough to trigger intervention in v0.",
        metadata={"stage": "omnia_gate_v0"},
    )


def demo_samples() -> List[Tuple[str, str, str]]:
    """
    Small built-in demo set for smoke testing.
    Tuple = (sample_id, input_text, model_output)
    """
    return [
        (
            "solid_correct_like",
            "Return a JSON object with keys answer and rationale.",
            '{"answer": "4", "rationale": "2+2=4"}',
        ),
        (
            "fragile_but_surface_valid",
            "Return a JSON object with keys answer and rationale.",
            '{"answer":"4","rationale":"2+2 is 4 because 2 and 2 make sense, therefore maybe always 4"}',
        ),
        (
            "surface_valid_but_unstable",
            "Return a JSON object with keys status and explanation.",
            '{"status":"ok","explanation":"The process is stable stable stable stable stable stable stable"}',
        ),
        (
            "surface_invalid",
            "Return a JSON object with keys answer and rationale.",
            '{"answer": "4", "rationale": "2+2=4"',
        ),
    ]


def main() -> None:
    rows = []
    for sample_id, input_text, model_output in demo_samples():
        result = omnia_gate(input_text=input_text, model_output=model_output)
        rows.append(
            {
                "sample_id": sample_id,
                "input_text": input_text,
                "model_output": model_output,
                "result": asdict(result),
            }
        )

    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()