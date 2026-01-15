from __future__ import annotations

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig
from omnia.generator import ConstrainedGenerator
from omnia.cas import CASBuilder


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
        meta={"demo": "zea_to_cas"},
    )

    cas = CASBuilder()
    cert = cas.build(
        res,
        run_meta={
            "name": "ZEA→CAS demo",
            "rounds": 2,
            "top_k": 6
        },
    )

    out_path = "examples/cas_output.json"
    cas.save(cert, out_path)

    print("CAS saved to:", out_path)
    print("\nSummary:", cert["summary"])


if __name__ == "__main__":
    main()