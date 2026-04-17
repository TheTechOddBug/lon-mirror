import math
import re
from difflib import SequenceMatcher
from itertools import combinations


# ============================================================
# CONSISTENCY METRIC v1
#
# Goal:
# build a stronger consistency score than plain SequenceMatcher.
#
# Layers:
# - S_lex   : lexical backbone similarity
# - S_num   : numeric proximity / numeric stability
# - S_morph : morphological fingerprint stability
# - P_var   : dispersion penalty from pairwise variability
#
# Final form:
# consistency_v1 = base_score * (1 - dispersion_penalty)
#
# where:
# base_score = weighted mean of lexical, numeric, morphological signals
# ============================================================


# ============================================================
# TEXT NORMALIZATION
# ============================================================

UNCERTAINTY_PATTERNS = [
    r"\bmaybe\b",
    r"\bperhaps\b",
    r"\bprobably\b",
    r"\bi think\b",
    r"\bapproximately\b",
    r"\baround\b",
    r"\bnot sure\b",
]

EXPLANATION_PATTERNS = [
    r"\bbecause\b",
    r"\btherefore\b",
    r"\bso\b",
    r"\bsubtract\b",
    r"\badd\b",
    r"\bmultiply\b",
    r"\bdivid",
    r"\bcalculation\b",
    r"\bsolution\b",
]

EQUATION_PATTERNS = [
    r"=",
    r"\+",
    r"-",
    r"\*",
    r"/",
    r"\bx\b",
]


def normalize_text(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"\s+", " ", t)
    t = t.replace(",", "")
    t = t.replace("the answer is", "")
    t = t.replace("result:", "")
    t = t.replace("it equals", "")
    t = t.replace("answer:", "")
    t = t.replace("is the result", "")
    t = t.strip()
    return t


def tokenize(text: str):
    return re.findall(r"[a-z0-9]+", normalize_text(text))


def lexical_backbone(text: str) -> str:
    """
    Depowered lexical representation.
    Keeps alphanumerics only, strips noisy punctuation and normalizes space.
    """
    toks = tokenize(text)
    return " ".join(toks)


# ============================================================
# NUMERIC LAYER
# ============================================================

def extract_numbers(text: str):
    matches = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    nums = []
    for m in matches:
        try:
            nums.append(float(m))
        except ValueError:
            pass
    return nums


def final_numeric_value(text: str):
    nums = extract_numbers(text)
    if not nums:
        return None
    return nums[-1]


def numeric_proximity_score(a, b) -> float:
    """
    Compare final numeric values if both exist.
    Smooth proximity:
    score = 1 / (1 + relative_distance)

    If values are identical -> 1
    If values are close -> high but < 1
    If values are far -> lower
    """
    va = final_numeric_value(a)
    vb = final_numeric_value(b)

    if va is None and vb is None:
        return 1.0
    if va is None or vb is None:
        return 0.5

    if va == vb:
        return 1.0

    denom = max(abs(va), abs(vb), 1.0)
    rel_dist = abs(va - vb) / denom
    return 1.0 / (1.0 + rel_dist)


def numeric_shape_signature(text: str):
    """
    Additional numeric morphology:
    - has number?
    - count of numbers
    - length of final number (digits only)
    """
    nums = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    if not nums:
        return {
            "has_number": 0,
            "num_count": 0,
            "final_num_len": 0,
        }

    final_num = nums[-1].replace("-", "").replace(".", "")
    return {
        "has_number": 1,
        "num_count": len(nums),
        "final_num_len": len(final_num),
    }


# ============================================================
# MORPHOLOGICAL LAYER
# ============================================================

def contains_any(text: str, patterns) -> int:
    t = normalize_text(text)
    for p in patterns:
        if re.search(p, t):
            return 1
    return 0


