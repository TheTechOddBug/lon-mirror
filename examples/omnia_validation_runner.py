import json
import math
import random
import statistics
from collections import defaultdict
from typing import Dict, List, Tuple

# ============================================================
# OMNIA VALIDATION RUNNER - C-OPERATOR v1.0
# ============================================================
# Notes:
# - This runner is coherent with Steps 1-4
# - omega_fn is now a first real C-Operator instance
# - Step 2 (stability) is separated from Step 4 (separability)
# - Current Omega is still minimal, but no longer a trivial placeholder
# ============================================================

BOOTSTRAP_RESAMPLES = 1000
DEFAULT_TAU = 0.95
DEFAULT_MIN_EFFECT = 0.5

# ------------------------------------------------------------
# Configurations F = {(G1,d1), (G2,d2), (G3,d3)}
# Same transformation family, different intensities, compatible d
# ------------------------------------------------------------
F_CONFIGS = [
    {
        "name": "G1_d1",
        "swap_pct": 0.05,
        "dropout_pct": 0.05,
        "char_noise_pct": 0.02,
        "edit_weight": 1.0,
        "embed_weight": 0.0,
    },
    {
        "name": "G2_d2",
        "swap_pct": 0.10,
        "dropout_pct": 0.05,
        "char_noise_pct": 0.03,
        "edit_weight": 0.8,
        "embed_weight": 0.2,
    },
    {
        "name": "G3_d3",
        "swap_pct": 0.15,
        "dropout_pct": 0.10,
        "char_noise_pct": 0.03,
        "edit_weight": 0.6,
        "embed_weight": 0.4,
    },
]


# ------------------------------------------------------------
# Tokenization
# ------------------------------------------------------------
def tokenize(text: str) -> List[str]:
    return text.strip().split()


# ------------------------------------------------------------
# Perturbations coherent with F
# ------------------------------------------------------------
def local_token_swap(tokens: List[str], swap_pct: float, rng: random.Random) -> List[str]:
    out = tokens[:]
    n = len(out)
    if n < 2:
        return out

    swaps = max(1, int(round(n * swap_pct)))
    for _ in range(swaps):
        i = rng.randrange(0, n - 1)
        out[i], out[i + 1] = out[i + 1], out[i]
    return out


def token_dropout(tokens: List[str], dropout_pct: float, rng: random.Random) -> List[str]:
    if not tokens:
        return tokens[:]

    keep = []
    for tok in tokens:
        if rng.random() > dropout_pct:
            keep.append(tok)

    if not keep:
        keep.append(tokens[rng.randrange(len(tokens))])

    return keep


def apply_char_noise(tokens: List[str], char_noise_pct: float, rng: random.Random) -> List[str]:
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    out = []

    for tok in tokens:
        if not tok:
            out.append(tok)
            continue

        chars = list(tok)
        n_changes = int(round(len(chars) * char_noise_pct))
        n_changes = min(len(chars), n_changes)

        if n_changes > 0:
            idxs = rng.sample(range(len(chars)), n_changes)
            for idx in idxs:
                chars[idx] = rng.choice(alphabet)

        out.append("".join(chars))

    return out


def perturb_with_config(text: str, config: Dict, seed: int) -> str:
    rng = random.Random(seed)
    tokens = tokenize(text)

    tokens = local_token_swap(tokens, config["swap_pct"], rng)
    tokens = token_dropout(tokens, config["dropout_pct"], rng)
    tokens = apply_char_noise(tokens, config["char_noise_pct"], rng)

    return " ".join(tokens)


