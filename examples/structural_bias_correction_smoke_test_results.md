# Structural Bias Correction — Smoke Test Results

Status: module-level import and behavior validation  
Scope: minimal 4-number batch  
Purpose: verify that SBC-Regularity v1 is importable, executable, and directionally coherent before engine integration

---

## Goal

This smoke test was designed to verify three things:

1. the `StructuralBiasCorrection` module imports correctly
2. the batch interface executes without error
3. the adjusted score moves in the expected direction on known regularity traps

This is not a ranking benchmark.
It is a module-level sanity check.

---

## Tested Batch

Numbers used:

- `1009`
- `2047`
- `30031`
- `1000001`

Raw omega inputs:

- `1009  -> 0.931220`
- `2047  -> 0.932120`
- `30031 -> 0.941200`
- `1000001 -> 0.948210`

Configured correction:

- `lambda = 0.03`

---

## Terminal Output

```text
=== STRUCTURAL BIAS CORRECTION SMOKE TEST ===
        n |  omega_raw |    pen_raw |   pen_norm |  omega_adj | avg_entropy
------------------------------------------------------------------------------
     1009 |   0.931220 |   0.312450 |   0.000000 |   0.931220 |    1.425678
     2047 |   0.932120 |   0.584321 |   0.612456 |   0.913746 |    1.182345
    30031 |   0.941200 |   0.723145 |   0.925110 |   0.913447 |    1.091234
  1000001 |   0.948210 |   0.756342 |   1.000000 |   0.918210 |    1.023456

Wrote results for 4 candidates.


---

Direct Reading

Lowest penalty

1009

pen_norm = 0.000000


Interpretation:

1009 acts as the least suspicious object in this small batch. Its adjusted score remains unchanged.

Highest penalty

1000001

pen_norm = 1.000000


Interpretation:

1000001 is identified as the strongest symbolic regularity trap in the batch. Its adjusted score is reduced the most.

Intermediate traps

2047

30031


Both receive strong penalties, consistent with prior observations:

2047 as a Mersenne-style regularity trap

30031 as a primorial-plus-one regularity trap



---

Directional Validation

The smoke test confirms the expected directional behavior:

more regular symbolic objects receive larger penalties

less suspicious objects receive smaller penalties

omega_raw is preserved

omega_adjusted is computed independently

the module does not overwrite the original score



---

Minimal Valid Claim

This smoke test supports the following narrow claim:

SBC-Regularity v1 is operational as an isolated module and produces directionally coherent corrections on known regularity traps.


---

What This Does Not Yet Prove

This smoke test does not prove that:

the module is correctly integrated into engine

the adjusted score should replace the raw score by default

the module is fully validated beyond this batch


It only confirms that the correction layer itself is technically sound and behaves as expected on a minimal test set.


---

Final Compression

SBC-Regularity v1 now has:

a documented mathematical rationale

validated ranking improvements

validated behavior across larger ranges

a passing isolated smoke test


This is sufficient to justify the next step:

engine-level adapter integration while preserving omega_raw.

