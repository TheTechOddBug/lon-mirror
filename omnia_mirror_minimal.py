# OMNIA MIRROR — MINIMAL v1
# MB-X.01 / Omniabase±

import zlib
import random
import math

# ----------------------------
# CORE TRANSFORMATIONS
# ----------------------------

def permute(s):
    l = list(s)
    random.seed(42)  # deterministico
    random.shuffle(l)
    return ''.join(l)

def reverse(s):
    return s[::-1]

def compress(s):
    return zlib.compress(s.encode())

def decompress(b):
    try:
        return zlib.decompress(b).decode(errors="ignore")
    except:
        return ""

def noise(s, level=0.1):
    l = list(s)
    n = int(len(l) * level)
    random.seed(42)
    idx = random.sample(range(len(l)), n)
    for i in idx:
        l[i] = chr(random.randint(32, 126))
    return ''.join(l)

# ----------------------------
# STRUCTURAL MEASURE (Ω)
# ----------------------------

def similarity(a, b):
    if not a or not b:
        return 0.0
    length = min(len(a), len(b))
    match = sum(1 for i in range(length) if a[i] == b[i])
    return match / length

def omega(original, transformed):
    return similarity(original, transformed)

# ----------------------------
# DYNAMIC METRICS
# ----------------------------

def t_delta(s, steps=10):
    base = s
    for t in range(1, steps+1):
        s = permute(s)
        if omega(base, s) < 0.2:
            return t
    return steps

def irreversibility(s):
    forward = permute(s)
    back = permute(forward)
    return 1 - omega(s, back)

# ----------------------------
# PIPELINE
# ----------------------------

def run(input_text):
    print("\nINPUT:")
    print(input_text)

    print("\nTRANSFORMATIONS:")

    rev = reverse(input_text)
    print("reverse:", rev)

    perm = permute(input_text)
    print("permute:", perm)

    comp = compress(input_text)
    decomp = decompress(comp)
    print("compress->decompress:", decomp)

    noisy = noise(input_text, 0.2)
    print("noise:", noisy)

    print("\nMEASURE:")

    print("Ω reverse:", round(omega(input_text, rev), 3))
    print("Ω permute:", round(omega(input_text, perm), 3))
    print("Ω noise:", round(omega(input_text, noisy), 3))

    print("\nDYNAMIC:")

    print("TΔ:", t_delta(input_text))
    print("IRI:", round(irreversibility(input_text), 3))


# ----------------------------
# ENTRY
# ----------------------------

if __name__ == "__main__":
    user_input = input("\nInsert any text: ")
    run(user_input)