# ------------------------------------------------------------
# Distances
# ------------------------------------------------------------
def levenshtein_distance(a: List[str], b: List[str]) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    prev = list(range(len(b) + 1))

    for i, ca in enumerate(a, start=1):
        curr = [i]
        for j, cb in enumerate(b, start=1):
            ins = curr[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (0 if ca == cb else 1)
            curr.append(min(ins, delete, sub))
        prev = curr

    return prev[-1]


def edit_distance_norm(text_a: str, text_b: str) -> float:
    a = tokenize(text_a)
    b = tokenize(text_b)
    denom = max(1, max(len(a), len(b)))
    return levenshtein_distance(a, b) / denom


def token_frequency_embedding(text: str) -> Dict[str, float]:
    toks = tokenize(text)
    if not toks:
        return {}

    total = len(toks)
    freq = defaultdict(float)

    for t in toks:
        freq[t] += 1.0

    for k in freq:
        freq[k] /= total

    return dict(freq)


def embedding_distance(text_a: str, text_b: str) -> float:
    fa = token_frequency_embedding(text_a)
    fb = token_frequency_embedding(text_b)
    keys = set(fa) | set(fb)

    if not keys:
        return 0.0

    sq = 0.0
    for k in keys:
        sq += (fa.get(k, 0.0) - fb.get(k, 0.0)) ** 2

    return math.sqrt(sq)


def pseudo_distance(text_a: str, text_b: str, config: Dict) -> float:
    d_edit = edit_distance_norm(text_a, text_b)
    d_embed = embedding_distance(text_a, text_b)

    return config["edit_weight"] * d_edit + config["embed_weight"] * d_embed


# ------------------------------------------------------------
# C-OPERATOR v1.0 - REAL STRUCTURAL MEASUREMENT
# ------------------------------------------------------------
def omega_fn(text: str) -> float:
    """
    First real C-Operator instance.

    It measures how much the text preserves structural regularity
    under a small family of deterministic token transformations.
    """

    tokens = tokenize(text)
    if not tokens:
        return 0.0

    def g_reverse_tokens(toks: List[str]) -> List[str]:
        return toks[::-1]

    def g_sort_tokens(toks: List[str]) -> List[str]:
        return sorted(toks)

    def g_rotate_left(toks: List[str]) -> List[str]:
        if len(toks) <= 1:
            return toks[:]
        return toks[1:] + toks[:1]

    G = [g_reverse_tokens, g_sort_tokens, g_rotate_left]

    base_text = " ".join(tokens)
    residuals = []

    for g in G:
        transformed_tokens = g(tokens)
        transformed_text = " ".join(transformed_tokens)
        residuals.append(edit_distance_norm(base_text, transformed_text))

    agg_residual = statistics.median(residuals)

    # Structural compactness factor:
    # repeated token patterns should score higher than fully diverse token streams
    unique_ratio = len(set(tokens)) / max(1, len(tokens))
    compactness = 1.0 - unique_ratio

    # Alternation / local repetition support:
    local_regularity = sum(
        1 for i in range(1, len(tokens)) if tokens[i] == tokens[i - 1]
    ) / max(1, len(tokens) - 1)

    # Weighted structural factor
    structure_factor = 0.8 * compactness + 0.2 * local_regularity

    omega_val = (1.0 - agg_residual) * structure_factor
    return max(0.0, min(1.0, omega_val))


# ------------------------------------------------------------
# Step 2 metrics
# Inv  = local stability under held-out perturbations
# Inv2 = multi-configuration variance for the same sample
# ------------------------------------------------------------
def inv_local(text: str, config: Dict, base_seed: int = 1000, n_samples: int = 5) -> float:
    base = omega_fn(text)
    vals = []

    for i in range(n_samples):
        perturbed = perturb_with_config(text, config, seed=base_seed + i)
        vals.append(abs(base - omega_fn(perturbed)))

    return mean(vals)


def inv2_local(text: str, configs: List[Dict]) -> float:
    vals = [
        omega_fn(perturb_with_config(text, cfg, seed=5000 + i))
        for i, cfg in enumerate(configs)
    ]
    return variance(vals)


# ------------------------------------------------------------
# Dataset I/O
# ------------------------------------------------------------
def load_jsonl(path: str) -> List[Dict]:
    rows = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))

    return rows


