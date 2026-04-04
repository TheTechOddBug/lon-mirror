import json
from omnia_rfs_core_v1_0 import omnia_rfs_v1

def evaluate_dataset(file_path):
    scores = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            text = obj["text"]
            score = omnia_rfs_v1(text)
            scores.append(score)

    return scores


def summary(name, scores):
    import numpy as np

    print(f"\n{name}")
    print("Mean:", np.mean(scores))
    print("Std:", np.std(scores))


if __name__ == "__main__":
    s = evaluate_dataset("baseline_s.jsonl")
    p = evaluate_dataset("baseline_p.jsonl")
    r = evaluate_dataset("baseline_r.jsonl")

    summary("Structured", s)
    summary("Perturbed", p)
    summary("Random", r)