import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CASES = [
    {
        "name": "CASE 01 — Suspicious-Clean Review",
        "script": "examples/llm_output_instability_v0.py",
        "expected": "baseline gives no warning / OMNIA triggers review",
    },
    {
        "name": "CASE 02 — Correctness vs Structural Stability",
        "script": "examples/run_gsm_formal_metrics_v0.py",
        "expected": "correctness remains true / Omega decreases / Score+ decreases",
    },
    {
        "name": "CASE 03 — Irreversibility",
        "script": "examples/iri_validation_v2.py",
        "expected": "recoverable < nonrecoverable < lossy",
    },
    {
        "name": "CASE 04 — Saturation",
        "script": "examples/sei_validation_v0.py",
        "expected": "saturated > converging > unstable",
    },
    {
        "name": "CASE 05 — Divergence Timing",
        "script": "examples/tdelta_validation_v0.py",
        "expected": "rapid divergence crosses threshold before slow divergence",
    },
    {
        "name": "CASE 06 — Resilience",
        "script": "examples/r_validation_v0.py",
        "expected": "perfect > partial > failed recovery",
    },
    {
        "name": "CASE 07 — Residual Invariants",
        "script": "examples/omega_hat_validation_v0.py",
        "expected": "surviving invariant components explicitly returned",
    },
]


def run_case(case):
    print("\n" + "=" * 100)
    print(case["name"])
    print("=" * 100)

    print(f"\nSCRIPT:\n{case['script']}")
    print(f"\nEXPECTED:\n{case['expected']}")

    script_path = ROOT / case["script"]

    if not script_path.exists():
        print("\nSTATUS: MISSING SCRIPT")
        return False

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
    )

    print("\nRETURN CODE:")
    print(result.returncode)

    print("\nSTDOUT:\n")
    print(result.stdout.strip() if result.stdout.strip() else "(empty)")

    if result.stderr.strip():
        print("\nSTDERR:\n")
        print(result.stderr.strip())

    return result.returncode == 0


def main():
    print("=" * 100)
    print("OMNIA — RUN ALL CANONICAL CASES")
    print("=" * 100)

    successes = 0

    for case in CASES:
        ok = run_case(case)
        if ok:
            successes += 1

    print("\n" + "=" * 100)
    print("FINAL SUMMARY")
    print("=" * 100)

    print(f"\nSUCCESSFUL CASES: {successes}/{len(CASES)}")

    if successes == len(CASES):
        print("\nSTATUS: ALL CANONICAL CASES EXECUTED")
    else:
        print("\nSTATUS: SOME CASES FAILED")

    print("\nIMPORTANT:")
    print("The framework remains bounded and experimental.")
    print("measurement != inference != decision")


if __name__ == "__main__":
    main()