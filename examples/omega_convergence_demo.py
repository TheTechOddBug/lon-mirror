from omnia.engine.superposition import SuperpositionKernel, simple_text_distance
from omnia.lenses.compression import CompressionLens
from omnia.lenses.permutation import PermutationLens
from omnia.lenses.constraints import ConstraintLens
from omnia.omega import OmegaEstimator

def main() -> None:
    obj = (
        "OMNIA measures what survives all representations. "
        "What collapses was never structural."
    )

    kernel = SuperpositionKernel(metric=simple_text_distance, fracture_threshold=0.5)
    omega_est = OmegaEstimator(kernel=kernel, epsilon=1e-3, max_iters=5)

    lens_sets = [
        [CompressionLens(summary_k=64)],
        [CompressionLens(summary_k=64), PermutationLens(seed=1)],
        [CompressionLens(summary_k=64), PermutationLens(seed=1), ConstraintLens(max_len=48)],
    ]

    history = []
    for i, lenses in enumerate(lens_sets, start=1):
        omega = omega_est.estimate(obj, lenses, history)
        history.append(omega)
        print(f"\n--- Ω̂ iteration {i} ---")
        print(f"Invariance: {omega.invariance:.4f}")
        print(f"Δ Invariance: {omega.delta_invariance:.6f}")
        print(f"SEI: {omega.sei:.4f}")
        print(f"IRI: {omega.iri:.4f}")
        print(f"Fractures: {omega.fractures if omega.fractures else 'none'}")

if __name__ == "__main__":
    main()