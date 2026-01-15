from __future__ import annotations

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig
from omnia.generator import ConstrainedGenerator


def main() -> None:
    baseline = "OMNIA measures structural invariants. It does not interpret meaning. It does not make decisions."

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
        rounds=2,
        top_k=6,
        meta={"demo": "zea_constrained_generation"},
    )

    print("\nBASELINE:\n", res.baseline)

    def show(title, items, limit=8):
        print(f"\n{title} ({len(items)}):")
        for i, (cand, rep) in enumerate(items[:limit], start=1):
            print(f"\n[{i}] op={cand.op} status={rep.status} ΔΩ={rep.delta_omega:.6f} margin={rep.saturation_margin:.6f}")
            print(cand.text)

    show("ACCEPTED", res.accepted)
    show("SATURATED", res.saturated)
    show("REJECTED", res.rejected)


if __name__ == "__main__":
    main()