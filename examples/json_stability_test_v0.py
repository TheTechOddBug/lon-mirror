import json
from statistics import mean


# ------------------------------------------------------------
# STRUCTURAL FEATURES (JSON-focused)
# ------------------------------------------------------------

def extract_features(obj):
    if not isinstance(obj, dict):
        return {}

    keys = list(obj.keys())
    values = list(obj.values())

    num_fields = len(keys)
    num_numeric = sum(isinstance(v, (int, float)) for v in values)
    num_strings = sum(isinstance(v, str) for v in values)
    num_nulls = sum(v is None for v in values)

    key_lengths = [len(k) for k in keys]
    avg_key_len = mean(key_lengths) if key_lengths else 0

    return {
        "num_fields": num_fields,
        "num_numeric": num_numeric,
        "num_strings": num_strings,
        "num_nulls": num_nulls,
        "avg_key_len": avg_key_len,
    }


def distance(a, b):
    keys = set(a) | set(b)
    diffs = []

    for k in keys:
        av = float(a.get(k, 0))
        bv = float(b.get(k, 0))
        denom = max(abs(av), abs(bv), 1.0)
        diffs.append(abs(av - bv) / denom)

    return mean(diffs) if diffs else 0.0


# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------

def omega(base, variants):
    f_base = extract_features(base)
    ds = []

    for v in variants:
        ds.append(distance(f_base, extract_features(v)))

    return 1 - mean(ds)


def coherence(obj):
    f = extract_features(obj)
    values = list(f.values())

    if len(values) < 2:
        return 1.0

    diffs = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            denom = max(abs(values[i]), abs(values[j]), 1.0)
            diffs.append(abs(values[i] - values[j]) / denom)

    return 1 - mean(diffs)


def score(o, c, alpha=0.5):
    return alpha * o + (1 - alpha) * c


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------

base = {
    "name": "Alice",
    "age": 30,
    "balance": 1000,
    "active": True
}

# Variant 1: harmless reorder (should be stable)
variant_1 = {
    "balance": 1000,
    "active": True,
    "name": "Alice",
    "age": 30
}

# Variant 2: structurally weird but still "valid"
variant_2 = {
    "name": "Alice",
    "age": "30",          # type drift
    "balance": "1000",    # type drift
    "active": "yes"       # semantic drift
}

# Variant 3: partial corruption but still parseable
variant_3 = {
    "name": "Alice",
    "age": None,
    "balance": 1000,
    "active": True
}

variants = [variant_1, variant_2, variant_3]


# ------------------------------------------------------------
# RUN
# ------------------------------------------------------------

o = omega(base, variants)

print("=" * 80)
print("JSON STABILITY TEST V0")
print("=" * 80)

print(f"Omega (invariance): {o:.6f}")
print()

for i, v in enumerate(variants, 1):
    c = coherence(v)
    s = score(o, c)

    print(f"Variant {i}")
    print(f"  coherence: {c:.6f}")
    print(f"  score:     {s:.6f}")
    print()

print("=" * 80)
print("INTERPRETATION")
print("=" * 80)

print("All variants are valid JSON.")
print("But structural properties differ.")
print("If scores drop → structural fragility detected.")