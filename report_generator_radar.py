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
    lines.append("# OMNIA-RADAR — Offline Report")
    lines.append("")
    lines.append(f"**Version:** {version}")
    lines.append(f"**Input file:** `{input_file}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total cases:** {summary.get('total_cases', 0)}")
    lines.append(f"- **Matched cases:** {summary.get('matched_cases', 0)}")
    lines.append(f"- **Mismatched cases:** {summary.get('mismatched_cases', 0)}")
    lines.append(f"- **GROWTH_ZONE count:** {summary.get('regime_counts', {}).get('GROWTH_ZONE', 0)}")
    lines.append(f"- **BORDERLINE_ZONE count:** {summary.get('regime_counts', {}).get('BORDERLINE_ZONE', 0)}")
    lines.append(f"- **DEAD_ZONE count:** {summary.get('regime_counts', {}).get('DEAD_ZONE', 0)}")
    lines.append("")
    lines.append("## Case results")
    lines.append("")
    lines.append("| Case | Opportunity | Recoverability | Stability Gate | Radar Score | Expected | Actual | Match | Reason |")
    lines.append("|---|---:|---:|---:|---:|---|---|---|---|")

    for result in results:
        sig = result["signals"]
        match_str = "YES" if result["match"] else "NO"
        lines.append(
            f"| `{result['case_id']}` | "
            f"{sig['opportunity']:.2f} | "
            f"{sig['recoverability']:.2f} | "
            f"{sig['stability_gate']:.2f} | "
            f"{result['radar_score']:.4f} | "
            f"{result['expected_regime']} | "
            f"{result['actual_regime']} | "
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
        lines.append(f"- **Opportunity:** {sig['opportunity']:.2f}")
        lines.append(f"- **Recoverability:** {sig['recoverability']:.2f}")
        lines.append(f"- **Stability gate:** {sig['stability_gate']:.2f}")
        lines.append(f"- **Radar score:** {result['radar_score']:.4f}")
        lines.append(f"- **Expected regime:** {result['expected_regime']}")
        lines.append(f"- **Actual regime:** {result['actual_regime']}")
        lines.append(f"- **Match:** {'YES' if result['match'] else 'NO'}")
        lines.append(f"- **Reason:** {result['reason']}")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- This report is based on synthetic RADAR cases only.")
    lines.append("- It is an offline opportunity-detection demonstrator, not an empirical runtime validator.")
    lines.append("- The score remains strictly non-semantic.")
    lines.append("- Regime thresholds are synthetic placeholders in v0.")

    return "\n".join(lines) + "\n"


def main() -> None:
    input_path = Path("data/radar_results_v0.json")
    output_path = Path("reports/radar_report_v0.md")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = load_json(input_path)
    report = generate_report(data)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(report)

    print(f"Wrote radar report to: {output_path}")


if __name__ == "__main__":
    main()