from omnia_sci_engine import omnia_multi_lens


def classify(o, sci):
    if o > 0.8 and sci > 0.8:
        return "stable_structure"

    if o > 0.8 and sci < 0.5:
        return "false_coherence"

    if o < 0.5:
        return "instability"

    return "mixed"


def run_demo():
    print("=== OMNIA VALIDATION DEMO ===\n")

    test_cases = {
        "uniform": "aaaaaa",
        "repetitive": "abcabcabc",
        "natural": "hello world",
        "random": "xqzptlrm",
        "mixed": "aaabbbcccxyz",
    }

    for name, s in test_cases.items():
        o, sci = omnia_multi_lens(s)
        label = classify(o, sci)

        print(f"{name:12} -> Ω={o:.3f}, SCI={sci:.3f} -> {label}")


if __name__ == "__main__":
    run_demo()