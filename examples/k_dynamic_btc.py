import numpy as np
import pandas as pd

# ==========================================
# k(t) DYNAMIC TRACKING ON REAL DATA
# ==========================================

WINDOW_SIZE = 60
THRESHOLD = 0.95
MAX_SHIFT = 30


def omega(x, y):
    c = np.corrcoef(x, y)[0, 1]
    if np.isnan(c):
        return 0.0
    return c


def sci(x, y):
    return abs(omega(x, y))


def find_k_local(window, threshold=THRESHOLD, max_shift=MAX_SHIFT):
    for shift in range(1, max_shift + 1):
        y = np.roll(window, shift)
        score = sci(window, y)
        if score < threshold:
            return shift
    return max_shift


def track_k_dynamic(series, window_size=WINDOW_SIZE):
    ks = []
    idxs = []

    for i in range(0, len(series) - window_size + 1):
        window = series[i:i + window_size]
        k = find_k_local(window)
        ks.append(k)
        idxs.append(i + window_size - 1)

    return np.array(idxs), np.array(ks)


def summarize_regime(k_values):
    return {
        "mean_k": float(np.mean(k_values)),
        "min_k": int(np.min(k_values)),
        "max_k": int(np.max(k_values)),
        "std_k": float(np.std(k_values)),
    }


def main(csv_path="btc.csv"):
    df = pd.read_csv(csv_path)

    if "close" not in df.columns:
        raise ValueError("CSV must contain a 'close' column")

    price = df["close"].astype(float).to_numpy()

    # Better than raw price: use returns
    returns = np.diff(np.log(price))
    idxs, k_vals = track_k_dynamic(returns)

    # Print full scan every 10 steps
    print("\n--- k(t) dynamic scan ---\n")
    for i in range(0, len(k_vals), 10):
        print(f"idx={idxs[i]:4d} | k={k_vals[i]:2d}")

    summary = summarize_regime(k_vals)

    print("\n--- summary ---\n")
    print(f"mean k : {summary['mean_k']:.2f}")
    print(f"min  k : {summary['min_k']}")
    print(f"max  k : {summary['max_k']}")
    print(f"std  k : {summary['std_k']:.2f}")

    # Optional crude regime labels
    print("\n--- regime estimate ---\n")
    for i in range(0, len(k_vals), 10):
        k = k_vals[i]
        if k >= 20:
            regime = "stable"
        elif k >= 8:
            regime = "transitional"
        else:
            regime = "unstable"
        print(f"idx={idxs[i]:4d} | k={k:2d} | regime={regime}")


if __name__ == "__main__":
    main("btc.csv")