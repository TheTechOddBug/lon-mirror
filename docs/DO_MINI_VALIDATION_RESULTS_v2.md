# OMNIA — dO Mini Validation Results v2

## Status

This document records the v0.2.1 execution of the dO mini validation protocol on the expanded synthetic validation set.

This is not a proof of universality.
It is the first operational baseline-level validation milestone for the current dO formulation.

Architectural boundary remains unchanged:

measurement != cognition != decision

---

## 1. Summary

Pairs tested: 36

- PASS: 33
- FAIL: 3

Family means:

- equivalent: mean_dO = 0.024105
- mild_variation: mean_dO = 0.181240
- structural_break: mean_dO = 0.458900

Observed ordering:

mean_dO(equivalent) < mean_dO(mild_variation) < mean_dO(structural_break)

This ordering held at the aggregate level in this run.

---

## 2. Progression

Observed progression across versions:

- v0.1: 15 / 36
- v0.2: 31 / 36
- v0.2.1: 33 / 36

This shows that the metric improved through structural correction,
not through ad hoc case-specific fitting.

Main corrections introduced across versions:

- explicit order-sensitive features
- explicit run-length sensitivity
- explicit local delta sensitivity
- explicit transformation cost
- explicit pre-canonicalization before signature extraction

---

## 3. What improved in v0.2.1

The v0.2.1 patch corrected failures caused by superficial input formatting before structural signature extraction.

Recovered cases include in particular:

- eq_v1_001: leading zeros
- eq_v1_010: currency symbol and numeric surface form

This supports the interpretation that v0.2 residual failures were concentrated in pre-ingestion and canonicalization, not in the structural core.

---

## 4. Residual failures

The remaining failures are:

- mv_v1_012
- br_v1_004
- br_v1_012

These are boundary cases, not gross collapses.

### 4.1 mv_v1_012

Case:

- state_1 = 1,2,3
- state_2 = 1,3,2

Observed behavior:

- predicted as equivalence instead of mild variation

Interpretation:

A single local swap in a very short sequence does not yet generate enough structural distance to exceed the equivalence threshold.

### 4.2 br_v1_004

Case:

- state_1 = 1,2,3,1,2,3
- state_2 = 1,2,3,4,5,6

Observed behavior:

- predicted as mild variation instead of structural break

Interpretation:

The shift from cyclic regime to linear regime is detected, but not with enough magnitude to cross the current break threshold.

### 4.3 br_v1_012

Case:

- state_1 = ++++++++
- state_2 = +-+-+-+-

Observed behavior:

- predicted as mild variation instead of structural break

Interpretation:

The oscillatory regime is structurally distinct from the uniform regime, but still falls just below the current break threshold.

---

## 5. What this result supports

This run supports the following minimal claim:

dO v0.2.1 is a usable operational baseline for separating:

- representational equivalence
- mild structural variation
- structural break

on the current 36-pair synthetic validation set.

It also supports the claim that the architecture is corrigible in a principled way:

performance improved through structural revisions without collapsing the existing separation.

---

## 6. What this result does not support

This run does not prove:

- universality across domains
- semantic correctness
- truth detection
- production robustness on real-world data
- final threshold optimality
- final completeness of the signature space

No stronger claim should be made from this result alone.

---

## 7. Operational interpretation

At this stage, v0.2.1 may be treated as the current baseline operative formulation of dO for synthetic structural validation.

This does not mean the metric is finished.

It means:

- the current formulation is stable enough to serve as a reference point
- future revisions must be compared against this baseline
- any further tuning must preserve or improve current separation without introducing overfitting

---

## 8. Next step

The next correct step is not broad architectural rewrite.

The next correct step is one of the following two:

1. freeze v0.2.1 as baseline and define regime-use rules on top of dO
2. perform one last narrow calibration pass on boundary cases only

The decision must be made explicitly and documented.