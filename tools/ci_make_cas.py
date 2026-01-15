from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig
from omnia.generator import ConstrainedGenerator
from omnia.cas import CASBuilder


DEFAULT_BASELINE = (
    "OMNIA measures structural invariants. "
    "It does not interpret meaning. "
    "It does not make decisions."
)


def _stable_hint(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:10]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Output CAS path (json)")
    ap.add_argument("--baseline", default=DEFAULT_BASELINE, help="Baseline text for CAS generation")
    ap.add_argument("--rounds", type=int, default=2)
    ap.add_argument("--top_k", type=int, default=8)

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

    gen = ConstrainedGenerator(zea)
    res = gen.generate(
        args.baseline,
        rounds=args.rounds,
        top_k=args.top_k,
        meta={"ci": True, "rounds": args.rounds, "top_k": args.top_k},
    )

    cas = CASBuilder()
    cert = cas.build(
        res,
        run_meta={
            "ci": True,
            "baseline_hash_hint": _stable_hint(args.baseline),
            "rounds": args.rounds,
            "top_k": args.top_k,
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
    print("Summary:", cert["summary"])


if __name__ == "__main__":
    main(