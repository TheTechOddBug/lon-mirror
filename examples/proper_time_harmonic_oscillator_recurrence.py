import numpy as np

# ==========================================
# PROPER-TIME HARMONIC OSCILLATOR
# continuous vs true discrete recurrence
# ==========================================

K = 0.05
A = 1.0
OMEGA = 1.2
PHI = 0.3
TAU_MAX = 20.0
N_CONT = 5000


def x_continuous(tau, omega):
    return A * np.cos(omega * tau + PHI)


def discrete_exact_samples(k, tau_max, omega):
    n_steps = int(np.floor(tau_max / k)) + 1
    tau_n = np.arange(n_steps, dtype=float) * k
    x_n = x_continuous(tau_n, omega)
    return tau_n, x_n


def discrete_recurrence(k, tau_max, omega):
    """
    True discrete harmonic oscillator:
    x_{n+1} = (2 - (omega*k)^2) x_n - x_{n-1}

    Initial conditions are chosen from the exact continuous solution
    only to start the recurrence consistently.
    """
    n_steps = int(np.floor(tau_max / k)) + 1
    tau_n = np.arange(n_steps, dtype=float) * k
    x_n = np.zeros(n_steps, dtype=float)

    # initial conditions from continuous solution
    x_n[0] = x_continuous(np.array([0.0]), omega)[0]
    if n_steps > 1:
        x_n[1] = x_continuous(np.array([k]), omega)[0]

    coeff = 2.0 - (omega * k) ** 2

    for n in range(1, n_steps - 1):
        x_n[n + 1] = coeff * x_n[n] - x_n[n - 1]

    return tau_n, x_n


def interp_linear(tau_cont, tau_disc, x_disc):
    return np.interp(tau_cont, tau_disc, x_disc)


def residual_stats(x_ref, x_test):
    r = x_test - x_ref
    l2 = float(np.sqrt(np.mean(r ** 2)))
    linf = float(np.max(np.abs(r)))
    return r, l2, linf


def main():
    tau_cont = np.linspace(0.0, TAU_MAX, N_CONT)
    x_ref = x_continuous(tau_cont, OMEGA)

    # exact sampled discrete points
    tau_exact, x_exact = discrete_exact_samples(K, TAU_MAX, OMEGA)

    # true discrete recurrence
    tau_rec, x_rec = discrete_recurrence(K, TAU_MAX, OMEGA)

    # sampled-point comparison
    _, l2_pts, linf_pts = residual_stats(x_exact, x_rec)

    # continuous reconstructed comparison
    x_exact_lin = interp_linear(tau_cont, tau_exact, x_exact)
    x_rec_lin = interp_linear(tau_cont, tau_rec, x_rec)

    _, l2_exact_lin, linf_exact_lin = residual_stats(x_ref, x_exact_lin)
    _, l2_rec_lin, linf_rec_lin = residual_stats(x_ref, x_rec_lin)
    _, l2_between, lin