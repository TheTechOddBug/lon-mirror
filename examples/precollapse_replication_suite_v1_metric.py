import json
import re
import sys
from pathlib import Path

# Allow importing sibling file: examples/consistency_metric_v1.py
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

from consistency_metric_v1 import (
    consistency_metric_v1,
    classify_consistency_v1,
)

# ============================================================
# REPLICATION SUITE v1
# Same synthetic families as v0
# But uses consistency_metric_v1 instead of plain SequenceMatcher
# ============================================================

DATASET = [
    # --------------------------------------------------------
    # FAMILY A: arithmetic_addition_control
    # Negative control
    # --------------------------------------------------------
    {
        "family": "arithmetic_addition_control",
        "level": 1,
        "complexity_band": "control",
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
        "family": "arithmetic_addition_control",
        "level": 2,
        "complexity_band": "control",
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
        "family": "arithmetic_addition_control",
        "level": 3,
        "complexity_band": "control",
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

    # --------------------------------------------------------
    # FAMILY B: arithmetic_multiplication_dense
    # Main target family
    # --------------------------------------------------------
    {
        "family": "arithmetic_multiplication_dense",
        "level": 1,
        "complexity_band": "baseline",
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
        "family": "arithmetic_multiplication_dense",
        "level": 2,
        "complexity_band": "baseline",
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
        "family": "arithmetic_multiplication_dense",
        "level": 3,
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
        "family": "arithmetic_multiplication_dense",
        "level": 4,
        "complexity_band": "stress_initial",
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
        "family": "arithmetic_multiplication_dense",
        "level": 5,
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
        "family": "arithmetic_multiplication_dense",
        "level": 6,
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
        "family": "arithmetic_multiplication_dense",
        "level": 7,
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
    },

    # --------------------------------------------------------
    # FAMILY C: algebra_linear_equations
    # --------------------------------------------------------
    {
        "family": "algebra_linear_equations",
        "level": 1,
        "complexity_band": "baseline",
        "question_variants": [
            "Solve: x + 5 = 12",
            "Find x: x+5=12",
            "What is x if x+5=12?",
            "Solve x+5=12",
            "Equation: x+5=12"
        ],
        "ground_truth": "7",
        "model_outputs": [
            "7",
            "x = 7",
            "The answer is 7",
            "Result: 7",
            "It equals 7"
        ]
    },
    {
        "family": "algebra_linear_equations",
        "level": 2,
        "complexity_band": "stress_initial",
        "question_variants": [
            "Solve: 3x + 5 = 20",
            "Find x: 3x+5=20",
            "What is x if 3x+5=20?",
            "Solve 3x+5=20",
            "Equation: 3x+5=20"
        ],
        "ground_truth": "5",
        "model_outputs": [
            "5",
            "x = 5",
            "The answer is 5",
            "Result: 5",
            "It equals 5"
        ]
    },
    {
        "family": "algebra_linear_equations",
        "level": 3,
        "complexity_band": "high_stress",
        "question_variants": [
            "Solve: 7x - 13 = 50",
            "Find x: 7x-13=50",
            "What is x if 7x-13=50?",
            "Solve 7x-13=50",
            "Equation: 7x-13=50"
        ],
        "ground_truth": "9",
        "model_outputs": [
            "9",
            "x = 9",
            "The answer is 9",
            "Result: 9",
            "Approximately 9"
        ]
    },
    {
        "family": "algebra_linear_equations",
        "level": 4,
        "complexity_band": "breakdown",
        "question_variants": [
            "Solve: 12x - 17 = 103",
            "Find x: 12x-17=103",
            "What is x if 12x-17=103?",
            "Solve 12x-17=103",
            "Equation: 12x-17=103"
        ],
        "ground_truth": "10",
        "model_outputs": [
            "10",
            "x = 10",
            "The answer is 10",
            "Result: 11",
            "Approximately 10"
        ]
    },

    # --------------------------------------------------------
    # FAMILY D: prime_check_control
    # --------------------------------------------------------
    {
        "family": "prime_check_control",
        "level": 1,
        "complexity_band": "control",
        "question_variants": [
            "Is 17 prime?",
            "Is 17 a prime number?",
            "Prime check: 17",
            "Does 17 have divisors other than 1 and itself?",
            "Check whether 17 is prime"
        ],
        "ground_truth": "yes",
        "model_outputs": [
            "yes",
            "Yes, 17 is prime",
            "The answer is yes",
            "Result: yes",
            "It is prime"
        ]
    },
    {
        "family": "prime_check_control",
        "level": 2,
        "complexity_band": "control",
        "question_variants": [
            "Is 19 prime?",
            "Is 19 a prime number?",
            "Prime check: 19",
            "Does 19 have divisors other than 1 and itself?",
            "Check whether 19 is prime"
        ],
        "ground_truth": "yes",
        "model_outputs": [
            "yes",
            "Yes, 19 is prime",
            "The answer is yes",
            "Result: yes",
            "It is prime"
        ]
    },

    # --------------------------------------------------------
    # FAMILY E: translation_control
    # --------------------------------------------------------
    {
        "family": "translation_control",
        "level": 1,
        "complexity_band": "control",
        "question_variants": [
            "Translate 'hello' to Spanish",
            "How do you say 'hello' in Spanish?",
            "Spanish for 'hello'?",
            "What is 'hello' in Spanish?",
            "Give the Spanish translation of 'hello'"
        ],
        "ground_truth": "hola",
        "model_outputs": [
            "hola",
            "The answer is hola",
            "hola",
            "Result: hola",
            "It equals hola"
        ]
    },
    {
        "family": "translation_control",
        "level": 2,
        "complexity_band": "control",
        "question_variants": [
            "Translate 'goodbye' to Spanish",
            "How do you say 'goodbye' in Spanish?",
            "Spanish for 'goodbye'?",
            "What is 'goodbye' in Spanish?",
            "Give the Spanish translation of 'goodbye'"
        ],
        "ground_truth": "adios",
        "model_outputs": [
            "adios",
            "The answer is adios",
            "adios",
            "Result: adios",
            "It equals adios"
        ]
    },
]


# ============================================================
# NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"\s+", " ", t)
    t = t.replace(",", "")
    t = t.replace("the answer is", "")
    t = t.replace("result:", "")
    t = t.replace("it equals", "")
    t = t.replace("answer:", "")
    t = t.replace("is the result", "")
    t = t.replace("approximately", "")
    t = t.replace("x =", "")
    t = t.replace("it is", "")
    t = t.strip()
    return t


def extract_number(text: str) -> str:
    matches = re.findall(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    return matches[-1] if matches else ""


def extract_yes_no(text: str) -> str:
    t = normalize_text(text)
    if re.search(r"\byes\b", t):
        return "yes"
    if re.search(r"\bno\b", t):
        return "no"
    if "prime" in t and "not" not in t:
        return "yes"
    return ""


def extract_translation(text: str, allowed):
    t = normalize_text(text)
    for item in allowed:
        if item in t:
            return item
    return ""


def normalize_output_by_family(family: str, text: str) -> str:
    if family in {"arithmetic_addition_control", "arithmetic_multiplication_dense", "algebra_linear_equations"}:
        n = extract_number(text)
        return n if n else normalize_text(text)

    if family == "prime_check_control":
        y = extract_yes_no(text)
        return y if y else normalize_text(text)

    if family == "translation_control":
        x = extract_translation(text, ["hola", "adios"])
        return x if x else normalize_text(text)

    return normalize_text(text)


# ============================================================
# ACCURACY / DELTAS / LEAD
# ============================================================

def compute_accuracy(outputs, ground_truth, family):
    normalized = [normalize_output_by_family(family, o) for o in outputs]
    correct_flags = [n == ground_truth for n in normalized]
    return sum(correct_flags) / len(correct_flags), correct_flags, normalized


def compute_deltas(rows):
    enriched = []
    prev_acc = None
    prev_cons = None

    for row in rows:
        current = dict(row)
        if prev_acc is None:
            current["delta_accuracy"] = None
            current["delta_consistency_v1"] = None
        else:
            current["delta_accuracy"] = round(row["accuracy"] - prev_acc, 4)
            current["delta_consistency_v1"] = round(row["consistency_v1"] - prev_cons, 4)

        prev_acc = row["accuracy"]
        prev_cons = row["consistency_v1"]
        enriched.append(current)

    return enriched


def detect_lead_signal(rows):
    first_drop = None
    first_error = None

    for row in rows:
        da = row.get("delta_accuracy")
        dc = row.get("delta_consistency_v1")

        if first_drop is None and da is not None and row["accuracy"] == 1.0 and dc < 0:
            first_drop = {
                "level": row["level"],
                "delta_accuracy": da,
                "delta_consistency_v1": dc,
            }

        if first_error is None and row["accuracy"] < 1.0:
            first_error = {
                "level": row["level"],
                "accuracy": row["accuracy"],
            }

    lead_levels = None
    if first_drop is not None and first_error is not None:
        lead_levels = first_error["level"] - first_drop["level"]

    return {
        "early_drop_detected": first_drop is not None,
        "first_consistency_drop": first_drop,
        "first_accuracy_drop": first_error,
        "lead_levels": lead_levels,
    }


# ============================================================
# FAMILY ANALYSIS
# ============================================================

def analyze_family(items):
    rows = []

    for item in items:
        family = item["family"]
        accuracy, correct_flags, normalized_outputs = compute_accuracy(
            item["model_outputs"],
            item["ground_truth"],
            family,
        )

        metric = consistency_metric_v1(item["model_outputs"])
        consistency_v1 = metric["consistency_v1"]
        consistency_class_v1 = classify_consistency_v1(consistency_v1)

        rows.append({
            "family": family,
            "level": item["level"],
            "complexity_band": item["complexity_band"],
            "ground_truth": item["ground_truth"],
            "question_variants": item["question_variants"],
            "model_outputs": item["model_outputs"],
            "normalized_outputs": normalized_outputs,
            "correct_flags": correct_flags,
            "accuracy": round(accuracy, 4),
            "consistency_v1": round(consistency_v1, 4),
            "consistency_class_v1": consistency_class_v1,
            "base_score": round(metric["base_score"], 4),
            "dispersion_penalty": round(metric["dispersion_penalty"], 4),
            "aggregates": metric["aggregates"],
        })

    rows = sorted(rows, key=lambda x: x["level"])
    rows = compute_deltas(rows)
    lead_signal = detect_lead_signal(rows)

    return {
        "family": rows[0]["family"] if rows else None,
        "rows": rows,
        "lead_signal": lead_signal,
    }


def aggregate_suite(family_payloads):
    summary = {
        "families_total": len(family_payloads),
        "families_with_early_drop": 0,
        "families_with_accuracy_drop": 0,
        "families_with_positive_lead": 0,
    }

    for payload in family_payloads:
        lead = payload["lead_signal"]

        if lead["early_drop_detected"]:
            summary["families_with_early_drop"] += 1

        if lead["first_accuracy_drop"] is not None:
            summary["families_with_accuracy_drop"] += 1

        if lead["lead_levels"] is not None and lead["lead_levels"] > 0:
            summary["families_with_positive_lead"] += 1

    return summary


# ============================================================
# MAIN
# ============================================================

def build_suite(dataset):
    families = sorted(set(item["family"] for item in dataset))
    family_payloads = []

    for family in families:
        items = [x for x in dataset if x["family"] == family]
        family_payloads.append(analyze_family(items))

    suite_summary = aggregate_suite(family_payloads)

    return {
        "suite_summary": suite_summary,
        "families": family_payloads,
    }


def print_suite(payload):
    summary = payload["suite_summary"]
    families = payload["families"]

    print("PRECOLLAPSE REPLICATION SUITE v1 METRIC")
    print("=" * 108)
    print()

    print("Suite summary:")
    print(f"- families_total: {summary['families_total']}")
    print(f"- families_with_early_drop: {summary['families_with_early_drop']}")
    print(f"- families_with_accuracy_drop: {summary['families_with_accuracy_drop']}")
    print(f"- families_with_positive_lead: {summary['families_with_positive_lead']}")
    print()

    for fam in families:
        print(f"[FAMILY] {fam['family']}")
        for row in fam["rows"]:
            da = "None" if row["delta_accuracy"] is None else f"{row['delta_accuracy']:+.4f}"
            dc = "None" if row["delta_consistency_v1"] is None else f"{row['delta_consistency_v1']:+.4f}"

            print(
                f"  L{row['level']:>2} | "
                f"band={row['complexity_band']:<13} | "
                f"acc={row['accuracy']:.4f} | "
                f"cons_v1={row['consistency_v1']:.4f} | "
                f"class={row['consistency_class_v1']:<9} | "
                f"base={row['base_score']:.4f} | "
                f"pen={row['dispersion_penalty']:.4f} | "
                f"dAcc={da} | "
                f"dCons={dc}"
            )

        lead = fam["lead_signal"]
        first_drop_level = lead["first_consistency_drop"]["level"] if lead["first_consistency_drop"] else None
        first_acc_drop_level = lead["first_accuracy_drop"]["level"] if lead["first_accuracy_drop"] else None

        print("  Lead analysis:")
        print(f"  - early_drop_detected: {lead['early_drop_detected']}")
        print(f"  - first_consistency_drop_level: {first_drop_level}")
        print(f"  - first_accuracy_drop_level: {first_acc_drop_level}")
        print(f"  - lead_levels: {lead['lead_levels']}")
        print()

    print("Interpretation:")
    print("- consistency_v1 uses lexical + numeric + morphological layers plus dispersion penalty")
    print("- early_drop_detected means consistency_v1 decreased while accuracy remained 1.0")
    print("- positive lead means consistency_v1 deterioration appeared before the first accuracy loss")
    print("- control families help check false positives")


def save_payload(payload, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    output_file = "examples/precollapse_replication_suite_results_v1_metric.json"
    payload = build_suite(DATASET)
    print_suite(payload)
    save_payload(payload, output_file)
    print()
    print(f"Results saved to {output_file}")