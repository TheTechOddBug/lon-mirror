from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class CASDiffConfig:
    eps: float = 1e-9
    # soglie conservative per decidere progress/regress
    min_count_delta: int = 1
    min_margin_delta: float = 0.02
    min_delta_omega_delta: float = 0.0  # >=0 non peggiora

    # confronto "loop": se firma aggregata cambia poco => giro in tondo
    loop_tol: float = 0.02


def _safe_mean(xs: List[float], default: float = 0.0) -> float:
    if not xs:
        return default
    return sum(xs) / len(xs)


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def _load(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _bucket(cert: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return list(cert.get("buckets", {}).get(name, []) or [])


def _stats(cert: Dict[str, Any]) -> Dict[str, Any]:
    acc = _bucket(cert, "accepted")
    sat = _bucket(cert, "saturated")
    rej = _bucket(cert, "rejected")

    def extract(items, key):
        out = []
        for it in items:
            v = it.get(key, None)
            if isinstance(v, (int, float)) and not (isinstance(v, float) and math.isnan(v)):
                out.append(float(v))
        return out

    # preferiamo stats su accepted; se vuoto, usiamo saturated come segnali di bordo
    acc_margins = extract(acc, "saturation_margin")
    sat_margins = extract(sat, "saturation_margin")
    rej_margins = extract(rej, "saturation_margin")

    acc_domega = extract(acc, "delta_omega")
    sat_domega = extract(sat, "delta_omega")
    rej_domega = extract(rej, "delta_omega")

    # pressione SNRC è in details.snrc_pressure (se presente)
    def snrc_pressure(items):
        out = []
        for it in items:
            d = it.get("details", {}) or {}
            p = d.get("snrc_pressure", None)
            if isinstance(p, (int, float)) and not (isinstance(p, float) and math.isnan(p)):
                out.append(float(p))
        return out

    acc_snrc = snrc_pressure(acc)
    sat_snrc = snrc_pressure(sat)
    rej_snrc = snrc_pressure(rej)

    return {
        "counts": {
            "accepted": len(acc),
            "saturated": len(sat),
            "rejected": len(rej),
        },
        "accepted": {
            "mean_margin": _safe_mean(acc_margins, 0.0),
            "min_margin": min(acc_margins) if acc_margins else 0.0,
            "mean_delta_omega": _safe_mean(acc_domega, 0.0),
            "min_delta_omega": min(acc_domega) if acc_domega else 0.0,
            "mean_snrc_pressure": _safe_mean(acc_snrc, 0.0),
        },
        "saturated": {
            "mean_margin": _safe_mean(sat_margins, 0.0),
            "mean_delta_omega": _safe_mean(sat_domega, 0.0),
            "mean_snrc_pressure": _safe_mean(sat_snrc, 0.0),
        },
        "rejected": {
            "mean_margin": _safe_mean(rej_margins, 0.0),
            "mean_delta_omega": _safe_mean(rej_domega, 0.0),
            "mean_snrc_pressure": _safe_mean(rej_snrc, 0.0),
        },
        # firma aggregata semplice (per loop detection)
        "signature": {
            "acc_rate": 0.0,
            "sat_rate": 0.0,
            "rej_rate": 0.0,
            "acc_mean_margin": _safe_mean(acc_margins, 0.0),
            "acc_mean_domega": _safe_mean(acc_domega, 0.0),
            "acc_mean_snrc": _safe_mean(acc_snrc, 0.0),
        },
    }


def _signature_finalize(stats: Dict[str, Any]) -> Dict[str, float]:
    c = stats["counts"]
    total = max(1, c["accepted"] + c["saturated"] + c["rejected"])
    sig = stats["signature"]
    sig["acc_rate"] = c["accepted"] / total
    sig["sat_rate"] = c["saturated"] / total
    sig["rej_rate"] = c["rejected"] / total
    # clamp safe
    for k, v in list(sig.items()):
        if isinstance(v, (int, float)):
            sig[k] = float(v)
    return sig


def _sig_distance(a: Dict[str, float], b: Dict[str, float]) -> float:
    # distanza L1 normalizzata su chiavi comuni
    keys = sorted(set(a.keys()) | set(b.keys()))
    if not keys:
        return 0.0
    s = 0.0
    for k in keys:
        s += abs(float(a.get(k, 0.0)) - float(b.get(k, 0.0)))
    return s / len(keys)


class CASDiff:
    def __init__(self, config: Optional[CASDiffConfig] = None) -> None:
        self.cfg = config or CASDiffConfig()

    def compare(self, a: Dict[str, Any], b: Dict[str, Any], *, meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        a = older, b = newer
        """
        meta = meta or {}

        sa = _stats(a)
        sb = _stats(b)
        siga = _signature_finalize(sa)
        sigb = _signature_finalize(sb)

        # deltas
        da = sa["counts"]["accepted"]
        db = sb["counts"]["accepted"]
        delta_acc = db - da

        delta_margin = sb["accepted"]["mean_margin"] - sa["accepted"]["mean_margin"]
        delta_domega = sb["accepted"]["mean_delta_omega"] - sa["accepted"]["mean_delta_omega"]
        delta_snrc = sb["accepted"]["mean_snrc_pressure"] - sa["accepted"]["mean_snrc_pressure"]

        # decisione: progress / regress / stall
        verdict = "STALL"
        reason = "no_significant_change"

        # regressione: meno accepted o margini peggiori o ΔΩ peggiora
        if (delta_acc <= -self.cfg.min_count_delta) or (delta_margin <= -self.cfg.min_margin_delta) or (delta_domega < -self.cfg.eps):
            verdict = "REGRESSION"
            reason = "accepted_down_or_margin_down_or_delta_omega_down"
        # progresso: più accepted e margini migliori e ΔΩ non peggiora
        elif (delta_acc >= self.cfg.min_count_delta) and (delta_margin >= self.cfg.min_margin_delta) and (delta_domega >= -self.cfg.eps):
            verdict = "PROGRESS"
            reason = "accepted_up_and_margin_up_and_delta_omega_not_down"

        # loop detection: firma quasi uguale nonostante nuove varianti
        sig_dist = _sig_distance(siga, sigb)
        loop_like = sig_dist <= self.cfg.loop_tol

        return {
            "schema": "CAS-DIFF-1.0",
            "timestamp_utc": b.get("timestamp_utc", None),
            "meta": meta,
            "a": {
                "timestamp_utc": a.get("timestamp_utc", None),
                "summary": a.get("summary", {}),
                "stats": sa,
                "signature": siga,
            },
            "b": {
                "timestamp_utc": b.get("timestamp_utc", None),
                "summary": b.get("summary", {}),
                "stats": sb,
                "signature": sigb,
            },
            "delta": {
                "accepted": delta_acc,
                "accepted_mean_margin": delta_margin,
                "accepted_mean_delta_omega": delta_domega,
                "accepted_mean_snrc_pressure": delta_snrc,
                "signature_distance": sig_dist,
                "loop_like": loop_like,
            },
            "verdict": {
                "label": verdict,
                "reason": reason,
                "loop_warning": loop_like,
            },
        }

    def save(self, report: Dict[str, Any], path: str, *, indent: int = 2) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=indent)