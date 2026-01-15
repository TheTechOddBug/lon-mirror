from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from omnia.generator import GenerationResult, Candidate
from omnia.zea import ZEAReport


@dataclass(frozen=True)
class CASConfig:
    schema_version: str = "CAS-1.0"
    engine: str = "OMNIA"
    artifact: str = "CAS"
    # quante entry includere nel certificato (per non esplodere)
    max_items_per_bucket: int = 25


def _iso_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _pack_item(cand: Candidate, rep: ZEAReport) -> Dict[str, Any]:
    return {
        "op": cand.op,
        "text": cand.text,
        "delta_omega": rep.delta_omega,
        "omega_before": rep.omega_before,
        "omega_after": rep.omega_after,
        "snrc_candidate": rep.snrc_candidate,
        "saturation_margin": rep.saturation_margin,
        "notes": rep.notes,
        "details": rep.details,
    }


class CASBuilder:
    """
    CAS: certificato di arresto/ammissibilità strutturale.
    - Non spiega il contenuto.
    - Congela lo stato: dove è ammesso, dove è saturo, dove è illegittimo.
    """

    def __init__(self, config: Optional[CASConfig] = None) -> None:
        self.cfg = config or CASConfig()

    def build(
        self,
        result: GenerationResult,
        *,
        run_meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        run_meta = run_meta or {}

        acc = [_pack_item(c, r) for (c, r) in result.accepted[: self.cfg.max_items_per_bucket]]
        sat = [_pack_item(c, r) for (c, r) in result.saturated[: self.cfg.max_items_per_bucket]]
        rej = [_pack_item(c, r) for (c, r) in result.rejected[: self.cfg.max_items_per_bucket]]

        # stato globale: se esiste almeno un SATURATED e nessun ACCEPTED, la run è al bordo
        # se nessun ACCEPTED e molti REJECTED, siamo in regime rumore
        status = "OPEN"
        if len(result.accepted) == 0 and len(result.saturated) > 0:
            status = "SATURATED"
        if len(result.accepted) == 0 and len(result.saturated) == 0:
            status = "ILLEGITIMATE"

        # derive un “stop recommendation” duro
        stop = False
        stop_reason = "continue"
        if status in ("SATURATED", "ILLEGITIMATE"):
            stop = True
            stop_reason = "structural_saturation" if status == "SATURATED" else "noise_regime"

        payload: Dict[str, Any] = {
            "schema": self.cfg.schema_version,
            "engine": self.cfg.engine,
            "artifact": self.cfg.artifact,
            "timestamp_utc": _iso_utc_now(),
            "run_meta": run_meta,
            "baseline": {"text": result.baseline},
            "summary": {
                "status": status,
                "stop_recommended": stop,
                "stop_reason": stop_reason,
                "counts": {
                    "accepted": len(result.accepted),
                    "saturated": len(result.saturated),
                    "rejected": len(result.rejected),
                },
            },
            "buckets": {
                "accepted": acc,
                "saturated": sat,
                "rejected": rej,
            },
        }

        return payload

    def to_json(self, cert: Dict[str, Any], *, indent: int = 2) -> str:
        return json.dumps(cert, ensure_ascii=False, indent=indent, sort_keys=False)

    def save(self, cert: Dict[str, Any], path: str, *, indent: int = 2) -> None:
        s = self.to_json(cert, indent=indent)
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)