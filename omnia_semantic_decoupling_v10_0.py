import random
from typing import List, Dict
from omnia_rfs_core_v1_0 import omnia_rfs_v1


def tokenize(text: str) -> List[str]:
    return text.split()


def controlled_shuffle(tokens: List[str], seed: int = 42) -> List[str]:
    rng = random.Random(seed)
    shuffled = list(tokens)
    rng.shuffle(shuffled)
    return shuffled


def semantic_decoupling_score(text: str, seed: int = 42) -> Dict[str, float]:
    tokens = tokenize(text)

    if len(tokens) < 10:
        return {
            "omega_raw": 0.0,
            "omega_shuffle": 0.0,
            "delta_struct": 0.0,
        }

    raw_text = " ".join(tokens)
    shuffled_text = " ".join(controlled_shuffle(tokens, seed=seed))

    omega_raw = omnia_rfs_v1(raw_text)
    omega_shuffle = omnia_rfs_v1(shuffled_text)
    delta_struct = omega_raw - omega_shuffle

    return {
        "omega_raw": omega_raw,
        "omega_shuffle": omega_shuffle,
        "delta_struct": delta_struct,
    }


if __name__ == "__main__":
    sample = "start_node step_1 step_2 step_3 step_4 end_node"
    out = semantic_decoupling_score(sample)
    print(out)