from __future__ import annotations

import json
import math
import random
from collections import defaultdict
from statistics import mean, median

from omnia.lenses.base_lens import OmniabaseLens


def build_random_integers(n: int, low: int = 10_000, high: int = 999_999) -> list[int]:
    return [random.randint(low, high) for _ in range(n)]


def build_repeated_pattern_integers(n: int) -> list[int]:
    values: list[int] = []
    seeds = ["1", "2", "3", "7", "9", "12", "21", "37", "101", "121"]
    i = 0
    while len(values) < n:
        seed = seeds[i % len(seeds)]
        reps = 3 + (i % 4)
        s = seed * reps
        values.append(int(s[:18]))
        i += 1
    return values


def build_powers(n: int) -> list[int]:
    values: list[int] = []
    k = 0
    while len(values) < n:
        candidate = 2 ** (10 + k)
        if candidate >= 10_000:
            values.append(candidate)
        k += 1
    return values[:n]


def build_arithmetic_constructions(n: int) -> list[int]:
    values: list[int] = []
    start = 12345
    step = 6789
    for i in range(n):
        values.append(start + i * step)
    return values


def build_prime_subset(n: int, low: int = 10_000, high: int = 200_000) -> list[int]:
    values: list[int] = []
    candidate = low
    while len(values) < n and candidate <= high:
        if is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return values


def build_logistic_mapped_integers(n: int, x0: float = 0.217, r: float = 3.91) -> list[int]:
    values: list[int] = []
    x = x0
    for _ in range(n):
        x = r * x * (1.0 - x)
        mapped = int(10_000 + x * 900_000)
        values.append(mapped)
    return values


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    limit = int(math.isqrt(x))
    for d in range(3, limit + 1, 2):
        if x % d == 0:
            return False
    return True


def summarize_metric(values: list[float]) -> dict[str, float]:
    return {
        "mean": round(mean(values), 6),
        "median": round(median(values), 6),
        "min": round(min(values), 6),
        "max": round(max(values), 6),
    }


def summarize_int_metric(values: list[int]) -> dict[str, float]:
    return {
        "mean": round(mean(values), 6),
        "median": round(median(values), 6),
        "min": int(min(values)),
        "max": int(max(values)),
    }


def main() -> None:
    random.seed(42)

    lens = OmniabaseLens(
        bases=list(range(2, 17)),
        collapse_threshold=0.20,
    )

    n = 30

    datasets: dict[str, list[int]] = {
        "random": build_random_integers(n),
        "repeated_pattern": build_repeated_pattern_integers(n),
        "powers_of_two": build_powers(n),
        "arithmetic_construction": build_arithmetic_constructions(n),
        "prime_subset": build_prime_subset(n),
        "logistic_mapped": build_logistic_mapped_integers(n),
    }

    raw_results: dict[str, list[dict]] = defaultdict(list)
    summary: dict[str, dict] = {}

    for class_name, values in datasets.items():
        for value in values:
            result = lens.evaluate(value)
            raw_results[class_name].append(
                {
                    "value": value,
                    "cross_base_stability": result.cross_base_stability,
                    "representation_drift": result.representation_drift,
                    "base_sensitivity": result.base_sensitivity,
                    "collapse_count": result.collapse_count,
                }
            )

    for class_name, items in raw_results.items():
        summary[class_name] = {
            "sample_size": len(items),
            "cross_base_stability": summarize_metric(
                [item["cross_base_stability"] for item in items]
            ),
            "representation_drift": summarize_metric(
                [item["representation_drift"] for item in items]
            ),
            "base_sensitivity": summarize_metric(
                [item["base_sensitivity"] for item in items]
            ),
            "collapse_count": summarize_int_metric(
                [item["collapse_count"] for item in items]
            ),
        }

    payload = {
        "benchmark_name": "OMNIABASE Lens Synthetic Benchmark v0",
        "bases": lens.bases,
        "collapse_threshold": lens.collapse_threshold,
        "classes": list(datasets.keys()),
        "summary": summary,
        "raw_results": raw_results,
    }

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()