from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional, Tuple

# Reuse existing OMNIA pieces (already present in lon-mirror, per il tuo stato attuale)
from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.lenses.compression import CompressionLens
from omnia.lenses.permutation import PermutationLens
from omnia.lenses.constraints import ConstraintLens


class ZEAStatus(str, Enum):
    ADMISSIBLE = "ADMISSIBLE"
    SATURATED = "SATURATED"
    ILLEGITIMATE = "ILLEGITIMATE"


@dataclass(frozen=True)
class ZEAReport:
    status: ZEAStatus
    delta_omega: float
    omega_before: float
    omega_after: float
    snrc_candidate: bool
    saturation_margin: float
    notes: str
    details: Dict[str, Any]


@dataclass(frozen=True)
class ZEAConfig:
    # tolleranze numeriche
    eps: float = 1e-9

    # soglie: scegliere conservative
    # se ΔΩ < -delta_omega_floor -> illegittimo
    delta_omega_floor: float = 0.0

    # se vicino al bordo (margine piccolo) -> saturated
    # margine = 1 - snrc_pressure (definita sotto)
    saturated_margin_max: float = 0.08

    # come aggregare la “pressione SNRC” dalle lenti
    # max = più conservativo
    snrc_agg: str = "max"  # "max" | "mean"


class ZEA:
    """
    ZEA-CORE: misura dove è ammesso creare struttura senza oltrepassare i limiti.

    - Non genera contenuto.
    - Non interpreta semantica.
    - Classifica candidati in base a ΔΩ e pressione di saturazione (SNRC-like).
    """

    def __init__(
        self,
        omega: OmegaEstimator,
        kernel: Optional[SuperpositionKernel] = None,
        compression: Optional[CompressionLens] = None,
        permutation: Optional[PermutationLens] = None,
        constraints: Optional[ConstraintLens] = None,
        config: Optional[ZEAConfig] = None,
    ) -> None:
        self.omega = omega
        self.kernel = kernel or SuperpositionKernel()

        self.compression = compression or CompressionLens()
        self.permutation = permutation or PermutationLens()
        self.constraints = constraints or ConstraintLens()

        self.cfg = config or ZEAConfig()

    def evaluate_text(
        self,
        baseline_text: str,
        candidate_text: str,
        *,
        meta: Optional[Dict[str, Any]] = None,
    ) -> ZEAReport:
        meta = meta or {}

        # 1) Ω prima/dopo (stimato tramite OmegaEstimator già presente)
        omega_before = float(self.omega.estimate_from_text(baseline_text))
        omega_after = float(self.omega.estimate_from_text(candidate_text))
        delta_omega = omega_after - omega_before

        # 2) pressione di saturazione: quanto collassa sotto lenti
        # idea: misuriamo la robustezza del candidato sotto trasformazioni
        # e la confrontiamo con il baseline, per evitare “trucchetti” locali.
        snrc_pressure, pressure_details = self._snrc_pressure_pair(
            baseline_text, candidate_text
        )

        # 3) margine dal bordo: 1 = lontano, 0 = sul bordo
        saturation_margin = max(0.0, 1.0 - snrc_pressure)

        # 4) classificazione
        # illegittimo se riduce Ω oltre soglia o se pressione è estrema (collasso)
        if delta_omega < (self.cfg.delta_omega_floor - self.cfg.eps):
            status = ZEAStatus.ILLEGITIMATE
            notes = "ΔΩ < 0: candidate reduces invariant residue (structural regression)."
        elif snrc_pressure >= (1.0 - self.cfg.eps):
            status = ZEAStatus.ILLEGITIMATE
            notes = "SNRC pressure at max: candidate collapses under superposition (noise regime)."
        elif saturation_margin <= (self.cfg.saturated_margin_max + self.cfg.eps):
            status = ZEAStatus.SATURATED
            notes = "Near boundary: admissible but at saturation edge (high fragility)."
        else:
            status = ZEAStatus.ADMISSIBLE
            notes = "Within admissible expansion zone: ΔΩ non-negative and stable under lenses."

        snrc_candidate = status in (ZEAStatus.SATURATED, ZEAStatus.ILLEGITIMATE) and snrc_pressure > 0.5

        return ZEAReport(
            status=status,
            delta_omega=delta_omega,
            omega_before=omega_before,
            omega_after=omega_after,
            snrc_candidate=bool(snrc_candidate),
            saturation_margin=saturation_margin,
            notes=notes,
            details={
                "meta": meta,
                "snrc_pressure": snrc_pressure,
                "pressure_details": pressure_details,
            },
        )

    def _snrc_pressure_pair(self, baseline: str, candidate: str) -> Tuple[float, Dict[str, Any]]:
        """
        Costruisce una proxy di “pressione verso SNRC” misurando quanto la struttura
        è instabile sotto lenti (compression/permutation/constraints).

        Restituisce:
        - pressure in [0,1] (1 = collasso massimo)
        - dettagli per audit
        """
        # Applica lenti al testo e misura distanza (kernel distance) tra originale e trasformato.
        # Normalizziamo e confrontiamo baseline vs candidate.
        b_scores = self._lens_instability_scores(baseline)
        c_scores = self._lens_instability_scores(candidate)

        # pressioni relative: se candidate è più instabile del baseline, aumenta pressione
        rel = {}
        for k in c_scores.keys():
            b = b_scores[k]
            c = c_scores[k]
            # evitare divisioni
            denom = max(self.cfg.eps, (b + 1e-6))
            rel[k] = min(1.0, max(0.0, (c - b) / denom))

        if self.cfg.snrc_agg == "mean":
            pressure = sum(rel.values()) / max(1, len(rel))
        else:
            pressure = max(rel.values()) if rel else 0.0

        details = {
            "baseline_scores": b_scores,
            "candidate_scores": c_scores,
            "relative_pressure": rel,
            "agg": self.cfg.snrc_agg,
        }
        return float(pressure), details

    def _lens_instability_scores(self, text: str) -> Dict[str, float]:
        """
        Per ogni lente:
        - genera una variante trasformata
        - misura distanza kernel (0 = identico, 1 = molto diverso) con clamp
        """
        # Nota: usiamo kernel interno; se già hai simple_text_distance nel kernel,
        # qui rimane compatibile.
        comp = self.compression.apply(text)
        perm = self.permutation.apply(text)
        cons = self.constraints.apply(text)

        def d(a: str, b: str) -> float:
            # distanza normalizzata, clamp in [0,1]
            val = float(self.kernel.distance(a, b))
            if val != val:  # NaN guard
                val = 1.0
            return max(0.0, min(1.0, val))

        return {
            "compression": d(text, comp),
            "permutation": d(text, perm),
            "constraints": d(text, cons),
        }