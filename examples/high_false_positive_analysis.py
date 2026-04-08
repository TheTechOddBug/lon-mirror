import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


TARGET_PAIRS: List[Tuple[int, int, str]] = [
    (1007, 1009, "1007 composite vs 1009 prime"),
    (2021, 2017, "2021 composite vs 2017 prime"),
    (2047, 2039, "2047 composite vs 2039 prime"),
]

OUTPUT_JSON_PATH = Path("examples/high_false_positive_analysis.json")
OUTPUT_MD_PATH = Path("examples/high_false_positive_analysis.md")


def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = []
    value = n
    while value > 0:
        value, rem = divmod(value, base)
        out.append(digits[rem])
    return "".join(reversed(out))


def digit_sum_in_base(rep: str) -> int:
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    value_map = {ch: i for i, ch in enumerate(digits)}
    return sum(value_map[ch] for ch in rep)


def factorize_trial(n: int) -> List[int]:
    factors: List[int] = []
    value = n
    d = 2
    while d * d <= value:
        while value % d == 0:
            factors.append(d)
            value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def build_number_profile(n: int) -> Dict[str, Any]:
    reps: Dict[int, str] = {}
    for base in range(2, 17):
        reps[base] = to_base(n, base)

    profile = {
        "n": n,
        "is_prime": is_prime_trial(n),
        "factors": factorize_trial(n),
        "decimal_digit_sum": sum(int(ch) for ch in str(n)),
        "decimal_length": len(str(n)),
        "representations": {},
    }

    for base, rep in reps.items():
        profile["representations"][str(base)] = {
            "repr": rep,
            "length": len(rep),
            "digit_sum": digit_sum_in_base(rep),
            "unique_chars": len(set(rep)),
            "has_repeat": len(set(rep)) != len(rep),
        }

    return profile


def compare_profiles(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    same_repr_bases: List[int] = []
    same_length_bases: List[int] = []
    same_digit_sum_bases: List[int] = []
    length_deltas: Dict[int, int] = {}
    digit_sum_deltas: Dict[int, int] = {}

    for base in range(2, 17):
        key = str(base)
        ar = a["representations"][key]
        br = b["representations"][key]

        if ar["repr"] == br["repr"]:
            same_repr_bases.append(base)
        if ar["length"] == br["length"]:
            same_length_bases.append(base)
        if ar["digit_sum"] == br["digit_sum"]:
            same_digit_sum_bases.append(base)

        length_deltas[base] = ar["length"] - br["length"]
        digit_sum_deltas[base] = ar["digit_sum"] - br["digit_sum"]

    return {
        "same_repr_bases": same_repr_bases,
        "same_length_bases": same_length_bases,
        "same_digit_sum_bases": same_digit_sum_bases,
        "length_deltas": length_deltas,
        "digit_sum_deltas": digit_sum_deltas,
    }


def build_report() -> Dict[str, Any]:
    pairs_report: List[Dict[str, Any]] = []

    for composite_n, prime_n, label in TARGET_PAIRS:
        composite_profile = build_number_profile(composite_n)
        prime_profile = build_number_profile(prime_n)
        comparison = compare_profiles(composite_profile, prime_profile)

        pairs_report.append(
            {
                "label": label,
                "composite": composite_profile,
                "prime": prime_profile,
                "comparison": comparison,
            }
        )

    return {"pairs": pairs_report}


def write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_markdown(path: Path, data: Dict[str, Any]) -> None:
    lines: List[str] = []
    lines.append("# High False Positive Analysis")
    lines.append("")
    lines.append("Purpose: compare high-scoring composites against nearby true primes.")
    lines.append("")
    lines.append("This is not a scoring run.")
    lines.append("It is a feature inspection step.")
    lines.append("")

    for pair in data["pairs"]:
        lines.append(f"## {pair['label']}")
        lines.append("")

        c = pair["composite"]
        p = pair["prime"]
        cmp = pair["comparison"]

        lines.append(f"- Composite: `{c['n']}`")
        lines.append(f"  - factors: `{c['factors']}`")
        lines.append(f"  - decimal digit sum: `{c['decimal_digit_sum']}`")
        lines.append(f"  - decimal length: `{c['decimal_length']}`")
        lines.append(f"- Prime: `{p['n']}`")
        lines.append(f"  - factors: `{p['factors']}`")
        lines.append(f"  - decimal digit sum: `{p['decimal_digit_sum']}`")
        lines.append(f"  - decimal length: `{p['decimal_length']}`")
        lines.append("")

        lines.append("### Cross-base comparison")
        lines.append("")
        lines.append(f"- Same full representation bases: `{cmp['same_repr_bases']}`")
        lines.append(f"- Same representation length bases: `{cmp['same_length_bases']}`")
        lines.append(f"- Same digit-sum bases: `{cmp['same_digit_sum_bases']}`")
        lines.append("")

        lines.append("| base | composite_repr | prime_repr | len_c | len_p | dsum_c | dsum_p |")
        lines.append("|---|---|---:|---:|---:|---:|---:|")

        for base in range(2, 17):
            key = str(base)
            cr = c["representations"][key]
            pr = p["representations"][key]
            lines.append(
                f"| {base} | `{cr['repr']}` | `{pr['repr']}` | "
                f"{cr['length']} | {pr['length']} | {cr['digit_sum']} | {pr['digit_sum']} |"
            )

        lines.append("")
        lines.append("---")
        lines.append("")

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    data = build_report()
    write_json(OUTPUT_JSON_PATH, data)
    write_markdown(OUTPUT_MD_PATH, data)

    print(f"Wrote {OUTPUT_JSON_PATH}")
    print(f"Wrote {OUTPUT_MD_PATH}")


if __name__ == "__main__":
    main()