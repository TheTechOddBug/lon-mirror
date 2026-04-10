#!/usr/bin/env python3
"""
OMNIA Retry Loop Adapter Path v0
Minimal runtime integration wrapper.

Purpose
-------
Turn the calibrated OMNIA Silent Failure Gate into a small runtime middleware
that manages:

- generation attempt #1
- OMNIA gate evaluation
- optional retry
- final workflow action
- audit-ready runtime result
- operational efficiency summary

This implementation uses a deterministic mock generator so the adapter path
can be tested without external API noise.

Author: Massimiliano Brighindi
Project: MB-X.01 / OMNIA
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from omnia_silent_failure_gate_v0 import omnia_gate


INPUT_PATH = "data/omnia_silent_failure_retry_loop_v0_samples.jsonl"
OUTPUT_PATH = "data/omnia_retry_loop_adapter_path_v0_results.jsonl"


@dataclass
class RuntimeAttempt:
    attempt_index: int
    model_output: str
    surface_accept: bool
    gate_action: str
    triggered_rules: List[str] = field(default_factory=list)
    signals: Dict[str, Any] = field(default_factory=dict)
    rationale: str = ""


@dataclass
class RuntimeMetrics:
    retry_used: bool = False
    retry_improved: bool = False
    baseline_harmful_accept: bool = False
    final_harmful_accept: bool = False
    safety_dividend: int = 0
    retry_waste: int = 0
    escalation_precision_candidate: bool = False


@dataclass
class RuntimeResult:
    sample_id: str
    input_payload: str
    attempts: List[RuntimeAttempt]
    final_action: str
    final_output: Optional[str]
    retry_count: int
    escalated: bool
    accepted: bool
    audit_label: str
    metrics: RuntimeMetrics
    notes: str = ""


class MockGenerator:
    """
    Deterministic generator bound to a single sample.

    attempt_index:
    - 1 -> candidate_1_output
    - 2 -> candidate_2_output
    """

    def __init__(self, sample: Dict[str, Any]) -> None:
        self.sample = sample

    def generate(self, attempt_index: int) -> str:
        if attempt_index == 1:
            return self.sample["candidate_1_output"]
        if attempt_index == 2:
            return self.sample["candidate_2_output"]
        raise ValueError(f"Unsupported attempt_index: {attempt_index}")


def load_samples_jsonl(path: str) -> List[Dict[str, Any]]:
    samples: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                sample = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {lineno} of {path}: {e}") from e

            required = [
                "sample_id",
                "input_text",
                "candidate_1_output",
                "candidate_1_real_outcome",
                "candidate_2_output",
                "candidate_2_real_outcome",
            ]
            missing = [k for k in required if k not in sample]
            if missing:
                raise ValueError(
                    f"Missing required keys on line {lineno} of {path}: {missing}"
                )

            samples.append(sample)
    return samples


def surface_accept(model_output: str) -> bool:
    try:
        obj = json.loads(model_output)
        return isinstance(obj, dict) and len(obj) > 0
    except Exception:
        return False


def outcome_is_correct(outcome: str) -> bool:
    return outcome in {"correct", "fragile_correct"}


def accepted_from_final_action(final_action: str) -> bool:
    return final_action in {
        "pass",
        "low_confidence_flag",
        "accepted_after_retry",
        "accepted_after_retry_flagged",
    }


def classify_audit_label(
    baseline_harmful_accept: bool,
    final_harmful_accept: bool,
    baseline_correct: bool,
    final_correct: bool,
    accepted: bool,
) -> str:
    if baseline_harmful_accept and not final_harmful_accept:
        return "silent_failure_avoided"

    if baseline_harmful_accept and final_harmful_accept:
        return "harm_not_resolved"

    if baseline_correct and final_correct and accepted:
        return "stable_success_preserved"

    if baseline_correct and not accepted:
        return "over_defensive_intervention"

    return "neutral"


def normalize_final_action(initial_action: str, retry_action: Optional[str]) -> str:
    if initial_action != "retry":
        return initial_action

    if retry_action is None:
        return "retry_failed"

    if retry_action == "reject_surface":
        return "retry_failed"

    if retry_action == "escalate":
        return "escalate_after_retry"

    if retry_action == "retry":
        return "retry_failed"

    if retry_action == "low_confidence_flag":
        return "accepted_after_retry_flagged"

    if retry_action == "pass":
        return "accepted_after_retry"

    return "retry_failed"


def build_attempt(attempt_index: int, output_text: str) -> RuntimeAttempt:
    gate = omnia_gate(output_text)
    return RuntimeAttempt(
        attempt_index=attempt_index,
        model_output=output_text,
        surface_accept=gate.baseline_accept,
        gate_action=gate.action,
        triggered_rules=gate.triggered_rules,
        signals=asdict(gate.signals),
        rationale=gate.rationale,
    )


def run_with_omnia_retry_loop(
    input_payload: str,
    generator: MockGenerator,
    candidate_1_real_outcome: str,
    candidate_2_real_outcome: str,
    max_retries: int = 1,
    notes: str = "",
    sample_id: str = "",
) -> RuntimeResult:
    attempts: List[RuntimeAttempt] = []

    # Attempt 1
    output_1 = generator.generate(attempt_index=1)
    attempt_1 = build_attempt(1, output_1)
    attempts.append(attempt_1)

    baseline_harmful_accept = attempt_1.surface_accept and not outcome_is_correct(candidate_1_real_outcome)
    baseline_correct = outcome_is_correct(candidate_1_real_outcome)

    retry_used = False
    retry_improved = False
    final_action = attempt_1.gate_action
    final_output = output_1
    final_real_outcome = candidate_1_real_outcome

    if attempt_1.gate_action == "retry" and max_retries >= 1:
        retry_used = True
        output_2 = generator.generate(attempt_index=2)
        attempt_2 = build_attempt(2, output_2)
        attempts.append(attempt_2)

        final_action = normalize_final_action(attempt_1.gate_action, attempt_2.gate_action)
        final_output = output_2
        final_real_outcome = candidate_2_real_outcome

        retry_improved = (
            not outcome_is_correct(candidate_1_real_outcome)
            and outcome_is_correct(candidate_2_real_outcome)
            and accepted_from_final_action(final_action)
        )

    accepted = accepted_from_final_action(final_action)
    final_harmful_accept = accepted and not outcome_is_correct(final_real_outcome)
    final_correct = outcome_is_correct(final_real_outcome)

    audit_label = classify_audit_label(
        baseline_harmful_accept=baseline_harmful_accept,
        final_harmful_accept=final_harmful_accept,
        baseline_correct=baseline_correct,
        final_correct=final_correct,
        accepted=accepted,
    )

    metrics = RuntimeMetrics(
        retry_used=retry_used,
        retry_improved=retry_improved,
        baseline_harmful_accept=baseline_harmful_accept,
        final_harmful_accept=final_harmful_accept,
        safety_dividend=1 if baseline_harmful_accept and not final_harmful_accept else 0,
        retry_waste=1 if retry_used and not retry_improved and final_action in {"retry_failed", "accepted_after_retry_flagged"} else 0,
        escalation_precision_candidate=final_action in {"escalate", "escalate_after_retry"} and not outcome_is_correct(final_real_outcome),
    )

    return RuntimeResult(
        sample_id=sample_id,
        input_payload=input_payload,
        attempts=attempts,
        final_action=final_action,
        final_output=final_output,
        retry_count=1 if retry_used else 0,
        escalated=final_action in {"escalate", "escalate_after_retry"},
        accepted=accepted,
        audit_label=audit_label,
        metrics=metrics,
        notes=notes,
    )


def summarize(results: List[RuntimeResult]) -> Dict[str, Any]:
    final_action_distribution = {
        "pass": 0,
        "low_confidence_flag": 0,
        "accepted_after_retry": 0,
        "accepted_after_retry_flagged": 0,
        "escalate": 0,
        "escalate_after_retry": 0,
        "retry_failed": 0,
        "reject_surface": 0,
    }

    net_effect_distribution = {
        "silent_failure_avoided": 0,
        "stable_success_preserved": 0,
        "over_defensive_intervention": 0,
        "harm_not_resolved": 0,
        "neutral": 0,
    }

    retry_used = 0
    retry_improved = 0
    baseline_harmful_accepts = 0
    gated_harmful_accepts = 0
    safety_dividend = 0
    retry_waste = 0

    for r in results:
        if r.final_action in final_action_distribution:
            final_action_distribution[r.final_action] += 1

        if r.audit_label in net_effect_distribution:
            net_effect_distribution[r.audit_label] += 1

        if r.metrics.retry_used:
            retry_used += 1
        if r.metrics.retry_improved:
            retry_improved += 1
        if r.metrics.baseline_harmful_accept:
            baseline_harmful_accepts += 1
        if r.metrics.final_harmful_accept:
            gated_harmful_accepts += 1

        safety_dividend += r.metrics.safety_dividend
        retry_waste += r.metrics.retry_waste

    return {
        "total_processed": len(results),
        "retry_used": retry_used,
        "retry_improved_outcome": retry_improved,
        "baseline_harmful_accepts": baseline_harmful_accepts,
        "gated_harmful_accepts": gated_harmful_accepts,
        "net_harmful_acceptance_reduction": baseline_harmful_accepts - gated_harmful_accepts,
        "safety_dividend": safety_dividend,
        "retry_waste": retry_waste,
        "final_action_distribution": final_action_distribution,
        "net_effect_distribution": net_effect_distribution,
    }


def main() -> None:
    if not os.path.exists(INPUT_PATH):
        print(f"Error: {INPUT_PATH} not found.")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    samples = load_samples_jsonl(INPUT_PATH)
    results: List[RuntimeResult] = []

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        for sample in samples:
            generator = MockGenerator(sample)
            result = run_with_omnia_retry_loop(
                input_payload=sample["input_text"],
                generator=generator,
                candidate_1_real_outcome=sample["candidate_1_real_outcome"],
                candidate_2_real_outcome=sample["candidate_2_real_outcome"],
                max_retries=1,
                notes=sample.get("notes", ""),
                sample_id=sample["sample_id"],
            )
            results.append(result)
            out.write(json.dumps(asdict(result), ensure_ascii=False) + "\n")

    summary = summarize(results)

    print("\n--- OMNIA Retry Loop Adapter Path v0 Summary ---")
    print(f"Total processed: {summary['total_processed']}")
    print(f"Retry used: {summary['retry_used']}")
    print(f"Retry improved outcome: {summary['retry_improved_outcome']}")
    print(f"Baseline harmful accepts: {summary['baseline_harmful_accepts']}")
    print(f"Gated harmful accepts: {summary['gated_harmful_accepts']}")
    print(f"Net harmful acceptance reduction: {summary['net_harmful_acceptance_reduction']}")
    print(f"Safety dividend: {summary['safety_dividend']}")
    print(f"Retry waste: {summary['retry_waste']}")
    print(f"Final action distribution: {summary['final_action_distribution']}")
    print(f"Net effect distribution: {summary['net_effect_distribution']}")
    print(f"Results saved to: {OUTPUT_PATH}\n")


if __name__ == "__main__":
    main()