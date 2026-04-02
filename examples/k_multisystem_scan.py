import numpy as np

# ------------------------
# GENERATORS
# ------------------------

def sine_signal(n=500):
    t = np.linspace(0, 10, n)
    return np.sin(t)

def logistic_map(n=500, r=3.9):
    x = np.zeros(n)
    x[0] = 0.2
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def random_signal(n=500):
    return np.random.randn(n)


# ------------------------
# STRUCTURAL MEASURE
# ------------------------

def omega(x, y):
    return np.corrcoef(x, y)[0, 1]

def sci(x, y):
    return abs(omega(x, y))


# ------------------------
# K DETECTION
# ------------------------

def find_k(x, threshold=0.95, max_shift=100):
    for shift in range(1, max_shift):
        y = np.roll(x, shift)
        score = sci(x, y)
        if score < threshold:
            return shift
    return None


# ------------------------
# RUN
# ------------------------

def run():
    systems = {
        "sine": sine_signal(),
        "logistic_r3.9": logistic_map(),
        "random": random_signal(),
    }

    print("\n--- k SCAN ACROSS SYSTEMS ---\n")

    results = {}

    for name, x in systems.items():
        k = find_k(x)
        results[name] = k
        print(f"{name:15s} -> k = {k}")

    print("\n--- INTERPRETATION ---\n")

    ks = [v for v in results.values() if v is not None]

    if len(set(ks)) == 1:
        print("k appears invariant across systems")
    else:
        print("k varies across systems (non-universal)")

    return results


if __name__ == "__main__":
    run()