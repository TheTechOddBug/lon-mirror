from omnia.engine.superposition import (
    SuperpositionKernel,
    simple_text_distance,
)
from omnia.lenses.compression import CompressionLens
from omnia.lenses.permutation import PermutationLens
from omnia.lenses.constraints import ConstraintLens


def main() -> None:
    obj = (
        "OMNIA measures structure only. "
        "If structure collapses under transformation, "
        "it was never fundamental."
    )

    reps = []

    reps.extend(CompressionLens(summary_k=64).views(obj))
    reps.extend(PermutationLens(seed=2).views(obj))
    reps.extend(ConstraintLens(max_len=48).views(obj))

    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    report = kernel.run(reps)

    print("=== OMNIA MULTI-LENS SUPERPOSITION ===")
    print(f"Views: {report.meta['n_views']}")
    print(f"Invariance: {report.invariance:.4f}")
    print("Fractures:", report.fractures if report.fractures else "none")


if __name__ == "__main__":
    main()