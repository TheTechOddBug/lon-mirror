from __future__ import annotations

import json
import re
from collections import defaultdict
from statistics import mean

from examples.omnia_base_gate_adapter_demo import OmniabaseGateAdapter


def baseline_score(text: str) -> dict[str, object]:
    """
    Minimal sandbox baseline.

    This is intentionally weak and transparent.
    It does not try to be smart.
    It only emits a few shallow signals.

    Signals:
    - repeated_char_warning
    - repeated_token_warning
    - numeric_power_of_two_warning
    - baseline_warning
    """
    stripped = text.strip()
    lowered = stripped.lower()

    repeated_char_warning = has_long_repeated_char_run(stripped, min_run=8)
    repeated_token_warning = has_repeated_token_loop(lowered, min_repetitions=4)

    numeric_value = extract_last_integer(stripped)
    numeric_power_of_two_warning = False
    if numeric_value is not None and numeric_value > 0:
        numeric_power_of_two_warning = is_power_of_two(numeric_value)

    baseline_warning = (
        repeated_char_warning
        or repeated_token_warning
        or numeric_power_of_two_warning
    )

    return {
        "repeated_char_warning": repeated_char_warning,
        "repeated_token_warning": repeated_token_warning,
        "numeric_power_of_two_warning": numeric_power_of_two_warning,
        "baseline_warning": baseline_warning,
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

    counts = defaultdict(int)
    for token in tokens:
        counts[token] += 1

    return any(count >= min_repetitions for count in counts.values())


def extract_last_integer(text: str) -> int | None:
    matches = re.findall(r"-?\d+", text)
    if not matches:
        return None
    return abs(int(matches[-1]))


def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1) == 0)


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
        "baseline_warning": summarize_bool_rate(
            [bool(item["baseline"]["baseline_warning"]) for item in items]
        ),
        "omniabase_warning": summarize_bool_rate(
            [bool(item["omniabase"]["cross_base_fragility_warning"]) for item in items]
        ),
        "agreement_rate": round(
            mean(
                1.0
                if bool(item["baseline"]["baseline_warning"]) == bool(item["omniabase"]["cross_base_fragility_warning"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "omniabase_only_rate": round(
            mean(
                1.0
                if (not bool(item["baseline"]["baseline_warning"]))
                and bool(item["omniabase"]["cross_base_fragility_warning"])
                else 0.0
                for item in items
            ),
            6,
        ),
        "baseline_only_rate": round(
            mean(
                1.0
                if bool(item["baseline"]["baseline_warning"])
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
            baseline = baseline_score(text)
            omniabase = adapter.evaluate_text(text).to_dict()

            class_items.append(
                {
                    "input_text": text,
                    "baseline": baseline,
                    "omniabase": omniabase,
                }
            )

        raw_results[class_name] = class_items
        summary[class_name] = summarize_class(class_items)

    payload = {
        "comparison_name": "OMNIA Gate Sandbox Baseline vs OMNIABASE v0",
        "baseline_description": "repeated-char + repeated-token + power-of-two shallow warnings",
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