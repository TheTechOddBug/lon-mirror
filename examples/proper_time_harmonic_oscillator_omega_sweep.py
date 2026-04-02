import numpy as np

# ==========================================
# PROPER-TIME HARMONIC OSCILLATOR
# omega sweep at fixed k
# ==========================================

K = 0.05
A = 1.0
PHI = 0.3
TAU_MAX = 20.0
N_CONT = 5000

OMEGAS = np.linspace(0.2, 20.0, 60)


def x_continuous(tau, omega):
    return A * np.cos(omega * tau + PHI)


def discrete_samples(k, tau_max, omega):
    n_steps = int(np.floor(tau_max / k)) + 1
    tau_n = np.arange(n_steps, dtype=float) * k
    x_n = x_continuous(tau_n, omega)
    return tau_n, x_n


def interp_hold(tau_cont, tau_disc, x_disc):
    x = np.empty_like(tau_cont)
    j = 0
    last = x_disc[0]
    for i, tau in enumerate(tau_cont):
        while j + 1 < len(tau_disc) and tau_disc[j + 1] <= tau:
            j += 1
            last = x_disc[j]
        x[i] = last
    return x


def interp_linear(tau_cont, tau_disc, x_disc):
    return np.interp(tau_cont, tau_disc, x_disc)


def residual_stats(x_ref, x_test):
    r = x_test - x_ref
    l2 = float(np.sqrt(np.mean(r ** 2)))
    linf = float(np.max(np.abs(r)))
    return l2, linf


def main():
    tau_cont = np.linspace(0.0, TAU_MAX, N_CONT)

    print("\n--- OMEGA SWEEP AT FIXED k ---\n")
    print(f"k = {K}")
    print(f"tau_max = {TAU_MAX}")
    print(f"continuous pts = {N_CONT}")
    print()

    print(f"{'omega':>8} | {'L2_hold':>12} | {'L2_linear':>12} | {'ratio':>10}")
    print("-" * 52)

    first_nontrivial = None

    for omega in OMEGAS:
        x_ref = x_continuous(tau_cont, omega)
        tau_disc, x_disc = discrete_samples(K, TAU_MAX, omega)

        x_hold = interp_hold(tau_cont, tau_disc, x_disc)
        x_linear = interp_linear(tau_cont, tau_disc, x_disc)

        l2_hold, _ = residual_stats(x_ref, x_hold)
        l2_linear, _ = residual_stats(x_ref, x_linear)

        ratio = l2_linear / l2_hold if l2_hold > 0 else np.nan

        print(f"{omega:8.4f} | {l2_hold:12.8f} | {l2_linear:12.8f} | {ratio:10.6f}")

        # first regime where the linear residue is no longer near-zero relative to hold
        if first_nontrivial is None and ratio > 0.2:
            first_nontrivial = (omega, l2_hold, l2_linear, ratio)

    print("\n--- DIAGNOSTIC ---\n")

    if first_nontrivial is None:
        print("No non-trivial regime found in the scanned omega range.")
    else:
        omega, l2h, l2l, ratio = first_nontrivial
        print("First non-trivial regime detected:")
        print(f"omega      = {omega:.6f}")
        print(f"L2_hold    = {l2h:.10f}")
        print(f"L2_linear  = {l2l:.10f}")
        print(f"ratio      = {ratio:.6f}")

    print("\nInterpretation:")
    print("- ratio near 0   -> residue mostly hold-specific")
    print("- ratio moderate -> part of the residue survives smoother interpolation")
    print("- ratio high     -> residue less attributable to hold artifact")


if __name__ == "__main__":
    main()