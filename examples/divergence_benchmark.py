import math
import random
from typing import Callable, Dict, List, Optional, Tuple


# =========================================================
# Minimal standalone structural stability core
# =========================================================

def compressibility_score(data: bytes) -> float:
    import zlib
    if not data:
        return 1.0
    compressed = zlib.compress(data, level=9)
    ratio = len(compressed) / len(data)
    score = 1.0 - ratio
    return max(0.0, min(1.0, score))


def shannon_entropy_norm(data: bytes) -> float:
    if not data:
        return 0.0
    counts: Dict[int, int] = {}
    for b in data:
        counts[b] = counts.get(b, 0) + 1
    n = len(data)
    entropy = 0.0
    for c in counts.values():
        p = c / n
        entropy -= p * math.log2(p)
    return max(0.0, min(1.0, entropy / 8.0))


def perturb_bytes(data: bytes, step: int = 7) -> bytes:
    if not data:
        return data
    arr = bytearray(data)
    for i in range(0, len(arr), step):
        arr[i] ^= 0xFF
    return bytes(arr)


def stability(serialized: str) -> Dict[str, float | str]:
    raw = serialized.encode("utf-8")

    c1 = compressibility_score(raw)
    h1 = shannon_entropy_norm(raw)

    perturbed = perturb_bytes(raw)
    c2 = compressibility_score(perturbed)
    h2 = shannon_entropy_norm(perturbed)

    # K here means structural perturbation sensitivity
    k = abs(c1 - c2) + abs(h1 - h2)

    if c1 >= 0.4 and k <= 0.08:
        state = "STABLE"
    elif c1 <= 0.1 and k >= 0.12:
        state = "COLLAPSE"
    else:
        state = "UNSTABLE"

    return {
        "state": state,
        "C": round(c1, 4),
        "H": round(h1, 4),
        "K": round(k, 4),
    }


# =========================================================
# Dynamical systems
# =========================================================

def logistic_map(x: float, r: float) -> float:
    return r * x * (1.0 - x)


def linear_contraction(x: float, a: float) -> float:
    return a * x


def linear_expansion(x: float, a: float) -> float:
    return a * x


def random_series(steps: int, seed: int) -> List[float]:
    rng = random.Random(seed)
    return [rng.random() for _ in range(steps)]


def evolve(
    f: Callable[..., float],
    x0: float,
    steps: int,
    **params: float,
) -> List[float]:
    xs = [x0]
    x = x0
    for _ in range(steps - 1):
        x = f(x, **params)
        xs.append(x)
    return xs


def delta_series(xs1: List[float], xs2: List[float]) -> List[float]:
    if len(xs1) != len(xs2):
        raise ValueError("Trajectories must have the same length.")
    return [abs(a - b) for a, b in zip(xs1, xs2)]


def serialize_series(xs: List[float], decimals: int = 12) -> str:
    return ",".join(f"{x:.{decimals}f}" for x in xs)


def rolling_windows(xs: List[float], window: int) -> List[List[float]]:
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(xs):
        return [xs[:]]
    return [xs[i:i + window] for i in range(len(xs) - window + 1)]


def classify_delta_windows(
    delta: List[float],
    window: int = 32,
    decimals: int = 12,
) -> List[Dict[str, float | str | int]]:
    results: List[Dict[str, float | str | int]] = []
    for i, w in enumerate(rolling_windows(delta, window=window)):
        s = stability(serialize_series(w, decimals=decimals))
        results.append(
            {
                "window_index": i,
                "start_step": i,
                "end_step": i + len(w) - 1,
                "state": s["state"],
                "C": s["C"],
                "H": s["H"],
                "K": s["K"],
            }
        )
    return results


def first_state_time(
    scan: List[Dict[str, float | str | int]],
    target_state: str,
) -> Optional[int]:
    for row in scan:
        if row["state"] == target_state:
            return int(row["start_step"])
    return None


def summarize_scan(
    scan: List[Dict[str, float | str | int]],
) -> Dict[str, object]:
    counts = {"STABLE": 0, "UNSTABLE": 0, "COLLAPSE": 0}
    for row in scan:
        counts[str(row["state"])] += 1

    return {
        "counts": counts,
        "T_unstable": first_state_time(scan, "UNSTABLE"),
        "T_collapse": first_state_time(scan, "COLLAPSE"),
        "final_state": str(scan[-1]["state"]) if scan else None,
    }


# =========================================================
# Benchmark cases
# =========================================================

