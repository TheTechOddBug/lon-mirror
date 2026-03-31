from typing import Callable, Dict, List, Any, Optional

from omnia.stability_core import stability


def logistic_map(x: float, r: float) -> float:
    """
    Classic logistic map:
        x_{t+1} = r * x_t * (1 - x_t)
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


def delta_series(xs1: List[float], xs2: List[float]) -> List[float]:
    """
    Pointwise absolute difference between two trajectories.
    """
    if len(xs1) != len(xs2):
        raise ValueError("Trajectories must have the same length.")
    return [abs(a - b) for a, b in zip(xs1, xs2)]


def serialize_series(xs: List[float], decimals: int = 12) -> str:
    """
    Deterministic textual representation of a float series.
    """
    return ",".join(f"{x:.{decimals}f}" for x in xs)


def rolling_windows(xs: List[float], window: int) -> List[List[float]]:
    """
    Generate rolling windows from the full series.
    """
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
    """
    Apply the structural stability core on rolling windows of Delta(t).
    """
    results: List[Dict[str, Any]] = []

    windows = rolling_windows(delta, window=window)
    for i, w in enumerate(windows):
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


def find_divergence_time(
    scan: List[Dict[str, Any]],
    target_state: str = "COLLAPSE",
) -> Optional[int]:
    """
    Return the first start_step where the requested target_state appears.

    This is the first simple definition of TΔ:
    the first window where Delta(t) becomes structurally classified as COLLAPSE.
    """
    for row in scan:
        if row["state"] == target_state:
            return row["start_step"]
    return None


def summarize_scan(scan: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Summarize counts and first appearances of each state.
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


def print_scan_preview(scan: List[Dict[str, Any]], max_rows: int = 12) -> None:
    """
    Print a compact preview of the rolling analysis.
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


def run_case(
    name: str,
    r: float,
    x0: float = 0.123456789,
    epsilon: float = 1e-10,
    steps: int = 128,
    window: int = 32,
    decimals: int = 12,
) -> None:
    """
    Run a divergence experiment:
    compare two nearby trajectories x0 and x0 + epsilon,
    then analyze Delta(t) with the structural stability core.
    """
    print("=" * 80)
    print(f"CASE: {name}")
    print(
        f"Parameters: r={r}, x0={x0}, epsilon={epsilon}, "
        f"steps={steps}, window={window}, decimals={decimals}"
    )

    t1 = evolve(logistic_map, x0=x0, steps=steps, r=r)
    t2 = evolve(logistic_map, x0=x0 + epsilon, steps=steps, r=r)

    delta = delta_series(t1, t2)
    scan = classify_delta_windows(delta, window=window, decimals=decimals)
    summary = summarize_scan(scan)

    T_delta_unstable = find_divergence_time(scan, target_state="UNSTABLE")
    T_delta_collapse = find_divergence_time(scan, target_state="COLLAPSE")

    print()
    print("Trajectory 1 preview:")
    print(", ".join(f"{x:.6f}" for x in t1[:10]), "...")
    print()

    print("Trajectory 2 preview:")
    print(", ".join(f"{x:.6f}" for x in t2[:10]), "...")
    print()

    print("Delta(t) preview:")
    print(", ".join(f"{x:.12f}" for x in delta[:12]), "...")
    print()

    print("Rolling stability on Delta(t):")
    print_scan_preview(scan, max_rows=12)
    print()

    print("Summary:")
    print(summary)
    print()

    print("Divergence times:")
    print(f"TΔ (first UNSTABLE): {T_delta_unstable}")
    print(f"TΔ (first COLLAPSE): {T_delta_collapse}")
    print()


if __name__ == "__main__":
    # Expected qualitative behavior:
    # r = 2.8 -> nearby trajectories remain close / stable
    # r = 3.2 -> medium divergence / transitional
    # r = 3.9 -> fast divergence / collapse of equivalence
    run_case("Stable regime", r=2.8)
    run_case("Oscillatory regime", r=3.2)
    run_case("Chaotic regime", r=3.9)