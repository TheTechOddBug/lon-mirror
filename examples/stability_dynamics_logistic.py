import math
from typing import Callable, Dict, List, Any

from omnia.stability_core import stability


def logistic_map(x: float, r: float) -> float:
    """
    Classic logistic map:
        x_{t+1} = r * x_t * (1 - x_t)

    Useful because:
    - low r -> stable fixed behavior
    - medium r -> oscillatory regimes
    - high r -> chaotic behavior
    """
    return r * x * (1.0 - x)


def evolve(
    F: Callable[..., float],
    x0: float,
    steps: int,
    **params: Any,
) -> List[float]:
    """
    Evolve a scalar dynamical system for a fixed number of steps.
    """
    xs = [x0]
    x = x0
    for _ in range(steps - 1):
        x = F(x, **params)
        xs.append(x)
    return xs


def serialize_series(xs: List[float], decimals: int = 8) -> str:
    """
    Convert the trajectory into a deterministic textual representation.
    """
    return ",".join(f"{x:.{decimals}f}" for x in xs)


def rolling_windows(xs: List[float], window: int) -> List[List[float]]:
    """
    Generate rolling windows from the full trajectory.
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(xs):
        return [xs[:]]
    return [xs[i:i + window] for i in range(len(xs) - window + 1)]


def dynamic_stability_scan(
    xs: List[float],
    window: int = 32,
    decimals: int = 8,
) -> List[Dict[str, Any]]:
    """
    Evaluate stability on rolling windows of the trajectory.

    Each window is serialized and passed through the structural stability core.
    """
    results: List[Dict[str, Any]] = []
    for i, w in enumerate(rolling_windows(xs, window=window)):
        serialized = serialize_series(w, decimals=decimals)
        s = stability(serialized)
        results.append(
            {
                "window_index": i,
                "start_step": i,
                "end_step": i + len(w) - 1,
                "state": s["state"],
                "C": s["C"],
                "N": s["N"],
                "K": s["K"],
            }
        )
    return results


def summarize_scan(scan: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Summarize counts and first transition points.
    """
    counts = {"STABLE": 0, "UNSTABLE": 0, "COLLAPSE": 0}
    first_seen = {"STABLE": None, "UNSTABLE": None, "COLLAPSE": None}

    for row in scan:
        state = row["state"]
        counts[state] += 1
        if first_seen[state] is None:
            first_seen[state] = row["start_step"]

    return {
        "counts": counts,
        "first_seen": first_seen,
        "num_windows": len(scan),
    }


def print_scan_preview(scan: List[Dict[str, Any]], max_rows: int = 10) -> None:
    """
    Print a compact preview of the scan.
    """
    print("window_index | steps      | state      | C      | N      | K")
    print("-" * 66)
    for row in scan[:max_rows]:
        print(
            f"{row['window_index']:>12} | "
            f"{row['start_step']:>3}-{row['end_step']:<3} | "
            f"{row['state']:<10} | "
            f"{row['C']:<6.4f} | "
            f"{row['N']:<6.4f} | "
            f"{row['K']:<6.4f}"
        )
    if len(scan) > max_rows:
        print("...")


def run_case(name: str, r: float, x0: float = 0.123456, steps: int = 128, window: int = 32) -> None:
    """
    Run one dynamical regime and print trajectory stability diagnostics.
    """
    print("=" * 80)
    print(f"CASE: {name}")
    print(f"Parameters: r={r}, x0={x0}, steps={steps}, window={window}")

    xs = evolve(logistic_map, x0=x0, steps=steps, r=r)
    scan = dynamic_stability_scan(xs, window=window)
    summary = summarize_scan(scan)

    print()
    print("Trajectory preview:")
    print(", ".join(f"{x:.6f}" for x in xs[:12]), "...")
    print()

    print("Stability scan preview:")
    print_scan_preview(scan, max_rows=12)
    print()

    print("Summary:")
    print(summary)
    print()


if __name__ == "__main__":
    # Typical logistic map regimes:
    # r = 2.8  -> convergent / stable
    # r = 3.2  -> periodic / transitional
    # r = 3.9  -> chaotic / unstable
    run_case("Stable regime", r=2.8)
    run_case("Oscillatory regime", r=3.2)
    run_case("Chaotic regime", r=3.9)