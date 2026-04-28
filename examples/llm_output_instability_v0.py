from statistics import mean
import re


# ------------------------------------------------------------
# FEATURE EXTRACTION (TEXT STRUCTURE)
# ------------------------------------------------------------

def extract_features(text):
    text = str(text).lower()

    tokens = re.findall(r"\w+", text)
    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)

    token_count = len(tokens)
    unique_tokens = len(set(tokens))
    number_count = len(numbers)

    avg_token_len = mean([len(t) for t in tokens]) if tokens else 0

    return {
        "token_count": token_count,
        "unique_ratio": safe_div(unique_tokens, token_count),
        "number_count": number_count,
        "avg_token_len": avg_token_len,
    }


def safe_div(a, b):
    return a / b if b else 0.0


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


def coherence_variant(base, variant):
    return 1 - distance(extract_features(base), extract_features(variant))


def score(o, c, alpha=0.5):
    return alpha * o + (1 - alpha) * c


# ------------------------------------------------------------
# TEST CASE
# ------------------------------------------------------------

question = "If a train travels 60 miles in 1 hour, how far does it travel in 3 hours?"

# Simulated LLM outputs (all correct in content, different structure)

response_1 = """
The train travels 60 miles per hour. In 3 hours, it travels 60 * 3 = 180 miles.
Final answer: 180
"""

response_2 = """
Speed is 60 mph. Multiply by time: 3 hours → 60 × 3 = 180. So the distance is 180 miles.
"""

response_3 = """
60 miles in one hour means linear scaling. For 3 hours, distance equals 180 miles.
"""

responses = [response_1, response_2, response_3]


# ------------------------------------------------------------
# RUN
# ------------------------------------------------------------

base = responses[0]
variants = responses[1:]

o = omega(base, variants)

print("=" * 80)
print("LLM OUTPUT INSTABILITY TEST V0")
print("=" * 80)

print(f"Omega (invariance): {o:.6f}")
print()

for i, r in enumerate(responses, 1):
    c = coherence_variant(base, r)
    s = score(o, c)

    print(f"Response {i}")
    print(f"  coherence_variant: {c:.6f}")
    print(f"  score:             {s:.6f}")
    print()

print("=" * 80)
print("INTERPRETATION")
print("=" * 80)

print("All responses are semantically correct.")
print("Structural differences should produce measurable variation.")
print("If scores diverge → instability is detected.")