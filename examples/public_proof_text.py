import random
import re
from collections import Counter
from statistics import mean, pstdev


def tokenize(text: str):
    return re.findall(r"\w+|[^\w\s]", text.lower())


def adjacency_pairs(tokens):
    return [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]


def shuffle_tokens(tokens, seed=42):
    rng = random.Random(seed)
    out = list(tokens)
    rng.shuffle(out)
    return out


def perturb_tokens(tokens, noise_level=0.20, seed=42):
    rng = random.Random(seed)
    out = list(tokens)
    n = len(out)
    k = max(1, int(n * noise_level))

    for _ in range(k):
        i = rng.randint(0, n - 2)
        out[i], out[i + 1] = out[i + 1], out[i]

    return out


def compute_I(base_pairs, pert_pairs):
    base_set = set(base_pairs)
    pert_set = set(pert_pairs)
    d = len(base_set.symmetric_difference(pert_set))
    return d / max(1, len(base_set))


def compute_V(sig, alpha=1.0):
    return 1.0 / (1.0 + alpha * sig)


def compute_omega(tokens, trials=12, base_seed=42):
    base_pairs = adjacency_pairs(tokens)
    i_values = []

    for t in range(trials):
        pert = perturb_tokens(tokens, noise_level=0.20, seed=base_seed + t)
        pert_pairs = adjacency_pairs(pert)
        i_values.append(compute_I(base_pairs, pert_pairs))

    i_mean = mean(i_values)
    sig = pstdev(i_values) if len(i_values) > 1 else 0.0
    v = compute_V(sig)
    omega = 0.7 * v + 0.3 * i_mean
    return omega


def compute_delta_struct(tokens, seed=42):
    omega_raw = compute_omega(tokens, base_seed=seed)
    omega_shuffle = compute_omega(shuffle_tokens(tokens, seed=seed), base_seed=seed)
    return omega_raw - omega_shuffle


def make_random_from_vocab(tokens, seed=42):
    rng = random.Random(seed)
    vocab = list(set(tokens))
    return [rng.choice(vocab) for _ in range(len(tokens))]


def main():
    structured_text = (
        "The solar system consists of the Sun and the objects that orbit it. "
        "Earth is the third planet from the Sun. "
        "The Moon orbits Earth. "
        "Gravity keeps planets in their paths around the Sun."
    )

    structured = tokenize(structured_text)
    perturbed = perturb_tokens(structured, noise_level=0.35, seed=42)
    random_tokens = make_random_from_vocab(structured, seed=42)

    d_structured = compute_delta_struct(structured, seed=42)
    d_perturbed = compute_delta_struct(perturbed, seed=42)
    d_random = compute_delta_struct(random_tokens, seed=42)

    print("\n--- OMNIA Public Proof Test (Natural Text) ---\n")
    print(f"Δ_struct (structured): {d_structured:.4f}")
    print(f"Δ_struct (perturbed):  {d_perturbed:.4f}")
    print(f"Δ_struct (random):     {d_random:.4f}")

    print("\nExpected invariant:")
    print("structured > perturbed > random\n")

    if d_structured > d_perturbed > d_random:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")


if __name__ == "__main__":
    main()