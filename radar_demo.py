from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class RadarSignals:
    opportunity: float
    recoverability: float
    stability_gate: float


@dataclass
class RadarCase:
    case_id: str
    description: str
    signals: RadarSignals
    expected_regime: str


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def parse_cases(data: Dict[str, Any]) -> List[RadarCase]:
    parsed: List[RadarCase] = []

    for case in data.get("cases", []):
        sig = case["signals"]
        parsed.append(
            RadarCase(
                case_id=case["id"],
                description=case["description"],
                signals=RadarSignals(
                    opportunity=float(sig["opportunity"]),
                    recoverability=float(sig["recoverability"]),
                    stability_gate=float(sig["stability_gate"]),
                ),
                expected_regime=case["expected_regime"],
            )
        )

    return parsed


def radar_score(signals: RadarSignals) -> float:
    """
    OMNIA-RADAR v0

    radar_score = opportunity * recoverability * stability_gate
    """
    value = signals.opportunity * signals.recoverability * signals.stability_gate
    return max(0.0, min(1.0, value))


def classify_regime(score: float) -> str:
    if score >= 0.50:
        return "GROWTH_ZONE"
    if score >= 0.20:
        return "BORDERLINE_ZONE"
    return "DEAD_ZONE"


def classify_reason(signals: RadarSignals, score: float, regime: str) -> str:
    if regime == "GROWTH_ZONE":
        return "Residual structural opportunity remains high enough to justify continuation."

    if regime == "BORDERLINE_ZONE":
        if signals.stability_gate < 0.50:
            return "Opportunity exists, but gate weakness suppresses stronger growth classification."
        if signals.opportunity < 0.30:
            return "Recoverability remains decent, but residual opportunity is limited."
        return "Moderate residual opportunity with incomplete structural strength."

    if signals.stability_gate < 0.30:
        return "Apparent opportunity is suppressed by a weak structural gate."
    if signals.recoverability < 0.20:
        return "Recoverability is too weak for meaningful opportunity."
    return "Residual structural opportunity is too low to justify growth classification."


def evaluate_case(case: RadarCase) -> Dict[str, Any]:
    score = radar_score(case.signals)
    regime = classify_regime(score)
    match = regime == case.expected_regime

    return {
        "case_id": case.case_id,
        "description": case.description,
        "signals": {
            "opportunity": case.signals.opportunity,
            "recoverability": case.signals.recoverability,
            "stability_gate": case.signals.stability_gate,
        },
        "radar_score": round(score, 6),
        "expected_regime": case.expected_regime,
        "actual_regime": regime,
        "match": match,
        "reason": classify_reason(case.signals, score, regime),
    }


def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(results)
    matched = sum(1 for r in results if r["match"])
    mismatched = total - matched

    counts = {
        "GROWTH_ZONE": 0,
        "BORDERLINE_ZONE": 0,
        "DEAD_ZONE": 0,
    }

    for r in results:
        counts[r["actual_regime"]] += 1

    return {
        "total_cases": total,
        "matched_cases": matched,
        "mismatched_cases": mismatched,
        "regime_counts": counts,
    }


def main() -> None:
    input_path = Path("data/radar_cases_v0.json")
    output_path = Path("data/radar_results_v0.json")

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

    print(f"Wrote radar results to: {output_path}")
    print(
        f"matched={summary['matched_cases']}/{summary['total_cases']} | "
        f"GROWTH={summary['regime_counts']['GROWTH_ZONE']} | "
        f"BORDERLINE={summary['regime_counts']['BORDERLINE_ZONE']} | "
        f"DEAD={summary['regime_counts']['DEAD_ZONE']}"
    )


if __name__ == "__main__":
    main()