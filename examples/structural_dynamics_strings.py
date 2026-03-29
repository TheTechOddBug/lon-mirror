import numpy as np


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

    num = 0
    for z in zs:
        num += np.linalg.norm(z - C) ** 2

    denom = np.linalg.norm(C) ** 2 + 1e-12

    D = num / len(zs) / denom
    omega = np.exp(-D)

    return omega


def analyze(strings):
    print("\n=== STRING STRUCTURAL ANALYSIS ===")
    for s in strings:
        o = omega_string(s)
        print(f"{s} -> Ω={o:.3f}")


if __name__ == "__main__":
    test_strings = [
        "hello",
        "aaaaaa",
        "abcabc",
        "random",
        "xyzxyzxyz",
    ]

    analyze(test_strings)