"""
MB-X.01 / OMNIA
Self-model toy system


Purpose:
- simulate a deterministic real system S_t
- simulate a partial observation O(S_t)
- simulate an internal model M_t
- measure:
    E_t   = self-model error
    E_p   = predictive error
    C_t   = internal coherence error

This is a minimal operational example of:
real state vs internal model vs divergence

No external dependencies required.
"""

from __future__ import annotations

import math


def real_dynamics(x: float) -> float:
    """
    Real deterministic dynamics of the system.

    Chosen to be nonlinear but simple.
    """
    return x + 0.2 * math.sin(3.0 * x) - 0.05 * x


def observe(x: float) -> float:
    """
    Partial observation of the real state.

    The system does not see the full precision of reality.
    """
    return round(x, 2)


def model_prediction(m: float) -> float:
    """
    What the internal model predicts as the next state.

    Intentionally imperfect: the model uses an approximate dynamics,
    not the true real_dynamics().
    """
    return m + 0.18 * math.sin(3.0 * m) - 0.04 * m


def update_model(m: float, y: float, gain: float) -> float:
    """
    Internal model update from previous model + current observation.

    gain controls correction strength.
    """
    return m + gain * (y - m)


def expected_model_update(m: float) -> float:
    """
    Internal expectation of how the model should evolve.

    This is intentionally not identical to update_model(),
    so internal coherence can fail.
    """
    expected_gain = 0.50
    predicted_observation = round(model_prediction(m), 2)
    return m + expected_gain * (predicted_observation - m)


def main() -> None:
    # Initial real state
    s_t = 0.73

    # Initial internal model
    m_t = 0.30

    # Learning / correction gain
    gain = 0.65

    # Number of simulation steps
    steps = 30

    print("=" * 100)
    print("SELF-MODEL TOY SYSTEM")
    print("=" * 100)
    print(
        f"{'t':>2} | {'S_t (real)':>12} | {'Y_t (obs)':>10} | {'M_t (model)':>12} | "
        f"{'Pred(S_t+1)':>12} | {'E_t':>10} | {'E_p':>10} | {'C_t':>10}"
    )
    print("-" * 100)

    for t in range(steps):
        # Observation of current real state
        y_t = observe(s_t)

        # Self-model error: distance between current real state and current model
        e_t = abs(s_t - m_t)

        # Model predicts next state using its own internal dynamics
        s_pred_next = model_prediction(m_t)

        # Real next state
        s_next = real_dynamics(s_t)

        # Predictive error: distance between true next state and predicted next state
        e_p = abs(s_next - s_pred_next)

        # Internal expected update
        m_expected_next = expected_model_update(m_t)

        # Actual model update from observation
        m_next = update_model(m_t, y_t, gain)

        # Internal coherence error
        c_t = abs(m_next - m_expected_next)

        print(
            f"{t:>2} | "
            f"{s_t:>12.6f} | "
            f"{y_t:>10.2f} | "
            f"{m_t:>12.6f} | "
            f"{s_pred_next:>12.6f} | "
            f"{e_t:>10.6f} | "
            f"{e_p:>10.6f} | "
            f"{c_t:>10.6f}"
        )

        # Advance system
        s_t = s_next
        m_t = m_next

    print("-" * 100)
    print("Legend:")
    print("S_t   = real state")
    print("Y_t   = observed state (partial / compressed)")
    print("M_t   = internal model")
    print("E_t   = self-model error")
    print("E_p   = predictive error")
    print("C_t   = internal coherence error")
    print("=" * 100)


if __name__ == "__main__":
    main()