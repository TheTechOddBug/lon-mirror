import math
import random
from typing import Dict, List, Optional, Tuple


def logistic_map(x: float, r: float) -> float:
    return r * x * (1.0 - x)


def linear_map(x: float, a: float) -> float:
    return a * x


def evolve_logistic(x0: float, r: float, steps: int) -> List[float]:
    xs = [x0]
    x = x0
    for _ in range(steps - 1):
        x = logistic_map(x, r)
        xs.append(x)
    return xs


def evolve_linear(x0: float, a: float, steps: int) -> List[float]:
    xs = [x0]
    x = x0
    for _ in range(steps - 1):
        x = linear_map(x, a)
        xs.append(x)
    return xs


def random_series(seed: int, steps: int) -> List[float]:
    rng = random.Random(seed)
    return [rng.random() for _ in range(steps)]


def delta_series(xs1: List[float], xs2: List[float]) -> List[float]:
    return [abs(a - b) for a, b in zip(xs1, xs2)]


def find_tdelta(delta: List[float], threshold: float = 1e-6) -> Optional[int]:
    for i, d in enumerate(delta):
        if d > threshold:
            return i
    return None


def compute_iri(delta: List[float], threshold: float = 1e-6) -> float:
    if not delta:
        return 0.0
    count = sum(1 for d in delta if d > threshold)
    return count / len(delta)


def classify_regime(tdelta: Optional[int], iri: float) -> str:
    if tdelta is None and iri == 0.0:
        return "STABLE"
    if tdelta == 0 and iri > 0.9:
        return "IMMEDIATE COLLAPSE"
    if iri > 0.5:
        return "COLLAPSE"
    return "UNSTABLE"


def benchmark_logistic(r: float, x0: float, epsilon: float, steps: int) -> Tuple[Optional[int], float, str]:
    xs1 = evolve_logistic(x0, r, steps)
    xs2 = evolve_logistic(x0 + epsilon, r, steps)
    delta = delta_series(xs1, xs2)
    tdelta = find_tdelta(delta)
    iri = compute_iri(delta)
    regime = classify_regime(tdelta, iri)
    return tdelta, iri, regime


def benchmark_linear(a: float, x0: float, epsilon: float, steps: int) -> Tuple[Optional[int], float, str]:
    xs1 = evolve_linear(x0, a, steps)
    xs2 = evolve_linear(x0 + epsilon, a, steps)
    delta = delta_series(xs1, xs2)
    tdelta = find_tdelta(delta)
    iri = compute_iri(delta)
    regime = classify_regime(tdelta, iri)
    return tdelta, iri, regime


def benchmark_random(seed1: int, seed2: int, steps: int) -> Tuple[Optional[int], float, str]:
    xs1 = random_series(seed1, steps)
    xs2 = random_series(seed2, steps)
    delta = delta_series(xs1, xs2)
    tdelta = find_tdelta(delta)
    iri = compute_iri(delta)
    regime = classify_regime(tdelta, iri)
    return tdelta, iri, regime


def print_result(name: str, tdelta: Optional[int], iri: float, regime: str) -> None:
    print(f"System: {name}")
    print(f"TΔ: {tdelta}")
    print(f"IRI: {iri:.2f}")
    print(f"Regime: {regime}")
    print()


def main() -> None:
    x0 = 0.123456789
    epsilon = 1e-10
    steps = 128

    tdelta, iri, regime = benchmark_logistic(2.8, x0, epsilon, steps)
    print_result("logistic_r2.8", tdelta, iri, regime)

    tdelta, iri, regime = benchmark_logistic(3.2, x0, epsilon, steps)
    print_result("logistic_r3.2", tdelta, iri, regime)

    tdelta, iri, regime = benchmark_logistic(3.9, x0, epsilon, steps)
    print_result("logistic_r3.9", tdelta, iri, regime)

    tdelta, iri, regime = benchmark_linear(0.8, x0, epsilon, steps)
    print_result("linear_0.8", tdelta, iri, regime)

    tdelta, iri, regime = benchmark_random(1, 2, steps)
    print_result("random", tdelta, iri, regime)


if __name__ == "__main__":
    main()