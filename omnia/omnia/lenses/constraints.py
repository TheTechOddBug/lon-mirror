from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

from omnia.engine.superposition import Representation


@dataclass(frozen=True)
class ConstraintLens:
    """
    Constraint Lens

    Applies deterministic constraints to the same object.
    Measures whether structure survives under restriction.

    This lens produces views only. It does not score, decide, or interpret.
    """
    id: str = "constraints"
    max_len: int = 64

    def views(self, obj: Any) -> List[Representation]:
        text = str(obj)

        reps: List[Representation] = [
            Representation(name="orig", payload=text, meta={"transform": "identity"})
        ]

        reps.append(
            Representation(
                name=f"len_cap_{self.max_len}",
                payload=text[: self.max_len],
                meta={"max_len": self.max_len, "constraint": "truncate"},
            )
        )

        reps.append(
            Representation(
                name="no_whitespace",
                payload="".join(text.split()),
                meta={"constraint": "strip_whitespace"},
            )
        )

        return reps