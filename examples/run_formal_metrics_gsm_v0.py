import json
import re
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = ROOT / "examples" / "gsm_symbolic_v0_model_outputs.jsonl"
OUTPUT_FILE = ROOT / "examples" / "gsm_symbolic_v0_omnia_scores.jsonl"


def read_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s\+\-\*\/\=\.\,\?]", "", text)
    return text.strip()


def structural_features(row):
    question = normalize_text(row.get("question", ""))
    output = normalize_text(row.get("model_raw_output", ""))
    final_answer = str(row.get("model_final_extracted_answer", "")).strip()

    numbers_q = re.findall(r"-?\d+(?:\.\d+)?", question)
    numbers_o = re.findall(r"-?\d+(?:\.\d+)?", output)

    tokens_q = question.split()
    tokens_o = output.split()

    return {
        "question_token_count": len(tokens_q),
        "output_token_count": len(tokens_o),
        "question_number_count": len(numbers_q),
        "output_number_count": len(numbers_o),
        "question_unique_token_ratio": safe_ratio(len(set(tokens_q)), len(tokens_q)),
        "output_unique_token_ratio": safe_ratio(len(set(tokens_o)), len(tokens_o)),
        "final_answer_length": len(final_answer),
        "operator_count": sum(question.count(op) for op in ["+", "-", "*", "/", "="]),
    }


def safe_ratio(a, b):
    return a / b if b else 0.0


def distance(a, b):
    keys = sorted(set(a) | set(b))
    diffs = []

    for key in keys:
        av = float(a.get(key, 0.0))
        bv = float(b.get(key, 0.0))
        denom = max(abs(av), abs(bv), 1.0)
        diffs.append(abs(av - bv) / denom)

    return min(1.0, mean(diffs)) if diffs else 0.0


def omega_for_group(rows):
    """
    Ω = invariance across variants belonging to the same template_id.

    This is a practical v0 approximation:
    - base variant is treated as reference when present
    - other variants are compared against it
    - lower Ω means higher structural instability
    """
    base_rows = [r for r in rows if r.get("variant_type") == "base"]
    reference = base_rows[0] if base_rows else rows[0]
    ref_features = structural_features(reference)

    scored = []
    for row in rows:
        d = distance(ref_features, structural_features(row))
        omega = 1.0 - d
        scored.append((row, omega))

    return scored


def coherence_plus(row):
    """
    Co⁺ = internal structural coherence proxy.

    v0 proxy:
    compares structural balance between question and model output.
    It does not judge semantic correctness.
    """
    f = structural_features(row)

    q_len = f["question_token_count"]
    o_len = f["output_token_count"]
    q_num = f["question_number_count"]
    o_num = f["output_number_count"]

    length_balance = 1.0 - min(1.0, abs(q_len - o_len) / max(q_len, o_len, 1))
    number_balance = 1.0 - min(1.0, abs(q_num - o_num) / max(q_num, o_num, 1))

    lexical_balance = 1.0 - abs(
        f["question_unique_token_ratio"] - f["output_unique_token_ratio"]
    )

    return clamp(mean([length_balance, number_balance, lexical_balance]))


def score_plus(omega, coherence, alpha=0.5):
    return clamp(alpha * omega + (1.0 - alpha) * coherence)


def clamp(x):
    return max(0.0, min(1.0, float(x)))


def fragility_rank(score):
    if score >= 0.80:
        return "stable"
    if score >= 0.60:
        return "watch"
    if score >= 0.40:
        return "fragile"
    return "unstable"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}")

    rows = read_jsonl(INPUT_FILE)

    groups = {}
    for row in rows:
        groups.setdefault(row.get("template_id", "unknown"), []).append(row)

    output_rows = []

    for template_id, group_rows in groups.items():
        omega_rows = omega_for_group(group_rows)

        for row, omega in omega_rows:
            co = coherence_plus(row)
            score = score_plus(omega, co, alpha=0.5)

            out = dict(row)
            out["omega"] = round(omega, 6)
            out["coherence_plus"] = round(co, 6)
            out["score_plus"] = round(score, 6)
            out["fragility_rank"] = fragility_rank(score)

            output_rows.append(out)

    write_jsonl(OUTPUT_FILE, output_rows)

    print("=" * 88)
    print("FORMAL METRICS GSM V0")
    print("=" * 88)
    print(f"input:  {INPUT_FILE}")
    print(f"output: {OUTPUT_FILE}")
    print(f"rows:   {len(output_rows)}")

    print()
    print("score_plus summary:")
    scores = [r["score_plus"] for r in output_rows]
    print(f"min:  {min(scores):.6f}")
    print(f"max:  {max(scores):.6f}")
    print(f"mean: {mean(scores):.6f}")

    print()
    print("fragility_rank counts:")
    counts = {}
    for row in output_rows:
        counts[row["fragility_rank"]] = counts.get(row["fragility_rank"], 0) + 1

    for key in ["stable", "watch", "fragile", "unstable"]:
        print(f"{key}: {counts.get(key, 0)}")


if __name__ == "__main__":
    main()