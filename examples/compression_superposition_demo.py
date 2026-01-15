from __future__ import annotations

from omnia.engine.superposition import (
    SuperpositionKernel,
    simple_text_distance,
)
from omnia.lenses.compression import CompressionLens
from omnia.engine.superposition import Representation


def main() -> None:
    obj = (
        "OMNIA measures structure, not meaning. "
        "Compression tests whether structure survives reduction. "
        "If invariance collapses, the property was not structural."
    )

    # Generate compression-based views
    lens = CompressionLens(summary_k=64)
    reps = lens.views(obj)

    # Run superposition
    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    report = kernel.run(reps)

    print("=== OMNIA COMPRESSION SUPERPOSITION DEMO ===")
    print(f"Views: {report.meta['n_views']}")
    print(f"Invariance: {report.invariance:.4f}")
    print(f"Mean distance: {report.meta['mean_distance']:.4f}")
    print("Fractures:", report.fractures if report.fractures else "none")

    print("\nPairwise distances:")
    for k, v in sorted(report.pairwise.items()):
        print(f"  {k}: {v:.4f}")

    print("\nView details:")
    for r in reps:
        size = (
            len(r.payload)
            if isinstance(r.payload, (str, bytes))
            else 1
        )
        print(f"  {r.name:12s} | size={size} | meta={r.meta}")


if __name__ == "__main__":
    main(