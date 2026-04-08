import json
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATH = Path("examples/fragility_display_triplets_v1.jsonl")
OUTPUT_JSONL_PATH = Path("examples/fragility_display_triplets_v1_scores.jsonl")
OUTPUT_MD_PATH = Path("examples/sbc_fragility_monitor_results.md")


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


def validate_records(records: List[Dict[str, Any]]) -> None:
    required = {
        "triplet_id",
        "variant",
        "question",
        "model_raw_output",
        "final_extracted_answer",
        "expected_answer",
        "is_correct",
    }

    seen = set()
    for record in records:
        missing = required - set(record.keys())
        if missing:
            raise ValueError(f"Missing required fields {missing} in record {record}")

        key = (record["triplet_id"], record["variant"])
        if key in seen:
            raise ValueError(f"Duplicate triplet/variant found: {key}")
        seen.add(key)

    if len(records) != 3:
        raise ValueError(f"Expected exactly 3 records for v1 triplet, found {len(records)}")


def build_tokens(record: Dict[str, Any]) -> List[str]:
    question = record["question"]
    output = record["model_raw_output"]
    final_answer = str(record["final_extracted_answer"])
    expected_answer = str(record["expected_answer"])

    tokens: List[str] = []
    tokens.append(f"triplet_id={record['triplet_id']}")
    tokens.append(f"variant={record['variant']}")
    tokens.append(f"question={question}")
    tokens.append(f"output={output}")
    tokens.append(f"final_answer={final_answer}")
    tokens.append(f"expected_answer={expected_answer}")
    tokens.append(f"is_correct={record['is_correct']}")
    return tokens


def score_record(record: Dict[str, Any]) -> Dict[str, Any]:
    from omnia.engine import run_omnia_totale

    tokens = build_tokens(record)
    token_numbers = [len(t) for t in tokens]

    # No numeric "n" here on purpose.
    # This is a fragility display run for reasoning text, so engine stays in legacy text mode.
    result = run_omnia_totale(
        extra={
            "tokens": tokens,
            "token_numbers": token_numbers,
        }
    )

    scored = dict(record)
    scored["omega_total"] = float(result.omega_total)

    omega_raw = getattr(result, "omega_raw", None)
    omega_adjusted = getattr(result, "omega_adjusted", None)
    structural_bias_meta = getattr(result, "structural_bias_meta", None)

    scored["omega_raw"] = None if omega_raw is None else float(omega_raw)
    scored["omega_adjusted"] = None if omega_adjusted is None else float(omega_adjusted)

    if structural_bias_meta is None:
        scored["structural_bias_meta"] = None
    else:
        scored["structural_bias_meta"] = {
            "bias_penalty_raw": float(structural_bias_meta.bias_penalty_raw),
            "bias_penalty_norm": float(structural_bias_meta.bias_penalty_norm),
            "lambda_value": float(structural_bias_meta.lambda_value),
        }

    return scored


def classify_fragility(rank_index: int) -> str:
    if rank_index == 0:
        return "HIGH"
    if rank_index == 1:
        return "MEDIUM"
    return "LOW"


def classify_collapse_risk(rank_index: int) -> str:
    if rank_index == 0:
        return "Low"
    if rank_index == 1:
        return "Moderate"
    return "High"


def write_markdown(path: Path, scored_records: List[Dict[str, Any]]) -> None:
    ranked = sorted(scored_records, key=lambda r: r["omega_total"], reverse=True)

    lines: List[str] = []
    lines.append("# SBC Fragility Monitor Results")
    lines.append("")
    lines.append("Status: display-branch benchmark")
    lines.append("Scope: 1 reasoning triplet with 3 near-equivalent variants")
    lines.append("Purpose: show that surface correctness can remain constant while structural stability changes")
    lines.append("")
    lines.append("## Core result")
    lines.append("")
    lines.append("All three variants are correct on the surface.")
    lines.append("OMNIA still separates them by structural stability.")
    lines.append("")

    lines.append("| Variant | is_correct | omega_total | Structural Stability | Collapse Risk |")
    lines.append("|---|---:|---:|---|---|")
    for idx, record in enumerate(ranked):
        lines.append(
            f"| {record['variant']} | "
            f"{'true' if record['is_correct'] else 'false'} | "
            f"{record['omega_total']:.6f} | "
            f"{classify_fragility(idx)} | "
            f"{classify_collapse_risk(idx)} |"
        )

    lines.append("")
    lines.append("## Ranked reading")
    lines.append("")

    for idx, record in enumerate(ranked, start=1):
        lines.append(f"### Rank {idx} — {record['variant']}")
        lines.append("")
        lines.append(f"- triplet_id: `{record['triplet_id']}`")
        lines.append(f"- omega_total: `{record['omega_total']:.6f}`")
        lines.append(f"- is_correct: `{record['is_correct']}`")
        lines.append(f"- final_extracted_answer: `{record['final_extracted_answer']}`")
        lines.append(f"- expected_answer: `{record['expected_answer']}`")
        lines.append("")
        lines.append(f"Question: {record['question']}")
        lines.append("")
        lines.append(f"Model output: {record['model_raw_output']}")
        lines.append("")

    lines.append("## Compression")
    lines.append("")
    lines.append("A standard evaluator sees three correct answers.")
    lines.append("OMNIA sees three different stability levels.")
    lines.append("")
    lines.append("This is the display-level claim:")
    lines.append("")
    lines.append("**surface correctness can remain unchanged while structural reliability collapses.**")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records = read_jsonl(INPUT_PATH)
    validate_records(records)

    scored_records = [score_record(record) for record in records]
    write_jsonl(OUTPUT_JSONL_PATH, scored_records)
    write_markdown(OUTPUT_MD_PATH, scored_records)

    ranked = sorted(scored_records, key=lambda r: r["omega_total"], reverse=True)

    print("=== FRAGILITY DISPLAY BENCHMARK ===")
    for idx, record in enumerate(ranked, start=1):
        print(
            f"rank={idx} | variant={record['variant']} | "
            f"omega_total={record['omega_total']:.6f} | "
            f"is_correct={record['is_correct']}"
        )

    print(f"\nWrote {OUTPUT_JSONL_PATH}")
    print(f"Wrote {OUTPUT_MD_PATH}")


if __name__ == "__main__":
    main()