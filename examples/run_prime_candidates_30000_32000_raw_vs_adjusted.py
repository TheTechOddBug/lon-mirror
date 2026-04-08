import json
import math
from pathlib import Path
from typing import Any, Dict, List


CANDIDATES_PATH = Path("examples/prime_candidates_30000_32000.jsonl")
TRUTH_PATH = Path("examples/prime_candidates_30000_32000_truth.jsonl")
OUTPUT_PATH = Path("examples/prime_candidates_30000_32000_raw_vs_adjusted_scores.jsonl")

BASES = list(range(2, 17))
LAMBDA = 0.03

TRACK_NUMBERS = [
    30007,
    30011,
    30013,
    30029,
    30031,
    30203,
    30323,
    30941,
    31337,
    31397,
    31721,
]


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}: {e}") from e
    return records


def write_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def to_base(n: int, base: int) -> str:
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if n == 0:
        return "0"

    value = n
    out: List[str] = []
    while value > 0:
        value, rem = divmod(value, base)
        out.append(digits[rem])
    return "".join(reversed(out))


def shannon_entropy(rep: str) -> float:
    if not rep:
        return 0.0

    counts: Dict[str, int] = {}
    for ch in rep:
        counts[ch] = counts.get(ch, 0) + 1

    ent = 0.0
    n = len(rep)
    for count in counts.values():
        p = count / n
        ent -= p * math.log2(p)
    return ent


def dominant_char_ratio(rep: str) -> float:
    if not rep:
        return 0.0
    counts = [rep.count(ch) for ch in set(rep)]
    return max(counts) / len(rep)


def max_run_ratio(rep: str) -> float:
    if not rep:
        return 0.0

    best = 1
    cur = 1
    for i in range(1, len(rep)):
        if rep[i] == rep[i - 1]:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best / len(rep)


def palindrome_mismatch_ratio(rep: str) -> float:
    n = len(rep)
    if n <= 1:
        return 0.0

    pairs = n // 2
    if pairs == 0:
        return 0.0

    mismatches = 0
    for i in range(pairs):
        if rep[i] != rep[n - 1 - i]:
            mismatches += 1

    return mismatches / pairs


def build_number_features(n: int) -> Dict[str, Any]:
    decimal_str = str(n)

    bases = {
        2: format(n, "b"),
        3: to_base(n, 3),
        4: to_base(n, 4),
        5: to_base(n, 5),
        6: to_base(n, 6),
        7: to_base(n, 7),
        8: format(n, "o"),
        9: to_base(n, 9),
        10: decimal_str,
        12: to_base(n, 12),
        16: format(n, "x"),
    }

    return {
        "n": n,
        "decimal_str": decimal_str,
        "digit_sum_10": sum(int(ch) for ch in decimal_str),
        "length_10": len(decimal_str),
        "bases": bases,
    }


def compute_raw_omnia_score(n: int) -> float:
    from omnia.engine import run_omnia_totale

    features = build_number_features(n)

    tokens: List[str] = []
    tokens.append(f"n={features['n']}")
    tokens.append(f"digit_sum_10={features['digit_sum_10']}")
    tokens.append(f"length_10={features['length_10']}")

    for base, rep in sorted(features["bases"].items()):
        tokens.append(f"b{base}:{rep}")

    token_numbers = [len(token) for token in tokens]

    result = run_omnia_totale(
        extra={
            "tokens": tokens,
            "token_numbers": token_numbers,
        }
    )

    return float(result.omega_total)


def build_regularity_metrics(n: int) -> Dict[str, float]:
    entropy_sum = 0.0
    dom_sum = 0.0
    run_sum = 0.0
    pal_closeness_sum = 0.0

    for base in BASES:
        rep = to_base(n, base)
        entropy_sum += shannon_entropy(rep)
        dom_sum += dominant_char_ratio(rep)
        run_sum += max_run_ratio(rep)
        pal_closeness_sum += (1.0 - palindrome_mismatch_ratio(rep))

    n_bases = len(BASES)

    avg_entropy = entropy_sum / n_bases
    avg_dominance = dom_sum / n_bases
    avg_run_ratio = run_sum / n_bases
    avg_pal_closeness = pal_closeness_sum / n_bases

    raw_penalty = (
        0.35 * (1.0 / (1.0 + avg_entropy)) +
        0.25 * avg_dominance +
        0.25 * avg_run_ratio +
        0.15 * avg_pal_closeness
    )

    return {
        "avg_entropy": avg_entropy,
        "avg_dominance": avg_dominance,
        "avg_run_ratio": avg_run_ratio,
        "avg_pal_closeness": avg_pal_closeness,
        "regularity_penalty_raw": raw_penalty,
    }


def load_truth_map(path: Path) -> Dict[int, bool]:
    truth_records = read_jsonl(path)
    truth_map: Dict[int, bool] = {}

    for record in truth_records:
        if "n" not in record or "is_prime" not in record:
            raise ValueError(f"Truth record missing required fields: {record}")

        n = int(record["n"])
        is_prime = bool(record["is_prime"])

        if n in truth_map:
            raise ValueError(f"Duplicate truth entry for n={n}")

        truth_map[n] = is_prime

    return truth_map


