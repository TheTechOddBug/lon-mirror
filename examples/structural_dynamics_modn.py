from math import gcd


def orbit_mod_n(n: int, k: int, start: int, max_steps: int = 100):
    """
    Compute the orbit of x -> kx mod n starting from 'start'.

    Returns:
        seq: visited states in order
        cycle_start: index where the cycle begins, or None if not found
    """
    seen = {}
    seq = []
    x = start % n

    for step in range(max_steps):
        if x in seen:
            cycle_start = seen[x]
            return seq, cycle_start
        seen[x] = step
        seq.append(x)
        x = (k * x) % n

    return seq, None


def omega_from_orbit(seq, cycle_start):
    """
    Minimal structural coherence score.

    Omega = cycle_length / total_visited_length

    Interpretation:
    - Omega = 1.0  -> pure cycle, no transient collapse
    - Omega < 1.0  -> transient + cycle, dissipative behavior
    """
    if cycle_start is None or len(seq) == 0:
        return 0.0

    cycle_length = len(seq) - cycle_start
    total_length = len(seq)

    return cycle_length / total_length


def classify_regime(n: int, k: int) -> str:
    """
    Structural regime classification.
    """
    if gcd(k, n) == 1:
        return "conservative"
    return "dissipative"


def format_orbit(seq, cycle_start):
    """
    Pretty-print an orbit with cycle brackets.
    """
    if cycle_start is None:
        return " -> ".join(map(str, seq))

    prefix = seq[:cycle_start]
    cycle = seq[cycle_start:]

    left = " -> ".join(map(str, prefix))
    right = " -> ".join(map(str, cycle))

    if left:
        return f"{left} -> [{right}]"
    return f"[{right}]"


def analyze(n: int, k: int, max_steps: int = 100):
    """
    Analyze all distinct orbit components of x -> kx mod n.
    """
    print(f"\n=== n={n}, k={k} ===")
    print(f"regime: {classify_regime(n, k)}")
    print(f"gcd(k, n) = {gcd(k, n)}")

    visited_global = set()
    omegas = []

    for x in range(n):
        if x in visited_global:
            continue

        seq, cycle_start = orbit_mod_n(n, k, x, max_steps=max_steps)
        visited_global.update(seq)

        omega = omega_from_orbit(seq, cycle_start)
        omegas.append(omega)

        orbit_text = format_orbit(seq, cycle_start)
        print(f"{x}: {orbit_text} | Ω={omega:.2f}")

    if omegas:
        omega_mean = sum(omegas) / len(omegas)
    else:
        omega_mean = 0.0

    print(f"mean Ω = {omega_mean:.2f}")


if __name__ == "__main__":
    # Core examples
    analyze(9, 2)
    analyze(9, 3)
    analyze(9,