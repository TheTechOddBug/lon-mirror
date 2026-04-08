import math
from pathlib import Path
from typing import List, Dict, Any

TARGET_NUMBERS = [
    (1007, False, "1007 composite"),
    (1009, True, "1009 prime"),
    (2021, False, "2021 composite"),
    (2017, True, "2017 prime"),
    (2047, False, "2047 composite"),
    (2039, True, "2039 prime"),
]

def to_base(n: int, base: int) -> str:
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if n == 0: return "0"
    out = []
    while n > 0:
        n, rem = divmod(n, base)
        out.append(digits[rem])
    return "".join(reversed(out))

def calculate_base_entropy(rep: str) -> float:
    """Calcola l'entropia di Shannon della stringa nella base data."""
    if not rep: return 0.0
    counts = {}
    for char in rep:
        counts[char] = counts.get(char, 0) + 1
    entropy = 0.0
    for char in counts:
        p = counts[char] / len(rep)
        entropy -= p * math.log2(p)
    return entropy

def regularity_metrics(n: int) -> Dict[str, Any]:
    bases = range(2, 17)
    total_entropy = 0.0
    repunit_like_count = 0  # Basi con una sola cifra dominante (>80%)
    palindrome_count = 0
    
    for b in bases:
        rep = to_base(n, b)
        entropy = calculate_base_entropy(rep)
        total_entropy += entropy
        
        # Check Repunit-like (es. 11111 o 33233)
        counts = [rep.count(c) for c in set(rep)]
        if any(c / len(rep) >= 0.8 for c in counts):
            repunit_like_count += 1
            
        if rep == rep[::-1]:
            palindrome_count += 1
            
    return {
        "avg_entropy": total_entropy / len(bases),
        "reg_signature": repunit_like_count + palindrome_count,
        "repunit_like": repunit_like_count,
        "palindromes": palindrome_count
    }

def main():
    print(f"{'Number':>15} | {'Type':>10} | {'Avg Entropy':>12} | {'Reg Score':>10} | {'Palin':>6} | {'RepL':>6}")
    print("-" * 75)
    
    for n, is_prime, label in TARGET_NUMBERS:
        metrics = regularity_metrics(n)
        p_type = "PRIME" if is_prime else "COMP"
        print(f"{n:15d} | {p_type:10} | {metrics['avg_entropy']:12.4f} | {metrics['reg_signature']:10d} | {metrics['palindromes']:6d} | {metrics['repunit_like']:6d}")

if __name__ == "__main__":
    main()
