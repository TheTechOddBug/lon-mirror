import math
import random
from typing import Callable, Dict, List, Optional, Any


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

    # structural perturbation sensitivity
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
# Systems
# =========================================================

def logistic_map(x: float, r: float) -> float:
    return r * x * (1.0 - x)


def adaptive_logistic_map(
    x: float,
    r: float,
    target: float,
    gain: float,
    max_step: float,
) -> float:
    """
    Adaptive version:
    - computes nominal next state
    - applies bounded correction toward a target
    """
    y = r * x * (1.0 - x)
    correction = gain * (target - y)

    if correction > max_step:
        correction = max_step
    elif correction < -max_step:
        correction = -max_step

    return y + correction


def linear_contraction(x: float, a: float) -> float:
    return a * x


# =========================================================
# Dynamics helpers
# =========================================================

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
) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
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
    scan: List[Dict[str, Any]],
    target_state: str,
) -> Optional[int]:
    for row in scan:
        if row["state"] == target_state:
            return int(row["start_step"])
    return None


# =========================================================
# Resilience metrics
# =========================================================

def recovery_time(
    delta: List[float],
    threshold: float,
) -> Optional[int]:
    """
    First time Delta(t) goes below threshold.
    """
    for i, d in enumerate(delta):
        if d <= threshold:
            return i
    return None


def peak_divergence(delta: List[float]) -> float:
    return max(delta) if delta else 0.0


def tail_mean(delta: List[float], tail: int = 16) -> float:
    if not delta:
        return 0.0
    segment = delta[-tail:] if len(delta) >= tail else delta
    return sum(segment) / len(segment)


def resilience_score(
    delta: List[float],
    threshold: float,
    t_collapse: Optional[int],
) -> float:
    """
    Heuristic resilience score in [0,1].

    Higher if:
    - Delta remains small
    - recovery occurs
    - collapse is absent or late
    """
    if not delta:
        return 0.0

    peak = peak_divergence(delta)
    tail = tail_mean(delta)
    rec = recovery_time(delta, threshold=threshold)

    peak_term = 1.0 / (1.0 + 1000.0 * peak)
    tail_term = 1.0 / (1.0 + 1000.0 * tail)

    if rec is None:
        rec_term = 0.0
    else:
        rec_term = 1.0 / (1.0 + rec)

    if t_collapse is None:
        collapse_term = 1.0
    else:
        collapse_term = 1.0 / (1.0 + t_collapse)

    # Favor late/no collapse:
    collapse_bonus = 1.0 - collapse_term

    score = 0.35 * peak_term + 0.35 * tail_term + 0.15 * rec_term + 0.15 * collapse_bonus
    return round(max(0.0, min(1.0, score)), 4)


# =========================================================
# Benchmark cases
# =========================================================

def run_case(
    name: str,
    f: Callable[..., float],
    x0: float,
    epsilon: float,
    steps: int,
    window: int,
    threshold: float,
    **params: float,
) -> Dict[str, Any]:
    t1 = evolve(f, x0=x0, steps=steps, **params)
    t2 = evolve(f, x0=x0 + epsilon, steps=steps, **params)

    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window)

    t_unstable = first_state_time(scan, "UNSTABLE")
    t_collapse = first_state_time(scan, "COLLAPSE")
    t_recovery = recovery_time(delta, threshold=threshold)
    peak = peak_divergence(delta)
    tail = tail_mean(delta)
    R = resilience_score(delta, threshold=threshold, t_collapse=t_collapse)

    final_state = scan[-1]["state"] if scan else None

    return {
        "system": name,
        "params": params,
        "T_unstable": t_unstable,
        "T_collapse": t_collapse,
        "T_recovery": t_recovery,
        "peak_delta": round(peak, 12),
        "tail_mean": round(tail, 12),
        "final_state": final_state,
        "R": R,
    }


def print_results_table(results: List[Dict[str, Any]]) -> None:
    print(
        "system               | T_unstable | T_collapse | T_recovery | R      | final_state"
    )
    print("-" * 92)
    for row in results:
        print(
            f"{row['system']:<20} | "
            f"{str(row['T_unstable']):<10} | "
            f"{str(row['T_collapse']):<10} | "
            f"{str(row['T_recovery']):<10} | "
            f"{row['R']:<6.4f} | "
            f"{str(row['final_state'])}"
        )


def print_details(results: List[Dict[str, Any]]) -> None:
    print("\nDetailed metrics:")
    print("-" * 92)
    for row in results:
        print(
            f"{row['system']}: "
            f"peak_delta={row['peak_delta']} "
            f"tail_mean={row['tail_mean']} "
            f"params={row['params']}"
        )


def run_benchmark() -> None:
    x0 = 0.123456789
    epsilon = 1e-10
    steps = 128
    window = 32
    threshold = 1e-8

    results = [
        run_case(
            name="linear_contraction",
            f=linear_contraction,
            x0=x0,
            epsilon=epsilon,
            steps=steps,
            window=window,
            threshold=threshold,
            a=0.8,
        ),
        run_case(
            name="logistic_stable",
            f=logistic_map,
            x0=x0,
            epsilon=epsilon,
            steps=steps,
            window=window,
            threshold=threshold,
            r=2.8,
        ),
        run_case(
            name="logistic_chaotic",
            f=logistic_map,
            x0=x0,
            epsilon=epsilon,
            steps=steps,
            window=window,
            threshold=threshold,
            r=3.9,
        ),
        run_case(
            name="adaptive_logistic",
            f=adaptive_logistic_map,
            x0=x0,
            epsilon=epsilon,
            steps=steps,
            window=window,
            threshold=threshold,
            r=3.9,
            target=0.5,
            gain=0.15,
            max_step=0.03,
        ),
    ]

    print("\nOMNIA Minimal Resilience Benchmark")
    print("=" * 92)
    print(f"steps={steps}, window={window}, epsilon={epsilon}, recovery_threshold={threshold}\n")

    print_results_table(results)
    print_details(results)

    print("\nInterpretation:")
    print("- higher R means better retention or recovery of equivalence")
    print("- adaptive systems should delay collapse or reduce tail divergence")
    print("- this measures resilience of the description, not intelligence itself")


if __name__ == "__main__":
    run_benchmark()