def validate_candidates(candidate_records: List[Dict[str, Any]], truth_map: Dict[int, bool]) -> List[int]:
    values: List[int] = []
    seen = set()

    for record in candidate_records:
        if "n" not in record:
            raise ValueError(f"Candidate record missing 'n': {record}")

        n = int(record["n"])

        if n in seen:
            raise ValueError(f"Duplicate candidate found: {n}")
        seen.add(n)

        if n not in truth_map:
            raise ValueError(f"Candidate {n} not found in truth file")

        values.append(n)

    if len(truth_map) != len(values):
        missing = sorted(set(truth_map.keys()) - set(values))
        extra = sorted(set(values) - set(truth_map.keys()))
        raise ValueError(
            "Candidate/truth mismatch. "
            f"truth_only={missing[:10]} "
            f"candidate_only={extra[:10]}"
        )

    return values


def assign_rank(records: List[Dict[str, Any]], score_key: str, rank_key: str) -> None:
    ranked = sorted(records, key=lambda r: r[score_key], reverse=True)
    for idx, record in enumerate(ranked, start=1):
        record[rank_key] = idx


def summarize(records: List[Dict[str, Any]], rank_key: str) -> Dict[str, float]:
    ranked = sorted(records, key=lambda r: r[rank_key])

    total = len(ranked)
    total_primes = sum(1 for r in ranked if r["is_prime"])

    top10 = ranked[:10]
    top20 = ranked[:20]

    top10_primes = sum(1 for r in top10 if r["is_prime"])
    top20_primes = sum(1 for r in top20 if r["is_prime"])

    prime_ranks = [r[rank_key] for r in ranked if r["is_prime"]]
    nonprime_ranks = [r[rank_key] for r in ranked if not r["is_prime"]]

    return {
        "total": total,
        "total_primes": total_primes,
        "density": total_primes / total,
        "top10_primes": top10_primes,
        "top20_primes": top20_primes,
        "mean_prime_rank": sum(prime_ranks) / len(prime_ranks),
        "mean_nonprime_rank": sum(nonprime_ranks) / len(nonprime_ranks),
    }


def print_tracked(records: List[Dict[str, Any]]) -> None:
    by_n = {r["n"]: r for r in records}

    print("\n=== TRACKED NUMBERS ===")
    print(
        f"{'n':>6} | {'prime':>5} | {'raw_rank':>8} | {'adj_rank':>8} | "
        f"{'raw_score':>10} | {'adj_score':>10} | {'pen_norm':>8}"
    )
    print("-" * 88)

    for n in TRACK_NUMBERS:
        if n not in by_n:
            continue
        r = by_n[n]
        print(
            f"{r['n']:6d} | "
            f"{str(r['is_prime']):>5} | "
            f"{r['raw_rank']:8d} | "
            f"{r['adjusted_rank']:8d} | "
            f"{r['raw_omnia_score']:10.6f} | "
            f"{r['adjusted_score']:10.6f} | "
            f"{r['regularity_penalty_norm']:8.4f}"
        )


def main() -> None:
    candidate_records = read_jsonl(CANDIDATES_PATH)
    truth_map = load_truth_map(TRUTH_PATH)
    candidates = validate_candidates(candidate_records, truth_map)

    records: List[Dict[str, Any]] = []
    raw_penalties: List[float] = []

    for n in candidates:
        raw_score = compute_raw_omnia_score(n)
        reg = build_regularity_metrics(n)

        record = {
            "n": n,
            "is_prime": truth_map[n],
            "raw_omnia_score": raw_score,
            **reg,
            "regularity_penalty_norm": None,
            "adjusted_score": None,
            "raw_rank": None,
            "adjusted_rank": None,
        }
        records.append(record)
        raw_penalties.append(reg["regularity_penalty_raw"])

    min_pen = min(raw_penalties)
    max_pen = max(raw_penalties)

    if max_pen == min_pen:
        for record in records:
            record["regularity_penalty_norm"] = 0.0
            record["adjusted_score"] = record["raw_omnia_score"]
    else:
        for record in records:
            norm = (record["regularity_penalty_raw"] - min_pen) / (max_pen - min_pen)
            record["regularity_penalty_norm"] = norm
            record["adjusted_score"] = record["raw_omnia_score"] - LAMBDA * norm

    assign_rank(records, score_key="raw_omnia_score", rank_key="raw_rank")
    assign_rank(records, score_key="adjusted_score", rank_key="adjusted_rank")

    raw_summary = summarize(records, rank_key="raw_rank")
    adjusted_summary = summarize(records, rank_key="adjusted_rank")

    print("=== PRIME CANDIDATES 30000-32000 ===")
    print(f"Lambda: {LAMBDA:.6f}")
    print(f"Total candidates: {raw_summary['total']}")
    print(f"Total primes: {raw_summary['total_primes']}")
    print(f"Natural prime density: {raw_summary['density']:.6f}")
    print()

    print("--- RAW OMNIA ---")
    print(f"Top 10 primes: {raw_summary['top10_primes']}")
    print(f"Top 20 primes: {raw_summary['top20_primes']}")
    print(f"Mean prime rank: {raw_summary['mean_prime_rank']:.6f}")
    print(f"Mean non-prime rank: {raw_summary['mean_nonprime_rank']:.6f}")
    print()

    print("--- ADJUSTED OMNIA (lambda = 0.03) ---")
    print(f"Top 10 primes: {adjusted_summary['top10_primes']}")
    print(f"Top 20 primes: {adjusted_summary['top20_primes']}")
    print(f"Mean prime rank: {adjusted_summary['mean_prime_rank']:.6f}")
    print(f"Mean non-prime rank: {adjusted_summary['mean_nonprime_rank']:.6f}")

    print_tracked(records)

    output_records = sorted(records, key=lambda r: r["adjusted_rank"])
    write_jsonl(OUTPUT_PATH, output_records)

    print(f"\nWrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()