def benchmark_case_logistic(
    r: float,
    x0: float,
    epsilon: float,
    steps: int,
    window: int,
) -> Dict[str, object]:
    t1 = evolve(logistic_map, x0=x0, steps=steps, r=r)
    t2 = evolve(logistic_map, x0=x0 + epsilon, steps=steps, r=r)
    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window)
    summary = summarize_scan(scan)

    return {
        "system": "logistic",
        "param": f"r={r}",
        "T_unstable": summary["T_unstable"],
        "T_collapse": summary["T_collapse"],
        "final_state": summary["final_state"],
        "counts": summary["counts"],
    }


def benchmark_case_linear_contraction(
    a: float,
    x0: float,
    epsilon: float,
    steps: int,
    window: int,
) -> Dict[str, object]:
    t1 = evolve(linear_contraction, x0=x0, steps=steps, a=a)
    t2 = evolve(linear_contraction, x0=x0 + epsilon, steps=steps, a=a)
    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window)
    summary = summarize_scan(scan)

    return {
        "system": "linear_contraction",
        "param": f"a={a}",
        "T_unstable": summary["T_unstable"],
        "T_collapse": summary["T_collapse"],
        "final_state": summary["final_state"],
        "counts": summary["counts"],
    }


def benchmark_case_linear_expansion(
    a: float,
    x0: float,
    epsilon: float,
    steps: int,
    window: int,
) -> Dict[str, object]:
    t1 = evolve(linear_expansion, x0=x0, steps=steps, a=a)
    t2 = evolve(linear_expansion, x0=x0 + epsilon, steps=steps, a=a)
    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window)
    summary = summarize_scan(scan)

    return {
        "system": "linear_expansion",
        "param": f"a={a}",
        "T_unstable": summary["T_unstable"],
        "T_collapse": summary["T_collapse"],
        "final_state": summary["final_state"],
        "counts": summary["counts"],
    }


def benchmark_case_random(
    steps: int,
    window: int,
    seed1: int,
    seed2: int,
) -> Dict[str, object]:
    t1 = random_series(steps, seed=seed1)
    t2 = random_series(steps, seed=seed2)
    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window)
    summary = summarize_scan(scan)

    return {
        "system": "random",
        "param": f"seed1={seed1},seed2={seed2}",
        "T_unstable": summary["T_unstable"],
        "T_collapse": summary["T_collapse"],
        "final_state": summary["final_state"],
        "counts": summary["counts"],
    }


# =========================================================
# Reporting
# =========================================================

def fmt_time(x: object) -> str:
    return "None" if x is None else str(x)


def print_results_table(results: List[Dict[str, object]]) -> None:
    print(
        "system              | param              | T_unstable | T_collapse | final_state"
    )
    print("-" * 82)
    for row in results:
        print(
            f"{str(row['system']):<19} | "
            f"{str(row['param']):<18} | "
            f"{fmt_time(row['T_unstable']):<10} | "
            f"{fmt_time(row['T_collapse']):<10} | "
            f"{str(row['final_state'])}"
        )


def print_counts(results: List[Dict[str, object]]) -> None:
    print("\nWindow state counts:")
    print("-" * 82)
    for row in results:
        counts = row["counts"]
        print(
            f"{str(row['system'])} ({row['param']}): "
            f"STABLE={counts['STABLE']} "
            f"UNSTABLE={counts['UNSTABLE']} "
            f"COLLAPSE={counts['COLLAPSE']}"
        )


def run_benchmark() -> None:
    x0 = 0.123456789
    epsilon = 1e-10
    steps = 128
    window = 32

    results = [
        benchmark_case_logistic(r=2.8, x0=x0, epsilon=epsilon, steps=steps, window=window),
        benchmark_case_logistic(r=3.2, x0=x0, epsilon=epsilon, steps=steps, window=window),
        benchmark_case_logistic(r=3.9, x0=x0, epsilon=epsilon, steps=steps, window=window),
        benchmark_case_linear_contraction(a=0.8, x0=x0, epsilon=epsilon, steps=steps, window=window),
        benchmark_case_linear_expansion(a=1.05, x0=x0, epsilon=epsilon, steps=steps, window=window),
        benchmark_case_random(steps=steps, window=window, seed1=1, seed2=2),
    ]

    print("\nOMNIA Minimal Divergence Benchmark")
    print("=" * 82)
    print(f"steps={steps}, window={window}, epsilon={epsilon}, x0={x0}\n")

    print_results_table(results)
    print_counts(results)

    print("\nInterpretation:")
    print("- stable systems should resist divergence longer")
    print("- chaotic or random systems should reach instability faster")
    print("- this benchmark measures loss of equivalence, not 'chaos itself'")


if __name__ == "__main__":
    run_benchmark()