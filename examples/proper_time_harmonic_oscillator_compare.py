import numpy as np

# ==========================================
# PROPER-TIME HARMONIC OSCILLATOR
# compare inter-step models
# ==========================================

K = 0.05
A = 1.0
OMEGA = 1.2
PHI = 0.3
TAU_MAX = 20.0
N_CONT = 5000


def x_continuous(tau):
    return A * np.cos(OMEGA * tau + PHI)


def discrete_samples(k, tau_max):
    n_steps = int(np.floor(tau_max / k)) + 1
    tau_n = np.arange(n_steps, dtype=float) * k
    x_n = x_continuous(tau_n)
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
    return r, l2, linf


def main():
    tau_cont = np.linspace(0.0, TAU_MAX, N_CONT)
    x_ref = x_continuous(tau_cont)

    tau_disc, x_disc = discrete_samples(K, TAU_MAX)

    # exact sampled baseline
    x_sampled = np.interp(tau_disc, tau_cont, x_ref)
    _, l2_sampled, linf_sampled = residual_stats(x_sampled, x_disc)

    # hold reconstruction
    x_hold = interp_hold(tau_cont, tau_disc, x_disc)
    _, l2_hold, linf_hold = residual_stats(x_ref, x_hold)

    # linear reconstruction
    x_linear = interp_linear(tau_cont, tau_disc, x_disc)
    _, l2_linear, linf_linear = residual_stats(x_ref, x_linear)

    print("\n--- PROPER-TIME OSCILLATOR: MODEL COMPARISON ---\n")
    print(f"k               = {K}")
    print(f"omega_0         = {OMEGA}")
    print(f"tau_max         = {TAU_MAX}")
    print(f"continuous pts  = {len(tau_cont)}")
    print(f"discrete steps  = {len(tau_disc)}")

    print("\n--- BASELINE: EXACT SAMPLED POINTS ---\n")
    print(f"L2 residual     = {l2_sampled:.12f}")
    print(f"Linf residual   = {linf_sampled:.12f}")

    print("\n--- PIECEWISE HOLD ---\n")
    print(f"L2 residual     = {l2_hold:.12f}")
    print(f"Linf residual   = {linf_hold:.12f}")

    print("\n--- PIECEWISE LINEAR ---\n")
    print(f"L2 residual     = {l2_linear:.12f}")
    print(f"Linf residual   = {linf_linear:.12f}")

    print("\n--- DIAGNOSTIC ---\n")
    if l2_linear < l2_hold:
        print("Linear interpolation reduces the residue relative to hold.")
    else:
        print("Linear interpolation does not reduce the residue relative to hold.")

    ratio = l2_linear / l2_hold if l2_hold > 0 else np.nan
    print(f"L2 linear / L2 hold = {ratio:.6f}")

    if ratio < 0.2:
        print("Most of the residue is hold-specific.")
    elif ratio < 0.8:
        print("Part of the residue survives beyond hold-specific dynamics.")
    else:
        print("Residue is not strongly reduced by linear interpolation.")

if __name__ == "__main__":
    main()