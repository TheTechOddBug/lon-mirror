#!/usr/bin/env python3
"""
OMNIA Silent Failure Retry Loop v0
Minimal operational wrapper around the calibrated Silent Failure Gate.

Purpose
-------
Show how OMNIA changes workflow behavior, not only classification.

Flow
----
1. Load a structured sample set.
2. Evaluate candidate output #1 with baseline + OMNIA gate.
3. If action is:
   - pass -> accept
   - low_confidence_flag -> accept with warning
   - retry -> evaluate candidate output #2
   - escalate -> stop
4. Compare baseline outcome vs gated workflow outcome.
5. Save an audit-ready results file.

Important
---------
This is still a controlled example.
It demonstrates intervention logic, not production readiness.

Author: Massimiliano Brighindi
Project: MB-X.01 / OMNIA
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from omnia_silent_failure_gate_v0 import omnia_gate


INPUT_PATH = "data/omnia_silent_failure_retry_loop_v0_samples.jsonl"
OUTPUT_PATH = "data/omnia_silent_failure_retry_loop_v0_results.jsonl"


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


def baseline_surface_accept(model_output: str) -> bool:
    try:
        obj = json.loads(model_output)
        return isinstance(obj, dict) and len(obj) > 0
    except Exception:
        return False


def normalize_final_action(initial_action: str, retry_action: Optional[str]) -> str:
    """
    Final workflow action after optional retry.
    """
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


def gated_workflow_accepts(final_action: str) -> bool:
    return final_action in {
        "pass",
        "low_confidence_flag",
        "accepted_after_retry",
        "accepted_after_retry_flagged",
    }


def outcome_is_correct(outcome: str) -> bool:
    return outcome in {"correct", "fragile_correct"}


def classify_net_effect(
    baseline_accept: bool,
    baseline_outcome: str,
    final_accept: bool,
    final_outcome: Optional[str],
) -> str:
    """
    Compare baseline behavior against the gated workflow.
    """
    baseline_harmful_accept = baseline_accept and not outcome_is_correct(baseline_outcome)
    gated_harmful_accept = final_accept and final_outcome is not None and not outcome_is_correct(final_outcome)

    if baseline_harmful_accept and not gated_harmful_accept:
        return "silent_failure_avoided"

    if not baseline_harmful_accept and gated_harmful_accept:
        return "harm_introduced"

    if baseline_accept and outcome_is_correct(baseline_outcome) and final_accept and final_outcome is not None and outcome_is_correct(final_outcome):
        return "stable_success_preserved"

    if baseline_harmful_accept and gated_harmful_accept:
        return "harm_not_resolved"

    if baseline_accept and outcome_is_correct(baseline_outcome) and not final_accept:
        return "over_defensive_intervention"

    return "neutral"


def evaluate_sample(sample: Dict[str, Any]) -> Dict[str, Any]:
    input_text = sample["input_text"]

    c1_output = sample["candidate_1_output"]
    c1_outcome = sample["candidate_1_real_outcome"]

    c2_output = sample["candidate_2_output"]
    c2_outcome = sample["candidate_2_real_outcome"]

    baseline_accept = baseline_surface_accept(c1_output)

    gate_1 = omnia_gate(c1_output)

    gate_2 = None
    retry_used = False
    final_output = c1_output
    final_real_outcome: Optional[str] = c1_outcome
    final_gate_action = gate_1.action

    if gate_1.action == "retry":
        retry_used = True
        gate_2 = omnia_gate(c2_output)
        final_gate_action = normalize_final_action(gate_1.action, gate_2.action)
        final_output = c2_output
        final_real_outcome = c2_outcome

    final_accept = gated_workflow_accepts(final_gate_action)

    retry_improved = False
    if retry_used:
        retry_improved = (
            not outcome_is_correct(c1_outcome)
            and outcome_is_correct(c2_outcome)
            and final_accept
        )

    net_effect = classify_net_effect(
        baseline_accept=baseline_accept,
        baseline_outcome=c1_outcome,
        final_accept=final_accept,
        final_outcome=final_real_outcome,
    )

    return {
        "sample_id": sample["sample_id"],
        "input_text": input_text,
        "baseline": {
            "accepted": baseline_accept,
            "candidate_output": c1_output,
            "real_outcome": c1_outcome,
        },
        "gate_path": {
            "initial_action": gate_1.action,
            "initial_triggered_rules": gate_1.triggered_rules,
            "initial_rationale": gate_1.rationale,
            "initial_signals": asdict(gate_1.signals),
            "retry_used": retry_used,
            "retry_action": gate_2.action if gate_2 else None,
            "retry_triggered_rules": gate_2.triggered_rules if gate_2 else [],
            "retry_rationale": gate_2.rationale if gate_2 else "",
            "retry_signals": asdict(gate_2.signals) if gate_2 else None,
            "final_gate_action": final_gate_action,
        },
        "final_workflow": {
            "accepted": final_accept,
            "final_output": final_output,
            "final_real_outcome": final_real_outcome,
            "retry_improved": retry_improved,
            "net_effect": net_effect,
        },
        "notes": sample.get("notes", ""),
    }


def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(results)

    counts = {
        "pass": 0,
        "low_confidence_flag": 0,
        "retry": 0,
        "escalate": 0,
        "reject_surface": 0,
        "accepted_after_retry": 0,
        "accepted_after_retry_flagged": 0,
        "escalate_after_retry": 0,
        "retry_failed": 0,
    }

    net_effect_counts = {
        "silent_failure_avoided": 0,
        "stable_success_preserved": 0,
        "over_defensive_intervention": 0,
        "harm_not_resolved": 0,
        "harm_introduced": 0,
        "neutral": 0,
    }

    retry_used_count = 0
    retry_improved_count = 0
    baseline_harmful_accept_count = 0
    gated_harmful_accept_count = 0

    for row in results:
        final_action = row["gate_path"]["final_gate_action"]
        if final_action in counts:
            counts[final_action] += 1

        net_effect = row["final_workflow"]["net_effect"]
        if net_effect in net_effect_counts:
            net_effect_counts[net_effect] += 1

        if row["gate_path"]["retry_used"]:
            retry_used_count += 1
        if row["final_workflow"]["retry_improved"]:
            retry_improved_count += 1

        baseline_accept = row["baseline"]["accepted"]
        baseline_outcome = row["baseline"]["real_outcome"]
        final_accept = row["final_workflow"]["accepted"]
        final_outcome = row["final_workflow"]["final_real_outcome"]

        if baseline_accept and not outcome_is_correct(baseline_outcome):
            baseline_harmful_accept_count += 1
        if final_accept and final_outcome is not None and not outcome_is_correct(final_outcome):
            gated_harmful_accept_count += 1

    return {
        "total_processed": total,
        "final_action_distribution": counts,
        "net_effect_distribution": net_effect_counts,
        "retry_used_count": retry_used_count,
        "retry_improved_count": retry_improved_count,
        "baseline_harmful_accept_count": baseline_harmful_accept_count,
        "gated_harmful_accept_count": gated_harmful_accept_count,
        "net_harmful_acceptance_reduction": baseline_harmful_accept_count - gated_harmful_accept_count,
    }


def main() -> None:
    if not os.path.exists(INPUT_PATH):
        print(f"Error: {INPUT_PATH} not found.")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    samples = load_samples_jsonl(INPUT_PATH)
    results: List[Dict[str, Any]] = []

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        for sample in samples:
            row = evaluate_sample(sample)
            results.append(row)
            out.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary = summarize(results)

    print("\n--- OMNIA Silent Failure Retry Loop v0 Summary ---")
    print(f"Total processed: {summary['total_processed']}")
    print(f"Retry used: {summary['retry_used_count']}")
    print(f"Retry improved outcome: {summary['retry_improved_count']}")
    print(f"Baseline harmful accepts: {summary['baseline_harmful_accept_count']}")
    print(f"Gated harmful accepts: {summary['gated_harmful_accept_count']}")
    print(f"Net harmful acceptance reduction: {summary['net_harmful_acceptance_reduction']}")
    print(f"Final action distribution: {summary['final_action_distribution']}")
    print(f"Net effect distribution: {summary['net_effect_distribution']}")
    print(f"Results saved to: {OUTPUT_PATH}\n")


if __name__ == "__main__":
    main()