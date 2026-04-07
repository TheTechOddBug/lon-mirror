import json
from pathlib import Path
from typing import Any, Dict, List


MODEL_OUTPUTS_PATH = Path("examples/gsm_symbolic_v0_model_outputs.jsonl")
OMNIA_SCORES_PATH = Path("examples/gsm_symbolic_v0_omnia_scores.jsonl")
TARGET_TEMPLATE_ID = "gsmsym_001"


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


def get_template_records(records: List[Dict[str, Any]], template_id: str) -> List[Dict[str, Any]]:
    selected = [r for r in records if r.get("template_id") == template_id]
    if len(selected) != 3:
        raise ValueError(
            f"Expected exactly 3 records for template_id={template_id}, found {len(selected)}"
        )
    return selected


def validate_variant_set(template_records: List[Dict[str, Any]]) -> None:
    expected = {"base", "num_perturbed", "clause_augmented"}
    found = {r.get("variant_type") for r in template_records}
    if found != expected:
        raise ValueError(f"Unexpected variant set for template: {found} != {expected}")


def compute_omnia_score(record: Dict[str, Any], template_records: List[Dict[str, Any]]) -> float:
    """
    Adapter point to the real OMNIA method.

    Replace the body of this function with the actual call into the repo's OMNIA code.
    This runner is intentionally complete except for this single integration point.

    Required contract:
    - input: one record + the 3-record template context
    - output: one numeric stability score (higher = more stable)

    Example target shape:
        return some_omnia_function(
            text=record["model_raw_output"],
            context=[r["model_raw_output"] for r in template_records],
        )
    """
    raise NotImplementedError(
        "Connect this function to the real OMNIA scoring method already present in the repo."
    )


def assign_fragility_ranks(scored_records: List[Dict[str, Any]]) -> None:
    """
    Rank convention:
    - rank 1 = least fragile = highest stability
    - rank 2 = intermediate
    - rank 3 = most fragile = lowest stability

    If any exact tie exists, all records in the template get fragility_rank = None.
    This matches the v0 protocol tie rule: the template becomes non-conforming.
    """
    scores = [r["omnia_score"] for r in scored_records]

    if len(set(scores)) != len(scores):
        for r in scored_records:
            r["fragility_rank"] = None
        return

    ranked = sorted(scored_records, key=lambda r: r["omnia_score"], reverse=True)
    for i, record in enumerate(ranked, start=1):
        record["fragility_rank"] = i


def update_target_records(
    all_score_records: List[Dict[str, Any]],
    template_id: str,
    template_scored_records: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    by_variant = {r["variant_type"]: r for r in template_scored_records}

    updated: List[Dict[str, Any]] = []
    for record in all_score_records:
        if record.get("template_id") == template_id:
            variant = record.get("variant_type")
            if variant not in by_variant:
                raise ValueError(
                    f"Missing scored record for template_id={template_id}, variant_type={variant}"
                )
            new_record = dict(record)
            new_record["omnia_score"] = by_variant[variant]["omnia_score"]
            new_record["fragility_rank"] = by_variant[variant]["fragility_rank"]
            updated.append(new_record)
        else:
            updated.append(record)

    return updated


def main() -> None:
    model_output_records = read_jsonl(MODEL_OUTPUTS_PATH)
    omnia_score_records = read_jsonl(OMNIA_SCORES_PATH)

    template_records = get_template_records(model_output_records, TARGET_TEMPLATE_ID)
    validate_variant_set(template_records)

    scored_template_records: List[Dict[str, Any]] = []
    for record in template_records:
        if not record.get("model_raw_output"):
            raise ValueError(
                f"model_raw_output is empty for {record['template_id']} / {record['variant_type']}"
            )

        scored_record = dict(record)
        score = compute_omnia_score(record, template_records)

        if not isinstance(score, (int, float)):
            raise TypeError(
                f"compute_omnia_score must return int or float, got {type(score).__name__}"
            )

        scored_record["omnia_score"] = float(score)
        scored_record["fragility_rank"] = None
        scored_template_records.append(scored_record)

    assign_fragility_ranks(scored_template_records)

    updated_all_records = update_target_records(
        all_score_records=omnia_score_records,
        template_id=TARGET_TEMPLATE_ID,
        template_scored_records=scored_template_records,
    )

    write_jsonl(OMNIA_SCORES_PATH, updated_all_records)

    print(f"Updated {TARGET_TEMPLATE_ID} in {OMNIA_SCORES_PATH}")
    for r in sorted(scored_template_records, key=lambda x: x["variant_type"]):
        print(
            f"{r['template_id']} | {r['variant_type']} | "
            f"omnia_score={r['omnia_score']} | fragility_rank={r['fragility_rank']}"
        )


if __name__ == "__main__":
    main()