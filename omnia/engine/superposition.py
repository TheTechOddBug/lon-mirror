from dataclasses import dataclass
from typing import Any, Dict, List, Protocol, Callable

@dataclass(frozen=True)
class Representation:
    name: str                 # es: "base_2", "base_16", "chars", "subwords", "perm_3"
    payload: Any              # vista concreta (stringa, lista, numeri, grafi, ecc.)
    meta: Dict[str, Any]      # parametri che l'hanno generata (base, tokenizer, perm seed...)

class Lens(Protocol):
    id: str
    def views(self, obj: Any) -> List[Representation]: ...

Metric = Callable[[Representation, Representation], float]

@dataclass
class SuperpositionReport:
    pairwise: Dict[str, float]     # distanze tra viste
    invariance: float              # 0..1
    fractures: List[str]           # coppie/aree dove collassa
    meta: Dict[str, Any]

class SuperpositionKernel:
    def __init__(self, metric: Metric):
        self.metric = metric

    def run(self, reps: List[Representation]) -> SuperpositionReport:
        pairwise = {}
        scores = []
        fractures = []
        for i in range(len(reps)):
            for j in range(i+1, len(reps)):
                key = f"{reps[i].name}__{reps[j].name}"
                d = self.metric(reps[i], reps[j])
                pairwise[key] = d
                scores.append(d)
                if d > 0.5:  # soglia iniziale; poi la leghi a ICE/OMNIA-LIMIT
                    fractures.append(key)

        # invariance alta = distanze basse
        # normalizzazione minimale: inv = 1 - clamp(mean(d), 0, 1)
        mean_d = sum(scores)/len(scores) if scores else 0.0
        inv = max(0.0, min(1.0, 1.0 - mean_d))

        return SuperpositionReport(
            pairwise=pairwise,
            invariance=inv,
            fractures=fractures,
            meta={"n_views": len(reps)}
        )