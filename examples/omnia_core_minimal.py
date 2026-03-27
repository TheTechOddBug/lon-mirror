import math
from typing import Callable, List
import numpy as np

EPS = 1e-12

Vector = np.ndarray
Transform = Callable[[object], object]
Lens = Callable[[object], Vector]


def cosine(a: Vector, b: Vector) -> float:
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na < EPS or nb < EPS:
        return 0.0
    return float(np.dot(a, b) / (na * nb))


def lens_dispersion(x, transforms: List[Transform], lens: Lens):
    zs = [np.asarray(lens(t(x)), dtype=float) for t in transforms]
    C = np.mean(zs, axis=0)
    denom = float(np.linalg.norm(C) ** 2 + EPS)
    D = float(np.mean([np.linalg.norm(z - C) ** 2 / denom for z in zs]))
    I = math.exp(-D)
    return {
        "vectors": zs,
        "centroid": C,
        "dispersion": D,
        "invariance": I,
    }


def omnia_core(x, transforms: List[Transform], lenses: List[Lens]):
    lens_states = [lens_dispersion(x, transforms, lens) for lens in lenses]

    omega = float(np.mean([s["invariance"] for s in lens_states]))

    centroids = [s["centroid"] for s in lens_states]
    pairwise = []
    for i in range(len(centroids)):
        for j in range(i + 1, len(centroids)):
            pairwise.append(cosine(centroids[i], centroids[j]))
    sci = float(np.mean(pairwise)) if pairwise else 1.0

    truth_omega = omega * max(0.0, sci)

    return {
        "omega": omega,
        "sci": sci,
        "truth_omega": truth_omega,
        "lenses": lens_states,
    }


def iri(c_a: Vector, c_b: Vector, c_a2: Vector) -> float:
    num = np.linalg.norm(c_a - c_a2)
    den = np.linalg.norm(c_a - c_b) + EPS
    return float(num / den)


def sei(prev_omega: float, curr_omega: float, prev_cost: float, curr_cost: float) -> float:
    return float((curr_omega - prev_omega) / (curr_cost - prev_cost + EPS))


def should_stop(omega: float, sci: float, sei_value: float,
                tau_omega: float = 0.35,
                tau_sci: float = 0.20,
                tau_sei: float = 0.00) -> bool:
    return (omega < tau_omega) or (sci < tau_sci) or (sei_value <= tau_sei)