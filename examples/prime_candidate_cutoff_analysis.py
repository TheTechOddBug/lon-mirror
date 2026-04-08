import json
import math
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATHS = [
    Path("examples/prime_candidates_1000_1200_scores.jsonl"),
    Path("examples/prime_candidates_1200_1400_scores.jsonl"),
    Path("examples/prime_candidates_2000_2200_scores.jsonl"),
]

CUTOFFS = [0.05, 0.10, 0.20, 0.25, 0.50]


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


def validate_records(records: List[Dict[str, Any]]) -> None:
    seen = set()
    for record in records:
        if "n" not in record or "is_prime" not in record or "omnia_score" not in record:
            raise ValueError(f"Record missing required fields: {record}")

        n = int(record["n"])
        if n in seen:
            raise ValueError(f"Duplicate candidate detected across merged files: {n}")
        seen.add(n)

        if not isinstance(record["is_prime"], bool):
            raise TypeError(f"is_prime must be bool for n={n}")

        if not isinstance(record["omnia_score"], (int, float)):
            raise TypeError(f"omnia_score must be numeric for n={n}")


def analyze_cutoffs(records: List[Dict[str, Any]], cutoffs: List[float]) -> List[Dict[str, Any]]:
    ranked = sorted(records, key=lambda r: r["omnia_score"], reverse=True)

    total_candidates = len(ranked)
    total_primes = sum(1 for r in ranked if r["is_prime"])

    results: List[Dict[str, Any]] = []
    for cutoff in cutoffs:
        keep_n = max(1, math.ceil(total_candidates * cutoff))
        subset = ranked[:keep_n]
        primes_kept = sum(1 for r in subset if r["is_prime"])

        recall = primes_kept / total_primes if total_primes > 0 else 0.0
        density = primes_kept / keep_n if keep_n > 0 else 0.0

        results.append(
            {
                "cutoff": cutoff,
                "candidates_kept": keep_n,
                "primes_kept": primes_kept,
                "prime_recall": recall,
                "prime_density": density,
            }
        )

    return results


def print_summary(records: List[Dict[str, Any]], results: List[Dict[str, Any]]) -> None:
    total_candidates = len(records)
    total_primes = sum(1 for r in records if r["is_prime"])
    baseline_density = total_primes / total_candidates if total_candidates > 0 else 0.0

    print("=== OMNIA PRIME CANDIDATE CUTOFF ANALYSIS ===")
    print(f"Total candidates: {total_candidates}")
    print(f"Total primes: {total_primes}")
    print(f"Natural prime density: {baseline_density:.6f}")
    print()
    print(
        f"{'cutoff':>8} | {'kept':>6} | {'primes':>6} | {'recall':>10} | {'density':>10} | {'lift':>10}"
    )
    print("-" * 68)

    for row in results:
        lift = row["prime_density"] / baseline_density if baseline_density > 0 else 0.0
        print(
            f"{row['cutoff']*100:7.0f}% | "
            f"{row['candidates_kept']:6d} | "
            f"{row['primes_kept']:6d} | "
            f"{row['prime_recall']:9.4f} | "
            f"{row['prime_density']:9.4f} | "
            f"{lift:9.4f}"
        )


def main() -> None:
    records = load_all_records(INPUT_PATHS)
    validate_records(records)
    results = analyze_cutoffs(records, CUTOFFS)
    print_summary(records, results)


if __name__ == "__main__":
    main()