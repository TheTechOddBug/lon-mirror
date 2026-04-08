import json
from pathlib import Path
from typing import Any, Dict, List


CANDIDATES_PATH = Path("examples/prime_candidates_1200_1400.jsonl")
TRUTH_PATH = Path("examples/prime_candidates_1200_1400_truth.jsonl")
OUTPUT_PATH = Path("examples/prime_candidates_1200_1400_scores.jsonl")


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


def load_truth_map(records: List[Dict[str, Any]]) -> Dict[int, bool]:
    truth_map: Dict[int, bool] = {}
    for record in records:
        if "n" not in record or "is_prime" not in record:
            raise ValueError(f"Truth record missing required fields: {record}")
        n = int(record["n"])
        is_prime = bool(record["is_prime"])
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

    return values


def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = []
    value = n
    while value > 0:
        value, rem = divmod(value, base)
        out.append(digits[rem])
    return "".join(reversed(out))


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


def compute_omnia_score(n: int) -> float:
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


def assign_rank_desc(records: List[Dict[str, Any]], score_key: str, rank_key: str) -> None:
    scores = [record[score_key] for record in records]

    if len(set(scores)) != len(scores):
        raise ValueError(
            "Exact score tie detected. Rank is undefined under the current strict rule."
        )

    ranked = sorted(records, key=lambda r: r[score_key], reverse=True)
    for idx, record in enumerate(ranked, start=1):
        record[rank_key] = idx


def summarize(records: List[Dict[str, Any]]) -> None:
    total = len(records)
    total_primes = sum(1 for r in records if r["is_prime"])
    ranked = sorted(records, key=lambda r: r["omnia_score"], reverse=True)
    top_10 = ranked[:10]
    top_20 = ranked[:20]

    top_10_primes = sum(1 for r in top_10 if r["is_prime"])
    top_20_primes = sum(1 for r in top_20 if r["is_prime"])

    print(f"Total candidates: {total}")
    print(f"Total primes: {total_primes}")
    print(f"Top 10 primes: {top_10_primes} / 10")
    print(f"Top 20 primes: {top_20_primes} / 20")

    prime_ranks = sorted(r["omnia_rank"] for r in records if r["is_prime"])
    nonprime_ranks = sorted(r["omnia_rank"] for r in records if not r["is_prime"])

    mean_prime_rank = sum(prime_ranks) / len(prime_ranks)
    mean_nonprime_rank = sum(nonprime_ranks) / len(nonprime_ranks)

    print(f"Mean prime rank: {mean_prime_rank:.4f}")
    print(f"Mean non-prime rank: {mean_nonprime_rank:.4f}")

    print("\nTop 15 by OMNIA score:")
    for record in ranked[:15]:
        print(
            f"rank={record['omnia_rank']:>2} | "
            f"n={record['n']} | "
            f"is_prime={record['is_prime']} | "
            f"omnia_score={record['omnia_score']:.6f}"
        )


def main() -> None:
    candidate_records = read_jsonl(CANDIDATES_PATH)
    truth_records = read_jsonl(TRUTH_PATH)

    truth_map = load_truth_map(truth_records)
    candidates = validate_candidates(candidate_records, truth_map)

    scored_records: List[Dict[str, Any]] = []
    for n in candidates:
        score = compute_omnia_score(n)

        if not isinstance(score, (int, float)):
            raise TypeError(
                f"compute_omnia_score must return int or float, got {type(score).__name__}"
            )

        scored_records.append(
            {
                "n": n,
                "is_prime": truth_map[n],
                "omnia_score": float(score),
                "omnia_rank": None,
            }
        )

    assign_rank_desc(scored_records, score_key="omnia_score", rank_key="omnia_rank")
    write_jsonl(OUTPUT_PATH, scored_records)
    summarize(scored_records)

    print(f"\nWrote scored candidates to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()