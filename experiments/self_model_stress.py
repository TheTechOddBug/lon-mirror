import random
import math
from statistics import mean

def real_dynamics(x):
    return x + 0.2 * math.sin(3 * x) - 0.05 * x

def model_prediction(m, mismatch=0.0):
    return m + (0.18 + mismatch) * math.sin(3 * m) - (0.04 + mismatch) * m

def observe(x, noise=0.0):
    return round(x + random.gauss(0, noise), 2)

def update_model(m, y, gain):
    return m + gain * (y - m)

def run(noise=0.0, mismatch=0.0, gain=0.6, steps=40, seed=42):
    random.seed(seed)

    s = 0.7
    m = 0.3

    E = []
    Ep = []
    C = []

    for _ in range(steps):
        y = observe(s, noise)

        e = abs(s - m)

        s_next = real_dynamics(s)
        pred = model_prediction(m, mismatch)
        ep = abs(s_next - pred)

        m_next = update_model(m, y, gain)
        expected = m + 0.5 * (round(pred,2) - m)
        c = abs(m_next - expected)

        E.append(e)
        Ep.append(ep)
        C.append(c)

        s = s_next
        m = m_next

    return mean(E), mean(Ep), mean(C)

def main():
    print("SELF MODEL STRESS TEST")

    cases = [
        ("baseline", 0.0, 0.0, 0.6),
        ("noise", 0.05, 0.0, 0.6),
        ("mismatch", 0.0, 0.05, 0.6),
        ("bias_gain_low", 0.0, 0.0, 0.2),
        ("bias_gain_high", 0.0, 0.0, 1.1),
    ]

    for name, n, m, g in cases:
        e, ep, c = run(noise=n, mismatch=m, gain=g)
        print(f"{name:15} | E={e:.4f} | Ep={ep:.4f} | C={c:.4f}")

if __name__ == "__main__":
    main()