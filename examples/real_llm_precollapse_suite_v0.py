import json
import re
import sys
from collections import defaultdict
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
# REAL LLM PRECOLLAPSE SUITE v0
#
# Input:
#   JSONL file with one row per prompt/output pair
#
# Expected fields per row:
# {
#   "family": "arithmetic_multiplication_real",
#   "level": 1,
#   "question_group_id": "mul_23_47",
#   "prompt_variant_id": 1,
#   "prompt": "What is 23*47?",
#   "ground_truth": "1081",
#   "model_name": "gpt-4o-mini",
#   "model_output": "1081"
# }
#
# Output:
# - per-group metrics
# - per-family / per-model summary
# - early-drop / lead-style summaries on real grouped outputs
# ============================================================


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
    # arithmetic / algebra
    if any(k in family for k in ["arithmetic", "algebra", "math", "numeric"]):
        n = extract_number(text)
        return n if n else normalize_text(text)

    # prime / yes-no
    if any(k in family for k in ["prime", "boolean", "yesno", "yes_no"]):
        y = extract_yes_no(text)
        return y if y else normalize_text(text)

    # translation
    if "translation" in family:
        # extend allowed list if needed
        x = extract_translation(text, ["hola", "adios", "bonjour", "ciao"])
        return x if x else normalize_text(text)

    return normalize_text(text)


# ============================================================
# ACCURACY
# ============================================================

def compute_group_accuracy(rows):
    """
    Accuracy inside a question group:
    fraction of prompt variants whose normalized output matches normalized ground truth.
    """
    if not rows:
        return 0.0, [], []

    family = rows[0]["family"]
    ground_truth = rows[0]["ground_truth"]

    normalized_gt = normalize_output_by_family(family, ground_truth)
    normalized_outputs = [
        normalize_output_by_family(family, r["model_output"]) for r in rows
    ]
    correct_flags = [x == normalized_gt for x in normalized_outputs]
    accuracy = sum(correct_flags) / len(correct_flags)

    return accuracy, correct_flags, normalized_outputs


# ============================================================
# GROUPING
# ============================================================

def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def validate_rows(rows):
    required = {
        "family",
        "level",
        "question_group_id",
        "prompt_variant_id",
        "prompt",
        "ground_truth",
        "model_name",
        "model_output",
    }

    missing = []
    for i, row in enumerate(rows, start=1):
        row_missing = [k for k in required if k not in row]
        if row_missing:
            missing.append({"line": i, "missing": row_missing})

    if missing:
        raise ValueError(f"Invalid input rows. Missing fields: {missing[:5]}")


def group_rows(rows):
    """
    Group by:
    (model_name, family, question_group_id)
    """
    grouped = defaultdict(list)
    for row in rows:
        key = (row["model_name"], row["family"], row["question_group_id"])
        grouped[key].append(row)

    # keep rows ordered by prompt_variant_id if present
    for key in grouped:
        grouped[key] = sorted(grouped[key], key=lambda x: x["prompt_variant_id"])

    return grouped


# ============================================================
# GROUP METRICS
# ============================================================

def analyze_group(rows):
    """
    Analyze one real grouped question:
    same model, same family, same question_group_id, multiple prompt variants
    """
    model_name = rows[0]["model_name"]
    family = rows[0]["family"]
    level = rows[0]["level"]
    question_group_id = rows[0]["question_group_id"]
    ground_truth = rows[0]["ground_truth"]

    prompts = [r["prompt"] for r in rows]
    outputs = [r["model_output"] for r in rows]

    accuracy, correct_flags, normalized_outputs = compute_group_accuracy(rows)
    metric = consistency_metric_v1(outputs)

    return {
        "model_name": model_name,
        "family": family,
        "level": level,
        "question_group_id": question_group_id,
        "ground_truth": ground_truth,
        "n_variants": len(rows),
        "prompts": prompts,
        "model_outputs": outputs,
        "normalized_outputs": normalized_outputs,
        "correct_flags": correct_flags,
        "accuracy": round(accuracy, 4),
        "consistency_v1": round(metric["consistency_v1"], 4),
        "consistency_class_v1": classify_consistency_v1(metric["consistency_v1"]),
        "base_score": round(metric["base_score"], 4),
        "dispersion_penalty": round(metric["dispersion_penalty"], 4),
        "aggregates": metric["aggregates"],
    }


# ============================================================
# FAMILY / MODEL TIMELINE
# ============================================================

def sort_group_records(group_records):
    """
    Order by level, then group id for stability.
    """
    return sorted(group_records, key=lambda x: (x["level"], x["question_group_id"]))


def add_deltas(group_records):
    enriched = []
    prev_acc = None
    prev_cons = None

    for row in group_records:
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


