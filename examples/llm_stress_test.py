import os
import sys
from statistics import mean

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from omnia_semantic_decoupling_v10_0 import semantic_decoupling_score


def score_group(texts, seed=42):
    scores = [semantic_decoupling_score(t, seed=seed) for t in texts]
    return {
        "omega_raw": mean(s["omega_raw"] for s in scores),
        "omega_shuffle": mean(s["omega_shuffle"] for s in scores),
        "delta_struct": mean(s["delta_struct"] for s in scores),
    }


def main():
    logic_strong = [
        (
            "If all mammals are warm blooded and whales are mammals, "
            "then whales are warm blooded. Therefore the conclusion follows "
            "from the premises by class inclusion."
        ),
        (
            "A is greater than B. B is greater than C. Therefore A is greater than C. "
            "The relation is transitive and the result is consistent."
        ),
        (
            "If the contract is signed before payment, and payment happened after signature, "
            "then the event order is coherent. The conclusion matches the timeline."
        ),
    ]

    hallucination_fluent = [
        (
            "The treaty was signed in 1842 after the digital census was completed, "
            "which explains why satellite calibration shaped the medieval tax code. "
            "This is historically coherent because the institutions were aligned."
        ),
        (
            "The patient improved because the diagnosis confirmed the economic cycle, "
            "and the financial recovery stabilized the bloodstream in a constitutional sense. "
            "The reasoning sounds complete but the causal chain is invented."
        ),
        (
            "The engine worked because the algorithm inherited thermal gravity from the archive, "
            "which naturally caused the database to rotate into legal compliance. "
            "The language is fluent but the logic is fabricated."
        ),
    ]

    degenerated_loop = [
        (
            "The answer is correct because it is correct. "
            "It is correct for the same reason that it is correct. "
            "Therefore the answer remains correct because it is correct."
        ),
        (
            "This works because it works and it keeps working because it works. "
            "The explanation repeats the same claim in different surface forms."
        ),
        (
            "The model is reliable because it is reliable. "
            "Its reliability proves reliability and the proof repeats reliability."
        ),
    ]

    groups = {
        "logic_strong": logic_strong,
        "hallucination_fluent": hallucination_fluent,
        "degenerated_loop": degenerated_loop,
    }

    print("\n--- OMNIA LLM Stress Test ---\n")

    results = {}
    for name, texts in groups.items():
        res = score_group(texts, seed=42)
        results[name] = res
        print(
            f"{name:22} "
            f"Ω_raw={res['omega_raw']:.4f} | "
            f"Ω_shuffle={res['omega_shuffle']:.4f} | "
            f"Δ_struct={res['delta_struct']:.4f}"
        )

    print("\nExpected ordering:")
    print("logic_strong > hallucination_fluent > degenerated_loop")
    print("\nInterpretation:")
    print("- logic_strong should keep the highest structural signal")
    print("- hallucination_fluent should remain fluent but lose relational integrity")
    print("- degenerated_loop should collapse toward low structural variety")

    ds_logic = results["logic_strong"]["delta_struct"]
    ds_hall = results["hallucination_fluent"]["delta_struct"]
    ds_loop = results["degenerated_loop"]["delta_struct"]

    print("\nInvariant check:")
    if ds_logic > ds_hall > ds_loop:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")


if __name__ == "__main__":
    main()