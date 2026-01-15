from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

from omnia.engine.superposition import Representation


@dataclass(frozen=True)
class PermutationLens:
    """
    Permutation Lens

    Generates deterministic order-variant representations.
    Used to detect order-dependence and rhetorical structure.
    """
    id: str = "permutation"
    seed: int = 0

    def views(self, obj: Any) -> List[Representation]:
        text = str(obj)
        parts = [p.strip() for p in text.split(".") if p.strip()]

        reps: List[Representation] = [
            Representation(name="orig", payload=text, meta={})
        ]

        if len(parts) < 2:
            return reps

        idx = list(range(len(parts)))
        x = (self.seed + 1) & 0x7FFFFFFF
        for k in range(len(idx) - 1, 0, -1):
            x = (1103515245 * x + 12345) & 0x7FFFFFFF
            r = x % (k + 1)
            idx[k], idx[r] = idx[r], idx[k]

        permuted = ". ".join(parts[i] for i in idx) + "."
        reps.append(
            Representation(
                name=f"perm_seed_{self.seed}",
                payload=permuted,
                meta={"seed": self.seed, "n_parts": len(parts)},
            )
        )
        return reps