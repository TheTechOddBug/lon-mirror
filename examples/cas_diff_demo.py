from __future__ import annotations

import os

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig
from omnia.generator import ConstrainedGenerator
from omnia.cas import CASBuilder
from omnia.cas_diff import CASDiff


def make_cas(baseline: str, rounds: int, top_k: int, out_path: str) -> None:
    omega = OmegaEstimator()
    zea = ZEA(
        omega=omega,
        kernel=SuperpositionKernel(),
        config=ZEAConfig(
            delta_omega_floor=0.0,
            saturated_margin_max=0.08,
            snrc_agg="max",
        ),
    )
    gen = ConstrainedGenerator(zea)
    res = gen.generate(
        baseline,
        rounds=rounds,
        top_k=top_k,
        meta={"demo": "cas_diff_demo"},
    )
    cas = CASBuilder()
    cert = cas.build(res, run_meta={"rounds": rounds, "top_k": top_k})
    cas.save(cert, out_path)
    print("saved:", out_path, "summary:", cert["summary"])


def main() -> None:
    baseline = "OMNIA measures structural invariants. It does not interpret meaning. It does not make decisions."

    p1 = "examples/cas_run_A.json"
    p2 = "examples/cas_run_B.json"

    # run A: più conservativa
    make_cas(baseline, rounds=1, top_k=4, out_path=p1)
    # run B: più esplorativa
    make_cas(baseline, rounds=2, top_k=8, out_path=p2)

    # compare
    from omnia.cas_diff import _load  # local helper

    a = _load(p1)
    b = _load(p2)

    diff = CASDiff().compare(a, b, meta={"name": "A→B"})
    out = "examples/cas_diff_report.json"
    CASDiff().save(diff, out)

    print("\nDIFF saved:", out)
    print("VERDICT:", diff["verdict"])
    print("DELTA:", diff["delta"])


if __name__ == "__main__":
    main()