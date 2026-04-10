#!/usr/bin/env python3
"""
OMNIA Silent Failure Gate v0.1
Validation and Intervention Engine.

Purpose
-------
1. Load a labeled sample set (JSONL).
2. Measure structural stability using the enhanced v0.1 fallback sensor.
3. Apply the intervention gate (Pass, Flag, Retry, Escalate).
4. Save results for audit and impact analysis.

Author: Massimiliano Brighindi
Project: MB-X.01 / OMNIA
"""

from __future__ import annotations

import json
import math
import os
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# Calibration v0.1
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


# --- SENSOR v0.1 UTILITIES ---

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
    return max(0.0, min(1.0, h / hmax))


def repetition_ratio(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    return max(0.0, min(1.0, 1.0 - (len(set(tokens)) / len(tokens))))


def circularity_score(text: str) -> float:
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


def field_redundancy_score(model_output: str) -> float:
    try:
        fields = json.loads(model_output)
        if not isinstance(fields, dict) or len(fields) < 2:
            return 0.0
        items = [set(tokenize_simple(str(v))) for v in fields.values() if v is not None]
        overlaps = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if not items[i] or not items[j]:
                    continue
                overlaps.append(len(items[i] & items[j]) / len(items[i] | items[j]))
        return max(overlaps) if overlaps else 0.0
    except Exception:
        return 0.0


def contradiction_hint_score(model_output: str) -> float:
    t = model_output.lower()
    risk_patterns = [
        ("healthy", ["timeout", "failed", "error", "repeated"]),
        ("ok", ["failed", "error", "not", "timeout"]),
        ("true", ["false"]),
        ("false", ["true"]),
        ("yes", ["no", "not"]),
        ("no", ["yes"]),
        ("delete_all_files", ["only", "temp"]),
    ]
    score = 0.0
    for anchor, negatives in risk_patterns:
        if anchor in t and any(n in t for n in negatives):
            score += 0.25
    return min(1.0, score)


def superficial_acceptance_check(model_output: str) -> bool:
    """
    Minimal baseline acceptance rule:
    - parseable JSON
    - top-level object is dict
    - at least one key
    """
    try:
        obj = json.loads(model_output)
        return isinstance(obj, dict) and len(obj) > 0
    except Exception:
        return False


def simple_structural_score_v01(model_output: str) -> Tuple[float, Dict[str, float]]:
    tokens = tokenize_simple(model_output)
    entropy = normalized_entropy(model_output)
    rep = repetition_ratio(tokens)
    circ = circularity_score(model_output)
    red = field_redundancy_score(model_output)
    contra = contradiction_hint_score(model_output)

    score = (
        0.20 * entropy
        + 0.20 * (1.0 - rep)
        + 0.20 * (1.0 - circ)
        + 0.20 * (1.0 - red)
        + 0.20 * (1.0 - contra)
    )

    meta = {
        "entropy": entropy,
        "repetition_ratio": rep,
        "circularity_score": circ,
        "field_redundancy_score": red,
        "contradiction_hint_score": contra,
    }
    return max(0.0, min(1.0, score)), meta


def perturb_text_v01(text: str) -> str:
    perturbed = re.sub(r"\s+", " ", text).strip()
    perturbed = re.sub(
        r"\b(stable|healthy|correct|result|failure)\b(?:\s+\1\b)+",
        r"\1",
        perturbed,
        flags=re.IGNORECASE,
    )
    return perturbed


# --- CORE GATE LOGIC ---

def fallback_measure(model_output: str) -> GateSignals:
    raw_score, raw_meta = simple_structural_score_v01(model_output)
    perturbed_output = perturb_text_v01(model_output)
    adjusted_score, pert_meta = simple_structural_score_v01(perturbed_output)

    fragility = max(0.0, raw_score - adjusted_score)
    compatibility = max(
        0.0,
        min(1.0, 1.0 - (fragility + 0.30 * pert_meta["contradiction_hint_score"]))
    )

    return GateSignals(
        compatibility=compatibility,
        irreversibility=None,
        purity=raw_score,
        fragility_drop=fragility,
        raw_score=raw_score,
        adjusted_score=adjusted_score,
        diagnostics={
            "raw": raw_meta,
            "perturbed": pert_meta,
            "perturbed_output": perturbed_output,
        },
    )


def omnia_gate(model_output: str) -> GateResult:
    baseline = superficial_acceptance_check(model_output)

    if not baseline:
        return GateResult(
            action="reject_surface",
            baseline_accept=False,
            signals=GateSignals(),
            triggered_rules=["json_parse_failed"],
            rationale="Output failed the superficial baseline acceptance rule.",
            metadata={"stage": "baseline"},
        )

    sig = fallback_measure(model_output)
    rules: List[str] = []

    if (sig.purity is not None and sig.purity < TAU_P - 0.15) or (
        sig.compatibility is not None and sig.compatibility < TAU_C - 0.15
    ):
        rules.append("strong_fragility")
        return GateResult(
            action="escalate",
            baseline_accept=True,
            signals=sig,
            triggered_rules=rules,
            rationale="Critical structural collapse detected.",
            metadata={"stage": "omnia_gate_v0.1"},
        )

    if (sig.purity is not None and sig.purity < TAU_P) or (
        sig.compatibility is not None and sig.compatibility < TAU_C
    ):
        rules.append("moderate_fragility")
        return GateResult(
            action="retry",
            baseline_accept=True,
            signals=sig,
            triggered_rules=rules,
            rationale="Significant instability detected.",
            metadata={"stage": "omnia_gate_v0.1"},
        )

    if sig.fragility_drop is not None and sig.fragility_drop > TAU_FRAGILITY_DROP:
        rules.append("mild_fragility")
        return GateResult(
            action="low_confidence_flag",
            baseline_accept=True,
            signals=sig,
            triggered_rules=rules,
            rationale="Slight structural drop under perturbation.",
            metadata={"stage": "omnia_gate_v0.1"},
        )

    return GateResult(
        action="pass",
        baseline_accept=True,
        signals=sig,
        triggered_rules=[],
        rationale="Stable structure.",
        metadata={"stage": "omnia_gate_v0.1"},
    )


# --- BATCH EXECUTION ---

def load_samples_jsonl(path: str) -> List[Dict[str, Any]]:
    samples: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                sample = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {lineno} of {path}: {e}") from e

            required = [
                "sample_id",
                "input_text",
                "model_output",
                "expected_baseline_accept",
                "expected_real_outcome",
                "expected_gate_preference",
            ]
            missing = [k for k in required if k not in sample]
            if missing:
                raise ValueError(
                    f"Missing required keys on line {lineno} of {path}: {missing}"
                )

            samples.append(sample)
    return samples


def main() -> None:
    input_path = "data/omnia_silent_failure_gate_v0_samples.jsonl"
    output_path = "data/omnia_silent_failure_gate_v0_results.jsonl"

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    samples = load_samples_jsonl(input_path)

    stats = {
        "pass": 0,
        "low_confidence_flag": 0,
        "retry": 0,
        "escalate": 0,
        "reject_surface": 0,
    }
    matches = 0
    baseline_matches = 0

    with open(output_path, "w", encoding="utf-8") as out:
        for sample in samples:
            res = omnia_gate(sample["model_output"])

            match_expected_gate = sample["expected_gate_preference"] == res.action
            match_expected_baseline = sample["expected_baseline_accept"] == res.baseline_accept

            if match_expected_gate:
                matches += 1
            if match_expected_baseline:
                baseline_matches += 1

            stats[res.action] += 1

            output_row = {
                "sample_id": sample["sample_id"],
                "input_text": sample["input_text"],
                "model_output": sample["model_output"],
                "expected_baseline_accept": sample["expected_baseline_accept"],
                "actual_baseline_accept": res.baseline_accept,
                "expected_real_outcome": sample["expected_real_outcome"],
                "expected_gate_preference": sample["expected_gate_preference"],
                "actual_gate_action": res.action,
                "match_expected_gate": match_expected_gate,
                "match_expected_baseline": match_expected_baseline,
                "triggered_rules": res.triggered_rules,
                "rationale": res.rationale,
                "signals": asdict(res.signals),
                "metadata": res.metadata,
                "notes": sample.get("notes", ""),
            }
            out.write(json.dumps(output_row, ensure_ascii=False) + "\n")

    total = len(samples)
    print("\n--- OMNIA Gate v0.1 Summary ---")
    print(f"Total processed: {total}")
    print(f"Baseline acceptance matches: {baseline_matches}/{total} ({baseline_matches / total * 100:.1f}%)")
    print(f"Gate matches expected: {matches}/{total} ({matches / total * 100:.1f}%)")
    print(f"Distribution: {stats}")
    print(f"Results saved to: {output_path}\n")


if __name__ == "__main__":
    main()