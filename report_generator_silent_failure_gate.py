from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def generate_report(data: Dict[str, Any]) -> str:
    version = data.get("version", "unknown")
    input_file = data.get("input_file", "unknown")
    summary = data.get("summary", {})
    results: List[Dict[str, Any]] = data.get("results", [])

    lines: List[str] = []
    lines.append("# OMNIA — Silent Failure Gate Report")
    lines.append("")
    lines.append(f"**Version:** {version}")
    lines.append(f"**Input file:** `{input_file}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total cases:** {summary.get('total_cases', 0)}")
    lines.append(f"- **Matched cases:** {summary.get('matched_cases', 0)}")
    lines.append(f"- **Mismatched cases:** {summary.get('mismatched_cases', 0)}")
    lines.append(f"- **PASS count:** {summary.get('action_counts', {}).get('PASS', 0)}")
    lines.append(f"- **RETRY count:** {summary.get('action_counts', {}).get('RETRY', 0)}")
    lines.append(f"- **ESCALATE count:** {summary.get('action_counts', {}).get('ESCALATE', 0)}")
    lines.append("")
    lines.append("## Case results")
    lines.append("")
    lines.append("| Case | Stability | Fragility | Irrecoverability | Retry Budget | Expected | Actual | Match | Reason |")
    lines.append("|---|---:|---:|---:|---:|---|---|---|---|")

    for result in results:
        sig = result["signals"]
        match_str = "YES" if result["match"] else "NO"
        lines.append(
            f"| `{result['case_id']}` | "
            f"{sig['stability']:.2f} | "
            f"{sig['fragility']:.2f} | "
            f"{sig['irrecoverability']:.2f} | "
            f"{sig['retry_budget']} | "
            f"{result['expected_action']} | "
            f"{result['actual_action']} | "
            f"{match_str} | "
            f"{result['reason']} |"
        )

    lines.append("")
    lines.append("## Detailed notes")
    lines.append("")

    for result in results:
        sig = result["signals"]
        lines.append(f"### {result['case_id']}")
        lines.append("")
        lines.append(f"- **Description:** {result['description']}")
        lines.append(f"- **Stability:** {sig['stability']:.2f}")
        lines.append(f"- **Fragility:** {sig['fragility']:.2f}")
        lines.append(f"- **Irrecoverability:** {sig['irrecoverability']:.2f}")
        lines.append(f"- **Retry budget:** {sig['retry_budget']}")
        lines.append(f"- **Expected action:** {result['expected_action']}")
        lines.append(f"- **Actual action:** {result['actual_action']}")
        lines.append(f"- **Match:** {'YES' if result['match'] else 'NO'}")
        lines.append(f"- **Reason:** {result['reason']}")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- This report is based on synthetic gate cases only.")
    lines.append("- It is an offline routing demonstrator, not a production gate.")
    lines.append("- The action space is intentionally bounded to PASS / RETRY / ESCALATE.")
    lines.append("- No semantics are used in this branch.")

    return "\n".join(lines) + "\n"


def main() -> None:
    input_path = Path("data/silent_failure_gate_results_v0.json")
    output_path = Path("reports/silent_failure_gate_report_v0.md")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = load_json(input_path)
    report = generate_report(data)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(report)

    print(f"Wrote gate report to: {output_path}")


if __name__ == "__main__":
    main()