from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Any, Dict, List, Optional

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig
from omnia.generator import Candidate, GenerationResult
from omnia.cas import CASBuilder


DEFAULT_BASELINE = (
    "OMNIA measures structural invariants. "
    "It does not interpret meaning. "
    "It does not make decisions."
)

AUTO_FIELDS = [
    "output",
    "completion",
    "response",
    "text",
    "answer",
    "prediction",
    "model_output",
    "final",
    "raw",
    "response.output_text",
    "response.text",
    "choices.0.text",
    "choices.0.message.content",
    "message.content",
]


def _stable_hint(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:10]


def _load_jsonl(path: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def _get_dotted(obj: Any, dotted: str) -> Any:
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, list):
            try:
                idx = int(part)
            except ValueError:
                return None
            if idx < 0 or idx >= len(cur):
                return None
            cur = cur[idx]
            continue
        if isinstance(cur, dict):
            if part not in cur:
                return None
            cur = cur[part]
            continue
        return None
    return cur


def _extract_text(rec: Dict[str, Any], field: Optional[str]) -> Optional[str]:
    if field:
        v = _get_dotted(rec, field)
        if isinstance(v, str) and v.strip():
            return v.strip()

    for f in AUTO_FIELDS:
        v = _get_dotted(rec, f)
        if isinstance(v, str) and v.strip():
            return v.strip()

    for v in rec.values():
        if isinstance(v, str) and len(v.strip()) >= 8:
            return v.strip()

    return None


def _sample_records(recs: List[Dict[str, Any]], limit: Optional[int], seed: int) -> List[Dict[str, Any]]:
    if limit is None or limit >= len(recs):
        return recs
    rng = random.Random(seed)
    idxs = list(range(len(recs)))
    rng.shuffle(idxs)
    idxs = idxs[:limit]
    return [recs[i] for i in idxs]


def main() -> None:
    ap = argparse.ArgumentParser()

    ap.add_argument("--out", required=True, help="Output CAS path (json)")
    ap.add_argument("--jsonl", required=True, help="Path to JSONL dataset (LLM outputs)")

    ap.add_argument("--baseline", default=DEFAULT_BASELINE, help="Baseline text reference for ZEA")
    ap.add_argument("--field", default=None, help="Dotted field path to extract text from record (optional)")
    ap.add_argument("--limit", type=int, default=200, help="Sample N records deterministically")
    ap.add_argument("--seed", type=int, default=7, help="Sampling seed")

    # ZEA config
    ap.add_argument("--delta_omega_floor", type=float, default=0.0)
    ap.add_argument("--saturated_margin_max", type=float, default=0.08)
    ap.add_argument("--snrc_agg", choices=["max", "mean"], default="max")

    args = ap.parse_args()

    omega = OmegaEstimator()
    zea = ZEA(
        omega=omega,
        kernel=SuperpositionKernel(),
        config=ZEAConfig(
            delta_omega_floor=args.delta_omega_floor,
            saturated_margin_max=args.saturated_margin_max,
            snrc_agg=args.snrc_agg,
        ),
    )

    baseline = args.baseline

    recs = _load_jsonl(args.jsonl)
    recs = _sample_records(recs, args.limit, args.seed)

    accepted = []
    saturated = []
    rejected = []

    kept = 0
    skipped = 0

    for i, rec in enumerate(recs):
        txt = _extract_text(rec, args.field)
        if not txt:
            skipped += 1
            continue

        rep = zea.evaluate_text(baseline, txt, meta={"mode": "jsonl", "i": i})
        cand = Candidate(text=txt, op="jsonl_record", meta={"i": i})

        if rep.status.value == "ADMISSIBLE":
            accepted.append((cand, rep))
        elif rep.status.value == "SATURATED":
            saturated.append((cand, rep))
        else:
            rejected.append((cand, rep))

        kept += 1

    res = GenerationResult(
        baseline=baseline,
        accepted=accepted,
        saturated=saturated,
        rejected=rejected,
    )

    cas = CASBuilder()
    cert = cas.build(
        res,
        run_meta={
            "ci": True,
            "mode": "jsonl",
            "jsonl_path": args.jsonl,
            "field": args.field,
            "limit": args.limit,
            "seed": args.seed,
            "kept": kept,
            "skipped": skipped,
            "baseline_hash_hint": _stable_hint(baseline),
            "zea": {
                "delta_omega_floor": args.delta_omega_floor,
                "saturated_margin_max": args.saturated_margin_max,
                "snrc_agg": args.snrc_agg,
            },
        },
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cas.save(cert, str(out))

    print("CAS written:", out)
    print("Mode: jsonl")
    print("kept:", kept, "skipped:", skipped)
    print("Summary:", cert["summary"])


if __name__ == "__main__":
    main()