# ------------------------------------------------------------
# Statistics
# ------------------------------------------------------------
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def variance(xs: List[float]) -> float:
    if len(xs) < 2:
        return 0.0
    return statistics.pvariance(xs)


def std(xs: List[float]) -> float:
    return math.sqrt(variance(xs))


def median(xs: List[float]) -> float:
    return statistics.median(xs) if xs else 0.0


def mad(xs: List[float]) -> float:
    if not xs:
        return 0.0

    m = median(xs)
    return median([abs(x - m) for x in xs])


def pooled_std(a: List[float], b: List[float]) -> float:
    sa = std(a)
    sb = std(b)
    pooled = math.sqrt((sa * sa + sb * sb) / 2.0)
    return pooled if pooled > 1e-12 else 1e-12


def interval_overlap(a: List[float], b: List[float]) -> float:
    if not a or not b:
        return 0.0

    a_min, a_max = min(a), max(a)
    b_min, b_max = min(b), max(b)

    inter = max(0.0, min(a_max, b_max) - max(a_min, b_min))
    union = max(a_max, b_max) - min(a_min, b_min)

    if union <= 1e-12:
        return 0.0

    return inter / union


# ------------------------------------------------------------
# Kappa estimation from structured baseline
# Step 2 only
# ------------------------------------------------------------
def estimate_kappa(structured_rows: List[Dict], configs: List[Dict]) -> Tuple[float, float]:
    inv_vals = []
    inv2_vals = []

    for idx, row in enumerate(structured_rows):
        text = row["text"]

        inv_cfgs = [
            inv_local(text, cfg, base_seed=10000 + idx * 100 + j)
            for j, cfg in enumerate(configs)
        ]
        inv_vals.append(median(inv_cfgs))
        inv2_vals.append(inv2_local(text, configs))

    k1 = median(inv_vals) + 2.0 * mad(inv_vals)
    k2 = median(inv2_vals) + 2.0 * mad(inv2_vals)

    return k1, k2


# ------------------------------------------------------------
# Bootstrap order probability
# Step 4 only
# ------------------------------------------------------------
def bootstrap_order_probability(
    omega_s: List[float],
    omega_p: List[float],
    omega_r: List[float],
    n_resamples: int = BOOTSTRAP_RESAMPLES,
    seed: int = 999,
) -> float:
    rng = random.Random(seed)
    success = 0

    for _ in range(n_resamples):
        s = [rng.choice(omega_s) for _ in range(len(omega_s))]
        p = [rng.choice(omega_p) for _ in range(len(omega_p))]
        r = [rng.choice(omega_r) for _ in range(len(omega_r))]

        if mean(s) > mean(p) > mean(r):
            success += 1

    return success / n_resamples


