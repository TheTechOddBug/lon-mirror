# OMNIA MIRROR v2
# MB-X.01 / OMNIA
# Single-file, deterministic, no external deps

import math
import random
import zlib
from collections import Counter

# ============================================================
# BASIC UTILITIES
# ============================================================

RNG_SEED = 42
PRINT_WIDTH = 78

def safe_text(s):
    return "".join(ch for ch in s if 32 <= ord(ch) <= 126)

def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))

def normalize_counter(counter):
    total = sum(counter.values())
    if total <= 0:
        return {}
    return {k: v / total for k, v in counter.items()}

def l1_distance(d1, d2):
    keys = set(d1) | set(d2)
    return sum(abs(d1.get(k, 0.0) - d2.get(k, 0.0)) for k in keys)

# ============================================================
# REPRESENTATIONS
# ============================================================

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be in [2, 36]")
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n > 0:
        n, r = divmod(n, base)
        out.append(ALPHABET[r])
    return sign + "".join(reversed(out))

def parse_ints_from_text(text):
    vals = []
    curr = ""
    for ch in text:
        if ch.isdigit() or (ch == "-" and not curr):
            curr += ch
        else:
            if curr not in ("", "-"):
                try:
                    vals.append(int(curr))
                except:
                    pass
            curr = ""
    if curr not in ("", "-"):
        try:
            vals.append(int(curr))
        except:
            pass
    return vals

def numeric_multibase_repr(text, bases=(2,3,5,7,10,16)):
    nums = parse_ints_from_text(text)
    if not nums:
        return {}
    out = {}
    for b in bases:
        out[b] = "|".join(to_base(n, b) for n in nums)
    return out

# ============================================================
# STRUCTURAL FEATURES
# ============================================================

def char_distribution(text):
    return normalize_counter(Counter(text))

def bigram_distribution(text):
    if len(text) < 2:
        return {}
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    return normalize_counter(Counter(bigrams))

def length_signature(text):
    return {"len": len(text)}

def compression_ratio(text):
    raw = text.encode("utf-8", errors="ignore")
    if not raw:
        return 1.0
    comp = zlib.compress(raw, level=9)
    return len(comp) / max(1, len(raw))

def entropy_bits_per_char(text):
    if not text:
        return 0.0
    dist = char_distribution(text)
    return -sum(p * math.log2(p) for p in dist.values() if p > 0)

def base_digit_distribution(multibase_repr):
    out = {}
    for base, rep in multibase_repr.items():
        out[base] = char_distribution(rep)
    return out

# ============================================================
# TRANSFORMATIONS
# ============================================================

def reverse_text(text):
    return text[::-1]

def permute_text(text, seed=RNG_SEED):
    rng = random.Random(seed)
    chars = list(text)
    rng.shuffle(chars)
    return "".join(chars)

def noise_text(text, level=0.10, seed=RNG_SEED):
    if not text:
        return text
    rng = random.Random(seed)
    chars = list(text)
    n = max(1, int(len(chars) * level))
    idxs = rng.sample(range(len(chars)), min(n, len(chars)))
    for i in idxs:
        chars[i] = chr(rng.randint(32, 126))
    return "".join(chars)

def progressive_noise_text(text, step, total_steps, seed=RNG_SEED):
    level = step / max(1, total_steps)
    return noise_text(text, level=level, seed=seed + step)

# ============================================================
# OMEGA (NON-POSITIONAL)
# ============================================================

def omega_text(original, transformed):
    """
    Non-positional structural stability score.
    Combines:
    - character distribution invariance
    - bigram distribution invariance
    - compressibility stability
    - entropy stability
    """
    if not original and not transformed:
        return 1.0
    if not original or not transformed:
        return 0.0

    c1 = char_distribution(original)
    c2 = char_distribution(transformed)
    b1 = bigram_distribution(original)
    b2 = bigram_distribution(transformed)

    char_score = 1.0 - 0.5 * l1_distance(c1, c2)
    bigram_score = 1.0 - 0.5 * l1_distance(b1, b2)

    cr1 = compression_ratio(original)
    cr2 = compression_ratio(transformed)
    cr_score = 1.0 - min(1.0, abs(cr1 - cr2) / max(cr1, cr2, 1e-9))

    e1 = entropy_bits_per_char(original)
    e2 = entropy_bits_per_char(transformed)
    e_score = 1.0 - min(1.0, abs(e1 - e2) / max(e1, e2, 1e-9, 1.0))

    omega = (
        0.30 * char_score +
        0.35 * bigram_score +
        0.20 * cr_score +
        0.15 * e_score
    )
    return clamp(omega)

