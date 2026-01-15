from __future__ import annotations

import gzip
import hashlib
from dataclasses import dataclass
from typing import Any, Dict, List

from omnia.engine.superposition import Representation


@dataclass(frozen=True)
class CompressionLens:
    """
    Compression Lens

    Generates multiple compressed representations of the same object.
    The goal is not efficiency, but structural survivability under compression.

    This lens produces deterministic views only.
    """
    id: str = "compression"
    summary_k: int = 128  # naive summary length (chars)

    def _to_text(self, obj: Any) -> str:
        return str(obj)

    def _summary(self, text: str) -> str:
        # Deterministic truncation summary (no semantics)
        if len(text) <= self.summary_k:
            return text
        return text[: self.summary_k]

    def _gzip_bytes(self, text: str) -> bytes:
        return gzip.compress(text.encode("utf-8"))

    def _sha256(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def views(self, obj: Any) -> List[Representation]:
        text = self._to_text(obj)

        reps: List[Representation] = []

        reps.append(
            Representation(
                name="orig",
                payload=text,
                meta={"transform": "identity"},
            )
        )

        reps.append(
            Representation(
                name=f"summary_{self.summary_k}",
                payload=self._summary(text),
                meta={"k": self.summary_k, "method": "truncate"},
            )
        )

        gz = self._gzip_bytes(text)
        reps.append(
            Representation(
                name="gzip_bytes",
                payload=gz,
                meta={"bytes": len(gz)},
            )
        )

        reps.append(
            Representation(
                name="sha256",
                payload=self._sha256(text),
                meta={"hash": "sha256"},
            )
        )

        return reps