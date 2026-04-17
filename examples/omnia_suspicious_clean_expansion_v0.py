from __future__ import annotations

import json
import re
from collections import Counter
from statistics import mean

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


def build_suspicious_clean_set() -> list[dict[str, str]]:
    """
    expected labels:
    - accept: looks normal enough, no intervention expected
    - review: superficially acceptable but structurally suspicious
    - retry: openly degraded or clearly brittle
    """
    return [
        {
            "id": "sc_001",
            "subclass": "soft_sentence_repetition",
            "text": "The answer seems correct. The answer seems correct. The answer seems correct.",
            "expected": "review",
        },
        {
            "id": "sc_002",
            "subclass": "soft_sentence_repetition",
            "text": "Result stable. Result stable. Result stable.",
            "expected": "review",
        },
        {
            "id": "sc_003",
            "subclass": "soft_sentence_repetition",
            "text": "No issue detected. No issue detected. No issue detected.",
            "expected": "review",
        },
        {
            "id": "sc_004",
            "subclass": "rigid_template_numeric",
            "text": "The final answer is 111111.",
            "expected": "review",
        },
        {
            "id": "sc_005",
            "subclass": "rigid_template_numeric",
            "text": "The system reports score 1024 with no visible issue.",
            "expected": "retry",
        },
        {
            "id": "sc_006",
            "subclass": "rigid_template_numeric",
            "text": "The final result is 121212121.",
            "expected": "review",
        },
        {
            "id": "sc_007",
            "subclass": "light_paraphrase_repetition",
            "text": "The answer appears correct. The result appears correct. The conclusion appears correct.",
            "expected": "review",
        },
        {
            "id": "sc_008",
            "subclass": "light_paraphrase_repetition",
            "text": "The output looks stable. The output seems stable. The output remains stable.",
            "expected": "review",
        },
        {
            "id": "sc_009",
            "subclass": "light_paraphrase_repetition",
            "text": "This seems fine. This looks fine. This remains fine.",
            "expected": "accept",
        },
        {
            "id": "sc_010",
            "subclass": "low_diversity_explanation",
            "text": "The reasoning is valid because the reasoning is valid in the final reasoning step.",
            "expected": "review",
        },
        {
            "id": "sc_011",
            "subclass": "low_diversity_explanation",
            "text": "The result follows because it follows from the result that follows.",
            "expected": "review",
        },
        {
            "id": "sc_012",
            "subclass": "low_diversity_explanation",
            "text": "The explanation is short and coherent.",
            "expected": "accept",
        },
        {
            "id": "sc_013",
            "subclass": "clean_controls",
            "text": "The reasoning is consistent and the conclusion follows from the premises.",
            "expected": "accept",
        },
        {
            "id": "sc_014",
            "subclass": "clean_controls",
            "text": "I checked the final step and no contradiction appears in the result.",
            "expected": "accept",
        },
        {
            "id": "sc_015",
            "subclass": "clean_controls",
            "text": "The model produced a concise answer with a short explanation.",
            "expected": "accept",
        },
        {
            "id": "sc_016",
            "subclass": "hybrid_suspicious",
            "text": "Answer: 333333. The result looks stable. The result looks stable.",
            "expected": "review",
        },
        {
            "id": "sc_017",
            "subclass": "hybrid_suspicious",
            "text": "Answer: 2048. Everything appears normal.",
            "expected": "retry",
        },
        {
            "id": "sc_018",
            "subclass": "hybrid_suspicious",
            "text": "Answer: 97. Everything appears normal.",
            "expected": "accept",
        },
        {
            "id": "sc_019",
            "subclass": "soft_loopish",
            "text": "The answer is correct and correct and correct in the final form.",
            "expected": "review",
        },
        {
            "id": "sc_020",
            "subclass": "soft_loopish",
            "text": "The output remains coherent and coherent in the same way.",
            "expected": "review",
        },
        {
            "id": "sc_021",
            "subclass": "soft_loopish",
            "text": "The answer is brief and coherent.",
            "expected": "accept",
        },
        {
            "id": "sc_022",
            "subclass": "pattern_near_threshold",
            "text": "abcabcabcx",
            "expected": "review",
        },
        {
            "id": "sc_023",
            "subclass": "pattern_near_threshold",
            "text": "12121213",
            "expected": "review",
        },
        {
            "id": "sc_024",
            "subclass": "pattern_near_threshold",
            "text": "The pattern is not obvious and the answer remains readable.",
            "expected": "accept",
        },
    ]


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