# ------------------------------------------------------------
# Main benchmark
# ------------------------------------------------------------
def run_benchmark(
    dataset_path: str,
    tau: float = DEFAULT_TAU,
    min_effect: float = DEFAULT_MIN_EFFECT,
) -> None:
    rows = load_jsonl(dataset_path)

    grouped_rows = defaultdict(list)
    for row in rows:
        grouped_rows[row["class"]].append(row)

    structured_rows = grouped_rows["structured"]
    perturbed_rows = grouped_rows["perturbed"]
    random_rows = grouped_rows["random"]

    # ------------------------
    # Step 2: estimate kappa
    # ------------------------
    k1, k2 = estimate_kappa(structured_rows, F_CONFIGS)

    # ------------------------
    # Step 2: stability checks
    # ------------------------
    structured_stable = []

    for idx, row in enumerate(structured_rows):
        text = row["text"]

        inv_cfgs = [
            inv_local(text, cfg, base_seed=30000 + idx * 100 + j)
            for j, cfg in enumerate(F_CONFIGS)
        ]
        inv_x = median(inv_cfgs)
        inv2_x = inv2_local(text, F_CONFIGS)

        structured_stable.append((inv_x <= k1) and (inv2_x <= k2))

    p_stable = mean([1.0 if x else 0.0 for x in structured_stable])

    # ------------------------
    # Step 4: separability
    # Aggregate Omega across configs
    # ------------------------
    def omega_multi(text: str, seed_base: int) -> float:
        vals = []
        for i, cfg in enumerate(F_CONFIGS):
            perturbed = perturb_with_config(text, cfg, seed=seed_base + i)
            vals.append(omega_fn(perturbed))
        return mean(vals)

    omega_s = []
    omega_p = []
    omega_r = []

    for i, row in enumerate(structured_rows):
        omega_s.append(omega_multi(row["text"], 40000 + i * 10))

    for i, row in enumerate(perturbed_rows):
        omega_p.append(omega_multi(row["text"], 50000 + i * 10))

    for i, row in enumerate(random_rows):
        omega_r.append(omega_multi(row["text"], 60000 + i * 10))

    mean_s = mean(omega_s)
    mean_p = mean(omega_p)
    mean_r = mean(omega_r)

    delta_sp = mean_s - mean_p
    delta_pr = mean_p - mean_r

    d_sp = delta_sp / pooled_std(omega_s, omega_p)
    d_pr = delta_pr / pooled_std(omega_p, omega_r)

    overlap_sp = interval_overlap(omega_s, omega_p)
    overlap_pr = interval_overlap(omega_p, omega_r)

    p_order = bootstrap_order_probability(omega_s, omega_p, omega_r)

    # ------------------------
    # Final decision
    # Step 2 != Step 4
    # ------------------------
    ordering_ok = mean_s > mean_p > mean_r
    effect_ok = (d_sp > min_effect) and (d_pr > min_effect)
    bootstrap_ok = p_order >= tau
    stability_ok = p_stable >= 0.80

    # ------------------------
    # Report
    # ------------------------
    print("\n=== OMNIA VALIDATION REPORT ===\n")

    print("[STEP 2 - STABILITY]")
    print(f"k1 (Inv threshold):  {k1:.6f}")
    print(f"k2 (Inv2 threshold): {k2:.6f}")
    print(f"p_stable (structured): {p_stable:.4f}")

    print("\n[STEP 4 - SEPARABILITY]")
    print(f"E[Omega_s]: {mean_s:.6f}")
    print(f"E[Omega_p]: {mean_p:.6f}")
    print(f"E[Omega_r]: {mean_r:.6f}")

    print(f"\nDelta_sp: {delta_sp:.6f}")
    print(f"Delta_pr: {delta_pr:.6f}")

    print(f"\nd_sp: {d_sp:.6f}")
    print(f"d_pr: {d_pr:.6f}")

    print(f"\nOverlap(s,p): {overlap_sp:.6f}")
    print(f"Overlap(p,r): {overlap_pr:.6f}")

    print(f"\nP(order preserved): {p_order:.6f}")

    print("\n[DECISION FLAGS]")
    print(f"ordering_ok  : {ordering_ok}")
    print(f"effect_ok    : {effect_ok}")
    print(f"bootstrap_ok : {bootstrap_ok}")
    print(f"stability_ok : {stability_ok}")

    print("\n[FAILURE MODES]")
    if not ordering_ok:
        print("- FAIL: ordering violated")
    if ordering_ok and not effect_ok:
        print("- FAIL: positive gaps but weak effect size")
    if not bootstrap_ok:
        print("- FAIL: unstable ordering under bootstrap")
    if not stability_ok:
        print("- FAIL: Step 2 stability not sufficient")
    if ordering_ok and effect_ok and bootstrap_ok and stability_ok:
        print("- None")

    final_pass = ordering_ok and effect_ok and bootstrap_ok and stability_ok

    print("\n[FINAL RESULT]")
    if final_pass:
        print("PASS: structurally stable and discriminative under current pipeline")
    else:
        print("FAIL: pipeline or Omega does not yet support reliable structural signal")


if __name__ == "__main__":
    run_benchmark("data/baseline_B.jsonl")