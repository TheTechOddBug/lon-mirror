from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from examples.omnia_base_gate_adapter_demo import OmniabaseGateAdapter


def stronger_baseline_score(text: str) -> dict[str, object]:
    stripped = text.strip()
    lowered = stripped.lower()

    repeated_char_warning = has_long_repeated_char_run(stripped, min_run=8)
    repeated_token_warning = has_repeated_token_loop(lowered, min_repetitions=4)

    numeric_value = extract_last_integer(stripped)
    numeric_power_of_two_warning = False
    repeated_numeric_block_warning = False

    if numeric_value is not None and numeric_value > 0:
        numeric_power_of_two_warning = is_power_of_two(numeric_value)
        repeated_numeric_block_warning = has_repeated_numeric_block(str(numeric_value))

    alternating_pattern_warning = has_short_cycle_pattern(
        stripped, max_cycle_len=4, min_repeats=4
    )
    repeated_block_warning = has_repeated_block_pattern(
        stripped, min_block_len=2, max_block_len=6, min_repeats=3
    )

    stronger_baseline_warning = (
        repeated_char_warning
        or repeated_token_warning
        or numeric_power_of_two_warning
        or alternating_pattern_warning
        or repeated_block_warning
        or repeated_numeric_block_warning
    )

    return {
        "repeated_char_warning": repeated_char_warning,
        "repeated_token_warning": repeated_token_warning,
        "numeric_power_of_two_warning": numeric_power_of_two_warning,
        "alternating_pattern_warning": alternating_pattern_warning,
        "repeated_block_warning": repeated_block_warning,
        "repeated_numeric_block_warning": repeated_numeric_block_warning,
        "stronger_baseline_warning": stronger_baseline_warning,
    }


def has_long_repeated_char_run(text: str, min_run: int = 8) -> bool:
    if not text:
        return False

    current = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current += 1
            if current >= min_run:
                return True
        else:
            current = 1
    return False


def has_repeated_token_loop(text: str, min_repetitions: int = 4) -> bool:
    tokens = re.findall(r"\w+", text)
    if not tokens:
        return False

    counts = Counter(tokens)
    return any(count >= min_repetitions for count in counts.values())


def extract_last_integer(text: str) -> int | None:
    matches = re.findall(r"-?\d+", text)
    if not matches:
        return None
    return abs(int(matches[-1]))


def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1) == 0)


