from omnia.engine import run_omnia_totale


def test_adapter() -> None:
    # Test 1: numeric context present -> SBC should attach
    n_test = 1000001
    extra_with_n = {"n": n_test}
    result_with_sbc = run_omnia_totale(extra=extra_with_n)

    print("=== TEST 1: NUMERIC CONTEXT PRESENT ===")
    print(f"n: {n_test}")
    print(f"omega_total (legacy):  {result_with_sbc.omega_total:.6f}")
    print(f"omega_raw (explicit):  {result_with_sbc.omega_raw:.6f}")
    print(f"omega_adjusted (SBC):  {result_with_sbc.omega_adjusted:.6f}")

    if result_with_sbc.structural_bias_meta is not None:
        meta = result_with_sbc.structural_bias_meta
        print(
            f"SBC Meta -> pen_raw: {meta.bias_penalty_raw:.6f} | "
            f"pen_norm: {meta.bias_penalty_norm:.6f} | "
            f"lambda: {meta.lambda_value:.6f}"
        )

    assert result_with_sbc.omega_total == result_with_sbc.omega_raw
    assert result_with_sbc.omega_adjusted <= result_with_sbc.omega_raw
    assert result_with_sbc.structural_bias_meta is not None

    print("STATUS: SUCCESS (SBC properly attached)\n")

    # Test 2: numeric context absent -> legacy behavior only
    result_legacy = run_omnia_totale(extra={})

    print("=== TEST 2: NUMERIC CONTEXT ABSENT ===")
    print(f"omega_total:           {result_legacy.omega_total:.6f}")
    print(f"omega_raw:             {result_legacy.omega_raw:.6f}")
    print(f"omega_adjusted:        {result_legacy.omega_adjusted:.6f}")
    print(f"structural_bias_meta:  {result_legacy.structural_bias_meta}")

    assert result_legacy.structural_bias_meta is None
    assert result_legacy.omega_total == result_legacy.omega_raw
    assert result_legacy.omega_adjusted == result_legacy.omega_raw

    print("STATUS: SUCCESS (Legacy fallback maintained)")


if __name__ == "__main__":
    test_adapter()