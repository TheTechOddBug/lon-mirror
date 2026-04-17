import json
import re
from difflib import SequenceMatcher
from itertools import combinations

# ============================================================
# DATASET
# ============================================================

DATASET = [
    {
        "level": 1,
        "task_type": "addition",
        "complexity_band": "baseline",
        "question_variants": [
            "What is 2+2?",
            "2+2=?",
            "Compute 2 + 2",
            "Calculate 2+2",
            "Sum of 2 and 2?"
        ],
        "ground_truth": "4",
        "model_outputs": [
            "4",
            "The answer is 4",
            "4",
            "Result: 4",
            "It equals 4"
        ]
    },
    {
        "level": 2,
        "task_type": "addition",
        "complexity_band": "baseline",
        "question_variants": [
            "What is 12+37?",
            "12+37=?",
            "Compute 12 + 37",
            "Calculate 12+37",
            "Sum of 12 and 37?"
        ],
        "ground_truth": "49",
        "model_outputs": [
            "49",
            "The answer is 49",
            "49",
            "Result: 49",
            "It equals 49"
        ]
    },
    {
        "level": 3,
        "task_type": "addition",
        "complexity_band": "baseline",
        "question_variants": [
            "What is 123+456?",
            "123+456=?",
            "Compute 123 + 456",
            "Calculate 123+456",
            "Sum of 123 and 456?"
        ],
        "ground_truth": "579",
        "model_outputs": [
            "579",
            "The answer is 579",
            "579",
            "Result: 579",
            "It equals 579"
        ]
    },
    {
        "level": 4,
        "task_type": "multiplication",
        "complexity_band": "stress_initial",
        "question_variants": [
            "What is 7*8?",
            "7*8=?",
            "Compute 7 times 8",
            "Multiply 7 and 8",
            "7 multiplied by 8?"
        ],
        "ground_truth": "56",
        "model_outputs": [
            "56",
            "The answer is 56",
            "56",
            "Result: 56",
            "It equals 56"
        ]
    },
    {
        "level": 5,
        "task_type": "multiplication",
        "complexity_band": "stress_initial",
        "question_variants": [
            "What is 23*47?",
            "23*47=?",
            "Compute 23 times 47",
            "Multiply 23 and 47",
            "23 multiplied by 47?"
        ],
        "ground_truth": "1081",
        "model_outputs": [
            "1081",
            "The answer is 1081",
            "1081",
            "Result: 1081",
            "It equals 1081"
        ]
    },
    {
        "level": 6,
        "task_type": "multiplication",
        "complexity_band": "stress_initial",
        "question_variants": [
            "What is 123*45?",
            "123*45=?",
            "Compute 123 times 45",
            "Multiply 123 and 45",
            "123 multiplied by 45?"
        ],
        "ground_truth": "5535",
        "model_outputs": [
            "5535",
            "The answer is 5535",
            "5535",
            "Result: 5535",
            "Answer: 5535"
        ]
    },
    {
        "level": 7,
        "task_type": "multiplication",
        "complexity_band": "high_stress",
        "question_variants": [
            "What is 123*456?",
            "123*456=?",
            "Compute 123 times 456",
            "Multiply 123 and 456",
            "123 multiplied by 456?"
        ],
        "ground_truth": "56088",
        "model_outputs": [
            "56088",
            "The answer is 56088",
            "56088",
            "Result: 56088",
            "56088 is the result"
        ]
    },
    {
        "level": 8,
        "task_type": "multiplication",
        "complexity_band": "high_stress",
        "question_variants": [
            "What is 1234*56?",
            "1234*56=?",
            "Compute 1234 times 56",
            "Multiply 1234 and 56",
            "1234 multiplied by 56?"
        ],
        "ground_truth": "69104",
        "model_outputs": [
            "69104",
            "The answer is 69104",
            "69104",
            "Answer: 69104",
            "It equals 69104"
        ]
    },
    {
        "level": 9,
        "task_type": "multiplication",
        "complexity_band": "high_stress",
        "question_variants": [
            "What is 1234*567?",
            "1234*567=?",
            "Compute 1234 times 567",
            "Multiply 1234 and 567",
            "1234 multiplied by 567?"
        ],
        "ground_truth": "699678",
        "model_outputs": [
            "699678",
            "The answer is 699678",
            "699678",
            "Result: 699678",
            "Approximately 699678"
        ]
    },
    {
        "level": 10,
        "task_type": "multiplication",
        "complexity_band": "breakdown",
        "question_variants": [
            "What is 12345*678?",
            "12345*678=?",
            "Compute 12345 times 678",
            "Multiply 12345 and 678",
            "12345 multiplied by 678?"
        ],
        "ground_truth": "8369910",
        "model_outputs": [
            "8369910",
            "The answer is 8369910",
            "8369010",
            "Result: 8369910",
            "Approximately 8,369,910"
        ]
    }
]

# ============================================================
# NORMALIZATION
# ============================================================