def omega_multibase(original_text, transformed_text, bases=(2,3,5,7,10,16)):
    """
    Numeric-only additional Omega.
    If no integers are present, returns None.
    """
    r1 = numeric_multibase_repr(original_text, bases=bases)
    r2 = numeric_multibase_repr(transformed_text, bases=bases)
    if not r1 or not r2:
        return None

    scores = []
    for b in bases:
        if b not in r1 or b not in r2:
            continue

        d1 = char_distribution(r1[b])
        d2 = char_distribution(r2[b])
        char_score = 1.0 - 0.5 * l1_distance(d1, d2)

        bg1 = bigram_distribution(r1[b])
        bg2 = bigram_distribution(r2[b])
        bigram_score = 1.0 - 0.5 * l1_distance(bg1, bg2)

        scores.append(0.5 * char_score + 0.5 * bigram_score)

    if not scores:
        return None
    return clamp(sum(scores) / len(scores))

def omega_total(original, transformed, bases=(2,3,5,7,10,16)):
    ot = omega_text(original, transformed)
    ob = omega_multibase(original, transformed, bases=bases)
    if ob is None:
        return ot
    return clamp(0.7 * ot + 0.3 * ob)

# ============================================================
# DYNAMIC METRICS
# ============================================================

def t_delta(original, threshold=0.55, steps=20):
    """
    First step where Omega falls below threshold under progressive noise.
    """
    prev = original
    for step in range(1, steps + 1):
        curr = progressive_noise_text(original, step, steps)
        om = omega_total(prev, curr)
        if om < threshold:
            return step
        prev = curr
    return steps + 1

def irreversibility_index(original, transform_fn, inverse_fn=None):
    """
    If inverse exists, compare original vs inverse(transform(original)).
    If inverse doesn't exist, use a second pass and measure residual loss.
    """
    forward = transform_fn(original)

    if inverse_fn is not None:
        recovered = inverse_fn(forward)
    else:
        recovered = transform_fn(forward)

    return clamp(1.0 - omega_total(original, recovered))

# ============================================================
# REPORT
# ============================================================

def summarize_multibase(text, bases=(2,3,5,7,10,16)):
    reps = numeric_multibase_repr(text, bases=bases)
    if not reps:
        return "No integers detected."
    lines = []
    for b in bases:
        if b in reps:
            rep = reps[b]
            short = rep if len(rep) <= 60 else rep[:57] + "..."
            lines.append(f"base {b:>2}: {short}")
    return "\n".join(lines)

def run_demo(user_input):
    original = safe_text(user_input)

    rev = reverse_text(original)
    perm = permute_text(original)
    noisy = noise_text(original, level=0.20)

    print("\n" + "=" * PRINT_WIDTH)
    print("OMNIA MIRROR v2")
    print("=" * PRINT_WIDTH)

    print("\nINPUT")
    print(original if original else "<empty>")

    print("\nBASIC FEATURES")
    print(f"length              : {len(original)}")
    print(f"entropy bits/char   : {entropy_bits_per_char(original):.4f}")
    print(f"compression ratio   : {compression_ratio(original):.4f}")

    print("\nMULTIBASE VIEW")
    print(summarize_multibase(original))

    print("\nTRANSFORMATIONS")
    print(f"reverse             : {rev[:70]}")
    print(f"permute             : {perm[:70]}")
    print(f"noise(20%)          : {noisy[:70]}")

    print("\nOMEGA")
    print(f"Ω reverse           : {omega_total(original, rev):.4f}")
    print(f"Ω permute           : {omega_total(original, perm):.4f}")
    print(f"Ω noise             : {omega_total(original, noisy):.4f}")

    mb_rev = omega_multibase(original, rev)
    mb_perm = omega_multibase(original, perm)
    mb_noise = omega_multibase(original, noisy)

    if mb_rev is not None:
        print(f"Ω multibase reverse : {mb_rev:.4f}")
        print(f"Ω multibase permute : {mb_perm:.4f}")
        print(f"Ω multibase noise   : {mb_noise:.4f}")

    print("\nDYNAMICS")
    print(f"TΔ(th=0.55)         : {t_delta(original, threshold=0.55, steps=20)}")
    print(f"IRI reverse         : {irreversibility_index(original, reverse_text, reverse_text):.4f}")
    print(f"IRI permute         : {irreversibility_index(original, permute_text):.4f}")
    print(f"IRI noise           : {irreversibility_index(original, lambda s: noise_text(s, 0.20)): .4f}")

    print("\nINTERPRETATION")
    print("Higher Ω  -> stronger structural invariance")
    print("Lower TΔ  -> faster collapse under perturbation")
    print("Higher IRI -> stronger irreversible loss")

if __name__ == "__main__":
    text = input("Insert any text / numbers: ")
    run_demo(text)