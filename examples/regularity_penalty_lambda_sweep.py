import json
import math
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATHS = [
    Path("examples/prime_candidates_1000_1200_scores.jsonl"),
    Path("examples/prime_candidates_1200_1400_scores.jsonl"),
    Path("examples/prime_candidates_2000_2200_scores.jsonl"),
]

OUTPUT_PATH = Path("examples/regularity_penalty_lambda_sweep_results.json")

BASES = list(range(2, 17))
LAMBDAS = [0.00, 0.01, 0.02, 0.03, 0.05, 0.08]

TRACK_NUMBERS = [1007, 2021, 2047, 1009, 2017, 2039]


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


def load_all_records(paths: List[Path]) -> List[Dict[str, Any]]:
    all_records: List[Dict[str, Any]] = []
    seen = set()

    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Missing score file: {path}")

        for record in read_jsonl(path):
            if "n" not in record or "is_prime" not in record or "omnia_score" not in record:
                raise ValueError(f"Missing required fields in record: {record}")

            n = int(record["n"])
            if n in seen:
                raise ValueError(f"Duplicate candidate across merged files: {n}")
            seen.add(n)

            if not isinstance(record["is_prime"], bool):
                raise TypeError(f"is_prime must be bool for n={n}")

            if not isinstance(record["omnia_score"], (int, float)):
                raise TypeError(f"omnia_score must be numeric for n={n}")

            all_records.append(
                {
                    "n": n,
                    "is_prime": record["is_prime"],
                    "omnia_score": float(record["omnia_score"]),
                }
            )

    return all_records


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

    return {
        "avg_entropy": avg_entropy,
        "avg_dominance": avg_dominance,
        "avg_run_ratio": avg_run_ratio,
        "avg_pal_closeness": avg_pal_closeness,
    }


def attach_penalties(records: List[Dict[str, Any]]) -> None:
    raw_penalties: List[float] = []

    for record in records:
        metrics = build_regularity_metrics(record["n"])
        record.update(metrics)

        raw_penalty = (
            0.35 * (1.0 / (1.0 + metrics["avg_entropy"])) +
            0.25 * metrics["avg_dominance"] +
            0.25 * metrics["avg_run_ratio"] +
            0.15 * metrics["avg_pal_closeness"]
        )
        record["regularity_penalty_raw"] = raw_penalty
        raw_penalties.append(raw_penalty)

    min_pen = min(raw_penalties)
    max_pen = max(raw_penalties)

    if max_pen == min_pen:
        for record in records:
            record["regularity_penalty_norm"] = 0.0
        return

    for record in records:
        norm = (record["regularity_penalty_raw"] - min_pen) / (max_pen - min_pen)
        record["regularity_penalty_norm"] = norm


def assign_rank(records: List[Dict[str, Any]], score_key: str, rank_key: str) -> None:
    ranked = sorted(records, key=lambda r: r[score_key], reverse=True)
    for idx, record in enumerate(ranked, start=1):
        record[rank_key] = idx


def summarize(records: List[Dict[str, Any]], score_key: str, rank_key: str) -> Dict[str, float]:
    ranked = sorted(records, key=lambda r: r[score_key], reverse=True)

    top10 = ranked[:10]
    top20 = ranked[:20]

    top10_primes = sum(1 for r in top10 if r["is_prime"])
    top20_primes = sum(1 for r in top20 if r["is_prime"])

    prime_ranks = [r[rank_key] for r in ranked if r["is_prime"]]
    nonprime_ranks = [r[rank_key] for r in ranked if not r["is_prime"]]

    return {
        "top10_primes": top10_primes,
        "top20_primes": top20_primes,
        "mean_prime_rank": sum(prime_ranks) / len(prime_ranks),
        "mean_nonprime_rank": sum(nonprime_ranks) / len(nonprime_ranks),
    }


def run_lambda(records: List[Dict[str, Any]], lam: float) -> Dict[str, Any]:
    working = [dict(r) for r in records]

    for record in working:
        record["adjusted_score"] = record["omnia_score"] - lam * record["regularity_penalty_norm"]

    assign_rank(working, score_key="adjusted_score", rank_key="adjusted_rank")
    summary = summarize(working, score_key="adjusted_score", rank_key="adjusted_rank")

    by_n = {r["n"]: r for r in working}
    tracked = {}
    for n in TRACK_NUMBERS:
        r = by_n[n]
        tracked[str(n)] = {
            "is_prime": r["is_prime"],
            "raw_score": r["omnia_score"],
            "pen_norm": r["regularity_penalty_norm"],
            "adjusted_score": r["adjusted_score"],
            "adjusted_rank": r["adjusted_rank"],
        }

    return {
        "lambda": lam,
        "summary": summary,
        "tracked": tracked,
    }


def print_results(results: List[Dict[str, Any]]) -> None:
    print("=== REGULARITY PENALTY LAMBDA SWEEP ===")
    print()
    print(
        f"{'lambda':>8} | {'top10':>5} | {'top20':>5} | {'mean_prime':>11} | {'mean_nonprime':>14} | {'gap':>9}"
    )
    print("-" * 72)

    for row in results:
        lam = row["lambda"]
        s = row["summary"]
        gap = s["mean_nonprime_rank"] - s["mean_prime_rank"]
        print(
            f"{lam:8.2f} | "
            f"{s['top10_primes']:5d} | "
            f"{s['top20_primes']:5d} | "
            f"{s['mean_prime_rank']:11.6f} | "
            f"{s['mean_nonprime_rank']:14.6f} | "
            f"{gap:9.6f}"
        )

    print("\n=== TRACKED NUMBERS BY LAMBDA ===")
    for n in TRACK_NUMBERS:
        print(f"\n--- n = {n} ---")
        print(f"{'lambda':>8} | {'adj_rank':>8} | {'adj_score':>10} | {'pen_norm':>8}")
        print("-" * 44)
        for row in results:
            t = row["tracked"][str(n)]
            print(
                f"{row['lambda']:8.2f} | "
                f"{t['adjusted_rank']:8d} | "
                f"{t['adjusted_score']:10.6f} | "
                f"{t['pen_norm']:8.4f}"
            )


def main() -> None:
    records = load_all_records(INPUT_PATHS)
    attach_penalties(records)

    results: List[Dict[str, Any]] = []
    for lam in LAMBDAS:
        results.append(run_lambda(records, lam))

    print_results(results)

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()