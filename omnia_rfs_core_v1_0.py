import numpy as np
from typing import List, Tuple

def tokenize(text: str) -> List[str]:
    return text.split()

def get_relational_response(
    tokens: List[str],
    n_trials: int = 60,
    swaps_per_trial: int = 3,
    volatility_scale: float = 5.0
) -> Tuple[float, float]:

    n = len(tokens)
    responses = []

    base_adj = set(zip(tokens[:-1], tokens[1:]))
    base_size = len(base_adj)

    if base_size == 0:
        return 0.0, 0.0

    for _ in range(n_trials):
        s_tokens = list(tokens)

        for _ in range(swaps_per_trial):
            idx = np.random.randint(0, n - 1)
            s_tokens[idx], s_tokens[idx + 1] = s_tokens[idx + 1], s_tokens[idx]

        stress_adj = set(zip(s_tokens[:-1], s_tokens[1:]))
        diff_size = len(base_adj ^ stress_adj)

        responses.append(diff_size / base_size)

    avg_impact = float(np.mean(responses))
    response_std = float(np.std(responses))

    vol_score = 1.0 / (1.0 + (response_std * volatility_scale))

    return avg_impact, vol_score


def omnia_rfs_v1(text: str) -> float:
    tokens = tokenize(text)

    if len(tokens) < 10:
        return 0.0

    avg_impact, vol_score = get_relational_response(tokens)

    score = (0.7 * vol_score) + (0.3 * avg_impact)

    return max(0.0, min(1.0, score))