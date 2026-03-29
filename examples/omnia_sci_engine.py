import numpy as np


# ---------- TRANSFORMS ----------

def transforms(s):
    return [
        s,
        s[::-1],
        s.upper(),
        s.lower(),
        s + s,
    ]


# ---------- LENSES ----------

def lens_basic(s):
    return np.array([
        len(s),
        sum(ord(c) for c in s),
        len(set(s)),
    ], dtype=float)


def lens_entropy(s):
    if len(s) == 0:
        return np.array([0.0])

    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1

    probs = np.array(list(counts.values())) / len(s)
    entropy = -np.sum(probs * np.log(probs + 1e-12))

    return np.array([entropy])


def lens_pattern(s):
    return np.array([
        sum(1 for i in range(len(s)-1) if s[i] == s[i+1]),
        sum(1 for i in range(len(s)-1) if s[i] != s[i+1]),
    ], dtype=float)


LENSES = [
    lens_basic,
    lens_entropy,
    lens_pattern,
]


# ---------- CORE ----------

def centroid(vectors):
    return np.mean(vectors, axis=0)


def cosine(a, b):
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)

    if na < 1e-12 or nb < 1e-12:
        return 0.0

    return float(np.dot(a, b) / (na * nb))


def omega_from_vectors(vectors):
    C = centroid(vectors)

    num = sum(np.linalg.norm(v - C) ** 2 for v in vectors)
    denom = np.linalg.norm(C) ** 2 + 1e-12

    D = num / len(vectors) / denom
    return float(np.exp(-D)), C


# ---------- SCI ----------

def sci(centroids):
    n = len(centroids)

    if n < 2:
        return 1.0

    sims = []
    for i in range(n):
        for j in range(i + 1, n):
            sims.append(cosine(centroids[i], centroids[j]))

    return float(np.mean(sims))


# ---------- OMNIA MULTI-LENS ----------

def omnia_multi_lens(s):
    centroids = []
    omegas = []

    for lens in LENSES:
        vectors = [lens(t) for t in transforms(s)]
        omega, C = omega_from_vectors(vectors)

        omegas.append(omega)
        centroids.append(C)

    omega_mean = float(np.mean(omegas))
    sci_value = sci(centroids)

    return omega_mean, sci_value


# ---------- DEMO ----------

if __name__ == "__main__":
    print("=== OMNIA SCI ENGINE ===")

    test_strings = [
        "aaaaaa",
        "abcabc",
        "hello",
        "random",
        "xyzxyzxyz",
    ]

    for s in test_strings:
        o, s_val = omnia_multi_lens(s)
        print(f"{s} -> Ω={o:.3f}, SCI={s_val:.3f}")