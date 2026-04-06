import json
from collections import defaultdict
from statistics import mean
from omnia_semantic_decoupling_v10_0 import semantic_decoupling_score


def load_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def main():
    data = load_data("data/temperature_outputs.jsonl")

    buckets = defaultdict(list)

    for x in data:
        t = x["temperature"]
        score = semantic_decoupling_score(x["text"], seed=42)
        buckets[t].append(score["delta_struct"])

    print("\n--- OMNIA TEMPERATURE TEST ---\n")

    results = {}

    for t in sorted(buckets.keys()):
        avg = mean(buckets[t])
        results[t] = avg
        print(f"T={t:.1f} → Δ_struct={avg:.4f}")

    print("\nExpected behavior:")
    print("Δ_struct decreases as temperature increases")

    temps = sorted(results.keys())
    monotonic = all(results[temps[i]] >= results[temps[i+1]] for i in range(len(temps)-1))

    print("\nInvariant check:")
    if monotonic:
        print("RESULT: PASS")
    else:
        print("RESULT: NON-MONOTONIC")


if __name__ == "__main__":
    main()