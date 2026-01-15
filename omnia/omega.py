from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Protocol

from omnia.engine.superposition import Representation, SuperpositionKernel

# Optional integration points (keep Omega robust even if these functions evolve)
try:
    from omnia.sei import compute_sei  # type: ignore
except Exception:  # pragma: no cover
    compute_sei = None  # type: ignore

try:
    from omnia.irreversibility import compute_iri  # type: ignore
except Exception:  # pragma: no cover
    compute_iri = None  # type: ignore


class Lens(Protocol):
    id: str

    def views(self, obj: Any) -> List[Representation]:
        ...


@dataclass
class OmegaReport:
    """
    Ω̂ (Omega-hat) report for one estimation step.

    invariance: aggregate invariance score (0..1) from SuperpositionKernel
    delta_invariance: absolute change vs previous step (history[-1])
    fractures: list of view-pair keys where distance exceeds fracture threshold
    sei: optional saturation proxy (trend), if available
    iri: optional irreversibility proxy (trend), if available
    meta: deterministic metadata (view count, epsilon, etc.)
    """
    invariance: float
    delta_invariance: float
    fractures: List[str]
    sei: float
    iri: float
    meta: Dict[str, Any]


def _dedupe_reps_by_name(reps: List[Representation]) -> List[Representation]:
    seen = set()
    out: List[Representation] = []
    for r in reps:
        if r.name in seen:
            continue
        seen.add(r.name)
        out.append(r)
    return out


def _clamp01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x


class OmegaEstimator:
    """
    Omega-set estimator (Ω̂).

    Approximates the invariant residue by measuring what survives
    under superposition across independent representations (lenses).

    Design constraints:
    - deterministic
    - bounded
    - no semantics
    - post-hoc only
    """

    def __init__(
        self,
        kernel: SuperpositionKernel,
        epsilon: float = 1e-3,
        max_iters: int = 10,
        dedupe_views: bool = True,
    ):
        self.kernel = kernel
        self.epsilon = float(epsilon)
        self.max_iters = int(max_iters)
        self.dedupe_views = bool(dedupe_views)

    def estimate(
        self,
        obj: Any,
        lenses: Iterable[Lens],
        history: Optional[List[OmegaReport]] = None,
    ) -> OmegaReport:
        """
        One estimation step given a set of lenses.

        For iterative convergence, pass the accumulated `history`
        from previous steps.
        """
        history = history or []

        reps: List[Representation] = []
        for lens in lenses:
            reps.extend(lens.views(obj))

        if self.dedupe_views:
            reps = _dedupe_reps_by_name(reps)

        sp = self.kernel.run(reps)

        inv = _clamp01(float(sp.invariance))
        prev_inv = history[-1].invariance if history else inv
        delta_inv = abs(inv - prev_inv)

        # Optional SEI/IRI hooks (robust to missing/changed implementations)
        sei = 1.0
        if history and compute_sei is not None:
            try:
                sei = float(compute_sei(history, sp))  # type: ignore[arg-type]
            except Exception:
                sei = 1.0

        iri = 0.0
        if history and compute_iri is not None:
            try:
                iri = float(compute_iri(history, sp))  # type: ignore[arg-type]
            except Exception:
                iri = 0.0

        return OmegaReport(
            invariance=inv,
            delta_invariance=delta_inv,
            fractures=list(sp.fractures),
            sei=sei,
            iri=iri,
            meta={
                "n_views": int(sp.meta.get("n_views", len(reps))),
                "epsilon": self.epsilon,
                "max_iters": self.max_iters,
                "dedupe_views": self.dedupe_views,
            },
        )

    def converged(self, history: List[OmegaReport]) -> bool:
        """
        Convergence predicate: |inv_k - inv_{k-1}| < epsilon
        """
        if len(history) < 2:
            return False
        return abs(history[-1].invariance - history[-2].invariance) < self.epsilon