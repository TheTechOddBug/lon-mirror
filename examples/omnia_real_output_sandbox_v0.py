from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
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

    alternating_pattern_warning = has_short_cycle_pattern(stripped, max_cycle_len=4, min_repeats=4)
    repeated_block_warning = has_repeated_block_pattern(stripped, min_block_len=2, max_block_len=6, min_repeats=3)

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


def has_short_cycle_pattern(text: str, max_cycle_len: int = 4, min_repeats: int = 4) -> bool:
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


def has_repeated_block_pattern(text: str, min_block_len: int = 2, max_block_len: int = 6, min_repeats: int = 3) -> bool:
    s = text.strip()
    n = len(s)

    for block_len in range(min_block_len, max_block_len + 1):
        if n < block_len * min_repeats:
            continue

        for start in range(0, n - block_len + 1):
            block = s[start:start + block_len]
            if len(block) < block_len:
                continue

            count = 0
            pos = 0
            while pos + block_len <= n:
                if s[pos:pos + block_len] == block:
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


def build_real_output_sandbox() -> dict[str, list[str]]:
    return {
        "clean_numeric_answers": [
            "The answer is 37.",
            "Final result: 91.",
            "After checking the arithmetic, the answer is 143.",
            "Output: 257.",
            "The correct result is 389.",
        ],
        "brittle_numeric_answers": [
            "The answer is 1024.",
            "Final result: 2048.",
            "After recomputing, the answer is 4096.",
            "Output: 8192.",
            "The correct result is 16384.",
        ],
        "clean_short_explanations": [
            "The reasoning is consistent and the conclusion follows from the premises.",
            "I checked the final step and no contradiction appears in the result.",
            "The output remains coherent under the current interpretation.",
            "The answer is supported by the previous computation steps.",
            "This result is internally consistent and concise.",
        ],
        "loop_like_outputs": [
            "the the the the the the",
            "retry retry retry retry retry",
            "same same same same same same",
            "error error error error error",
            "again again again again again",
        ],
        "pattern_heavy_outputs": [
            "abababababababab",
            "1212121212121212",
            "xyzxyzxyzxyzxyzx",
            "abcabcabcabcabca",
            "qwertqwertqwert",
        ],
        "superficially_clean_but_suspicious": [
            "The answer seems correct. The answer seems correct. The answer seems correct.",
            "Result stable. Result stable. Result stable.",
            "No issue detected, no issue detected, no issue detected.",
            "The final answer is 111111.",
            "The system reports score 1024 with no visible issue.",
        ],
        "natural_mixed_outputs": [
            "The model produced a short explanation and then a concise answer.",
            "This response looks normal at first glance and does not repeat tokens.",
            "A brief rationale is followed by a final statement without visible loops.",
            "The generated text remains readable and not obviously degenerate.",
            "Nothing in this output appears syntactically broken.",
        ],
    }


def summarize_bool_rate(values: list[bool]) -> dict[str, float | int]:
    true_count = sum(1 for v in values if v)
    total = len(values)
    return {
        "true_count": true_count,
        "false_count": total - true_count,
        "true_rate": round(true_count / total, 6),
    }


def summarize_float(values: list[float]) -> dict[str, float]:
    return {
        "mean": round(mean(values), 6),
        "min": round(min(values), 6),
        "max": round(max(values), 6),
    }


def summarize_class(items: list[dict[str, object]]) -> dict[str, object]:
    return {
        "sample_size": len(items),
        "stronger_baseline_warning": summarize_bool_rate(
            [bool(item["stronger_baseline"]["stronger_baseline_warning"]) for item in items]
        ),
        "omniabase_warning": summarize_bool_rate(
            [bool(item["omniabase"]["cross_base_fragility_warning"]) for item in items]
        ),
        "agreement_rate": round(
            mean(
                1.0
                if bool(item["stronger_baseline"]["stronger_baseline_warning"]) == bool(item["omniabase"]["cross_base_fragility_warning"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "omniabase_only_rate": round(
            mean(
                1.0
                if (not bool(item["stronger_baseline"]["stronger_baseline_warning"]))
                and bool(item["omniabase"]["cross_base_fragility_warning"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "baseline_only_rate": round(
            mean(
                1.0
                if bool(item["stronger_baseline"]["stronger_baseline_warning"])
                and (not bool(item["omniabase"]["cross_base_fragility_warning"]))
                else 0.0
                for item in items
            ),
            6,
        ),
        "mean_ob_cross_base_stability": summarize_float(
            [float(item["omniabase"]["ob_cross_base_stability"]) for item in items]
        ),
        "mean_ob_base_sensitivity": summarize_float(
            [float(item["omniabase"]["ob_base_sensitivity"]) for item in items]
        ),
    }


def main() -> None:
    adapter = OmniabaseGateAdapter()
    candidate_set = build_real_output_sandbox()

    raw_results: dict[str, list[dict[str, object]]] = {}
    summary: dict[str, dict[str, object]] = {}

    for class_name, texts in candidate_set.items():
        class_items: list[dict[str, object]] = []

        for text in texts:
            stronger_baseline = stronger_baseline_score(text)
            omniabase = adapter.evaluate_text(text).to_dict()

            class_items.append(
                {
                    "input_text": text,
                    "stronger_baseline": stronger_baseline,
                    "omniabase": omniabase,
                }
            )

        raw_results[class_name] = class_items
        summary[class_name] = summarize_class(class_items)

    payload = {
        "comparison_name": "OMNIA Real Output Sandbox v0",
        "stronger_baseline_description": (
            "repeated-char + repeated-token + power-of-two + "
            "alternating-pattern + repeated-block + repeated-numeric-block warnings"
        ),
        "omniabase_warning_rule": {
            "ob_cross_base_stability_lt": adapter.warning_stability_threshold,
            "ob_collapse_count_gte": adapter.warning_collapse_threshold,
            "ob_base_sensitivity_gte": adapter.warning_sensitivity_threshold,
        },
        "classes": list(candidate_set.keys()),
        "summary": summary,
        "raw_results": raw_results,
    }

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()