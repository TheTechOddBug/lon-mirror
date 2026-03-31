# OMNIA — Structural Stability Core (minimal prototype)
# MB-X.01 / Omniabase±

import math
import zlib
from collections import Counter

# -------------------------
# Utilities
# -------------------------

def _to_bytes(x):
    if isinstance(x, bytes):
        return x
    if isinstance(x, str):
        return x.encode("utf-8")
    # fallback generico
    return str(x).encode("utf-8")


# -------------------------
# T1 — Compressibility (C)
# -------------------------
def compressibility(x):
    b = _to_bytes(x)
    if len(b) == 0:
        return 0.0

    compressed = zlib.compress(b, level=9)
    ratio = len(compressed) / len(b)

    # invertiamo: più comprimibile = valore più alto
    C = 1.0 - ratio

    # clamp
    return max(0.0, min(1.0, C))


# -------------------------
# T2 — Noise Sensitivity (N)
# -------------------------
def _perturb_bytes(b, strength=0.01):
    if len(b) == 0:
        return b

    b = bytearray(b)
    step = max(1, int(len(b) * strength))

    for i in range(0, len(b), step):
        b[i] = (b[i] + 1) % 256

    return bytes(b)


def noise_sensitivity(x):
    b = _to_bytes(x)
    if len(b) == 0:
        return 1.0

    b2 = _perturb_bytes(b)

    c1 = zlib.compress(b)
    c2 = zlib.compress(b2)

    # differenza relativa
    diff = abs(len(c1) - len(c2)) / max(len(c1), 1)

    # più diff = più sensibile
    N = max(0.0, min(1.0, diff))
    return N


# -------------------------
# T3 — Coherence (K)
# -------------------------
def coherence(x):
    b = _to_bytes(x)
    if len(b) == 0:
        return 0.0

    counts = Counter(b)
    total = len(b)

    # Shannon entropy
    entropy = 0.0
    for c in counts.values():
        p = c / total
        entropy -= p * math.log2(p)

    # entropy max per byte = 8
    entropy_norm = entropy / 8.0

    # invertiamo: meno entropia = più struttura
    K = 1.0 - entropy_norm

    return max(0.0, min(1.0, K))


# -------------------------
# S(x) — Stability Function
# -------------------------
def stability(x, thresholds=None):
    if thresholds is None:
        thresholds = {
            "C_high": 0.4,
            "N_low": 0.1,
            "K_high": 0.4,
            "C_low": 0.1,
            "N_high": 0.3,
            "K_low": 0.1,
        }

    C = compressibility(x)
    N = noise_sensitivity(x)
    K = coherence(x)

    if C >= thresholds["C_high"] and N <= thresholds["N_low"] and K >= thresholds["K_high"]:
        state = "STABLE"
    elif C <= thresholds["C_low"] and N >= thresholds["N_high"] and K <= thresholds["K_low"]:
        state = "COLLAPSE"
    else:
        state = "UNSTABLE"

    return {
        "state": state,
        "C": round(C, 4),
        "N": round(N, 4),
        "K": round(K, 4),
    }


# -------------------------
# Quick test
# -------------------------
if __name__ == "__main__":
    samples = [
        "AAAAAAAAAAAAAAAAAAAA",
        "The quick brown fox jumps over the lazy dog",
        "asdkjashdkjahskdjhaksjdhkajshdkjashdkj",
    ]

    for s in samples:
        print(s)
        print(stability(s))
        print("-" * 40)