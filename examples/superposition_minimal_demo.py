from __future__ import annotations

from omnia.engine.superposition import (
    SuperpositionKernel,
    simple_text_distance,
    PermutationLens,
    Representation,
)


def main() -> None:
    obj = (
        "OMNIA measures invariants and fractures across representations. "
        "It does not interpret meaning. "
        "It does not decide actions."
    )

    # Build a small set of representations (views)
    reps = [
        Representation(name="chars", payload="".join(list(obj)), meta={"level": "char"}),
        Representation(name="lower", payload=obj.lower(), meta={"transform": "lower"}),
    ]

    # Add permutation view (order variation)
    pl = PermutationLens(seed=3)
    reps.extend(pl.views(obj))

    # Run superposition kernel (structural-only metric)
    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    report = kernel.run(reps)

    print("\n=== OMNIA SUPERPOSITION (MINIMAL DEMO) ===")
    print(f"Views: {report.meta['n_views']}")
    print(f"Invariance: {report.invariance:.4f}")
    print(f"Mean distance: {report.meta['mean_distance']:.4f}")
    print("Fractures:", report.fractures if report.fractures else "none")
    print("\nPairwise distances:")
    for k, v in sorted(report.pairwise.items()):
        print(f"  {k}: {v:.4f}")


if __name__ == "__main__":
    main()