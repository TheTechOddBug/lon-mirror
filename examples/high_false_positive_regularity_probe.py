import math
from pathlib import Path
from typing import Dict, Any, List, Tuple


TARGET_NUMBERS: List[Tuple[int, bool, str]] = [
    (1007, False, "1007 composite"),
    (1009, True,  "1009 prime"),
    (2021, False, "2021 composite"),
    (2017, True,  "2017 prime"),
    (2047, False, "2047 composite"),
    (2039, True,  "2039 prime"),
]

OUTPUT_MD_PATH = Path("examples/high_false_positive_regularity_probe.md")
BASES = list(range(2, 17))


def to_base(n: int, base: int) -> str:
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if n == 0:
        return "0"

    value = n
    out: List[str] = []
    while value > 0:
        value, rem = divmod(value, base)
        out.append(digits[rem])
    return "".join(reversed(out))


def shannon_entropy(rep: str) -> float:
    if not rep:
        return 0.0

    counts: Dict[str, int] = {}
    for ch in rep:
        counts[ch] = counts.get(ch, 0) + 1

    ent = 0.0
    n = len(rep)
    for count in counts.values():
        p = count / n
        ent -= p * math.log2(p)
    return ent


def dominant_char_ratio(rep: str) -> float:
    if not rep:
        return 0.0
    counts = [rep.count(ch) for ch in set(rep)]
    return max(counts) / len(rep)


def max_run_ratio(rep: str) -> float:
    if not rep:
        return 0.0

    best = 1
    cur = 1
    for i in range(1, len(rep)):
        if rep[i] == rep[i - 1]:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1

    return best / len(rep)


def palindrome_mismatch_ratio(rep: str) -> float:
    """
    0.0 = exact palindrome
    1.0 = maximally far from palindrome under pairwise comparison
    """
    n = len(rep)
    if n <= 1:
        return 0.0

    pairs = n // 2
    if pairs == 0:
        return 0.0

    mismatches = 0
    for i in range(pairs):
        if rep[i] != rep[n - 1 - i]:
            mismatches += 1

    return mismatches / pairs


def build_profile(n: int) -> Dict[str, Any]:
    base_rows: List[Dict[str, Any]] = []

    entropy_sum = 0.0
    dom_sum = 0.0
    run_sum = 0.0
    pal_sum = 0.0

    low_entropy_count = 0
    high_dominance_count = 0
    quasi_pal_count = 0
    high_run_count = 0

    for base in BASES:
        rep = to_base(n, base)
        ent = shannon_entropy(rep)
        dom = dominant_char_ratio(rep)
        run = max_run_ratio(rep)
        pal = palindrome_mismatch_ratio(rep)

        entropy_sum += ent
        dom_sum += dom
        run_sum += run
        pal_sum += pal

        if ent <= 1.0:
            low_entropy_count += 1
        if dom >= 0.70:
            high_dominance_count += 1
        if pal <= 0.25:
            quasi_pal_count += 1
        if run >= 0.50:
            high_run_count += 1

        base_rows.append(
            {
                "base": base,
                "repr": rep,
                "length": len(rep),
                "entropy": ent,
                "dominance": dom,
                "max_run_ratio": run,
                "pal_mismatch_ratio": pal,
            }
        )

    n_bases = len(BASES)

    return {
        "n": n,
        "avg_entropy": entropy_sum / n_bases,
        "avg_dominance": dom_sum / n_bases,
        "avg_run_ratio": run_sum / n_bases,
        "avg_pal_mismatch": pal_sum / n_bases,
        "low_entropy_count": low_entropy_count,
        "high_dominance_count": high_dominance_count,
        "quasi_pal_count": quasi_pal_count,
        "high_run_count": high_run_count,
        "regularity_signature": (
            low_entropy_count
            + high_dominance_count
            + quasi_pal_count
            + high_run_count
        ),
        "bases": base_rows,
    }


def write_markdown(path: Path, profiles: List[Tuple[str, bool, Dict[str, Any]]]) -> None:
    lines: List[str] = []
    lines.append("# High False Positive Regularity Probe")
    lines.append("")
    lines.append("Purpose: inspect whether high-scoring composites are being rewarded for excessive symbolic regularity across bases.")
    lines.append("")
    lines.append("Metrics used:")
    lines.append("- average Shannon entropy")
    lines.append("- average dominant-character ratio")
    lines.append("- average maximum run-length ratio")
    lines.append("- average palindrome mismatch ratio")
    lines.append("- counts of low-entropy / high-dominance / quasi-palindromic / high-run bases")
    lines.append("")

    lines.append("## Summary table")
    lines.append("")
    lines.append("| label | type | avg_entropy | avg_dominance | avg_run_ratio | avg_pal_mismatch | low_entropy | high_dom | quasi_pal | high_run | reg_signature |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    for label, is_prime, p in profiles:
        kind = "prime" if is_prime else "comp"
        lines.append(
            f"| {label} | {kind} | "
            f"{p['avg_entropy']:.4f} | "
            f"{p['avg_dominance']:.4f} | "
            f"{p['avg_run_ratio']:.4f} | "
            f"{p['avg_pal_mismatch']:.4f} | "
            f"{p['low_entropy_count']} | "
            f"{p['high_dominance_count']} | "
            f"{p['quasi_pal_count']} | "
            f"{p['high_run_count']} | "
            f"{p['regularity_signature']} |"
        )

    lines.append("")

    for label, is_prime, p in profiles:
        kind = "prime" if is_prime else "composite"
        lines.append(f"## {label} ({kind})")
        lines.append("")
        lines.append(
            f"- avg_entropy: `{p['avg_entropy']:.4f}`\n"
            f"- avg_dominance: `{p['avg_dominance']:.4f}`\n"
            f"- avg_run_ratio: `{p['avg_run_ratio']:.4f}`\n"
            f"- avg_pal_mismatch: `{p['avg_pal_mismatch']:.4f}`\n"
            f"- low_entropy_count: `{p['low_entropy_count']}`\n"
            f"- high_dominance_count: `{p['high_dominance_count']}`\n"
            f"- quasi_pal_count: `{p['quasi_pal_count']}`\n"
            f"- high_run_count: `{p['high_run_count']}`\n"
            f"- regularity_signature: `{p['regularity_signature']}`"
        )
        lines.append("")
        lines.append("| base | repr | len | entropy | dominance | max_run_ratio | pal_mismatch |")
        lines.append("|---|---|---:|---:|---:|---:|---:|")
        for row in p["bases"]:
            lines.append(
                f"| {row['base']} | `{row['repr']}` | {row['length']} | "
                f"{row['entropy']:.4f} | {row['dominance']:.4f} | "
                f"{row['max_run_ratio']:.4f} | {row['pal_mismatch_ratio']:.4f} |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    profiles: List[Tuple[str, bool, Dict[str, Any]]] = []
    for n, is_prime, label in TARGET_NUMBERS:
        profiles.append((label, is_prime, build_profile(n)))

    write_markdown(OUTPUT_MD_PATH, profiles)
    print(f"Wrote {OUTPUT_MD_PATH}")


if __name__ == "__main__":
    main()