def has_short_cycle_pattern(
    text: str, max_cycle_len: int = 4, min_repeats: int = 4
) -> bool:
    s = text.strip()
    if len(s) < 2:
        return False

    for cycle_len in range(1, max_cycle_len + 1):
        if len(s) < cycle_len * min_repeats:
            continue
        if len(s) % cycle_len != 0:
            continue

        cycle = s[:cycle_len]
        if cycle * (len(s) // cycle_len) == s:
            return True

    return False


def has_repeated_block_pattern(
    text: str, min_block_len: int = 2, max_block_len: int = 6, min_repeats: int = 3
) -> bool:
    s = text.strip()
    n = len(s)

    for block_len in range(min_block_len, max_block_len + 1):
        if n < block_len * min_repeats:
            continue

        for start in range(0, n - block_len + 1):
            block = s[start : start + block_len]
            if len(block) < block_len:
                continue

            count = 0
            pos = 0
            while pos + block_len <= n:
                if s[pos : pos + block_len] == block:
                    count += 1
                    pos += block_len
                else:
                    pos += 1

            if count >= min_repeats:
                return True

    return False


def has_repeated_numeric_block(s: str) -> bool:
    if len(s) < 6:
        return False

    if len(set(s)) == 1:
        return True

    for block_len in range(1, min(4, len(s) // 2) + 1):
        block = s[:block_len]
        repeats = len(s) // block_len
        reconstructed = (block * repeats) + block[: len(s) % block_len]
        if reconstructed == s and repeats >= 3:
            return True

    return False


def baseline_decision(baseline: dict[str, object]) -> str:
    return "retry" if bool(baseline["stronger_baseline_warning"]) else "accept"


def combined_decision(
    baseline: dict[str, object],
    omniabase: dict[str, object],
) -> str:
    if bool(baseline["stronger_baseline_warning"]):
        return "retry"

    if bool(omniabase["cross_base_fragility_warning"]):
        return "review"

    return "accept"


def build_validation_set() -> list[dict[str, str]]:
    return [
        {"id": "hv_001", "group": "clean", "text": "The answer is 37."},
        {"id": "hv_002", "group": "clean", "text": "The reasoning is consistent and the conclusion follows from the premises."},
        {"id": "hv_003", "group": "clean", "text": "The model produced a concise answer with a short explanation."},
        {"id": "hv_004", "group": "brittle_numeric", "text": "The answer is 1024."},
        {"id": "hv_005", "group": "brittle_numeric", "text": "Final result: 4096."},
        {"id": "hv_006", "group": "loop_like", "text": "retry retry retry retry retry"},
        {"id": "hv_007", "group": "loop_like", "text": "the the the the the the"},
        {"id": "hv_008", "group": "pattern_explicit", "text": "abababababababab"},
        {"id": "hv_009", "group": "pattern_explicit", "text": "1212121212121212"},
        {"id": "hv_010", "group": "suspicious_clean", "text": "The answer seems correct. The answer seems correct. The answer seems correct."},
        {"id": "hv_011", "group": "suspicious_clean", "text": "Result stable. Result stable. Result stable."},
        {"id": "hv_012", "group": "suspicious_clean", "text": "No issue detected. No issue detected. No issue detected."},
        {"id": "hv_013", "group": "paraphrase_like", "text": "The answer appears correct. The result appears correct. The conclusion appears correct."},
        {"id": "hv_014", "group": "paraphrase_like", "text": "The output looks stable. The output seems stable. The output remains stable."},
        {"id": "hv_015", "group": "low_diversity", "text": "The reasoning is valid because the reasoning is valid in the final reasoning step."},
        {"id": "hv_016", "group": "low_diversity", "text": "The result follows because it follows from the result that follows."},
        {"id": "hv_017", "group": "hybrid", "text": "Answer: 333333. The result looks stable. The result looks stable."},
        {"id": "hv_018", "group": "hybrid", "text": "Answer: 2048. Everything appears normal."},
        {"id": "hv_019", "group": "near_threshold", "text": "abcabcabcx"},
        {"id": "hv_020", "group": "near_threshold", "text": "12121213"},
    ]


def main() -> None:
    out_dir = Path("artifacts/human_validation_v0")
    out_dir.mkdir(parents=True, exist_ok=True)

    adapter = OmniabaseGateAdapter()
    dataset = build_validation_set()

    prediction_rows: list[dict[str, object]] = []
    rating_rows: list[dict[str, object]] = []

    for item in dataset:
        baseline = stronger_baseline_score(item["text"])
        omniabase = adapter.evaluate_text(item["text"]).to_dict()

        base_decision = baseline_decision(baseline)
        comb_decision = combined_decision(baseline, omniabase)

        prediction_rows.append(
            {
                "id": item["id"],
                "group": item["group"],
                "text": item["text"],
                "baseline_decision": base_decision,
                "combined_decision": comb_decision,
                "baseline_warning": bool(baseline["stronger_baseline_warning"]),
                "omniabase_warning": bool(omniabase["cross_base_fragility_warning"]),
                "ob_cross_base_stability": omniabase["ob_cross_base_stability"],
                "ob_base_sensitivity": omniabase["ob_base_sensitivity"],
                "ob_collapse_count": omniabase["ob_collapse_count"],
            }
        )

        rating_rows.append(
            {
                "id": item["id"],
                "group": item["group"],
                "text": item["text"],
                "human_label": "",
                "notes": "",
            }
        )

    predictions_path = out_dir / "omnia_human_validation_predictions_v0.json"
    rating_csv_path = out_dir / "omnia_human_validation_sheet_v0.csv"
    instructions_path = out_dir / "omnia_human_validation_instructions_v0.md"

    with predictions_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "validation_name": "OMNIA Human Validation Pack v0",
                "label_space": ["accept", "review", "retry"],
                "predictions": prediction_rows,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    with rating_csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "group", "text", "human_label", "notes"],
        )
        writer.writeheader()
        writer.writerows(rating_rows)

    instructions = """# OMNIA Human Validation Instructions v0

## Goal

Rate each output with exactly one label:

- accept
- review
- retry

## Meaning of labels

### accept
Use when the output looks normal enough to pass without intervention.

### review
Use when the output is not clearly broken, but looks suspicious, repetitive, rigid, low-diversity, or structurally questionable enough to deserve human or secondary inspection.

### retry
Use when the output looks clearly degraded, brittle, repetitive, or low-quality enough that it should not pass as-is.

## Important rule

Do not try to guess what the model predicted internally.
Rate only the observed output text.

## Notes field

Use the notes field only for short justification, for example:

- soft repetition
- obvious loop
- rigid template
- normal answer
- low-diversity explanation
- suspicious but not broken
"""

    instructions_path.write_text(instructions, encoding="utf-8")

    print(json.dumps(
        {
            "status": "ok",
            "output_dir": str(out_dir),
            "files_created": [
                str(predictions_path),
                str(rating_csv_path),
                str(instructions_path),
            ],
            "num_items": len(dataset),
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()