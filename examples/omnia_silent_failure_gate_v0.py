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


TAU_P = 0.78
TAU_C = 0.88
TAU_FRAGILITY_DROP = 0.04


@dataclass
class GateSignals:
    compatibility: Optional[float] = None
    irreversibility: Optional[float] = None
    purity: Optional[float] = None
    fragility_drop: Optional[float] = None
    raw_score: Optional[float] = None
    adjusted_score: Optional[float] = None
    diagnostics: Dict[str, Any] = field(default_factory=dict)


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


def tokenize_simple(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9_ ]+", " ", text)
    return [t for t in text.split() if t]


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


def repetition_ratio(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    unique = len(set(tokens))
    return max(0.0, min(1.0, 1.0 - (unique / len(tokens))))


def max_token_run_ratio(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    best = 1
    cur = 1
    for i in range(1, len(tokens)):
        if tokens[i] == tokens[i - 1]:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best / len(tokens)


def circularity_score(text: str) -> float:
    """
    Very simple structural circularity detector.
    Not semantic. Only catches cheap self-justification patterns.
    """
    t = text.lower()

    patterns = [
        r"\bbecause it is\b",
        r"\btrue because true\b",
        r"\bcorrect because correct\b",
        r"\bprime because it is prime\b",
        r"\bhealthy because .* healthy\b",
        r"\bfailure looks like failure\b",
        r"\btherefore .* is the result of .*",
    ]

    hits = sum(1 for p in patterns if re.search(p, t))
    return min(1.0, hits / 2.0)


def extract_json_fields(model_output: str) -> Dict[str, Any]:
    try:
        obj = json.loads(model_output)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    return {}


def field_redundancy_score(fields: Dict[str, Any]) -> float:
    """
    Detects when multiple fields carry almost the same text
    or when rationale/explanation mostly restates answer/status/action.
    """
    if not fields:
        return 0.0

    text_fields = {
        k: str(v).strip().lower()
        for k, v in fields.items()
        if isinstance(v, (str, int, float, bool))
    }
    if len(text_fields) < 2:
        return 0.0

    items = list(text_fields.items())
    overlaps = []

    for i in range(len(items)):
        _, vi = items[i]
        ti = set(tokenize_simple(vi))
        if not ti:
            continue
        for j in range(i + 1, len(items)):
            _, vj = items[j]
            tj = set(tokenize_simple(vj))
            if not tj:
                continue
            jacc = len(ti & tj) / max(1, len(ti | tj))
            overlaps.append(jacc)

    return max(overlaps) if overlaps else 0.0


def contradiction_hint_score(fields: Dict[str, Any]) -> float:
    """
    Very small mechanical mismatch detector for obvious risky contradictions.
    No deep semantics. Only catches crude tension patterns.
    """
    if not fields:
        return 0.0

    normalized = {k.lower(): str(v).lower() for k, v in fields.items()}
    joined = " | ".join(f"{k}:{v}" for k, v in normalized.items())

    risk_patterns = [
        ("healthy", ["timeout", "failed", "error", "repeated"]),
        ("ok", ["timeout", "failed", "error", "not"]),
        ("true", ["false"]),
        ("false", ["true"]),
        ("yes", ["not", "no"]),
        ("no", ["yes"]),
        ("delete_all_files", ["only", "temp"]),
    ]

    score = 0.0
    for anchor, negatives in risk_patterns:
        if anchor in joined:
            for neg in negatives:
                if neg in joined:
                    score += 0.25

    return min(1.0, score)


def punctuation_instability_score(text: str) -> float:
    if not text:
        return 0.0
    weird = 0
    weird += abs(text.count("{") - text.count("}"))
    weird += abs(text.count("[") - text.count("]"))
    weird += text.count(",,")
    weird += text.count("::")
    weird += text.count('""')
    return min(1.0, weird / 5.0)


def simple_structural_score_v01(model_output: str) -> Tuple[float, Dict[str, float]]:
    """
    Stronger fallback score for Silent Failure Gate v0.1.
    Still mechanical, still not semantic.
    """
    fields = extract_json_fields(model_output)
    tokens = tokenize_simple(model_output)

    entropy = normalized_entropy(model_output)
    rep_ratio = repetition_ratio(tokens)
    run_ratio = max_token_run_ratio(tokens)
    circ = circularity_score(model_output)
    redundancy = field_redundancy_score(fields)
    contradiction = contradiction_hint_score(fields)
    punct_instability = punctuation_instability_score(model_output)

    braces_balance = 1.0 if model_output.count("{") == model_output.count("}") else 0.4
    quote_balance = 1.0 if model_output.count('"') % 2 == 0 else 0.4
    parse_bonus = 1.0 if superficial_acceptance_check(model_output) else 0.0

    score = (
        0.16 * entropy
        + 0.12 * braces_balance
        + 0.10 * quote_balance
        + 0.12 * parse_bonus
        + 0.10 * (1.0 - rep_ratio)
        + 0.10 * (1.0 - run_ratio)
        + 0.10 * (1.0 - circ)
        + 0.10 * (1.0 - redundancy)
        + 0.10 * (1.0 - contradiction)
    ) - 0.10 * punct_instability

    score = max(0.0, min(1.0, score))

    meta = {
        "entropy": entropy,
        "repetition_ratio": rep_ratio,
        "max_token_run_ratio": run_ratio,
        "circularity_score": circ,
        "field_redundancy_score": redundancy,
        "contradiction_hint_score": contradiction,
        "punctuation_instability_score": punct_instability,
        "braces_balance": braces_balance,
        "quote_balance": quote_balance,
        "parse_bonus": parse_bonus,
    }
    return score, meta


def perturb_text_minimal_v01(text: str) -> str:
    """
    Slightly harder but still mechanical perturbation.
    """
    perturbed = text

    perturbed = re.sub(r"\s+", " ", perturbed).strip()
    perturbed = re.sub(r",\s*", ", ", perturbed)
    perturbed = re.sub(r":\s*", ": ", perturbed)

    perturbed = re.sub(
        r"\b(stable|healthy|correct|result|failure)\b(?:\s+\1\b)+",
        r"\1",
        perturbed,
        flags=re.IGNORECASE,
    )

    words = perturbed.split()
    out: List[str] = []
    seen_trigrams = set()
    for i in range(len(words)):
        tri = tuple(words[i:i + 3]) if i + 2 < len(words) else None
        if tri and tri in seen_trigrams:
            continue
        if tri:
            seen_trigrams.add(tri)
        out.append(words[i])

    return " ".join(out)


def fallback_measure(input_text: str, model_output: str) -> GateSignals:
    raw_score, raw_meta = simple_structural_score_v01(model_output)
    perturbed_output = perturb_text_minimal_v01(model_output)
    adjusted_score, pert_meta = simple_structural_score_v01(perturbed_output)

    fragility_drop = max(0.0, raw_score - adjusted_score)
    compatibility = max(
        0.0,
        min(1.0, 1.0 - (fragility_drop + 0.35 * pert_meta["contradiction_hint_score"]))
    )
    purity = raw_score

    return GateSignals(
        compatibility=compatibility,
        irreversibility=None,
        purity=purity,
        fragility_drop=fragility_drop,
        raw_score=raw_score,
        adjusted_score=adjusted_score,
        diagnostics={
            "raw_meta": raw_meta,
            "perturbed_meta": pert_meta,
            "perturbed_output": perturbed_output,
        },
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