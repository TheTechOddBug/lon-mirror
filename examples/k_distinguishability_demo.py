import numpy as np

# --- SIGNAL ---
def generate_signal(n=500):
    t = np.linspace(0, 10, n)
    x = np.sin(t) + 0.05 * np.random.randn(n)
    return t, x


# --- SHIFT ---
def shift_signal(x, shift):
    y = np.roll(x, shift)
    return y


# --- STRUCTURAL COHERENCE (Ω proxy) ---
def omega(x, y):
    return np.corrcoef(x, y)[0, 1]


# --- SCI proxy ---
def sci(x, y):
    return abs(omega(x, y))


# --- FIND k ---
def find_k(x, threshold=0.95):
    results = []
    for shift in range(1, 100):
        y = shift_signal(x, shift)
        score = sci(x, y)
        results.append((shift, score))

        if score < threshold:
            return shift, results

    return None, results


# --- MAIN ---
if __name__ == "__main__":
    t, x = generate_signal()

    k, history = find_k(x, threshold=0.95)

    print("\n--- Distinguishability Scan ---\n")

    for shift, score in history[:20]:
        print(f"shift={shift:3d} | SCI={score:.4f}")

    print("\n--- RESULT ---\n")

    if k is not None:
        print(f"k (first distinguishable step) = {k}")
    else:
        print("No distinguishability break found")