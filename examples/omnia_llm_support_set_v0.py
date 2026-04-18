import json
import re
from collections import Counter
from pathlib import Path


DATA_PATH = Path("data/LLM_SUPPORT_SET_v0.jsonl")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def repeated_token_ratio(tokens: list[str]) -> float:
    if not tokens:
        return 0.0
    counts = Counter(tokens)
    repeated = sum(c for c in counts.values() if c > 1)
    return repeated / len(tokens)


def max_consecutive_same_token(tokens: list[str]) -> int:
    if not tokens:
        return 0
    best = 1
    cur = 1
    for i in range(1, len(tokens)):
        if tokens[i] == tokens[i - 1]:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best


def baseline_check(text: str) -> tuple[str, str]:
    tokens = tokenize(text)
    if not tokens:
        return "warning", "empty output"

    if max_consecutive_same_token(tokens) >= 4:
        return "warning", "hard repeated-token loop"

    if len(set(tokens)) <= max(2, len(tokens) // 6):
        return "warning", "very low token diversity"

    if re.search(r"(.)\1{7,}", text):
        return "warning", "repeated character spam"

    return "no warning", "no obvious baseline failure"


def sentence_repetition_ratio(sentences: list[str]) -> float:
    if not sentences:
        return 0.0
    normalized = [s.lower() for s in sentences]
    counts = Counter(normalized)
    repeated = sum(c for c in counts.values() if c > 1)
    return repeated / len(sentences)


def local_rigidity_score(text: str) -> float:
    tokens = tokenize(text)
    if not tokens:
        return 0.0

    rep_ratio = repeated_token_ratio(tokens)
    uniq_ratio = len(set(tokens)) / len(tokens)

    sentences = split_sentences(text)
    sent_rep = sentence_repetition_ratio(sentences)

    bigrams = list(zip(tokens, tokens[1:]))
    bigram_rep = 0.0
    if bigrams:
        counts = Counter(bigrams)
        repeated_bigrams = sum(c for c in counts.values() if c > 1)
        bigram_rep = repeated_bigrams / len(bigrams)

    score = (
        0.35 * rep_ratio
        + 0.25 * sent_rep
        + 0.20 * bigram_rep
        + 0.20 * (1.0 - uniq_ratio)
    )
    return max(0.0, min(1.0, score))


def omnia_review_signal(text: str) -> tuple[str, str, float]:
    score = local_rigidity_score(text)

    if score >= 0.42:
        return "review", "suspicious-clean structural regularity", score
    return "accept", "no bounded OMNIA review signal", score


def action_from_signals(baseline_status: str, omnia_status: str) -> str:
    if baseline_status == "warning":
        return "retry"
    if omnia_status == "review":
        return "review"
    return "accept"


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def run_set(rows: list[dict]) -> tuple[list[dict], dict]:
    results = []

    baseline_false_accepts = 0
    combined_false_accepts = 0
    extra_reviews_from_omnia = 0

    baseline_correct = 0
    combined_correct = 0

    for row in rows:
        text = normalize_text(row["raw_output"])
        target = row["target_label"]

        baseline_status, baseline_reason = baseline_check(text)
        baseline_action = "retry" if baseline_status == "warning" else "accept"

        omnia_status, omnia_reason, omnia_score = omnia_review_signal(text)
        combined_action = action_from_signals(baseline_status, omnia_status)

        if baseline_action == target:
            baseline_correct += 1
        if combined_action == target:
            combined_correct += 1

        if baseline_action == "accept" and target != "accept":
            baseline_false_accepts += 1

        if combined_action == "accept" and target != "accept":
            combined_false_accepts += 1

        if baseline_action == "accept" and combined_action == "review":
            extra_reviews_from_omnia += 1

        results.append(
            {
                "id": row["id"],
                "target_label": target,
                "baseline_action": baseline_action,
                "baseline_reason": baseline_reason,
                "omnia_status": omnia_status,
                "omnia_reason": omnia_reason,
                "omnia_score": round(omnia_score, 3),
                "combined_action": combined_action,
                "note": row.get("note", ""),
                "raw_output": text,
            }
        )

    summary = {
        "n_examples": len(rows),
        "baseline_false_accepts": baseline_false_accepts,
        "combined_false_accepts": combined_false_accepts,
        "false_accept_reduction": baseline_false_accepts - combined_false_accepts,
        "extra_reviews_from_omnia": extra_reviews_from_omnia,
        "baseline_correct": baseline_correct,
        "combined_correct": combined_correct,
    }

    return results, summary


def print_results(results: list[dict], summary: dict) -> None:
    print("OMNIA LLM SUPPORT SET V0")
    print("=" * 60)

    for r in results:
        print(f"ID: {r['id']} | TARGET: {r['target_label']}")
        print(f"RAW_OUTPUT: {r['raw_output']}")
        print(f"BASELINE_ACTION: {r['baseline_action']} ({r['baseline_reason']})")
        print(f"OMNIA: {r['omnia_status']} ({r['omnia_reason']}) | SCORE: {r['omnia_score']:.3f}")
        print(f"COMBINED_ACTION: {r['combined_action']}")
        print(f"NOTE: {r['note']}")
        print("-" * 60)

    print("SUMMARY")
    print("=" * 60)
    print(f"N_EXAMPLES: {summary['n_examples']}")
    print(f"BASELINE_FALSE_ACCEPTS: {summary['baseline_false_accepts']}")
    print(f"COMBINED_FALSE_ACCEPTS: {summary['combined_false_accepts']}")
    print(f"FALSE_ACCEPT_REDUCTION: {summary['false_accept_reduction']}")
    print(f"EXTRA_REVIEWS_FROM_OMNIA: {summary['extra_reviews_from_omnia']}")
    print(f"BASELINE_CORRECT: {summary['baseline_correct']}")
    print(f"COMBINED_CORRECT: {summary['combined_correct']}")


if __name__ == "__main__":
    rows = load_jsonl(DATA_PATH)
    results, summary = run_set(rows)
    print_results(results, summary)