def normalize(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"\s+", " ", t)
    t = t.replace("the answer is", "")
    t = t.replace("result:", "")
    t = t.replace("it equals", "")
    t = t.replace("answer:", "")
    t = t.replace("is the result", "")
    t = t.replace("approximately", "")
    t = t.replace(",", "")
    t = t.strip()
    return t

def extract_number(text: str) -> str:
    matches = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    return matches[-1] if matches else normalize(text)

# ============================================================
# METRICS
# ============================================================

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def pairwise_similarity(outputs):
    pairs = list(combinations(outputs, 2))
    if not pairs:
        return 1.0, []
    sims = [similarity(a, b) for a, b in pairs]
    return sum(sims) / len(sims), sims

def compute_accuracy(outputs, ground_truth):
    normalized = [extract_number(o) for o in outputs]
    correct_flags = [n == ground_truth for n in normalized]
    return sum(correct_flags) / len(correct_flags), correct_flags, normalized

def classify_consistency(score: float) -> str:
    if score >= 0.85:
        return "invariant"
    if score >= 0.60:
        return "sensitive"
    return "degraded"

def compute_deltas(results):
    enriched = []
    prev_accuracy = None
    prev_consistency = None

    for row in results:
        current = dict(row)
        if prev_accuracy is None:
            current["delta_accuracy"] = None
            current["delta_consistency"] = None
        else:
            current["delta_accuracy"] = round(row["accuracy"] - prev_accuracy, 4)
            current["delta_consistency"] = round(row["consistency"] - prev_consistency, 4)

        prev_accuracy = row["accuracy"]
        prev_consistency = row["consistency"]
        enriched.append(current)

    return enriched

def detect_lead_signal(results):
    """
    Lead signal:
    first level where consistency decreases while accuracy remains 1.0.
    """
    for row in results:
        da = row.get("delta_accuracy")
        dc = row.get("delta_consistency")
        if da is None or dc is None:
            continue
        if row["accuracy"] == 1.0 and dc < 0:
            return {
                "lead_signal_detected": True,
                "level": row["level"],
                "delta_consistency": dc,
                "delta_accuracy": da
            }
    return {
        "lead_signal_detected": False,
        "level": None,
        "delta_consistency": None,
        "delta_accuracy": None
    }

# ============================================================
# MAIN
# ============================================================

def run_complexity_sweep(dataset):
    results = []

    for item in dataset:
        level = item["level"]
        outputs = item["model_outputs"]
        ground_truth = item["ground_truth"]

        accuracy, correct_flags, normalized_outputs = compute_accuracy(outputs, ground_truth)
        consistency, pairwise_scores = pairwise_similarity(normalized_outputs)
        consistency_class = classify_consistency(consistency)

        results.append({
            "level": level,
            "task_type": item["task_type"],
            "complexity_band": item["complexity_band"],
            "ground_truth": ground_truth,
            "question_variants": item["question_variants"],
            "model_outputs": outputs,
            "normalized_outputs": normalized_outputs,
            "correct_flags": correct_flags,
            "accuracy": round(accuracy, 4),
            "consistency": round(consistency, 4),
            "consistency_class": consistency_class,
            "pairwise_scores": [round(x, 4) for x in pairwise_scores],
        })

    results = compute_deltas(results)
    lead_signal = detect_lead_signal(results)

    return {
        "results": results,
        "lead_signal": lead_signal
    }

def print_results(payload):
    results = payload["results"]
    lead_signal = payload["lead_signal"]

    print("COMPLEXITY SWEEP TEST v1 DENSE")
    print("=" * 72)
    print()

    for r in results:
        da = "None" if r["delta_accuracy"] is None else f"{r['delta_accuracy']:+.4f}"
        dc = "None" if r["delta_consistency"] is None else f"{r['delta_consistency']:+.4f}"

        print(
            f"Level {r['level']:>2} | "
            f"band={r['complexity_band']:<14} | "
            f"type={r['task_type']:<14} | "
            f"accuracy={r['accuracy']:.4f} | "
            f"consistency={r['consistency']:.4f} | "
            f"class={r['consistency_class']:<9} | "
            f"dAcc={da} | "
            f"dCons={dc}"
        )

    print()
    print("Lead signal:")
    if lead_signal["lead_signal_detected"]:
        print(
            f"- detected at level {lead_signal['level']} "
            f"(delta_consistency={lead_signal['delta_consistency']:+.4f}, "
            f"delta_accuracy={lead_signal['delta_accuracy']:+.4f})"
        )
    else:
        print("- not detected")

    print()
    print("Interpretation:")
    print("- accuracy measures normalized correctness")
    print("- consistency measures pairwise agreement across prompt variants")
    print("- lead signal means consistency drops while accuracy is still 1.0")

def save_results(payload, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    output_file = "examples/complexity_sweep_results_v1_dense.json"
    payload = run_complexity_sweep(DATASET)
    print_results(payload)
    save_results(payload, output_file)
    print()
    print(f"Results saved to {output_file}")