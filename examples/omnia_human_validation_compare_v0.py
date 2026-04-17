from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean


VALID_LABELS = {"accept", "review", "retry"}


def load_predictions(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    predictions = payload["predictions"]

    by_id: dict[str, dict] = {}
    for row in predictions:
        by_id[row["id"]] = row
    return by_id


def load_human_labels(path: Path) -> dict[str, dict]:
    by_id: dict[str, dict] = {}

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            item_id = row["id"].strip()
            human_label = row["human_label"].strip().lower()

            if human_label and human_label not in VALID_LABELS:
                raise ValueError(
                    f"Invalid human_label '{human_label}' for id '{item_id}'. "
                    f"Allowed: {sorted(VALID_LABELS)}"
                )

            by_id[item_id] = {
                "id": item_id,
                "group": row["group"].strip(),
                "text": row["text"],
                "human_label": human_label,
                "notes": row.get("notes", "").strip(),
            }

    return by_id


def decision_correct(decision: str, human_label: str) -> bool:
    return decision == human_label


def summarize_bool(values: list[bool]) -> dict[str, float | int]:
    true_count = sum(1 for v in values if v)
    total = len(values)
    return {
        "true_count": true_count,
        "false_count": total - true_count,
        "true_rate": round(true_count / total, 6) if total else 0.0,
    }


def summarize_decisions(items: list[dict], key: str) -> dict[str, float]:
    total = len(items)
    counts = defaultdict(int)
    for item in items:
        counts[item[key]] += 1

    return {
        "accept_rate": round(counts["accept"] / total, 6) if total else 0.0,
        "review_rate": round(counts["review"] / total, 6) if total else 0.0,
        "retry_rate": round(counts["retry"] / total, 6) if total else 0.0,
    }


def summarize_group(items: list[dict]) -> dict[str, object]:
    baseline_correct = [bool(item["baseline_correct"]) for item in items]
    combined_correct = [bool(item["combined_correct"]) for item in items]

    return {
        "sample_size": len(items),
        "human_labels": summarize_decisions(items, "human_label"),
        "baseline_decisions": summarize_decisions(items, "baseline_decision"),
        "combined_decisions": summarize_decisions(items, "combined_decision"),
        "baseline_correct_rate": round(mean(1.0 if x else 0.0 for x in baseline_correct), 6),
        "combined_correct_rate": round(mean(1.0 if x else 0.0 for x in combined_correct), 6),
        "combined_better_than_baseline_rate": round(
            mean(
                1.0 if item["combined_correct"] and not item["baseline_correct"] else 0.0
                for item in items
            ),
            6,
        ),
        "combined_worse_than_baseline_rate": round(
            mean(
                1.0 if item["baseline_correct"] and not item["combined_correct"] else 0.0
                for item in items
            ),
            6,
        ),
        "human_review_requested_rate": round(
            mean(1.0 if item["human_label"] == "review" else 0.0 for item in items),
            6,
        ),
        "baseline_missed_human_review_rate": round(
            mean(
                1.0
                if item["human_label"] == "review" and item["baseline_decision"] != "review"
                else 0.0
                for item in items
            ),
            6,
        ),
        "combined_matched_human_review_rate": round(
            mean(
                1.0
                if item["human_label"] == "review" and item["combined_decision"] == "review"
                else 0.0
                for item in items
            ),
            6,
        ),
        "omniabase_gap_coverage_rate": round(
            mean(
                1.0
                if (
                    item["human_label"] == "review"
                    and item["baseline_decision"] == "accept"
                    and item["combined_decision"] == "review"
                )
                else 0.0
                for item in items
            ),
            6,
        ),
        "omniabase_false_alarm_rate": round(
            mean(
                1.0
                if (
                    item["combined_decision"] == "review"
                    and item["human_label"] == "accept"
                )
                else 0.0
                for item in items
            ),
            6,
        ),
    }


def main() -> None:
    base_dir = Path("artifacts/human_validation_v0")
    predictions_path = base_dir / "omnia_human_validation_predictions_v0.json"
    rating_csv_path = base_dir / "omnia_human_validation_sheet_v0.csv"
    report_path = base_dir / "omnia_human_validation_report_v0.json"

    predictions = load_predictions(predictions_path)
    human_rows = load_human_labels(rating_csv_path)

    merged: list[dict] = []
    missing_labels: list[str] = []
    unknown_prediction_ids: list[str] = []

    for item_id, human_row in human_rows.items():
        human_label = human_row["human_label"]
        if not human_label:
            missing_labels.append(item_id)
            continue

        if item_id not in predictions:
            unknown_prediction_ids.append(item_id)
            continue

        pred = predictions[item_id]

        merged.append(
            {
                "id": item_id,
                "group": human_row["group"],
                "text": human_row["text"],
                "notes": human_row["notes"],
                "human_label": human_label,
                "baseline_decision": pred["baseline_decision"],
                "combined_decision": pred["combined_decision"],
                "baseline_warning": bool(pred["baseline_warning"]),
                "omniabase_warning": bool(pred["omniabase_warning"]),
                "ob_cross_base_stability": pred["ob_cross_base_stability"],
                "ob_base_sensitivity": pred["ob_base_sensitivity"],
                "ob_collapse_count": pred["ob_collapse_count"],
                "baseline_correct": decision_correct(pred["baseline_decision"], human_label),
                "combined_correct": decision_correct(pred["combined_decision"], human_label),
            }
        )

    groups = sorted({item["group"] for item in merged})
    summary_by_group: dict[str, dict] = {}

    for group in groups:
        group_items = [item for item in merged if item["group"] == group]
        summary_by_group[group] = summarize_group(group_items)

    overall_summary = summarize_group(merged) if merged else {}

    payload = {
        "validation_name": "OMNIA Human Validation Compare v0",
        "paths": {
            "predictions": str(predictions_path),
            "ratings_csv": str(rating_csv_path),
            "report": str(report_path),
        },
        "num_predictions": len(predictions),
        "num_human_rows": len(human_rows),
        "num_compared_rows": len(merged),
        "missing_labels": missing_labels,
        "unknown_prediction_ids": unknown_prediction_ids,
        "overall_summary": overall_summary,
        "summary_by_group": summary_by_group,
        "row_results": merged,
    }

    report_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(json.dumps(
        {
            "status": "ok",
            "report_path": str(report_path),
            "num_compared_rows": len(merged),
            "missing_labels": missing_labels,
            "unknown_prediction_ids": unknown_prediction_ids,
            "overall_baseline_correct_rate": overall_summary.get("baseline_correct_rate"),
            "overall_combined_correct_rate": overall_summary.get("combined_correct_rate"),
            "overall_omniabase_gap_coverage_rate": overall_summary.get("omniabase_gap_coverage_rate"),
            "overall_omniabase_false_alarm_rate": overall_summary.get("omniabase_false_alarm_rate"),
        },
        indent=2,
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()