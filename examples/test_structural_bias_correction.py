from omnia.structural_bias_correction import StructuralBiasCorrection


def main() -> None:
    numbers = [1009, 2047, 30031, 1000001]
    omega_raw_values = [0.931220, 0.932120, 0.941200, 0.948210]

    sbc = StructuralBiasCorrection(lambda_value=0.03)
    results = sbc.apply_to_batch(
        numbers=numbers,
        omega_raw_values=omega_raw_values,
    )

    print("=== STRUCTURAL BIAS CORRECTION SMOKE TEST ===")
    print(
        f"{'n':>9} | {'omega_raw':>10} | {'pen_raw':>10} | "
        f"{'pen_norm':>10} | {'omega_adj':>10} | {'avg_entropy':>11}"
    )
    print("-" * 78)

    for n, result in zip(numbers, results):
        print(
            f"{n:9d} | "
            f"{result.omega_raw:10.6f} | "
            f"{result.bias_penalty_raw:10.6f} | "
            f"{result.bias_penalty_norm:10.6f} | "
            f"{result.omega_adjusted:10.6f} | "
            f"{result.features.avg_entropy:11.6f}"
        )


if __name__ == "__main__":
    main()