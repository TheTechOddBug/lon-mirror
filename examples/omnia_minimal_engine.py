import numpy as np
from math import gcd


# ---------- MOD N CORE ----------

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


def omega_mod_n(n, k):
    visited = set()
    total = 0
    weighted = 0

    for x in range(n):
        if x in visited:
            continue

        seq, c = orbit_mod_n(n, k, x)
        for s in seq:
            visited.add(s)

        if c is None:
            omega = 0.0
        else:
            omega = (len(seq) - c) / len(seq)

        weighted += omega * len(seq)
        total += len(seq)

    return weighted / total if total > 0 else 0.0


# ---------- STRING CORE ----------

def transforms(s):
    return [
        s,
        s[::-1],
        s.upper(),
        s.lower(),
        s + s,
    ]


def lens(s):
    return np.array([
        len(s),
        sum(ord(c) for c in s),
        len(set(s)),
    ], dtype=float)


def omega_string(s):
    zs = [lens(t) for t in transforms(s)]
    C = np.mean(zs, axis=0)

    num = sum(np.linalg.norm(z - C) ** 2 for z in zs)
    denom = np.linalg.norm(C) ** 2 + 1e-12

    D = num / len(zs) / denom
    return float(np.exp(-D))


# ---------- OMNIA MINIMAL ----------

def omnia_measure(obj):
    if isinstance(obj, tuple) and len(obj) == 2:
        n, k = obj
        return omega_mod_n(n, k)

    if isinstance(obj, str):
        return omega_string(obj)

    raise ValueError("Unsupported type")


# ---------- DEMO ----------

if __name__ == "__main__":
    print("=== OMNIA MINIMAL ENGINE ===")

    print("\n-- MOD N --")
    for case in [(9, 2), (9, 3), (12, 6)]:
        print(f"{case} -> Ω={omnia_measure(case):.3f}")

    print("\n-- STRINGS --")
    for s in ["hello", "aaaaaa", "abcabc", "random"]:
        print(f"{s} -> Ω={omnia_measure(s):.3f}")