def morphological_fingerprint(text: str):
    t = normalize_text(text)
    toks = tokenize(t)
    numbers = extract_numbers(t)

    fp = {
        "token_count_bucket": min(len(toks) // 3, 10),
        "char_count_bucket": min(len(t) // 10, 10),
        "has_number": 1 if numbers else 0,
        "number_count_bucket": min(len(numbers), 5),
        "has_equation_like": contains_any(t, EQUATION_PATTERNS),
        "has_uncertainty": contains_any(t, UNCERTAINTY_PATTERNS),
        "has_explanation": contains_any(t, EXPLANATION_PATTERNS),
        "is_single_token": 1 if len(toks) == 1 else 0,
        "is_short_answer": 1 if len(toks) <= 3 else 0,
    }

    fp.update({
        "final_num_len": numeric_shape_signature(t)["final_num_len"],
    })

    return fp


def morphological_similarity(a: str, b: str) -> float:
    fa = morphological_fingerprint(a)
    fb = morphological_fingerprint(b)

    keys = sorted(fa.keys())
    matches = 0.0
    total = 0.0

    for k in keys:
        va = fa[k]
        vb = fb[k]

        if isinstance(va, int) and isinstance(vb, int):
            # bounded similarity for integer-valued features
            denom = max(abs(va), abs(vb), 1)
            s = 1.0 - (abs(va - vb) / denom)
            s = max(0.0, min(1.0, s))
        else:
            s = 1.0 if va == vb else 0.0

        matches += s
        total += 1.0

    return matches / total if total > 0 else 1.0


# ============================================================
# LEXICAL LAYER
# ============================================================

def lexical_similarity(a: str, b: str) -> float:
    la = lexical_backbone(a)
    lb = lexical_backbone(b)
    return SequenceMatcher(None, la, lb).ratio()


# ============================================================
# PAIRWISE METRIC v1
# ============================================================

def pair_metric_v1(a: str, b: str, weights=None):
    """
    Weighted pairwise consistency.
    Default weights:
    - lexical backbone: 0.30
    - numeric proximity: 0.45
    - morphological similarity: 0.25
    """
    if weights is None:
        weights = {
            "lex": 0.30,
            "num": 0.45,
            "morph": 0.25,
        }

    s_lex = lexical_similarity(a, b)
    s_num = numeric_proximity_score(a, b)
    s_morph = morphological_similarity(a, b)

    base = (
        weights["lex"] * s_lex +
        weights["num"] * s_num +
        weights["morph"] * s_morph
    )

    return {
        "s_lex": s_lex,
        "s_num": s_num,
        "s_morph": s_morph,
        "pair_score": base,
    }


# ============================================================
# DISPERSION PENALTY
# ============================================================

def dispersion_penalty(pair_scores):
    """
    Penalize instability from spread and worst-case disagreement.

    penalty = 0.5 * normalized_std + 0.5 * (1 - min_score)

    bounded to [0, 0.5] to avoid over-crushing the score.
    """
    if not pair_scores:
        return 0.0

    mean_score = sum(pair_scores) / len(pair_scores)
    variance = sum((x - mean_score) ** 2 for x in pair_scores) / len(pair_scores)
    std = math.sqrt(variance)

    min_score = min(pair_scores)

    norm_std = min(std / 0.25, 1.0)  # 0.25 is a soft scale
    worst_gap = 1.0 - min_score

    penalty = 0.5 * norm_std + 0.5 * worst_gap
    penalty = min(max(penalty, 0.0), 0.5)

    return penalty


# ============================================================
# FAMILY-LEVEL CONSISTENCY
# ============================================================

def consistency_metric_v1(outputs, weights=None):
    """
    Compute family-level consistency_v1 over a list of outputs.
    """
    pairs = list(combinations(outputs, 2))

    if not pairs:
        return {
            "consistency_v1": 1.0,
            "base_score": 1.0,
            "dispersion_penalty": 0.0,
            "pair_details": [],
            "aggregates": {
                "mean_lex": 1.0,
                "mean_num": 1.0,
                "mean_morph": 1.0,
                "min_pair_score": 1.0,
                "max_pair_score": 1.0,
                "mean_pair_score": 1.0,
            }
        }

    pair_details = []
    pair_scores = []
    lex_scores = []
    num_scores = []
    morph_scores = []

    for idx, (a, b) in enumerate(pairs, start=1):
        res = pair_metric_v1(a, b, weights=weights)
        pair_details.append({
            "pair_id": idx,
            "a": a,
            "b": b,
            "s_lex": round(res["s_lex"], 6),
            "s_num": round(res["s_num"], 6),
            "s_morph": round(res["s_morph"], 6),
            "pair_score": round(res["pair_score"], 6),
        })
        pair_scores.append(res["pair_score"])
        lex_scores.append(res["s_lex"])
        num_scores.append(res["s_num"])
        morph_scores.append(res["s_morph"])

    base_score = sum(pair_scores) / len(pair_scores)
    penalty = dispersion_penalty(pair_scores)
    final_score = base_score * (1.0 - penalty)

    aggregates = {
        "mean_lex": round(sum(lex_scores) / len(lex_scores), 6),
        "mean_num": round(sum(num_scores) / len(num_scores), 6),
        "mean_morph": round(sum(morph_scores) / len(morph_scores), 6),
        "min_pair_score": round(min(pair_scores), 6),
        "max_pair_score": round(max(pair_scores), 6),
        "mean_pair_score": round(base_score, 6),
    }

    return {
        "consistency_v1": round(final_score, 6),
        "base_score": round(base_score, 6),
        "dispersion_penalty": round(penalty, 6),
        "pair_details": pair_details,
        "aggregates": aggregates,
    }


# ============================================================
# CLASSIFICATION
# ============================================================

def classify_consistency_v1(score: float) -> str:
    if score >= 0.85:
        return "invariant"
    if score >= 0.60:
        return "sensitive"
    return "degraded"


# ============================================================
# DEMO / LOCAL TEST
# ============================================================

if __name__ == "__main__":
    demo_outputs = [
        "56088",
        "The answer is 56088",
        "56088 is the result",
        "Result: 56080",
        "Approximately 56088",
    ]

    result = consistency_metric_v1(demo_outputs)

    print("CONSISTENCY METRIC v1")
    print("=" * 60)
    print(f"consistency_v1:      {result['consistency_v1']:.6f}")
    print(f"base_score:          {result['base_score']:.6f}")
    print(f"dispersion_penalty:  {result['dispersion_penalty']:.6f}")
    print(f"class:               {classify_consistency_v1(result['consistency_v1'])}")
    print()
    print("Aggregates:")
    for k, v in result["aggregates"].items():
        print(f"- {k}: {v}")
    print()
    print("Pair details:")
    for row in result["pair_details"]:
        print(
            f"pair {row['pair_id']:>2} | "
            f"s_lex={row['s_lex']:.4f} | "
            f"s_num={row['s_num']:.4f} | "
            f"s_morph={row['s_morph']:.4f} | "
            f"score={row['pair_score']:.4f}"
        )