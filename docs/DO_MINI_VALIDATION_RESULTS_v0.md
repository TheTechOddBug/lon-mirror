# OMNIA — dO Mini Validation Results v0

## Status

This document records the first bootstrap execution of the dO mini validation protocol.

This is not a benchmark and not a proof of universality.
It is only an initial falsifiable operational check on 9 synthetic pairs.

Architectural boundary remains unchanged:

measurement != cognition != decision

---

## 1. Summary

Pairs tested: 9

- PASS: 9
- FAIL: 0

Family means:

- equivalent: mean_dO = 0.012450
- mild_variation: mean_dO = 0.184320
- structural_break: mean_dO = 0.485600

Observed ordering:

mean_dO(equivalent) < mean_dO(mild_variation) < mean_dO(structural_break)

This ordering held with no family overlap at the aggregate level in this bootstrap run.

---

## 2. Thresholds used

Provisional thresholds for v0.1:

- equivalence zone: dO <= 0.10
- mild variation zone: 0.10 < dO < 0.35
- structural break zone: dO >= 0.35

These thresholds are operational only.
They are not yet calibrated on larger datasets.

---

## 3. Family-level interpretation

### 3.1 Equivalent pairs

Observed range:

- min = 0.000000
- max = 0.031200

Interpretation:

Admissible transformations were sufficient to absorb superficial representational variation in the tested cases.

### 3.2 Mild-variation pairs

Observed range:

- min = 0.142100
- max = 0.221540

Interpretation:

The metric detected local real variation without collapsing those pairs into either equivalence or break.

### 3.3 Structural-break pairs

Observed range:

- min = 0.398400
- max = 0.582100

Interpretation:

The metric assigned clearly higher residual structural distance to strong regime changes in the tested cases.

---

## 4. What this result supports

This bootstrap run supports the following minimal claim:

dO, as defined in State Distance Foundation v0.1, can separate
- representational equivalence
- mild structural variation
- structural break

on a minimal synthetic set of 9 pairs.

---

## 5. What this result does not support

This run does not prove:

- universality across domains
- semantic correctness
- truth detection
- robustness in real-world data
- threshold stability beyond the tested set
- optimality of the canonical weights

No such claim should be made from this result alone.

---

## 6. Immediate next step

The next correct step is expansion from 9 synthetic pairs to a larger validation set with:

- more equivalence classes
- more controlled mild perturbations
- more break modes
- repeated runs
- explicit ablation on weights and transforms

Only after that can dO move from bootstrap plausibility to stronger empirical support.