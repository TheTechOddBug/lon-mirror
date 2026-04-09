#!/usr/bin/env python3
"""
OMNIA - dO Mini Validation Benchmark v0

Reads:
    examples/do_mini_validation_pairs_v0.jsonl

Computes:
    - structural signature sigma(S)
    - primitive signature distance d_sigma
    - Delta_Omega(S1, S2) approximated over a minimal admissible transform set
    - kappa = 1 - Delta_Omega
    - predicted zone
    - pass/fail against expected zone

Writes:
    examples/do_mini_validation_results_v0.jsonl

Important:
This is a bootstrap runner for OMNIA State Distance Foundation v0.1.
It is not a universal validator.
It is a minimal falsifiable check.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent
INPUT_PATH = ROOT / "do_mini_validation_pairs_v0.jsonl"
OUTPUT_PATH = ROOT / "do_mini_validation_results_v0.jsonl"


# ---------------------------------------------------------------------
# Canonical weights v0.1
# ---------------------------------------------------------------------

W_OMEGA = 0.30
W_OMEGA_VARIANCE = 0.15
W_SEI = 0.20
W_DRIFT = 0.15
W_DRIFT_VECTOR = 0.10
W_ORDER_SENSITIVITY = 0.10

WEIGHT_SUM = (
    W_OMEGA
    + W_OMEGA_VARIANCE
    + W_SEI
    + W_DRIFT
    + W_DRIFT_VECTOR
    + W_ORDER_SENSITIVITY
)
if not math.isclose(WEIGHT_SUM, 1.0, rel_tol=1e-9, abs_tol=1e-9):
    raise ValueError(f"Canonical weights must sum to 1.0, got {WEIGHT_SUM}")


# ---------------------------------------------------------------------
# Thresholds v0.1
# ---------------------------------------------------------------------

EPSILON_EQ = 0.10
EPSILON_BREAK = 0.35


# ---------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------

@dataclass
class StructuralSignature:
    omega: float
    omega_variance: float
    sei: float
    drift: float
    drift_vector: float
    order_sensitivity: float


@dataclass
class ValidationResult:
    pair_id: str
    family: str
    state_1: str
    state_2: str
    expected_zone: str
    predicted_zone: str
    pass_fail: str
    delta_omega: float
    kappa: float
    best_transform: str
    sigma_1: Dict[str, float]
    sigma_2_best: Dict[str, float]
    notes: str


# ---------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def variance(values: List[float]) -> float:
    if not values:
        return 0.0
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def safe_div(n: float, d: float) -> float:
    return n / d if d != 0 else 0.0


def normalize_text_basic(s: str) -> str:
    return s.strip()


def normalize_text_soft(s: str) -> str:
    """
    Representation-preserving normalization used only as admissible transform.
    This is intentionally shallow and deterministic.
    """
    s = s.lower().strip()
    s = re.sub(r"\s+", "", s)
    s = s.replace("[", "").replace("]", "")
    s = s.replace("|", ",")
    return s


def tokenize_chars(s: str) -> List[str]:
    return list(s)


def digit_tokens(s: str) -> List[str]:
    return re.findall(r"\d", s)


def alpha_tokens(s: str) -> List[str]:
    return re.findall(r"[a-zA-Z]", s)


def parse_numeric_sequence_if_possible(s: str) -> List[float]:
    nums = re.findall(r"-?\d+(?:\.\d+)?", s)
    return [float(x) for x in nums] if nums else []


def shannon_entropy(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    counts: Dict[str, int] = {}
    for t in tokens:
        counts[t] = counts.get(t, 0) + 1
    total = len(tokens)
    ent = 0.0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    # normalize by max entropy log2(n_unique) when possible
    max_ent = math.log2(len(counts)) if len(counts) > 1 else 1.0
    return clamp01(safe_div(ent, max_ent))


def unique_ratio(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    return clamp01(len(set(tokens)) / len(tokens))


def adjacent_change_ratio(tokens: List[str]) -> float:
    """
    Measures local variability / directional change.
    """
    if len(tokens) < 2:
        return 0.0
    changes = sum(1 for i in range(len(tokens) - 1) if tokens[i] != tokens[i + 1])
    return clamp01(changes / (len(tokens) - 1))


def sequence_order_sensitivity(tokens: List[str]) -> float:
    """
    Simple proxy:
    compares token sequence to sorted sequence.
    High value means the current order differs strongly from sorted order.
    """
    if len(tokens) < 2:
        return 0.0
    sorted_tokens = sorted(tokens)
    mismatches = sum(1 for a, b in zip(tokens, sorted_tokens) if a != b)
    return clamp01(mismatches / len(tokens))


def numeric_drift_vector(nums: List[float]) -> float:
    """
    Directional proxy for numeric sequences.
    Uses signed trend normalized to [0,1].
    0.5 means neutral / unavailable.
    """
    if len(nums) < 2:
        return 0.5
    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    total_abs = sum(abs(x) for x in diffs)
    if total_abs == 0:
        return 0.5
    signed = sum(diffs)
    # map [-1, 1] to [0, 1]
    trend = signed / total_abs
    return clamp01((trend + 1.0) / 2.0)


def symbolic_drift_vector(tokens: List[str]) -> float:
    """
    Symbolic fallback.
    Uses the balance of "upward" vs "downward" lexicographic transitions.
    Returns [0,1], 0.5 neutral.
    """
    if len(tokens) < 2:
        return 0.5
    up = 0
    down = 0
    for a, b in zip(tokens[:-1], tokens[1:]):
        if a < b:
            up += 1
        elif a > b:
            down += 1
    total = up + down
    if total == 0:
        return 0.5
    trend = (up - down) / total
    return clamp01((trend + 1.0) / 2.0)


def l1_distance(a: float, b: float) -> float:
    return abs(a - b)


# ---------------------------------------------------------------------
# Signature extraction
# ---------------------------------------------------------------------

def structural_signature(state: str) -> StructuralSignature:
    """
    Bootstrap sigma(S).

    This is intentionally simple.
    It must be replaced later by native OMNIA signature extraction
    if/when integrated into the real engine.
    """
    s = normalize_text_basic(state)
    chars = tokenize_chars(s)
    alphas = alpha_tokens(s)
    nums = parse_numeric_sequence_if_possible(s)

    working_tokens: List[str]
    if nums:
        working_tokens = [str(int(x)) if x.is_integer() else str(x) for x in nums]
    elif alphas:
        working_tokens = [x.lower() for x in alphas]
    else:
        working_tokens = [c for c in chars if not c.isspace()]

    # omega: use pattern compactness + redundancy balance
    # high coherence for repeated / consistent structured patterns
    # low coherence for noisy heterogeneous patterns
    ent = shannon_entropy(working_tokens)
    uniq = unique_ratio(working_tokens)
    rep = 1.0 - uniq
    omega = clamp01(0.55 * rep + 0.45 * (1.0 - ent))

    # omega_variance: local irregularity proxy
    omega_variance = clamp01(adjacent_change_ratio(working_tokens))

    # sei: residual structure capacity
    # high when there is nontrivial pattern without total collapse into noise
    sei = clamp01(1.0 - abs(ent - 0.5) * 2.0)

    # drift: accumulated local deviation
    drift = clamp01(adjacent_change_ratio(working_tokens))

    # drift_vector
    drift_vector = (
        numeric_drift_vector(nums) if nums else symbolic_drift_vector(working_tokens)
    )

    # order sensitivity
    order_sensitivity = clamp01(sequence_order_sensitivity(working_tokens))

    return StructuralSignature(
        omega=omega,
        omega_variance=omega_variance,
        sei=sei,
        drift=drift,
        drift_vector=drift_vector,
        order_sensitivity=order_sensitivity,
    )


# ---------------------------------------------------------------------
# Admissible transforms G_v0.1
# ---------------------------------------------------------------------

def transform_identity(s: str) -> str:
    return s


def transform_permutation(s: str) -> str:
    """
    Deterministic permutation proxy:
    sort alphanumeric content but preserve coarse representation when possible.
    """
    nums = parse_numeric_sequence_if_possible(s)
    if nums:
        nums_sorted = sorted(nums)
        rendered = ",".join(
            str(int(x)) if float(x).is_integer() else str(x) for x in nums_sorted
        )
        return rendered

    chars = [c.lower() for c in s if c.isalnum()]
    return "".join(sorted(chars))


def transform_controlled_perturbation(s: str) -> str:
    """
    Minimal smoothing transform:
    lowercase, strip repeated spaces, standardize delimiters.
    """
    x = s.lower().strip()
    x = re.sub(r"\s+", " ", x)
    x = x.replace("|", ",")
    return x


def transform_compression(s: str) -> str:
    """
    Very shallow compression proxy:
    remove spaces and repeated delimiters.
    """
    x = re.sub(r"\s+", "", s)
    x = re.sub(r",+", ",", x)
    return x


def transform_representation_preserving_rewrite(s: str) -> str:
    return normalize_text_soft(s)


TRANSFORMS = {
    "identity": transform_identity,
    "permutation": transform_permutation,
    "controlled_perturbation": transform_controlled_perturbation,
    "compression": transform_compression,
    "representation_preserving_rewrite": transform_representation_preserving_rewrite,
}


# ---------------------------------------------------------------------
# Distance functions
# ---------------------------------------------------------------------

def d_vec(a: float, b: float) -> float:
    """
    For v0.1 drift_vector is scalarized in [0,1].
    """
    return abs(a - b)


def d_sigma(sig1: StructuralSignature, sig2: StructuralSignature) -> float:
    dist = (
        W_OMEGA * l1_distance(sig1.omega, sig2.omega)
        + W_OMEGA_VARIANCE * l1_distance(sig1.omega_variance, sig2.omega_variance)
        + W_SEI * l1_distance(sig1.sei, sig2.sei)
        + W_DRIFT * l1_distance(sig1.drift, sig2.drift)
        + W_DRIFT_VECTOR * d_vec(sig1.drift_vector, sig2.drift_vector)
        + W_ORDER_SENSITIVITY
        * l1_distance(sig1.order_sensitivity, sig2.order_sensitivity)
    )
    return clamp01(dist)


def delta_omega(state_1: str, state_2: str) -> Tuple[float, str, StructuralSignature, StructuralSignature]:
    """
    Delta_Omega(S1,S2) = inf_{g in G} d_sigma( sigma(g(S1)), sigma(S2) )

    Approximated over the minimal canonical transform set G_v0.1.
    """
    sig2 = structural_signature(state_2)

    best_distance = float("inf")
    best_transform_name = "identity"
    best_sig1 = structural_signature(state_1)

    for name, fn in TRANSFORMS.items():
        transformed = fn(state_1)
        sig1_candidate = structural_signature(transformed)
        dist = d_sigma(sig1_candidate, sig2)
        if dist < best_distance:
            best_distance = dist
            best_transform_name = name
            best_sig1 = sig1_candidate

    return clamp01(best_distance), best_transform_name, best_sig1, sig2


# ---------------------------------------------------------------------
# Zone prediction
# ---------------------------------------------------------------------

def predict_zone(delta: float) -> str:
    if delta <= EPSILON_EQ:
        return "equivalence"
    if delta < EPSILON_BREAK:
        return "mild_variation"
    return "structural_break"


# ---------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------

def load_jsonl(path: Path) -> List[dict]:
    rows: List[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: List[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


# ---------------------------------------------------------------------
# Main benchmark
# ---------------------------------------------------------------------

def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    rows = load_jsonl(INPUT_PATH)
    results: List[ValidationResult] = []

    family_to_scores: Dict[str, List[float]] = {
        "equivalent": [],
        "mild_variation": [],
        "structural_break": [],
    }

    for row in rows:
        pair_id = row["pair_id"]
        family = row["family"]
        state_1 = row["state_1"]
        state_2 = row["state_2"]
        expected_zone = row["expected_zone"]
        notes = row.get("notes", "")

        delta, best_transform, sig1_best, sig2 = delta_omega(state_1, state_2)
        kappa = clamp01(1.0 - delta)
        predicted_zone = predict_zone(delta)
        pass_fail = "PASS" if predicted_zone == expected_zone else "FAIL"

        family_to_scores.setdefault(family, []).append(delta)

        results.append(
            ValidationResult(
                pair_id=pair_id,
                family=family,
                state_1=state_1,
                state_2=state_2,
                expected_zone=expected_zone,
                predicted_zone=predicted_zone,
                pass_fail=pass_fail,
                delta_omega=round(delta, 6),
                kappa=round(kappa, 6),
                best_transform=best_transform,
                sigma_1={
                    k: round(v, 6) for k, v in asdict(sig1_best).items()
                },
                sigma_2_best={
                    k: round(v, 6) for k, v in asdict(sig2).items()
                },
                notes=notes,
            )
        )

    write_jsonl(OUTPUT_PATH, [asdict(r) for r in results])

    # Console summary
    print("OMNIA dO Mini Validation v0")
    print(f"Input : {INPUT_PATH}")
    print(f"Output: {OUTPUT_PATH}")
    print()

    total_pass = sum(1 for r in results if r.pass_fail == "PASS")
    print(f"Pairs tested : {len(results)}")
    print(f"Pass count   : {total_pass}")
    print(f"Fail count   : {len(results) - total_pass}")
    print()

    for fam in ("equivalent", "mild_variation", "structural_break"):
        scores = family_to_scores.get(fam, [])
        if scores:
            print(
                f"{fam:16s} mean_dO={mean(scores):.6f} "
                f"min={min(scores):.6f} max={max(scores):.6f}"
            )

    print()
    print("Detailed results:")
    for r in results:
        print(
            f"{r.pair_id} | family={r.family} | dO={r.delta_omega:.6f} "
            f"| kappa={r.kappa:.6f} | zone={r.predicted_zone} | {r.pass_fail}"
        )


if __name__ == "__main__":
    main()