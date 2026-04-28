import json
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = ROOT / "examples" / "gsm_symbolic_v0_omnia_scores.jsonl"


def read_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def avg(values):
    return mean(values) if values else 0.0


def group_by(rows, key):
    groups = {}
    for row in rows:
        groups.setdefault(row.get(key, "unknown"), []).append(row)
    return groups


def print_section(title):
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}")

    rows = read_jsonl(INPUT_FILE)

    print_section("FORMAL METRICS GSM V0 ANALYSIS")
    print(f"input: {INPUT_FILE}")
    print(f"rows:  {len(rows)}")

    # ------------------------------------------------------------------
    # Global summary
    # ------------------------------------------------------------------

    print_section("GLOBAL SUMMARY")

    for metric in ["omega", "coherence_plus", "score_plus"]:
        values = [float(r.get(metric, 0.0)) for r in rows]
        print(f"{metric}:")
        print(f"  min:  {min(values):.6f}")
        print(f"  max:  {max(values):.6f}")
        print(f"  mean: {avg(values):.6f}")

    correct = [r for r in rows if r.get("is_correct") is True]
    incorrect = [r for r in rows if r.get("is_correct") is False]

    print()
    print(f"correct:   {len(correct)}")
    print(f"incorrect: {len(incorrect)}")

    # ------------------------------------------------------------------
    # Variant summary
    # ------------------------------------------------------------------

    print_section("SUMMARY BY VARIANT TYPE")

    by_variant = group_by(rows, "variant_type")

    for variant_type in sorted(by_variant.keys()):
        group = by_variant[variant_type]
        print(f"{variant_type}:")
        print(f"  count:          {len(group)}")
        print(f"  omega_mean:     {avg([float(r.get('omega', 0.0)) for r in group]):.6f}")
        print(f"  coherence_mean: {avg([float(r.get('coherence_plus', 0.0)) for r in group]):.6f}")
        print(f"  score_mean:     {avg([float(r.get('score_plus', 0.0)) for r in group]):.6f}")
        print(f"  correct_ratio:  {avg([1.0 if r.get('is_correct') else 0.0 for r in group]):.6f}")

    # ------------------------------------------------------------------
    # Fragility rank counts
    # ------------------------------------------------------------------

    print_section("FRAGILITY RANK COUNTS")

    by_rank = group_by(rows, "fragility_rank")
    for rank in ["stable", "watch", "fragile", "unstable", "unknown"]:
        if rank in by_rank:
            print(f"{rank}: {len(by_rank[rank])}")

    # ------------------------------------------------------------------
    # Correct but structurally degraded
    # ------------------------------------------------------------------

    print_section("CORRECT BUT STRUCTURALLY DEGRADED")

    degraded = [
        r for r in rows
        if r.get("is_correct") is True
        and r.get("fragility_rank") in {"watch", "fragile", "unstable"}
    ]

    print(f"count: {len(degraded)}")

    for row in sorted(degraded, key=lambda r: float(r.get("score_plus", 0.0)))[:10]:
        print()
        print(f"template_id:    {row.get('template_id')}")
        print(f"variant_type:   {row.get('variant_type')}")
        print(f"expected:       {row.get('expected_answer')}")
        print(f"model_answer:   {row.get('model_final_extracted_answer')}")
        print(f"omega:          {float(row.get('omega', 0.0)):.6f}")
        print(f"coherence_plus: {float(row.get('coherence_plus', 0.0)):.6f}")
        print(f"score_plus:     {float(row.get('score_plus', 0.0)):.6f}")
        print(f"fragility_rank: {row.get('fragility_rank')}")

    # ------------------------------------------------------------------
    # Template degradation from base
    # ------------------------------------------------------------------

    print_section("TEMPLATE DEGRADATION FROM BASE")

    by_template = group_by(rows, "template_id")
    drops = []

    for template_id, group in by_template.items():
        base_rows = [r for r in group if r.get("variant_type") == "base"]
        if not base_rows:
            continue

        base = base_rows[0]
        base_score = float(base.get("score_plus", 0.0))
        base_omega = float(base.get("omega", 0.0))

        for row in group:
            if row.get("variant_type") == "base":
                continue

            score = float(row.get("score_plus", 0.0))
            omega = float(row.get("omega", 0.0))

            drops.append({
                "template_id": template_id,
                "variant_type": row.get("variant_type"),
                "base_score": base_score,
                "variant_score": score,
                "score_drop": base_score - score,
                "base_omega": base_omega,
                "variant_omega": omega,
                "omega_drop": base_omega - omega,
                "is_correct": row.get("is_correct"),
                "fragility_rank": row.get("fragility_rank"),
            })

    drops = sorted(drops, key=lambda x: x["score_drop"], reverse=True)

    for item in drops[:10]:
        print()
        print(f"template_id:    {item['template_id']}")
        print(f"variant_type:   {item['variant_type']}")
        print(f"score_drop:     {item['score_drop']:.6f}")
        print(f"omega_drop:     {item['omega_drop']:.6f}")
        print(f"base_score:     {item['base_score']:.6f}")
        print(f"variant_score:  {item['variant_score']:.6f}")
        print(f"base_omega:     {item['base_omega']:.6f}")
        print(f"variant_omega:  {item['variant_omega']:.6f}")
        print(f"is_correct:     {item['is_correct']}")
        print(f"fragility_rank: {item['fragility_rank']}")

    # ------------------------------------------------------------------
    # Core conclusion
    # ------------------------------------------------------------------

    print_section("CORE OBSERVATION")

    correct_degraded_ratio = len(degraded) / len(correct) if correct else 0.0

    print(f"correct_degraded_ratio: {correct_degraded_ratio:.6f}")

    if correct_degraded_ratio > 0:
        print()
        print("OBSERVATION:")
        print("Some outputs remain formally correct while structural stability decreases.")
        print()
        print("INTERPRETATION:")
        print("Correctness and structural stability are not equivalent signals.")
    else:
        print()
        print("OBSERVATION:")
        print("No correct-but-degraded cases detected in this run.")
        print()
        print("INTERPRETATION:")
        print("This run does not yet demonstrate separation between correctness and structural stability.")


if __name__ == "__main__":
    main()