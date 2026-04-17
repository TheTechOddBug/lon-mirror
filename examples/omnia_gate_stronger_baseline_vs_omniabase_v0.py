from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from statistics import mean

from examples.omnia_base_gate_adapter_demo import OmniabaseGateAdapter


def stronger_baseline_score(text: str) -> dict[str, object]:
    """
    Stronger sandbox baseline.

    Still handcrafted and transparent, but less naive than the first baseline.

    Signals:
    - repeated_char_warning
    - repeated_token_warning
    - numeric_power_of_two_warning
    - alternating_pattern_warning
    - repeated_block_warning
    - repeated_numeric_block_warning
    - stronger_baseline_warning
    """
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
    """
    Detect pure short-cycle repetition over the whole string, e.g.
    'abababab', '12121212', 'xyzxyzxyzxyz' (with cycle len 3).
    """
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
    """
    Detect repeated substring blocks inside the full string, less strict than pure cycle.
    Example candidates:
    - abcabcabcabc
    - qwertqwertqwert
    - xyzxyzxyzxyzxyzx  -> may fail exact repetition if tail breaks, as intended
    """
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
    """
    Detect repeated numeric motifs such as:
    - 111111
    - 121212121
    - 333333
    """
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


def build_candidate_set() -> dict[str, list[str]]:
    return {
        "simple_numeric": [
            "42",
            "The answer is 17.",
            "Final result: 73",
            "Output = 91",
            "The final answer is 255.",
        ],
        "power_numeric": [
            "1024",
            "The answer is 2048.",
            "Final result: 4096",
            "Score = 8192",
            "The final answer is 16384.",
        ],
        "repeated_numeric": [
            "111111",
            "The answer is 222222.",
            "Final result: 333333",
            "Score = 777777",
            "The final answer is 121212121.",
        ],
        "prime_like_numeric": [
            "104729",
            "The answer is 99991.",
            "Final result: 65537",
            "Output = 524287",
            "The final answer is 32771.",
        ],
        "regular_text": [
            "The result appears consistent across all steps.",
            "The system reports a stable configuration.",
            "No visible issue was detected in the final pass.",
            "The reasoning remains uniform and bounded.",
            "The output looks coherent under the current check.",
        ],
        "repetitive_text": [
            "aaaaaaaaaaaaaaaa",
            "bbbbbbbbbbbbbbbb",
            "xxxxxxxxxxxxxxxx",
            "zzzzzzzzzzzzzzzz",
            "mmmmmmmmmmmmmmmm",
        ],
        "token_loop_text": [
            "the the the the the",
            "error error error error",
            "loop loop loop loop loop",
            "retry retry retry retry",
            "same same same same same",
        ],
        "patterned_text": [
            "abababababababab",
            "1212121212121212",
            "xyzxyzxyzxyzxyzx",
            "abcabcabcabcabca",
            "qwertqwertqwert",
        ],
        "mixed_text": [
            "Alpha beta gamma delta.",
            "Signal drift is moderate but bounded.",
            "A clean output can still be fragile.",
            "Structural behavior changes under re-encoding.",
            "This response seems fine at first glance.",
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
    }


def main() -> None:
    adapter = OmniabaseGateAdapter()
    candidate_set = build_candidate_set()

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
        "comparison_name": "OMNIA Gate Sandbox Stronger Baseline vs OMNIABASE v0",
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