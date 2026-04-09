#!/usr/bin/env python3
"""
OMNIA - dO Validation Benchmark v0.2

Reads:
    examples/do_mini_validation_pairs_v1.jsonl

Computes:
    - structural signature sigma_v0.2(S)
    - primitive signature distance d_sigma_v0.2
    - transformation-cost-aware Delta_Omega_v0.2(S1, S2)
    - kappa = 1 - Delta_Omega
    - predicted zone
    - pass/fail against expected zone

Writes:
    examples/do_mini_validation_results_v1.jsonl

Important:
This is still a bootstrap validation runner.
It is not a proof of universality.
It is an operational falsifiable check for v0.2.
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
INPUT_PATH = ROOT / "do_mini_validation_pairs_v1.jsonl"
OUTPUT_PATH = ROOT / "do_mini_validation_results_v1.jsonl"


# ---------------------------------------------------------------------
# Canonical weights v0.2
# ---------------------------------------------------------------------

W_OMEGA = 0.20
W_OMEGA_VARIANCE = 0.10
W_SEI = 0.15
W_DRIFT = 0.10
W_DRIFT_VECTOR = 0.05
W_ORDER_SENSITIVITY = 0.10
W_TRANSITION_FREQUENCY = 0.10
W_RUN_LENGTH_IRREGULARITY = 0.10
W_LOCAL_DELTA_PATTERN = 0.10

WEIGHT_SUM = (
    W_OMEGA
    + W_OMEGA_VARIANCE
    + W_SEI
    + W_DRIFT
    + W_DRIFT_VECTOR
    + W_ORDER_SENSITIVITY
    + W_TRANSITION_FREQUENCY
    + W_RUN_LENGTH_IRREGULARITY
    + W_LOCAL_DELTA_PATTERN
)
if not math.isclose(WEIGHT_SUM, 1.0, rel_tol=1e-9, abs_tol=1e-9):
    raise ValueError(f"Canonical weights must sum to 1.0, got {WEIGHT_SUM}")


# ---------------------------------------------------------------------
# Thresholds
# ---------------------------------------------------------------------

EPSILON_EQ = 0.10
EPSILON_BREAK = 0.35


# ---------------------------------------------------------------------
# Transformation cost
# ---------------------------------------------------------------------

LAMBDA_TRANSFORM = 0.50

TRANSFORM_COSTS: Dict[str, float] = {
    "identity": 0.00,
    "controlled_perturbation": 0.03,
    "compression": 0.04,
    "representation_preserving_rewrite": 0.05,
    "permutation": 0.25,
}


# ---------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------

@dataclass
class StructuralSignatureV2:
    omega: float
    omega_variance: float
    sei: float
    drift: float
    drift_vector: float
    order_sensitivity: float
    transition_frequency: float
    run_length_irregularity: float
    local_delta_pattern: float


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
    transform_cost: float
    signature_distance: float
    sigma_1_best: Dict[str, float]
    sigma_2: Dict[str, float]
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


def tokenize_chars(s: str) -> List[str]:
    return [c for c in s if not c.isspace()]


def alpha_tokens(s: str) -> List[str]:
    return re.findall(r"[A-Za-z]+", s)


def alnum_char_tokens(s: str) -> List[str]:
    return [c.lower() for c in s if c.isalnum()]


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
    max_ent = math.log2(len(counts)) if len(counts) > 1 else 1.0
    return clamp01(safe_div(ent, max_ent))


def unique_ratio(tokens: List[str]) -> float:
    if not tokens:
        return 0.0
    return clamp01(len(set(tokens)) / len(tokens))


def adjacent_change_ratio(tokens: List[str]) -> float:
    if len(tokens) < 2:
        return 0.0
    changes = sum(1 for i in range(len(tokens) - 1) if tokens[i] != tokens[i + 1])
    return clamp01(changes / (len(tokens) - 1))


def sequence_order_sensitivity(tokens: List[str]) -> float:
    if len(tokens) < 2:
        return 0.0
    sorted_tokens = sorted(tokens)
    mismatches = sum(1 for a, b in zip(tokens, sorted_tokens) if a != b)
    return clamp01(mismatches / len(tokens))


def numeric_drift_vector(nums: List[float]) -> float:
    if len(nums) < 2:
        return 0.5
    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    total_abs = sum(abs(x) for x in diffs)
    if total_abs == 0:
        return 0.5
    signed = sum(diffs)
    trend = signed / total_abs
    return clamp01((trend + 1.0) / 2.0)


def symbolic_drift_vector(tokens: List[str]) -> float:
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


def run_lengths(tokens: List[str]) -> List[int]:
    if not tokens:
        return []
    runs: List[int] = []
    current = tokens[0]
    count = 1
    for tok in tokens[1:]:
        if tok == current:
            count += 1
        else:
            runs.append(count)
            current = tok
            count = 1
    runs.append(count)
    return runs


def transition_frequency(tokens: List[str]) -> float:
    return adjacent_change_ratio(tokens)


def run_length_irregularity(tokens: List[str]) -> float:
    runs = run_lengths(tokens)
    if not runs:
        return 0.0
    if len(runs) == 1:
        return 0.0
    # Normalize variance by squared sequence length
    v = variance([float(r) for r in runs])
    n = max(sum(runs), 1)
    return clamp01(v / (n * n))


def local_delta_pattern_numeric(nums: List[float]) -> float:
    if len(nums) < 3:
        return 0.0
    deltas = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    if len(deltas) < 2:
        return 0.0
    changes = sum(1 for i in range(len(deltas) - 1) if deltas[i] != deltas[i + 1])
    return clamp01(changes / (len(deltas) - 1))


def local_delta_pattern_symbolic(tokens: List[str]) -> float:
    if len(tokens) < 3:
        return 0.0
    # Pattern of equality/inequality between neighbors
    rel = [1 if tokens[i + 1] == tokens[i] else 0 for i in range(len(tokens) - 1)]
    if len(rel) < 2:
        return 0.0
    changes = sum(1 for i in range(len(rel) - 1) if rel[i] != rel[i + 1])
    return clamp01(changes / (len(rel) - 1))


def l1_distance(a: float, b: float) -> float:
    return abs(a - b)


def scalar_repr(x: float) -> str:
    if float(x).is_integer():
        return str(int(x))
    return str(x)


# ---------------------------------------------------------------------
# Canonicalization helpers
# ---------------------------------------------------------------------

def canonical_numeric_string(s: str) -> str:
    nums = parse_numeric_sequence_if_possible(s)
    if not nums:
        return s
    return ",".join(scalar_repr(x) for x in nums)


def canonical_symbolic_string(s: str) -> str:
    x = s.lower().strip()
    x = x.replace("_", "-")
    x = x.replace(";", ",")
    x = re.sub(r"[\{\}\[\]\(\)\$]", "", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x


# ---------------------------------------------------------------------
# Signature extraction v0.2
# ---------------------------------------------------------------------

def structural_signature_v2(state: str) -> StructuralSignatureV2:
    s = normalize_text_basic(state)
    nums = parse_numeric_sequence_if_possible(s)

    if nums:
        tokens = [scalar_repr(x) for x in nums]
        entropy = shannon_entropy(tokens)
        uniq = unique_ratio(tokens)
        rep = 1.0 - uniq
        omega = clamp01(0.55 * rep + 0.45 * (1.0 - entropy))
        omega_variance = clamp01(adjacent_change_ratio(tokens))
        sei = clamp01(1.0 - abs(entropy - 0.5) * 2.0)
        drift = clamp01(adjacent_change_ratio(tokens))
        drift_vector = numeric_drift_vector(nums)
        order_sensitivity = clamp01(sequence_order_sensitivity(tokens))
        tf = transition_frequency(tokens)
        rli = run_length_irregularity(tokens)
        ldp = local_delta_pattern_numeric(nums)
    else:
        alpha = alpha_tokens(s)
        if alpha:
            tokens = [tok.lower() for tok in alpha]
        else:
            tokens = alnum_char_tokens(s)

        entropy = shannon_entropy(tokens)
        uniq = unique_ratio(tokens)
        rep = 1.0 - uniq
        omega = clamp01(0.55 * rep + 0.45 * (1.0 - entropy))
        omega_variance = clamp01(adjacent_change_ratio(tokens))
        sei = clamp01(1.0 - abs(entropy - 0.5) * 2.0)
        drift = clamp01(adjacent_change_ratio(tokens))
        drift_vector = symbolic_drift_vector(tokens)
        order_sensitivity = clamp01(sequence_order_sensitivity(tokens))
        tf = transition_frequency(tokens)
        rli = run_length_irregularity(tokens)
        ldp = local_delta_pattern_symbolic(tokens)

    return StructuralSignatureV2(
        omega=omega,
        omega_variance=omega_variance,
        sei=sei,
        drift=drift,
        drift_vector=drift_vector,
        order_sensitivity=order_sensitivity,
        transition_frequency=tf,
        run_length_irregularity=rli,
        local_delta_pattern=ldp,
    )


# ---------------------------------------------------------------------
# Admissible transforms G_v0.2
# ---------------------------------------------------------------------

def transform_identity(s: str) -> str:
    return s


def transform_controlled_perturbation(s: str) -> str:
    x = s.lower().strip()
    x = re.sub(r"\s+", " ", x)
    x = x.replace("|", ",")
    x = x.replace(";", ",")
    return x


def transform_compression(s: str) -> str:
    x = re.sub(r"\s+", "", s)
    x = re.sub(r",+", ",", x)
    return x


def transform_representation_preserving_rewrite(s: str) -> str:
    nums = parse_numeric_sequence_if_possible(s)
    if nums:
        return canonical_numeric_string(s)
    return canonical_symbolic_string(s)


def transform_permutation(s: str) -> str:
    """
    Kept only as a high-cost transform.
    It is intentionally deterministic but not free.
    """
    nums = parse_numeric_sequence_if_possible(s)
    if nums:
        nums_sorted = sorted(nums)
        return ",".join(scalar_repr(x) for x in nums_sorted)

    chars = [c.lower() for c in s if c.isalnum()]
    return "".join(sorted(chars))


TRANSFORMS = {
    "identity": transform_identity,
    "controlled_perturbation": transform_controlled_perturbation,
    "compression": transform_compression,
    "representation_preserving_rewrite": transform_representation_preserving_rewrite,
    "permutation": transform_permutation,
}


# ---------------------------------------------------------------------
# Distance functions
# ---------------------------------------------------------------------

def d_vec(a: float, b: float) -> float:
    return abs(a - b)


def d_sigma_v2(sig1: StructuralSignatureV2, sig2: StructuralSignatureV2) -> float:
    dist = (
        W_OMEGA * l1_distance(sig1.omega, sig2.omega)
        + W_OMEGA_VARIANCE * l1_distance(sig1.omega_variance, sig2.omega_variance)
        + W_SEI * l1_distance(sig1.sei, sig2.sei)
        + W_DRIFT * l1_distance(sig1.drift, sig2.drift)
        + W_DRIFT_VECTOR * d_vec(sig1.drift_vector, sig2.drift_vector)
        + W_ORDER_SENSITIVITY * l1_distance(sig1.order_sensitivity, sig2.order_sensitivity)
        + W_TRANSITION_FREQUENCY * l1_distance(sig1.transition_frequency, sig2.transition_frequency)
        + W_RUN_LENGTH_IRREGULARITY * l1_distance(sig1.run_length_irregularity, sig2.run_length_irregularity)
        + W_LOCAL_DELTA_PATTERN * l1_distance(sig1.local_delta_pattern, sig2.local_delta_pattern)
    )
    return clamp01(dist)


def delta_omega_v2(
    state_1: str,
    state_2: str,
) -> Tuple[float, float, str, StructuralSignatureV2, StructuralSignatureV2]:
    """
    Delta_Omega_v0.2(S1,S2) =
      inf_{g in G} [ d_sigma_v2( sigma_v2(g(S1)), sigma_v2(S2) ) + lambda * C_transform(g) ]
    """
    sig2 = structural_signature_v2(state_2)

    best_total = float("inf")
    best_sig_distance = float("inf")
    best_transform_name = "identity"
    best_sig1 = structural_signature_v2(state_1)

    for name, fn in TRANSFORMS.items():
        transformed = fn(state_1)
        sig1_candidate = structural_signature_v2(transformed)
        sig_dist = d_sigma_v2(sig1_candidate, sig2)
        total_dist = sig_dist + LAMBDA_TRANSFORM * TRANSFORM_COSTS[name]
        total_dist = clamp01(total_dist)

        if total_dist < best_total:
            best_total = total_dist
            best_sig_distance = sig_dist
            best_transform_name = name
            best_sig1 = sig1_candidate

    return (
        clamp01(best_total),
        clamp01(best_sig_distance),
        best_transform_name,
        best_sig1,
        sig2,
    )


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

        delta, sig_distance, best_transform, sig1_best, sig2 = delta_omega_v2(state_1, state_2)
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
                transform_cost=round(TRANSFORM_COSTS[best_transform], 6),
                signature_distance=round(sig_distance, 6),
                sigma_1_best={k: round(v, 6) for k, v in asdict(sig1_best).items()},
                sigma_2={k: round(v, 6) for k, v in asdict(sig2).items()},
                notes=notes,
            )
        )

    write_jsonl(OUTPUT_PATH, [asdict(r) for r in results])

    print("OMNIA dO Validation v0.2")
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
            f"| sig={r.signature_distance:.6f} | g={r.best_transform} "
            f"| cost={r.transform_cost:.2f} | zone={r.predicted_zone} | {r.pass_fail}"
        )


if __name__ == "__main__":
    main()