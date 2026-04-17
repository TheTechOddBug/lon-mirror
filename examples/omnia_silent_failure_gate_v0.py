"""
OMNIA Silent Failure Gate v0
Toy structural sensitivity demo.

What this demo does:
- measures transform sensitivity of model outputs
- compares exact match vs normalized correctness
- shows that some normalized-correct outputs are structurally more sensitive than others

What this demo does NOT do:
- it does not prove semantic fragility in general
- it does not prove pre-collapse prediction
- it does not establish real-world failure forecasting
"""

import json
import re
from typing import Dict, List

from omnia.lenses.aperspective_invariance import (
    AperspectiveInvariance,
    t_identity,
    t_whitespace_collapse,
    t_reverse,
    t_drop_vowels,
)
from omnia.iri import IRI
from omnia.sei import SEI
from omnia.omega_set import OmegaSet


def normalize_text(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[\"'`]", "", text)
    return text


def extract_number(text: str) -> str:
    matches = re.findall(r"-?\d+(?:\.\d+)?", text)
    return matches[-1] if matches else ""


def extract_yes_no(text: str) -> str:
    t = normalize_text(text)
    if re.search(r"\byes\b", t):
        return "yes"
    if re.search(r"\bno\b", t):
        return "no"
    return ""


def extract_capital_answer(text: str) -> str:
    t = normalize_text(text)
    if "paris" in t:
        return "paris"
    if "lyon" in t:
        return "lyon"
    if "marseille" in t:
        return "marseille"
    return ""


def extract_translation_answer(text: str) -> str:
    t = normalize_text(text)
    if "hola" in t:
        return "hola"
    return ""


def normalize_answer(question: str, text: str) -> str:
    q = normalize_text(question)
    t = normalize_text(text)

    if "17 * 23" in q or "2 + 2" in q or "sqrt(144)" in q or "what year did wwii end" in q:
        num = extract_number(t)
        return num if num else t

    if "solve: x + 5 = 12" in q:
        num = extract_number(t)
        return f"x = {num}" if num else t

    if "capital of france" in q:
        ans = extract_capital_answer(t)
        return ans if ans else t

    if "is 17 prime" in q:
        ans = extract_yes_no(t)
        return ans if ans else t

    if "translate 'hello' to spanish" in q:
        ans = extract_translation_answer(t)
        return ans if ans else t

    return t


def measure_output(text: str) -> Dict:
    transforms = [
        ("id", t_identity),
        ("ws", t_whitespace_collapse),
        ("rev", t_reverse),
        ("vow-", t_drop_vowels),
    ]

    ap = AperspectiveInvariance(transforms=transforms)
    ap_result = ap.measure(text)

    omega_samples = list(ap_result.per_transform_scores.values())
    omega_set = OmegaSet(omega_samples)
    omega_stats = omega_set.estimate()

    cost_curve = list(range(len(omega_samples)))
    sei = SEI(window=1, eps=1e-12)
    sei_curve = sei.curve(omega_samples, cost_curve)
    sei_mean = sum(sei_curve) / len(sei_curve) if sei_curve else 0.0

    text_perturbed = re.sub(r"\s+", "  ", text).strip()
    ap_perturbed = ap.measure(text_perturbed)

    iri_calculator = IRI()
    iri_value = iri_calculator.value(
        ap_result.omega_score,
        ap_perturbed.omega_score
    )

    return {
        "omega": round(ap_result.omega_score, 6),
        "omega_median": round(omega_stats["median"], 6),
        "omega_mad": round(omega_stats["mad"], 6),
        "sei_mean": round(sei_mean, 6),
        "iri": round(iri_value, 6),
    }


def classify_structural_sensitivity(metrics: Dict) -> str:
    omega = metrics["omega"]
    mad = metrics["omega_mad"]
    iri = metrics["iri"]
    sei = metrics["sei_mean"]

    if omega < 0.30 or iri > 0.40 or abs(sei) < 0.01:
        return "degraded"

    if omega > 0.70 and mad < 0.10 and iri < 0.10:
        return "invariant"

    return "sensitive"


def process_dataset(input_path: str, output_path: str) -> List[Dict]:
    results = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            item = json.loads(line)

            metrics = measure_output(item["model_output"])
            structural_class = classify_structural_sensitivity(metrics)

            exact_match = item["model_output"].strip() == item["correct"].strip()

            normalized_model = normalize_answer(item["question"], item["model_output"])
            normalized_correct = normalize_answer(item["question"], item["correct"])
            normalized_match = normalized_model == normalized_correct

            result = {
                "id": item["id"],
                "question": item["question"],
                "correct": item["correct"],
                "model_output": item["model_output"],
                "exact_match": exact_match,
                "normalized_model_output": normalized_model,
                "normalized_correct": normalized_correct,
                "normalized_match": normalized_match,
                **metrics,
                "structural_class": structural_class,
            }
            results.append(result)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results


def summarize(results: List[Dict]) -> Dict:
    total = len(results)

    exact_match_count = sum(1 for r in results if r["exact_match"])
    normalized_match_count = sum(1 for r in results if r["normalized_match"])

    invariant_count = sum(1 for r in results if r["structural_class"] == "invariant")
    sensitive_count = sum(1 for r in results if r["structural_class"] == "sensitive")
    degraded_count = sum(1 for r in results if r["structural_class"] == "degraded")

    normalized_match_but_sensitive = sum(
        1 for r in results
        if r["normalized_match"] and r["structural_class"] == "sensitive"
    )
    normalized_match_but_degraded = sum(
        1 for r in results
        if r["normalized_match"] and r["structural_class"] == "degraded"
    )

    return {
        "total": total,
        "exact_match_count": exact_match_count,
        "normalized_match_count": normalized_match_count,
        "invariant_count": invariant_count,
        "sensitive_count": sensitive_count,
        "degraded_count": degraded_count,
        "normalized_match_but_sensitive": normalized_match_but_sensitive,
        "normalized_match_but_degraded": normalized_match_but_degraded,
    }


def print_summary(summary: Dict) -> None:
    total = summary["total"]

    print("OMNIA Silent Failure Gate v0")
    print("=" * 60)
    print()
    print(f"Total examples: {total}")
    print(f"Exact match: {summary['exact_match_count']} ({100.0 * summary['exact_match_count'] / total:.1f}%)")
    print(f"Normalized match: {summary['normalized_match_count']} ({100.0 * summary['normalized_match_count'] / total:.1f}%)")
    print()
    print(f"Invariant: {summary['invariant_count']} ({100.0 * summary['invariant_count'] / total:.1f}%)")
    print(f"Sensitive: {summary['sensitive_count']} ({100.0 * summary['sensitive_count'] / total:.1f}%)")
    print(f"Degraded: {summary['degraded_count']} ({100.0 * summary['degraded_count'] / total:.1f}%)")
    print()
    print("Among normalized-correct outputs:")
    print(f"  Sensitive: {summary['normalized_match_but_sensitive']}")
    print(f"  Degraded:  {summary['normalized_match_but_degraded']}")
    print()
    print("Interpretation:")
    print("- exact_match is strict string equality")
    print("- normalized_match is a toy task-aware normalization")
    print("- structural_class is transform sensitivity only")
    print("- no semantic truth claim is made here")


if __name__ == "__main__":
    input_file = "examples/silent_failure_v0.jsonl"
    output_file = "examples/silent_failure_results_v0.json"

    results = process_dataset(input_file, output_file)
    summary = summarize(results)
    print_summary(summary)

    print(f"Results written to: {output_file}")