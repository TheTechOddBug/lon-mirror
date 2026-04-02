import numpy as np

# ==========================================
# PROPER-TIME HARMONIC OSCILLATOR
# continuous vs discrete proper-time stepping
# ==========================================

# Fundamental hypothesis parameter
K = 0.05          # minimum proper-time step
A = 1.0           # amplitude
OMEGA = 1.2       # proper angular frequency
PHI = 0.3         # phase
TAU_MAX = 20.0    # total proper-time span

# Numerical resolution for continuous reference
N_CONT = 5000


def continuous_solution(tau: np.ndarray, amplitude: float, omega: float, phi: float) -> np.ndarray:
    return amplitude * np.cos(omega * tau + phi)


def discrete_solution(
    k: float,
    tau_max: float,
    amplitude: float,
    omega: float,
    phi: float,
) -> tuple[np.ndarray, np.ndarray]:
    n_steps = int(np.floor(tau_max / k)) + 1
    tau_n = np.arange(n_steps, dtype=float) * k
    x_n = amplitude * np.cos(omega * tau_n + phi)
    return tau_n, x_n


def nearest_sample_residual(
    tau_cont: np.ndarray,
    x_cont: np.ndarray,
    tau_disc: np.ndarray,
    x_disc: np.ndarray,
) -> tuple[np.ndarray, float, float]:
    """
    Compare each discrete point with the continuous solution at the same proper time.
    Since x_disc is sampled from the same analytic formula, this residual should be ~0.
    This is only a consistency baseline.
    """
    x_cont_interp = np.interp(tau_disc, tau_cont, x_cont)
    residual = x_disc - x_cont_interp
    l2 = float(np.sqrt(np.mean(residual ** 2)))
    linf = float(np.max(np.abs(residual)))
    return residual, l2, linf


def piecewise_hold_residual(
    tau_cont: np.ndarray,
    x_cont: np.ndarray,
    tau_disc: np.ndarray,
    x_disc: np.ndarray,
) -> tuple[np.ndarray, float, float]:
    """
    Physical distinguishability test:
    assume the system is only distinguishable at discrete proper-time steps n*k.
    Between steps, the observable state is held at the last distinguishable value.

    This creates a genuine difference from the continuous curve.
    """
    x_hold = np.empty_like(tau_cont)

    j = 0
    last_val = x_disc[0]

    for i, tau in enumerate(tau_cont):
        while j + 1 < len(tau_disc) and tau_disc[j + 1] <= tau:
            j += 1
            last_val = x_disc[j]
        x_hold[i] = last_val

    residual = x_hold - x_cont
    l2 = float(np.sqrt(np.mean(residual ** 2)))
    linf = float(np.max(np.abs(residual)))
    return residual, l2, linf


def phase_increment(omega: float, k: float) -> float:
    return omega * k


def intrinsic_frequency_bound(k: float, min_steps_per_cycle: int = 2) -> float:
    return 1.0 / (min_steps_per_cycle * k)


def run() -> None:
    tau_cont = np.linspace(0.0, TAU_MAX, N_CONT)
    x_cont = continuous_solution(tau_cont, A, OMEGA, PHI)

    tau_disc, x_disc = discrete_solution(K, TAU_MAX, A, OMEGA, PHI)

    # Baseline consistency: sampled discrete vs continuous at same points
    residual_sampled, l2_sampled, linf_sampled = nearest_sample_residual(
        tau_cont, x_cont, tau_disc, x_disc
    )

    # Distinguishability model: piecewise-held discrete evolution
    residual_hold, l2_hold, linf_hold = piecewise_hold_residual(
        tau_cont, x_cont, tau_disc, x_disc
    )

    dphi = phase_increment(OMEGA, K)
    f0 = OMEGA / (2.0 * np.pi)
    f0_max = intrinsic_frequency_bound(K, min_steps_per_cycle=2)

    print("\n--- PROPER-TIME HARMONIC OSCILLATOR ---\n")
    print(f"k                = {K}")
    print(f"omega_0          = {OMEGA}")
    print(f"f_0              = {f0:.6f}")
    print(f"phase step dphi  = omega_0 * k = {dphi:.6f} rad")
    print(f"tau_max          = {TAU_MAX}")
    print(f"continuous pts   = {len(tau_cont)}")
    print(f"discrete steps   = {len(tau_disc)}")
    print(f"f_0,max(2-step)  = {f0_max:.6f}")

    print("\n--- BASELINE: SAME-FORM SAMPLE CONSISTENCY ---\n")
    print("Interpretation: this must be ~0, otherwise implementation is wrong.")
    print(f"L2 residual      = {l2_sampled:.12f}")
    print(f"Linf residual    = {linf_sampled:.12f}")

    print("\n--- DISTINGUISHABILITY TEST: PIECEWISE-HOLD MODEL ---\n")
    print("Interpretation: this is the first real residue induced by discrete proper-time distinguishability.")
    print(f"L2 residual      = {l2_hold:.12f}")
    print(f"Linf residual    = {linf_hold:.12f}")

    print("\n--- DIAGNOSTIC ---\n")
    if l2_hold == 0.0 and linf_hold == 0.0:
        print("No distinguishability residue detected.")
    else:
        print("Non-zero residue detected between continuous evolution and discrete distinguishable evolution.")

    print("\n--- FIRST 10 DISCRETE SAMPLES ---\n")
    for i in range(min(10, len(tau_disc))):
        print(f"n={i:2d} | tau={tau_disc[i]:8.4f} | x={x_disc[i]: .8f}")

    print("\n--- FIRST 10 HELD RESIDUAL SAMPLES ---\n")
    sample_idx = np.linspace(0, len(tau_cont) - 1, 10, dtype=int)
    for idx in sample_idx:
        print(
            f"tau={tau_cont[idx]:8.4f} | x_cont={x_cont[idx]: .8f} | residual={residual_hold[idx]: .8f}"
        )


if __name__ == "__main__":
    run()