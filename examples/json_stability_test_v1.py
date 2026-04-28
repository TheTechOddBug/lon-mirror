import json
from statistics import mean


# ------------------------------------------------------------
# FEATURE EXTRACTION
# ------------------------------------------------------------

def extract_signature(obj):
    if not isinstance(obj, dict):
        return {}

    sig = {}

    for k, v in obj.items():
        sig[k] = {
            "type": type(v).__name__,
            "is_null": v is None,
            "is_numeric": isinstance(v, (int, float)),
            "is_string": isinstance(v, str),
        }

    return sig


# ------------------------------------------------------------
# DISTANCE (KEY-AWARE)
# ------------------------------------------------------------

def signature_distance(base, variant):
    keys = set(base) | set(variant)
    penalties = []

    for k in keys:
        if k not in base:
            penalties.append(1.0)  # extra key
            continue
        if k not in variant:
            penalties.append(1.0)  # missing key
            continue

        b = base[k]
        v = variant[k]

        p = 0.0

        # type mismatch
        if b["type"] != v["type"]:
            p += 0.6

        # null mismatch
        if b["is_null"] != v["is_null"]:
            p += 0.3

        # numeric/string mismatch
        if b["is_numeric"] != v["is_numeric"]:
            p += 0.2

        if b["is_string"] != v["is_string"]:
            p += 0.2

        penalties.append(min(1.0, p))

    return mean(penalties) if penalties else 0.0


# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------

def omega(base, variants):
    base_sig = extract_signature(base)
    ds = []

    for v in variants:
        ds.append(signature_distance(base_sig, extract_signature(v)))

    return 1 - mean(ds)


def coherence_variant(base, variant):
    base_sig = extract_signature(base)
    var_sig = extract_signature(variant)

    d = signature_distance(base_sig, var_sig)
    return 1 - d


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

# reorder only (should stay high)
variant_1 = {
    "balance": 1000,
    "active": True,
    "name": "Alice",
    "age": 30
}

# type drift (should drop)
variant_2 = {
    "name": "Alice",
    "age": "30",
    "balance": "1000",
    "active": "yes"
}

# null corruption (should drop)
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
print("JSON STABILITY TEST V1")
print("=" * 80)

print(f"Omega (invariance): {o:.6f}")
print()

for i, v in enumerate(variants, 1):
    c = coherence_variant(base, v)
    s = score(o, c)

    print(f"Variant {i}")
    print(f"  coherence_variant: {c:.6f}")
    print(f"  score:             {s:.6f}")
    print()

print("=" * 80)
print("EXPECTED BEHAVIOR")
print("=" * 80)

print("Variant 1 (reorder)     → high score")
print("Variant 2 (type drift) → low score")
print("Variant 3 (null)       → low score")