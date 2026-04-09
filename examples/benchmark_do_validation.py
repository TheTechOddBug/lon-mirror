#!/usr/bin/env python3
"""
OMNIA - Multi-Stream Temporal Series Engine v1

Operates on multiple interleaved numeric streams and preserves strict
trajectory-memory isolation per stream_id.

Reads:
    examples/multi_stream_demo_v1.jsonl

Computes:
    - pre-canonicalized structural signature sigma_v0.2.1(S)
    - dO = Delta_Omega_v0.2.1(S_t, S_t+1) per stream
    - kappa = 1 - dO
    - TransitionSignalV1
    - TrajectoryStatusV1
    - strict per-stream trajectory isolation

Writes:
    examples/do_mini_validation_results_v1.jsonl
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
INPUT_PATH = ROOT / "multi_stream_demo_v1.jsonl"
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
# Versions
# ---------------------------------------------------------------------

METRIC_VERSION = "v0.2.1"
PROTOCOL_VERSION = "v1"
SIGNAL_SCHEMA_VERSION = "v1"
MEMORY_VERSION = "v1"
MULTI_TRAJECTORY_VERSION = "v1"


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
class TransitionSignalV1:
    signal_id: str
    reference_state_id: str
    observed_state_id: str
    dO: float
    kappa: float
    assigned_zone: str
    protocol_label: str
    continuity_status: str
    drift_tracking_flag: bool
    regime_alert_flag: bool
    signature_distance: float
    best_transform: str
    transform_cost: float
    threshold_equivalence: float
    threshold_break: float
    metric_version: str
    protocol_version: str
    signal_schema_version: str
    family: str
    expected_zone: str
    predicted_zone: str
    pass_fail: str
    state_1: str
    state_2: str
    notes: str


@dataclass
class TrajectoryStatusV1:
    trajectory_id: str
    transition_index: int
    active_regime_id: str
    last_stable_regime_id: str
    regime_status: str
    cumulative_drift: float
    consecutive_mild_count: int
    consecutive_break_count: int
    trajectory_alert_flag: bool
    last_signal_id: str
    protocol_version: str
    memory_version: str


@dataclass
class OutputRecord:
    stream_id: str
    transition_signal: Dict
    trajectory_status: Dict


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
    if not runs or len(runs) == 1:
        return 0.0
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
# Pre-canonicalization v0.2.1
# ---------------------------------------------------------------------

def precanonicalize_state(state: str) -> str:
    s = state.strip()
    s = s.replace("\n", " ")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"^[\{\[\(]+", "", s)
    s = re.sub(r"[\}\]\)]+$", "", s)
    s = s.replace(";", ",")
    s = s.replace("|", ",")
    s = s.replace("_", "-")
    s = re.sub(r"(?<!\S)[$€£¥]\s*", "", s)
    s = s.lower()

    def normalize_numeric_token(match: re.Match) -> str:
        token = match.group(0)
        try:
            value = float(token)
            if value.is_integer():
                return str(int(value))
            return format(value, "g")
        except ValueError:
            return token

    s = re.sub(r"-?\d+(?:\.\d+)?", normalize_numeric_token, s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------------
# Canonicalization helpers
# ---------------------------------------------------------------------

def canonical_numeric_string(s: str) -> str:
    nums = parse_numeric_sequence_if_possible(precanonicalize_state(s))
    if not nums:
        return precanonicalize_state(s)
    return ",".join(scalar_repr(x) for x in nums)


def canonical_symbolic_string(s: str) -> str:
    x = precanonicalize_state(s)
    x = x.replace("_", "-")
    x = x.replace(";", ",")
    x = re.sub(r"[\{\}\[\]\(\)\$]", "", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x


# ---------------------------------------------------------------------
# Signature extraction
# ---------------------------------------------------------------------

def structural_signature_v2(state: str) -> StructuralSignatureV2:
    s = precanonicalize_state(normalize_text_basic(state))
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
# Admissible transforms
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
    nums = parse_numeric_sequence_if_possible(precanonicalize_state(s))
    if nums:
        return canonical_numeric_string(s)
    return canonical_symbolic_string(s)


def transform_permutation(s: str) -> str:
    nums = parse_numeric_sequence_if_possible(precanonicalize_state(s))
    if nums:
        nums_sorted = sorted(nums)
        return ",".join(scalar_repr(x) for x in nums_sorted)

    chars = [c.lower() for c in precanonicalize_state(s) if c.isalnum()]
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


def delta_omega_v2(state_1: str, state_2: str) -> Tuple[float, float, str]:
    sig2 = structural_signature_v2(state_2)

    best_total = float("inf")
    best_sig_distance = float("inf")
    best_transform_name = "identity"

    for name, fn in TRANSFORMS.items():
        transformed = fn(state_1)
        sig1_candidate = structural_signature_v2(transformed)
        sig_dist = d_sigma_v2(sig1_candidate, sig2)
        total_dist = clamp01(sig_dist + LAMBDA_TRANSFORM * TRANSFORM_COSTS[name])

        if total_dist < best_total:
            best_total = total_dist
            best_sig_distance = sig_dist
            best_transform_name = name

    return clamp01(best_total), clamp01(best_sig_distance), best_transform_name


# ---------------------------------------------------------------------
# Protocol logic
# ---------------------------------------------------------------------

def assign_zone(delta: float) -> str:
    if delta <= EPSILON_EQ:
        return "equivalence"
    if delta < EPSILON_BREAK:
        return "mild_variation"
    return "structural_break"


def protocol_fields_for_zone(zone: str) -> Tuple[str, str, bool, bool]:
    if zone == "equivalence":
        return ("EQUIVALENT_CONTINUITY", "continuous", False, False)
    if zone == "mild_variation":
        return ("TRACKED_DRIFT", "continuous_with_drift", True, False)
    return ("REGIME_SHIFT_CANDIDATE", "continuity_suspended", False, True)


# ---------------------------------------------------------------------
# Trajectory memory
# ---------------------------------------------------------------------

class TrajectoryTracker:
    def __init__(self, trajectory_id: str, initial_regime_id: str = "REG_ALPHA") -> None:
        self.trajectory_id = trajectory_id
        self.active_regime_id = initial_regime_id
        self.last_stable_regime_id = initial_regime_id
        self.regime_status = "STABLE"
        self.transition_index = 0
        self.previous_signal_id = ""
        self.cumulative_drift = 0.0
        self.consecutive_mild_count = 0
        self.consecutive_break_count = 0
        self.trajectory_alert_flag = False
        self._candidate_regime_counter = 0

    def _new_regime_id(self) -> str:
        self._candidate_regime_counter += 1
        return f"REG_CAND_{self._candidate_regime_counter:03d}"

    def update(self, signal: TransitionSignalV1) -> TrajectoryStatusV1:
        self.transition_index += 1
        self.previous_signal_id = signal.signal_id
        zone = signal.assigned_zone

        if zone == "equivalence":
            if self.regime_status == "SUSPENDED":
                self.active_regime_id = self.last_stable_regime_id
                self.regime_status = "STABLE"
                self.cumulative_drift = 0.0
            elif self.regime_status == "MIGRATING":
                self.active_regime_id = self._new_regime_id()
                self.last_stable_regime_id = self.active_regime_id
                self.regime_status = "STABLE"
                self.cumulative_drift = 0.0

            self.consecutive_mild_count = 0
            self.consecutive_break_count = 0
            self.trajectory_alert_flag = False

        elif zone == "mild_variation":
            self.cumulative_drift += signal.dO
            self.consecutive_mild_count += 1
            self.consecutive_break_count = 0
            self.regime_status = "DRIFTING"
            self.trajectory_alert_flag = self.consecutive_mild_count > 5

        else:  # structural_break
            self.consecutive_break_count += 1
            self.consecutive_mild_count = 0
            self.regime_status = "SUSPENDED"
            self.trajectory_alert_flag = True

            if self.consecutive_break_count >= 3:
                self.regime_status = "MIGRATING"

        return TrajectoryStatusV1(
            trajectory_id=self.trajectory_id,
            transition_index=self.transition_index,
            active_regime_id=self.active_regime_id,
            last_stable_regime_id=self.last_stable_regime_id,
            regime_status=self.regime_status,
            cumulative_drift=round(self.cumulative_drift, 6),
            consecutive_mild_count=self.consecutive_mild_count,
            consecutive_break_count=self.consecutive_break_count,
            trajectory_alert_flag=self.trajectory_alert_flag,
            last_signal_id=self.previous_signal_id,
            protocol_version=PROTOCOL_VERSION,
            memory_version=MEMORY_VERSION,
        )


# ---------------------------------------------------------------------
# Multi-trajectory manager
# ---------------------------------------------------------------------

class MultiTrajectoryManager:
    def __init__(self) -> None:
        self.trackers: Dict[str, TrajectoryTracker] = {}
        self.last_rows: Dict[str, dict] = {}

    def get_tracker(self, stream_id: str) -> TrajectoryTracker:
        if stream_id not in self.trackers:
            self.trackers[stream_id] = TrajectoryTracker(trajectory_id=f"T_{stream_id}")
        return self.trackers[stream_id]

    def has_previous(self, stream_id: str) -> bool:
        return stream_id in self.last_rows

    def previous_row(self, stream_id: str) -> dict:
        return self.last_rows[stream_id]

    def update_previous(self, stream_id: str, row: dict) -> None:
        self.last_rows[stream_id] = row


# ---------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------

def load_jsonl(path: Path) -> List[dict]:
    rows: List[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: List[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


# ---------------------------------------------------------------------
# Main engine
# ---------------------------------------------------------------------

def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    rows = load_jsonl(INPUT_PATH)
    if len(rows) < 2:
        raise ValueError("The input stream file must contain at least 2 rows.")

    manager = MultiTrajectoryManager()
    records: List[OutputRecord] = []

    per_stream_scores: Dict[str, List[float]] = {}

    for row in rows:
        stream_id = str(row["stream_id"])
        tracker = manager.get_tracker(stream_id)

        if not manager.has_previous(stream_id):
            manager.update_previous(stream_id, row)
            continue

        prev = manager.previous_row(stream_id)

        t1 = str(prev["t"])
        t2 = str(row["t"])
        s1_raw = str(prev["v"])
        s2_raw = str(row["v"])
        note = row.get("note", "")

        delta, sig_distance, best_transform = delta_omega_v2(s1_raw, s2_raw)
        kappa = clamp01(1.0 - delta)
        assigned_zone = assign_zone(delta)
        protocol_label, continuity_status, drift_tracking_flag, regime_alert_flag = protocol_fields_for_zone(assigned_zone)

        signal = TransitionSignalV1(
            signal_id=f"SIG_{stream_id}_{t1}_{t2}",
            reference_state_id=f"{stream_id}_S_{t1}",
            observed_state_id=f"{stream_id}_S_{t2}",
            dO=round(delta, 6),
            kappa=round(kappa, 6),
            assigned_zone=assigned_zone,
            protocol_label=protocol_label,
            continuity_status=continuity_status,
            drift_tracking_flag=drift_tracking_flag,
            regime_alert_flag=regime_alert_flag,
            signature_distance=round(sig_distance, 6),
            best_transform=best_transform,
            transform_cost=round(TRANSFORM_COSTS[best_transform], 6),
            threshold_equivalence=EPSILON_EQ,
            threshold_break=EPSILON_BREAK,
            metric_version=METRIC_VERSION,
            protocol_version=PROTOCOL_VERSION,
            signal_schema_version=SIGNAL_SCHEMA_VERSION,
            family="multi_stream_time_series",
            expected_zone="N/A",
            predicted_zone=assigned_zone,
            pass_fail="N/A",
            state_1=s1_raw,
            state_2=s2_raw,
            notes=note,
        )

        trajectory_status = tracker.update(signal)

        records.append(
            OutputRecord(
                stream_id=stream_id,
                transition_signal=asdict(signal),
                trajectory_status=asdict(trajectory_status),
            )
        )

        per_stream_scores.setdefault(stream_id, []).append(delta)
        manager.update_previous(stream_id, row)

    write_jsonl(OUTPUT_PATH, [asdict(r) for r in records])

    print("OMNIA Multi-Stream Temporal Series Engine v1")
    print(f"Input : {INPUT_PATH}")
    print(f"Output: {OUTPUT_PATH}")
    print()
    print(f"Transitions analyzed : {len(records)}")

    for stream_id, scores in sorted(per_stream_scores.items()):
        if scores:
            print(
                f"{stream_id:12s} "
                f"count={len(scores)} mean_dO={mean(scores):.6f} "
                f"min={min(scores):.6f} max={max(scores):.6f}"
            )

    print()
    print("Detailed records:")
    for r in records:
        ts = r.transition_signal
        mem = r.trajectory_status
        print(
            f"[{r.stream_id}] {ts['observed_state_id']} "
            f"| dO={ts['dO']:.6f} "
            f"| zone={ts['assigned_zone']} "
            f"| status={mem['regime_status']} "
            f"| drift_sum={mem['cumulative_drift']:.6f} "
            f"| mild_n={mem['consecutive_mild_count']} "
            f"| break_n={mem['consecutive_break_count']}"
        )


if __name__ == "__main__":
    main()