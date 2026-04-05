import os
import sys
from statistics import mean

# Ensure repo root is importable when running:
# python examples/omnia_validation_demo.py
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from omnia_semantic_decoupling_v10_0 import semantic_decoupling_score


def run_demo() -> None:
    print("=== OMNIA VALIDATION DEMO ===\n")

    samples = {
        "structured": [
            "alpha beta gamma alpha beta gamma alpha beta gamma alpha beta gamma",
            "node_1 connects_to node_2 node_2 connects_to node_3 node_3 connects_to node_4",
            "A B C A B C A B C A B C"
        ],
        "perturbed": [
            "alpha beta gamma alpha gamma beta alpha beta gamma alpha beta gamma",
            "node_1 connects_to node_2 node_3 connects_to node_2 node_3 connects_to node_4",
            "A B C A C B A B C A B C"
        ],
        "random": [
            "xqz rlm ptk vns qwe zmx trp ldk qnv wpt",
            "jfa qmr ztp lvn xkd pwo qzt mnr ttv bcx",
            "uio pql xmv znc rty bnm qaz wsx edc vfr"
        ],
    }

    for label, texts in samples.items():
        scores = [semantic_decoupling_score(t, seed=42) for t in texts]

        omega_raw = mean(s["omega_raw"] for s in scores)
        omega_shuffle = mean(s["omega_shuffle"] for s in scores)
        delta_struct = mean(s["delta_struct"] for s in scores)

        print(f"{label:10} -> "
              f"Ω_raw={omega_raw:.3f} | "
              f"Ω_shuffle={omega_shuffle:.3f} | "
              f"Δ_struct={delta_struct:.3f}")

    print("\nExpected ordering:")
    print("structured > perturbed > random (on Δ_struct)")


if __name__ == "__main__":
    run_demo()