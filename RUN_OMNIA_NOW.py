Nome file

RUN_OMNIA_NOW.py

Contenuto completo

import re
from collections import Counter


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


def claim_from_action(action: str) -> str:
    if action == "review":
        return "bounded review signal on suspicious-clean output"
    if action == "retry":
        return "obvious failure caught by baseline"
    return "no warning under this bounded demo"


def run_case(text: str) -> None:
    text = normalize_text(text)
    baseline_status, baseline_reason = baseline_check(text)
    omnia_status, omnia_reason, omnia_score = omnia_review_signal(text)
    action = action_from_signals(baseline_status, omnia_status)
    claim = claim_from_action(action)

    print(f"INPUT: {text}")
    print(f"BASELINE: {baseline_status}")
    print(f"BASELINE_REASON: {baseline_reason}")
    print(f"OMNIA: {omnia_status}")
    print(f"OMNIA_REASON: {omnia_reason}")
    print(f"OMNIA_SCORE: {omnia_score:.3f}")
    print(f"ACTION: {action}")
    print(f"CLAIM: {claim}")
    print("-" * 60)


if __name__ == "__main__":
    cases = [
        "The answer seems correct. The answer seems correct. The answer seems correct.",
        "retry retry retry retry retry",
    ]

    for case in cases:
        run_case(case)