def decision_matches_expected(decision: str, expected: str) -> bool:
    return decision == expected


def summarize_bool_rate(values: list[bool]) -> dict[str, float | int]:
    true_count = sum(1 for v in values if v)
    total = len(values)
    return {
        "true_count": true_count,
        "false_count": total - true_count,
        "true_rate": round(true_count / total, 6),
    }


def summarize_items(items: list[dict[str, object]]) -> dict[str, object]:
    return {
        "sample_size": len(items),
        "baseline_correct_rate": round(
            mean(1.0 if bool(item["baseline_correct"]) else 0.0 for item in items), 6
        ),
        "combined_correct_rate": round(
            mean(1.0 if bool(item["combined_correct"]) else 0.0 for item in items), 6
        ),
        "combined_better_than_baseline_rate": round(
            mean(
                1.0
                if bool(item["combined_correct"]) and not bool(item["baseline_correct"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "combined_worse_than_baseline_rate": round(
            mean(
                1.0
                if bool(item["baseline_correct"]) and not bool(item["combined_correct"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "baseline_accept_rate": round(
            mean(1.0 if item["baseline_decision"] == "accept" else 0.0 for item in items), 6
        ),
        "baseline_retry_rate": round(
            mean(1.0 if item["baseline_decision"] == "retry" else 0.0 for item in items), 6
        ),
        "combined_accept_rate": round(
            mean(1.0 if item["combined_decision"] == "accept" else 0.0 for item in items), 6
        ),
        "combined_review_rate": round(
            mean(1.0 if item["combined_decision"] == "review" else 0.0 for item in items), 6
        ),
        "combined_retry_rate": round(
            mean(1.0 if item["combined_decision"] == "retry" else 0.0 for item in items), 6
        ),
        "omniabase_warning_rate": summarize_bool_rate(
            [bool(item["omniabase"]["cross_base_fragility_warning"]) for item in items]
        ),
    }


def main() -> None:
    adapter = OmniabaseGateAdapter()
    dataset = build_suspicious_clean_set()

    raw_results: list[dict[str, object]] = []

    for item in dataset:
        baseline = stronger_baseline_score(item["text"])
        omniabase = adapter.evaluate_text(item["text"]).to_dict()

        baseline_dec = baseline_decision(baseline)
        combined_dec = combined_decision(baseline, omniabase)

        raw_results.append(
            {
                "id": item["id"],
                "subclass": item["subclass"],
                "text": item["text"],
                "expected": item["expected"],
                "baseline": baseline,
                "omniabase": omniabase,
                "baseline_decision": baseline_dec,
                "combined_decision": combined_dec,
                "baseline_correct": decision_matches_expected(baseline_dec, item["expected"]),
                "combined_correct": decision_matches_expected(combined_dec, item["expected"]),
            }
        )

    summary_by_subclass: dict[str, dict[str, object]] = {}
    subclass_names = sorted({item["subclass"] for item in raw_results})

    for subclass in subclass_names:
        subclass_items = [item for item in raw_results if item["subclass"] == subclass]
        summary_by_subclass[subclass] = summarize_items(subclass_items)

    overall_summary = summarize_items(raw_results)

    payload = {
        "sandbox_name": "OMNIA Suspicious Clean Expansion v0",
        "baseline_policy": {
            "warning_true": "retry",
            "warning_false": "accept",
        },
        "combined_policy": {
            "baseline_warning_true": "retry",
            "baseline_warning_false_and_omniabase_warning_true": "review",
            "no_warnings": "accept",
        },
        "expected_label_space": ["accept", "review", "retry"],
        "overall_summary": overall_summary,
        "summary_by_subclass": summary_by_subclass,
        "raw_results": raw_results,
    }

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()