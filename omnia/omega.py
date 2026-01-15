from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, List, Dict

from omnia.engine.superposition import SuperpositionKernel, Representation
from omnia.sei import compute_sei  # usa il tuo SEI esistente
from omnia.irreversibility import compute_iri  # usa il tuo IRI esistente


@dataclass
class OmegaReport:
    invariance: float
    delta_invariance: float
    fractures: List[str]
    sei: float
    iri: float
    meta: Dict[str, Any]


class OmegaEstimator:
    """
    Omega-set estimator.

    Approximates the invariant residual (Ω̂) by iterative superposition
    and convergence under expanding independent lenses.
    """

    def __init__(
        self,
        kernel: SuperpositionKernel,
        epsilon: float = 1e-3,
        max_iters: int = 10,
    ):
        self.kernel = kernel
        self.epsilon = epsilon
        self.max_iters = max_iters

    def estimate(
        self,
        obj: Any,
        lenses: Iterable[Any],  # lenses with .views(obj) -> List[Representation]
        history: List[OmegaReport] | None = None,
    ) -> OmegaReport:
        history = history or []

        reps: List[Representation] = []
        for lens in lenses:
            reps.extend(lens.views(obj))

        report = self.kernel.run(reps)

        prev_inv = history[-1].invariance if history else report.invariance
        delta_inv = abs(report.invariance - prev_inv)

        sei = compute_sei(history, report) if history else 1.0
        iri = compute_iri(history, report) if history else 0.0

        omega = OmegaReport(
            invariance=report.invariance,
            delta_invariance=delta_inv,
            fractures=report.fractures,
            sei=sei,
            iri=iri,
            meta={
                "n_views": report.meta.get("n_views", len(reps)),
                "epsilon": self.epsilon,
            },
        )

        return omega