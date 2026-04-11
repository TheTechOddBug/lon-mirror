from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class GateSignals:
    stability: float
    fragility: float
    irrecoverability: float
    retry_budget: int


@dataclass
class GateCase:
    case_id: str
    description: str
    signals: GateSignals
    expected_action: str


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def parse_cases(data: Dict[str, Any]) -> List[GateCase]:
    parsed: List[GateCase] = []

    for case in data.get("cases", []):
        sig = case["signals"]
        parsed.append(
            GateCase(
                case_id=case["id"],
                description=case["description"],
                signals=GateSignals(
                    stability=float(sig["stability"]),
                    fragility=float(sig["fragility"]),
                    irrecoverability=float(sig["irrecoverability"]),
                    retry_budget=int(sig["retry_budget"]),
                ),
                expected_action=case["expected_action"],
            )
        )

    return parsed


def decide_action(signals: GateSignals) -> str:
    """
    Silent Failure Gate v0

    Decision surface:
    1. ESCALATE if irrecoverability is high
    2. ESCALATE if fragility is extremely high
    3. RETRY if fragility is moderate/high and retry budget remains
    4. PASS otherwise
    """
    if signals.irrecoverability >= 0.80:
        return "ESCALATE"

    if signals.fragility >= 0.85:
        return "ESCALATE"

    if signals.fragility >= 0.45 and signals.retry_budget > 0:
        return "RETRY"

    return "PASS"


def classify_reason(signals: GateSignals, action: str) -> str:
    if action == "ESCALATE":
        if signals.irrecoverability >= 0.80:
            return "High irrecoverability"
        if signals.fragility >= 0.85:
            return "Extreme fragility"
        return "Escalation boundary reached"

    if action == "RETRY":
        return "Recoverable fragility with retry budget available"

    return "No bounded intervention required"


def evaluate_case(case: GateCase) -> Dict[str, Any]:
    action = decide_action(case.signals)
    match = action == case.expected_action

    return {
        "case_id": case.case_id,
        "description": case.description,
        "signals": {
            "stability": case.signals.stability,
            "fragility": case.signals.fragility,
            "irrecoverability": case.signals.irrecoverability,
            "retry_budget": case.signals.retry_budget,
        },
        "expected_action": case.expected_action,
        "actual_action": action,
        "match": match,
        "reason": classify_reason(case.signals, action),
    }


def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(results)
    matched = sum(1 for r in results if r["match"])
    mismatched = total - matched

    counts = {"PASS": 0, "RETRY": 0, "ESCALATE": 0}
    for r in results:
        counts[r["actual_action"]] += 1

    return {
        "total_cases": total,
        "matched_cases": matched,
        "mismatched_cases": mismatched,
        "action_counts": counts,
    }


def main() -> None:
    input_path = Path("data/gate_cases_v0.json")
    output_path = Path("data/silent_failure_gate_results_v0.json")

    data = load_json(input_path)
    cases = parse_cases(data)

    results = [evaluate_case(case) for case in cases]
    summary = summarize(results)

    payload = {
        "version": "v0",
        "input_file": str(input_path),
        "summary": summary,
        "results": results,
    }

    save_json(output_path, payload)

    print(f"Wrote gate results to: {output_path}")
    print(
        f"matched={summary['matched_cases']}/{summary['total_cases']} | "
        f"PASS={summary['action_counts']['PASS']} | "
        f"RETRY={summary['action_counts']['RETRY']} | "
        f"ESCALATE={summary['action_counts']['ESCALATE']}"
    )


if __name__ == "__main__":
    main()