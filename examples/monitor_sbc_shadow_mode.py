import json
from pathlib import Path
from typing import Any, Dict, List


INPUT_PATH = Path("examples/prime_candidates_1m_1m002_raw_vs_adjusted_scores.jsonl")
OUTPUT_PATH = Path("examples/sbc_shadow_mode_report.md")

RAW_HIGH_THRESHOLD = 0.90
ADJ_LOW_THRESHOLD = 0.85
PRIME_RANK_DROP_THRESHOLD = 5


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}: {e}") from e
    return records


def validate_records(records: List[Dict[str, Any]]) -> None:
    required = {
        "n",
        "is_prime",
        "raw_omnia_score",
        "adjusted_score",
        "raw_rank",
        "adjusted_rank",
        "regularity_penalty_norm",
    }

    seen = set()
    for record in records:
        missing = required - set(record.keys())
        if missing:
            raise ValueError(f"Missing required fields {missing} in record {record}")

        n = int(record["n"])
        if n in seen:
            raise ValueError(f"Duplicate n detected: {n}")
        seen.add(n)

        if not isinstance(record["is_prime"], bool):
            raise TypeError(f"is_prime must be bool for n={n}")


def summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    total_primes = sum(1 for r in records if r["is_prime"])
    total_composites = total - total_primes

    prime_rank_drops = []
    declassed_high_conf_composites = []

    for r in records:
        raw_score = float(r["raw_omnia_score"])
        adj_score = float(r["adjusted_score"])
        raw_rank = int(r["raw_rank"])
        adj_rank = int(r["adjusted_rank"])

        if (not r["is_prime"]) and raw_score > RAW_HIGH_THRESHOLD and adj_score < ADJ_LOW_THRESHOLD:
            declassed_high_conf_composites.append(r)

        if r["is_prime"]:
            rank_drop = adj_rank - raw_rank
            if rank_drop > PRIME_RANK_DROP_THRESHOLD:
                rr = dict(r)
                rr["rank_drop"] = rank_drop
                prime_rank_drops.append(rr)

    mean_prime_rank_raw = sum(int(r["raw_rank"]) for r in records if r["is_prime"]) / total_primes
    mean_prime_rank_adj = sum(int(r["adjusted_rank"]) for r in records if r["is_prime"]) / total_primes
    mean_comp_rank_raw = sum(int(r["raw_rank"]) for r in records if not r["is_prime"]) / total_composites
    mean_comp_rank_adj = sum(int(r["adjusted_rank"]) for r in records if not r["is_prime"]) / total_composites

    spread_raw = mean_comp_rank_raw - mean_prime_rank_raw
    spread_adj = mean_comp_rank_adj - mean_prime_rank_adj
    spread_widening = spread_adj - spread_raw

    sacrifice_ratio = None
    if len(prime_rank_drops) > 0:
        sacrifice_ratio = len(declassed_high_conf_composites) / len(prime_rank_drops)

    return {
        "total": total,
        "total_primes": total_primes,
        "total_composites": total_composites,
        "declassed_high_conf_composites": declassed_high_conf_composites,
        "prime_rank_drops": prime_rank_drops,
        "mean_prime_rank_raw": mean_prime_rank_raw,
        "mean_prime_rank_adj": mean_prime_rank_adj,
        "mean_comp_rank_raw": mean_comp_rank_raw,
        "mean_comp_rank_adj": mean_comp_rank_adj,
        "spread_raw": spread_raw,
        "spread_adj": spread_adj,
        "spread_widening": spread_widening,
        "sacrifice_ratio": sacrifice_ratio,
    }


def top_n(records: List[Dict[str, Any]], n: int, key: str, reverse: bool = True) -> List[Dict[str, Any]]:
    return sorted(records, key=lambda r: r[key], reverse=reverse)[:n]