def detect_group_sequence_lead(group_records):
    """
    Sequence-level lead detection within one (model, family) series.

    Rule:
    - first_consistency_drop = first record where delta_consistency_v1 < 0
      while accuracy is still 1.0
    - first_accuracy_drop = first record where accuracy < 1.0
    """
    first_drop = None
    first_error = None

    for row in group_records:
        da = row.get("delta_accuracy")
        dc = row.get("delta_consistency_v1")

        if first_drop is None and da is not None and row["accuracy"] == 1.0 and dc < 0:
            first_drop = {
                "level": row["level"],
                "question_group_id": row["question_group_id"],
                "delta_accuracy": da,
                "delta_consistency_v1": dc,
            }

        if first_error is None and row["accuracy"] < 1.0:
            first_error = {
                "level": row["level"],
                "question_group_id": row["question_group_id"],
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
# AGGREGATION
# ============================================================

def analyze_real_suite(rows):
    validate_rows(rows)
    grouped = group_rows(rows)

    group_records = []
    for _, rows_group in grouped.items():
        group_records.append(analyze_group(rows_group))

    # group by (model_name, family)
    family_series = defaultdict(list)
    for rec in group_records:
        key = (rec["model_name"], rec["family"])
        family_series[key].append(rec)

    family_payloads = []
    for (model_name, family), records in family_series.items():
        ordered = sort_group_records(records)
        enriched = add_deltas(ordered)
        lead = detect_group_sequence_lead(enriched)

        family_payloads.append({
            "model_name": model_name,
            "family": family,
            "records": enriched,
            "lead_signal": lead,
        })

    suite_summary = {
        "models_total": len(set(r["model_name"] for r in group_records)),
        "families_total": len(family_payloads),
        "groups_total": len(group_records),
        "families_with_early_drop": sum(1 for f in family_payloads if f["lead_signal"]["early_drop_detected"]),
        "families_with_accuracy_drop": sum(1 for f in family_payloads if f["lead_signal"]["first_accuracy_drop"] is not None),
        "families_with_positive_lead": sum(
            1 for f in family_payloads
            if f["lead_signal"]["lead_levels"] is not None and f["lead_signal"]["lead_levels"] > 0
        ),
    }

    return {
        "suite_summary": suite_summary,
        "families": sorted(family_payloads, key=lambda x: (x["model_name"], x["family"])),
    }


# ============================================================
# PRINTING
# ============================================================

def print_payload(payload):
    summary = payload["suite_summary"]
    families = payload["families"]

    print("REAL LLM PRECOLLAPSE SUITE v0")
    print("=" * 110)
    print()

    print("Suite summary:")
    print(f"- models_total: {summary['models_total']}")
    print(f"- families_total: {summary['families_total']}")
    print(f"- groups_total: {summary['groups_total']}")
    print(f"- families_with_early_drop: {summary['families_with_early_drop']}")
    print(f"- families_with_accuracy_drop: {summary['families_with_accuracy_drop']}")
    print(f"- families_with_positive_lead: {summary['families_with_positive_lead']}")
    print()

    for fam in families:
        print(f"[MODEL] {fam['model_name']} | [FAMILY] {fam['family']}")
        for row in fam["records"]:
            da = "None" if row["delta_accuracy"] is None else f"{row['delta_accuracy']:+.4f}"
            dc = "None" if row["delta_consistency_v1"] is None else f"{row['delta_consistency_v1']:+.4f}"

            print(
                f"  L{row['level']:>2} | "
                f"group={row['question_group_id']:<24} | "
                f"n={row['n_variants']:<2} | "
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
        first_drop_group = lead["first_consistency_drop"]["question_group_id"] if lead["first_consistency_drop"] else None
        first_acc_drop_level = lead["first_accuracy_drop"]["level"] if lead["first_accuracy_drop"] else None
        first_acc_drop_group = lead["first_accuracy_drop"]["question_group_id"] if lead["first_accuracy_drop"] else None

        print("  Lead analysis:")
        print(f"  - early_drop_detected: {lead['early_drop_detected']}")
        print(f"  - first_consistency_drop_level: {first_drop_level}")
        print(f"  - first_consistency_drop_group: {first_drop_group}")
        print(f"  - first_accuracy_drop_level: {first_acc_drop_level}")
        print(f"  - first_accuracy_drop_group: {first_acc_drop_group}")
        print(f"  - lead_levels: {lead['lead_levels']}")
        print()

    print("Interpretation:")
    print("- each row above is one real grouped question with multiple prompt variants")
    print("- consistency_v1 is computed on the raw model outputs inside the group")
    print("- accuracy is computed from normalized outputs against ground truth")
    print("- early_drop_detected means consistency_v1 declined while accuracy was still 1.0")


def save_payload(payload, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


# ============================================================
# CLI
# ============================================================

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python examples/real_llm_precollapse_suite_v0.py <input_jsonl> [output_json]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = (
        sys.argv[2]
        if len(sys.argv) >= 3
        else "examples/real_llm_precollapse_suite_results_v0.json"
    )

    rows = load_jsonl(input_path)
    payload = analyze_real_suite(rows)
    print_payload(payload)
    save_payload(payload, output_path)

    print()
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()