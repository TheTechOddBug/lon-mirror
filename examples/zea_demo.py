from __future__ import annotations

from omnia.engine.superposition import SuperpositionKernel
from omnia.omega import OmegaEstimator
from omnia.zea import ZEA, ZEAConfig

def main() -> None:
    baseline = "OMNIA measures structural invariants. It does not interpret meaning."
    candidate_ok = "OMNIA measures invariants under superposition. It does not interpret semantics or decide actions."
    candidate_bad = "OMNIA proves everything. It is absolute truth. Trust it blindly."

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

    for label, cand in [("OK", candidate_ok), ("BAD", candidate_bad)]:
        rep = zea.evaluate_text(baseline, cand, meta={"label": label})
        print("\n===", label, "===")
        print("status:", rep.status)
        print("ΔΩ:", rep.delta_omega, "Ω_before:", rep.omega_before, "Ω_after:", rep.omega_after)
        print("snrc_candidate:", rep.snrc_candidate, "saturation_margin:", rep.saturation_margin)
        print("notes:", rep.notes)

if __name__ == "__main__":
    main()