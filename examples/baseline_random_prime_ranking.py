import json
import random
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATHS = [
    Path("examples/prime_candidates_1000_1200_scores.jsonl"),
    Path("examples/prime_candidates_1200_1400_scores.jsonl"),
    Path("examples/prime_candidates_2000_2200_scores.jsonl"),
]

N_RUNS = 10000
RANDOM_SEED = 42


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


def summarize_omnia(records: List[Dict[str, Any]]) -> Dict[str, float]:
    ranked = sorted(records, key=lambda r: r["omnia_score"], reverse=True)
    total = len(ranked)
    total_primes = sum(1 for r in ranked if r["is_prime"])

    top10 = ranked[:10]
    top20 = ranked[:20]

    top10_primes = sum(1 for r in top10 if r["is_prime"])
    top20_primes = sum(1 for r in top20 if r["is_prime"])

    prime_ranks = [idx for idx, r in enumerate(ranked, start=1) if r["is_prime"]]
    nonprime_ranks = [idx for idx, r in enumerate(ranked, start=1) if not r["is_prime"]]

    return {
        "total": total,
        "total_primes": total_primes,
        "density": total_primes / total,
        "top10_primes": top10_primes,
        "top20_primes": top20_primes,
        "mean_prime_rank": sum(prime_ranks) / len(prime_ranks),
        "mean_nonprime_rank": sum(nonprime_ranks) / len(nonprime_ranks),
    }


def simulate_random_baseline(records: List[Dict[str, Any]], n_runs: int, seed: int) -> Dict[str, float]:
    rng = random.Random(seed)
    base = list(records)

    top10_counts: List[int] = []
    top20_counts: List[int] = []
    mean_prime_ranks: List[float] = []
    mean_nonprime_ranks: List[float] = []

    for _ in range(n_runs):
        shuffled = base[:]
        rng.shuffle(shuffled)

        top10 = shuffled[:10]
        top20 = shuffled[:20]

        top10_counts.append(sum(1 for r in top10 if r["is_prime"]))
        top20_counts.append(sum(1 for r in top20 if r["is_prime"]))

        prime_ranks = [idx for idx, r in enumerate(shuffled, start=1) if r["is_prime"]]
        nonprime_ranks = [idx for idx, r in enumerate(shuffled, start=1) if not r["is_prime"]]

        mean_prime_ranks.append(sum(prime_ranks) / len(prime_ranks))
        mean_nonprime_ranks.append(sum(nonprime_ranks) / len(nonprime_ranks))

    return {
        "top10_primes_mean": sum(top10_counts) / len(top10_counts),
        "top20_primes_mean": sum(top20_counts) / len(top20_counts),
        "mean_prime_rank_mean": sum(mean_prime_ranks) / len(mean_prime_ranks),
        "mean_nonprime_rank_mean": sum(mean_nonprime_ranks) / len(mean_nonprime_ranks),
    }


def main() -> None:
    records = load_all_records(INPUT_PATHS)
    omnia = summarize_omnia(records)
    random_baseline = simulate_random_baseline(records, n_runs=N_RUNS, seed=RANDOM_SEED)

    print("=== OMNIA vs RANDOM BASELINE ===")
    print(f"Total candidates: {omnia['total']}")
    print(f"Total primes: {omnia['total_primes']}")
    print(f"Natural prime density: {omnia['density']:.6f}")
    print()
    print("--- OMNIA observed ---")
    print(f"Top 10 primes: {omnia['top10_primes']}")
    print(f"Top 20 primes: {omnia['top20_primes']}")
    print(f"Mean prime rank: {omnia['mean_prime_rank']:.6f}")
    print(f"Mean non-prime rank: {omnia['mean_nonprime_rank']:.6f}")
    print()
    print("--- Random baseline expected ---")
    print(f"Top 10 primes mean: {random_baseline['top10_primes_mean']:.6f}")
    print(f"Top 20 primes mean: {random_baseline['top20_primes_mean']:.6f}")
    print(f"Mean prime rank mean: {random_baseline['mean_prime_rank_mean']:.6f}")
    print(f"Mean non-prime rank mean: {random_baseline['mean_nonprime_rank_mean']:.6f}")
    print()
    print("--- Lift over random ---")
    print(f"Top 10 lift: {omnia['top10_primes'] / random_baseline['top10_primes_mean']:.6f}")
    print(f"Top 20 lift: {omnia['top20_primes'] / random_baseline['top20_primes_mean']:.6f}")
    print(f"Prime rank improvement: {random_baseline['mean_prime_rank_mean'] - omnia['mean_prime_rank']:.6f}")
    print(f"Non-prime rank separation: {omnia['mean_nonprime_rank'] - omnia['mean_prime_rank']:.6f}")


if __name__ == "__main__":
    main()