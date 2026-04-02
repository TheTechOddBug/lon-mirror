import numpy as np

# ------------------------
# SIGNAL (regime change)
# ------------------------

def generate_signal(n=800):
    t = np.linspace(0, 20, n)

    # fase 1: stabile
    x1 = np.sin(t[:300])

    # fase 2: instabile (rumore)
    x2 = np.sin(t[300:600]) + 0.5 * np.random.randn(300)

    # fase 3: caos (random)
    x3 = np.random.randn(n - 600)

    return np.concatenate([x1, x2, x3])


# ------------------------
# STRUCTURAL MEASURE
# ------------------------

def omega(x, y):
    return np.corrcoef(x, y)[0, 1]

def sci(x, y):
    return abs(omega(x, y))


# ------------------------
# LOCAL k
# ------------------------

def find_k_local(window, threshold=0.95, max_shift=50):
    for shift in range(1, max_shift):
        y = np.roll(window, shift)
        score = sci(window, y)
        if score < threshold:
            return shift
    return max_shift


# ------------------------
# TRACKING
# ------------------------

def track_k(x, window_size=100):
    ks = []
    positions = []

    for i in range(0, len(x) - window_size):
        window = x[i:i+window_size]
        k = find_k_local(window)
        ks.append(k)
        positions.append(i)

    return positions, ks


# ------------------------
# MAIN
# ------------------------

if __name__ == "__main__":
    x = generate_signal()
    pos, ks = track_k(x)

    print("\n--- k(t) ---\n")

    for i in range(0, len(ks), 50):
        print(f"t={pos[i]:4d} | k={ks[i]}")

    print("\n--- SUMMARY ---\n")

    print(f"mean k: {np.mean(ks):.2f}")
    print(f"min  k: {np.min(ks)}")
    print(f"max  k: {np.max(ks)}")