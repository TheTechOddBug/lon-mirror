from __future__ import annotations

import json
from collections import defaultdict
from statistics import mean, median

from examples.omnia_base_gate_adapter_demo import OmniabaseGateAdapter


def summarize_float(values: list[float]) -> dict[str, float]:
    return {
        "mean": round(mean(values), 6),
        "median": round(median(values), 6),
        "min": round(min(values), 6),
        "max": round(max(values), 6),
    }


def summarize_int(values: list[int]) -> dict[str, float]:
    return {
        "mean": round(mean(values), 6),
        "median": round(median(values), 6),
        "min": int(min(values)),
        "max": int(max(values)),
    }


def summarize_bool(values: list[bool]) -> dict[str, float | int]:
    true_count = sum(1 for v in values if v)
    total = len(values)
    return {
        "true_count": true_count,
        "false_count": total - true_count,
        "true_rate": round(true_count / total, 6),
    }


def build_eval_set() -> dict[str, list[str]]:
    return {
        "direct_numeric_simple": [
            "42",
            "The answer is 17.",
            "Final result: 256",
            "Output = 999",
            "The final answer is 73.",
        ],
        "direct_numeric_powers": [
            "1024",
            "The answer is 2048.",
            "Final result: 4096",
            "Score = 8192",
            "The final answer is 16384.",
        ],
        "direct_numeric_repeated": [
            "111111",
            "The answer is 222222.",
            "Final result: 333333",
            "Score = 777777",
            "The final answer is 121212121.",
        ],
        "direct_numeric_prime_like": [
            "104729",
            "The answer is 99991.",
            "Final result: 65537",
            "Output = 524287",
            "The final answer is 32771.",
        ],
        "weighted_text_regular": [
            "The result appears consistent across all steps.",
            "The system reports a stable configuration.",
            "No visible issue was detected in the final pass.",
            "The reasoning remains uniform and bounded.",
            "The output looks coherent under the current check.",
        ],
        "weighted_text_repetitive": [
            "aaaaaaaaaaaaaaaa",
            "bbbbbbbbbbbbbbbb",
            "xxxxxxxxxxxxxxxx",
            "zzzzzzzzzzzzzzzz",
            "mmmmmmmmmmmmmmmm",
        ],
        "weighted_text_patterned": [
            "abababababababab",
            "1212121212121212",
            "xyzxyzxyzxyzxyzx",
            "abcabcabcabcabca",
            "qwertqwertqwert",
        ],
        "weighted_text_mixed": [
            "Alpha beta gamma delta.",
            "Signal drift is moderate but bounded.",
            "A clean output can still be fragile.",
            "Structural behavior changes under re-encoding.",
            "This response seems fine at first glance.",
        ],
    }


def main() -> None:
    adapter = OmniabaseGateAdapter()

    eval_set = build_eval_set()
    raw_results: dict[str, list[dict]] = defaultdict(list)
    summary: dict[str, dict] = {}

    for class_name, texts in eval_set.items():
        for text in texts:
            result = adapter.evaluate_text(text)
            raw_results[class_name].append(result.to_dict())

    for class_name, items in raw_results.items():
        summary[class_name] = {
            "sample_size": len(items),
            "projection_modes": {
                "direct_numeric": sum(1 for item in items if item["projection_mode"] == "direct_numeric"),
                "weighted_char_sum": sum(1 for item in items if item["projection_mode"] == "weighted_char_sum"),
            },
            "ob_cross_base_stability": summarize_float(
                [item["ob_cross_base_stability"] for item in items]
            ),
            "ob_representation_drift": summarize_float(
                [item["ob_representation_drift"] for item in items]
            ),
            "ob_base_sensitivity": summarize_float(
                [item["ob_base_sensitivity"] for item in items]
            ),
            "ob_collapse_count": summarize_int(
                [item["ob_collapse_count"] for item in items]
            ),
            "cross_base_fragility_warning": summarize_bool(
                [item["cross_base_fragility_warning"] for item in items]
            ),
        }

    payload = {
        "evaluation_name": "OMNIABASE Gate Adapter Eval v0",
        "warning_rule": {
            "ob_cross_base_stability_lt": adapter.warning_stability_threshold,
            "ob_collapse_count_gte": adapter.warning_collapse_threshold,
            "ob_base_sensitivity_gte": adapter.warning_sensitivity_threshold,
        },
        "classes": list(eval_set.keys()),
        "summary": summary,
        "raw_results": raw_results,
    }

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()