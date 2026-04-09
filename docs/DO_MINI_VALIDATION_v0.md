# OMNIA — dO Mini Validation v0

## Status

This document defines the first falsifiable validation protocol for the OMNIA state-distance unit:

dO = delta-Omnia

Goal:

test whether Delta_Omega behaves coherently across three minimal structural regimes:

1. representational equivalence
2. mild structural variation
3. clear structural rupture

This is a minimal validation protocol.
Not a benchmark.
Not a proof of universality.

---

## 1. Principle

For a useful structural distance, the following ordering must hold:

dO(equivalent) < dO(mild_variation) < dO(structural_break)

If this ordering fails systematically, the metric is invalid or badly specified.

---

## 2. Test families

### Family A — Representational equivalence

Two states differ only by admissible representation changes.

Examples:

- original text vs reordered but structurally preserved encoding
- numeric sequence vs equivalent base-transformed representation
- compressed / decompressed representation with preserved structure
- representation-preserving rewrite

Expected result:

- dO should remain low
- kappa should remain high

Target condition:

dO <= epsilon_eq

---

### Family B — Mild structural variation

Two states differ by small but real structural variation.

Examples:

- one local perturbation
- one token / symbol substitution
- one bounded numeric modification
- one small trajectory deformation

Expected result:

- dO should increase relative to Family A
- increase should remain moderate
- drift-sensitive components may activate

Target condition:

epsilon_eq < dO < epsilon_break

---

### Family C — Structural break

Two states differ by strong non-removable structural change.

Examples:

- incompatible ordering regime
- major perturbation across multiple positions
- broken dependency structure
- trajectory with regime shift

Expected result:

- dO should become clearly high
- kappa should decrease sharply
- break-sensitive behavior should appear

Target condition:

dO >= epsilon_break

---

## 3. Minimal ordering criterion

The protocol passes if the following ordering holds on the aggregate:

mean_dO(Family_A) < mean_dO(Family_B) < mean_dO(Family_C)

and if overlap remains limited.

A stricter version may require:

max_dO(Family_A) < median_dO(Family_B)
max_dO(Family_B) < median_dO(Family_C)

---

## 4. Default thresholds for v0.1

These thresholds are provisional and operational only.

- epsilon_eq = 0.10
- epsilon_break = 0.35

Interpretation:

- dO <= 0.10 -> structural equivalence zone
- 0.10 < dO < 0.35 -> mild variation zone
- dO >= 0.35 -> structural break candidate

These thresholds are not final.
They are initial validation anchors.

---

## 5. Required outputs

For each pair (S1, S2), compute and store:

- Delta_Omega(S1, S2)
- kappa(S1, S2)
- optional epsilon(S1 -> S2) if order exists
- test family label
- pass / fail against expected zone

---

## 6. Failure modes

The protocol fails if one or more of the following occur:

1. equivalent pairs repeatedly produce high dO
2. mild-variation pairs collapse into equivalence zone
3. structural-break pairs remain near equivalence zone
4. ordering between families is unstable across repeated runs
5. normalization or transformation choice dominates the result arbitrarily

---

## 7. Minimal claim

If the protocol passes, OMNIA gains an initial falsifiable operational basis for:

dO as a state-distance unit

If the protocol fails, dO must be revised before broader use.

---

## 8. Architectural boundary

This protocol does not test:

- semantics
- truth
- correctness
- usefulness
- decision quality

It tests only:

whether OMNIA can separate structural equivalence, mild variation, and structural rupture
using Delta_Omega.