def write_report(path: Path, summary: Dict[str, Any], source_path: Path) -> None:
    declassed = summary["declassed_high_conf_composites"]
    harmed_primes = summary["prime_rank_drops"]

    lines: List[str] = []
    lines.append("# SBC Shadow Mode Report")
    lines.append("")
    lines.append("Status: passive monitoring run")
    lines.append(f"Source file: `{source_path}`")
    lines.append("")
    lines.append("## Monitoring thresholds")
    lines.append("")
    lines.append(f"- Positive Gain threshold: raw score > `{RAW_HIGH_THRESHOLD}` and adjusted score < `{ADJ_LOW_THRESHOLD}`")
    lines.append(f"- Negative Impact threshold: prime loses more than `{PRIME_RANK_DROP_THRESHOLD}` ranking positions")
    lines.append("")
    lines.append("## Core counts")
    lines.append("")
    lines.append(f"- Total records: `{summary['total']}`")
    lines.append(f"- Total primes: `{summary['total_primes']}`")
    lines.append(f"- Total composites: `{summary['total_composites']}`")
    lines.append(f"- Positive Gain count (declassed high-confidence composites): `{len(declassed)}`")
    lines.append(f"- Negative Impact count (harmed primes): `{len(harmed_primes)}`")
    if summary["sacrifice_ratio"] is None:
        lines.append("- Sacrifice Ratio: `undefined`")
    else:
        lines.append(f"- Sacrifice Ratio: `{summary['sacrifice_ratio']:.6f}`")
    lines.append("")
    lines.append("## Spread widening")
    lines.append("")
    lines.append(f"- Raw spread: `{summary['spread_raw']:.6f}`")
    lines.append(f"- Adjusted spread: `{summary['spread_adj']:.6f}`")
    lines.append(f"- Spread widening: `{summary['spread_widening']:.6f}`")
    lines.append("")
    lines.append("## Top Positive Gain cases")
    lines.append("")
    lines.append("| n | raw_score | adjusted_score | raw_rank | adjusted_rank | pen_norm |")
    lines.append("|---:|---:|---:|---:|---:|---:|")
    for r in top_n(declassed, 15, key="regularity_penalty_norm"):
        lines.append(
            f"| {int(r['n'])} | {float(r['raw_omnia_score']):.6f} | {float(r['adjusted_score']):.6f} | "
            f"{int(r['raw_rank'])} | {int(r['adjusted_rank'])} | {float(r['regularity_penalty_norm']):.6f} |"
        )
    if not declassed:
        lines.append("| none | - | - | - | - | - |")
    lines.append("")
    lines.append("## Top Negative Impact cases")
    lines.append("")
    lines.append("| n | raw_rank | adjusted_rank | rank_drop | raw_score | adjusted_score | pen_norm |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for r in top_n(harmed_primes, 15, key="rank_drop"):
        lines.append(
            f"| {int(r['n'])} | {int(r['raw_rank'])} | {int(r['adjusted_rank'])} | {int(r['rank_drop'])} | "
            f"{float(r['raw_omnia_score']):.6f} | {float(r['adjusted_score']):.6f} | {float(r['regularity_penalty_norm']):.6f} |"
        )
    if not harmed_primes:
        lines.append("| none | - | - | - | - | - | - |")
    lines.append("")
    lines.append("## Compression")
    lines.append("")
    if summary["sacrifice_ratio"] is None:
        lines.append("No harmed primes crossed the configured rank-drop threshold in this batch.")
    else:
        lines.append(
            f"For this batch, SBC declassed `{len(declassed)}` high-confidence composite traps "
            f"while harming `{len(harmed_primes)}` primes above the configured threshold, "
            f"for a Sacrifice Ratio of `{summary['sacrifice_ratio']:.6f}`."
        )

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records = read_jsonl(INPUT_PATH)
    validate_records(records)
    summary = summarize(records)
    write_report(OUTPUT_PATH, summary, INPUT_PATH)

    print("=== SBC SHADOW MODE MONITOR ===")
    print(f"Source: {INPUT_PATH}")
    print(f"Total records: {summary['total']}")
    print(f"Positive Gain count: {len(summary['declassed_high_conf_composites'])}")
    print(f"Negative Impact count: {len(summary['prime_rank_drops'])}")
    if summary["sacrifice_ratio"] is None:
        print("Sacrifice Ratio: undefined")
    else:
        print(f"Sacrifice Ratio: {summary['sacrifice_ratio']:.6f}")
    print(f"Spread widening: {summary['spread_widening']:.6f}")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()