import json
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATHS = [
    Path("examples/prime_candidates_1000_1200_scores.jsonl"),
    Path("examples/prime_candidates_1200_1400_scores.jsonl"),
    Path("examples/prime_candidates_2000_2200_scores.jsonl"),
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


def load_all_records(paths: List[Path]) -> List[Dict[str, Any]]:
    all_records: List[Dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Missing score file: {path}")
        all_records.extend(read_jsonl(path))
    return all_records


def digit_sum(n: int) -> int:
    return sum(int(ch) for ch in str(n))


def build_digit_sum_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for record in records:
        if "n" not in record or "is_prime" not in record:
            raise ValueError(f"Record missing required fields: {record}")

        n = int(record["n"])
        out.append(
            {
                "n": n,
                "is_prime": bool(record["is_prime"]),
                "digit_sum_score": digit_sum(n),
                "digit_sum_rank": None,
            }
        )
    return out


def assign_rank_desc_with_tiebreak(records: List[Dict[str, Any]], score_key: str, rank_key: str) -> None:
    ranked = sorted(
        records,
        key=lambda r: (-r[score_key], r["n"])
    )
    for idx, record in enumerate(ranked, start=1):
        record[rank_key] = idx


def summarize(records: List[Dict[str, Any]]) -> Dict[str, float]:
    ranked = sorted(records, key=lambda r: r["digit_sum_rank"])
    total = len(ranked)
    total_primes = sum(1 for r in ranked if r["is_prime"])

    top10 = ranked[:10]
    top20 = ranked[:20]

    top10_primes = sum(1 for r in top10 if r["is_prime"])
    top20_primes = sum(1 for r in top20 if r["is_prime"])

    prime_ranks = [r["digit_sum_rank"] for r in ranked if r["is_prime"]]
    nonprime_ranks = [r["digit_sum_rank"] for r in ranked if not r["is_prime"]]

    return {
        "total": total,
        "total_primes": total_primes,
        "density": total_primes / total,
        "top10_primes": top10_primes,
        "top20_primes": top20_primes,
        "mean_prime_rank": sum(prime_ranks) / len(prime_ranks),
        "mean_nonprime_rank": sum(nonprime_ranks) / len(nonprime_ranks),
    }


def main() -> None:
    source_records = load_all_records(INPUT_PATHS)
    records = build_digit_sum_records(source_records)
    assign_rank_desc_with_tiebreak(records, score_key="digit_sum_score", rank_key="digit_sum_rank")
    summary = summarize(records)

    print("=== DIGIT SUM BASELINE ===")
    print(f"Total candidates: {summary['total']}")
    print(f"Total primes: {summary['total_primes']}")
    print(f"Natural prime density: {summary['density']:.6f}")
    print()
    print(f"Top 10 primes: {summary['top10_primes']}")
    print(f"Top 20 primes: {summary['top20_primes']}")
    print(f"Mean prime rank: {summary['mean_prime_rank']:.6f}")
    print(f"Mean non-prime rank: {summary['mean_nonprime_rank']:.6f}")
    print()
    print("Top 15 by digit sum score:")
    ranked = sorted(records, key=lambda r: r["digit_sum_rank"])
    for record in ranked[:15]:
        print(
            f"rank={record['digit_sum_rank']:>2} | "
            f"n={record['n']} | "
            f"is_prime={record['is_prime']} | "
            f"digit_sum_score={record['digit_sum_score']}"
        )


if __name__ == "__main__":
    main()