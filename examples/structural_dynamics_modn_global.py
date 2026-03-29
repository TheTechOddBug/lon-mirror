from math import gcd


def orbit_mod_n(n, k, start, max_steps=100):
    seen = {}
    seq = []
    x = start % n

    for step in range(max_steps):
        if x in seen:
            return seq, seen[x]
        seen[x] = step
        seq.append(x)
        x = (k * x) % n

    return seq, None


def omega_local(seq, cycle_start):
    if cycle_start is None or len(seq) == 0:
        return 0.0
    cycle_len = len(seq) - cycle_start
    return cycle_len / len(seq)


def omega_global(n, k):
    visited = set()
    total_weight = 0
    weighted_sum = 0

    for x in range(n):
        if x in visited:
            continue

        seq, c = orbit_mod_n(n, k, x)
        size = len(seq)

        for s in seq:
            visited.add(s)

        omega = omega_local(seq, c)

        weighted_sum += omega * size
        total_weight += size

    if total_weight == 0:
        return 0.0

    return weighted_sum / total_weight


def classify(n, k):
    return "conservative" if gcd(k, n) == 1 else "dissipative"


def analyze(n, k):
    print(f"\n=== n={n}, k={k} ===")
    print(f"regime: {classify(n, k)}")
    print(f"gcd(k,n)={gcd(k,n)}")

    og = omega_global(n, k)

    print(f"Ω_global = {og:.3f}")


if __name__ == "__main__":
    cases = [
        (9, 2),
        (9, 3),
        (9, 8),
        (7, 3),
        (10, 2),
        (12, 6),
    ]

    for n, k in cases:
        analyze(n, k)