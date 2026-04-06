import json
from statistics import mean
from omnia_semantic_decoupling_v10_0 import semantic_decoupling_score


def load_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def compute_group(data, label):
    scores = []
    for x in data:
        if x["label"] == label:
            s = semantic_decoupling_score(x["text"], seed=42)
            scores.append(s["delta_struct"])
    return mean(scores)


def main():
    data = load_data("data/llm_real_outputs.jsonl")

    correct = compute_group(data, "correct")
    incorrect = compute_group(data, "incorrect")

    print("\n--- OMNIA REAL LLM TEST ---\n")
    print(f"Δ_struct correct   = {correct:.4f}")
    print(f"Δ_struct incorrect = {incorrect:.4f}")

    print("\nExpected:")
    print("correct > incorrect")

    if correct > incorrect:
        print("\nRESULT: PASS")
    else:
        print("\nRESULT: FAIL")


if __name__ == "__main__":
    main()