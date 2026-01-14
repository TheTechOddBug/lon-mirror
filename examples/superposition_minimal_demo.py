from __future__ import annotations

from omnia.engine.superposition import (
    PermutationLens,
    Representation,
    SuperpositionKernel,
    simple_text_distance,
)


def main() -> None:
    obj = (
        "OMNIA measures invariants and fractures across representations. "
        "It does not interpret meaning. "
        "It does not decide actions."
    )

    # Build a small set of representations (views)
    reps = [
        Representation(name="orig", payload=obj, meta={"transform": "identity"}),
        Representation(name="lower", payload=obj.lower(), meta={"transform": "lower"}),
        Representation(name="chars", payload="".join(list(obj)), meta={"level": "char"}),
    ]

    # Add permutation view (order variation)
    pl = PermutationLens(seed=3)
    reps.extend(pl.views(obj))

    # De-duplicate by name (safety if lens already provides "orig")
    seen = set()
    unique_reps = []
    for r in reps:
        if r.name in seen:
            continue
        seen.add(r.name)
        unique_reps.append(r)

    # Run superposition kernel (structural-only metric)
    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    report = kernel.run(unique_reps)

    print("=== OMNIA SUPERPOSITION (MINIMAL DEMO) ===")
    print(f"Views: {report.meta.get('n_views', len(unique_reps))}")
    print(f"Invariance: {report.invariance:.4f}")
    print(f"Mean distance: {report.meta.get('mean_distance', 0.0):.4f}")
    print("Fractures:", report.fractures if report.fractures else "none")
    print("\nPairwise distances:")
    for k, v in sorted(report.pairwise.items()):
        print(f"  {k}: {v:.4f}")


if __name__ == "__main__":
    main()