import zlib
import math
from typing import List, Dict, Any, Optional


# =========================
# STABILITY CORE (MINIMALE)
# =========================

def compress_ratio(data: bytes) -> float:
    if not data:
        return 1.0
    compressed = zlib.compress(data)
    return len(compressed) / len(data)


def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1
    n = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / n
        entropy -= p * math.log2(p)
    return entropy / 8.0  # normalizzato (byte -> max 8 bit)


def perturb_bytes(data: bytes, step: int = 7) -> bytes:
    if not data:
        return data
    arr = bytearray(data)
    for i in range(0, len(arr), step):
        arr[i] ^= 0xFF  # flip bit semplice
    return bytes(arr)


def stability(serialized: str) -> Dict[str, Any]:
    raw = serialized.encode("utf-8")

    C = compress_ratio(raw)
    N = shannon_entropy(raw)

    perturbed = perturb_bytes(raw)
    C2 = compress_ratio(perturbed)
    N2 = shannon_entropy(perturbed)

    # variazione strutturale
    K = abs(C - C2) + abs(N - N2)

    # soglie empiriche (semplici)
    if C < 0.6 and K < 0.05:
        state = "STABLE"
    elif C < 0.9 and K < 0.15:
        state = "UNSTABLE"
    else:
        state = "COLLAPSE"

    return {
        "state": state,
        "C": C,
        "N": N,
        "K": K,
    }


# =========================
# DINAMICA
# =========================

def logistic_map(x: float, r: float) -> float:
    return r * x * (1.0 - x)


def evolve(x0: float, steps: int, r: float) -> List[float]:
    xs = [x0]
    x = x0
    for _ in range(steps - 1):
        x = logistic_map(x, r)
        xs.append(x)
    return xs


def delta_series(xs1: List[float], xs2: List[float]) -> List[float]:
    return [abs(a - b) for a, b in zip(xs1, xs2)]


def serialize_series(xs: List[float], decimals: int = 12) -> str:
    return ",".join(f"{x:.{decimals}f}" for x in xs)


def rolling_windows(xs: List[float], window: int) -> List[List[float]]:
    if window > len(xs):
        return [xs]
    return [xs[i:i + window] for i in range(len(xs) - window + 1)]


# =========================
# TΔ CALCOLO
# =========================

def classify_delta_windows(delta: List[float], window: int) -> List[Dict[str, Any]]:
    results = []
    windows = rolling_windows(delta, window)

    for i, w in enumerate(windows):
        s = stability(serialize_series(w))
        results.append({
            "index": i,
            "state": s["state"],
            "C": s["C"],
            "N": s["N"],
            "K": s["K"],
        })
    return results


def find_T_delta(scan: List[Dict[str, Any]], target: str) -> Optional[int]:
    for row in scan:
        if row["state"] == target:
            return row["index"]
    return None


# =========================
# RUN
# =========================

def run_case(r: float):
    x0 = 0.123456789
    epsilon = 1e-10
    steps = 128
    window = 32

    t1 = evolve(x0, steps, r)
    t2 = evolve(x0 + epsilon, steps, r)

    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window)

    T_unstable = find_T_delta(scan, "UNSTABLE")
    T_collapse = find_T_delta(scan, "COLLAPSE")

    print("\n==============================")
    print(f"r = {r}")
    print("TΔ unstable:", T_unstable)
    print("TΔ collapse:", T_collapse)

    print("\nPrime finestre:")
    for row in scan[:10]:
        print(row)


if __name__ == "__main__":
    run_case(2.8)
    run_case(3.2)
    run_case(3.9)