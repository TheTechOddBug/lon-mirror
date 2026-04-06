import random
import numpy as np


# -----------------------------
# Core OMNIA-like measurement
# -----------------------------

def adjacency_pairs(seq):
    return [(seq[i], seq[i+1]) for i in range(len(seq)-1)]


def perturb_sequence(seq, noise_level=0.2):
    seq = seq.copy()
    n = len(seq)
    k = int(n * noise_level)

    for _ in range(k):
        i = random.randint(0, n-1)
        seq[i] = random.randint(0, 9)

    return seq


def shuffle_sequence(seq):
    seq = seq.copy()
    random.shuffle(seq)
    return seq


def compute_I(base_pairs, pert_pairs):
    base_set = set(base_pairs)
    pert_set = set(pert_pairs)

    D = len(base_set.symmetric_difference(pert_set))
    return D / max(1, len(base_set))


def compute_sigma(I_values):
    return np.std(I_values)


def compute_V(sigma, alpha=1.0):
    return 1 / (1 + alpha * sigma)


def compute_omega(seq, trials=10):
    base_pairs = adjacency_pairs(seq)
    I_values = []

    for _ in range(trials):
        pert = perturb_sequence(seq)
        pert_pairs = adjacency_pairs(pert)
        I = compute_I(base_pairs, pert_pairs)
        I_values.append(I)

    I_mean = np.mean(I_values)
    sigma = compute_sigma(I_values)
    V = compute_V(sigma)

    omega = 0.7 * V + 0.3 * I_mean
    return omega


def compute_delta_struct(seq):
    omega_raw = compute_omega(seq)
    shuffled = shuffle_sequence(seq)
    omega_shuffle = compute_omega(shuffled)
    return omega_raw - omega_shuffle


# -----------------------------
# Test sequences
# -----------------------------

def generate_structured(n=100):
    # simple pattern: repeating + incremental
    return [(i % 5) for i in range(n)]


def generate_perturbed(base):
    return perturb_sequence(base, noise_level=0.4)


def generate_random(n=100):
    return [random.randint(0, 9) for _ in range(n)]


# -----------------------------
# Run test
# -----------------------------

def main():
    random.seed(42)
    np.random.seed(42)

    structured = generate_structured()
    perturbed = generate_perturbed(structured)
    random_seq = generate_random()

    d_structured = compute_delta_struct(structured)
    d_perturbed = compute_delta_struct(perturbed)
    d_random = compute_delta_struct(random_seq)

    print("\n--- OMNIA Public Proof Test ---\n")
    print(f"Δ_struct (structured): {d_structured:.4f}")
    print(f"Δ_struct (perturbed): {d_perturbed:.4f}")
    print(f"Δ_struct (random):     {d_random:.4f}")

    print("\nExpected invariant:")
    print("structured > perturbed > random\n")

    if d_structured > d_perturbed > d_random:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")


if __name__ == "__main__":
    main()