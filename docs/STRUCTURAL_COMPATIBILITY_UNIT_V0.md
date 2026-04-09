# OMNIA — Structural Compatibility Unit v0

## Status

This document defines the first formal approximation of the original target:
a measurable unit of structural relation between states.

This is not a universal final unit.
It is the first explicit formulation of what the unit must measure.

---

## 1. Goal

We want a quantity that does not measure raw content,
but the structural relation between two states.

The target is not:

- semantic truth
- prediction accuracy
- surface similarity

The target is:

- how much two states still belong to the same regime
- how much identity is preserved across transition
- whether the change is recoverable, irreversible, or chaotic

---

## 2. Core intuition

A state is not just an output.
A state is an observable configuration.

A regime is not just a label.
A regime is a class of mutually compatible states.

Therefore, the desired unit must measure:

**structural compatibility between states under allowed transformations**

---

## 3. Minimal object of measurement

Given two states:

- S1
- S2

we define the target quantity as a bounded compatibility object:

**U(S1, S2)**

where U is not yet a single final scalar,
but a structured measurement bundle.

---

## 4. First proposed decomposition

The unit is decomposed into three components:

### 4.1 Compatibility component

Measures how much S2 is still structurally compatible with S1.

Operational prototype already available:

- dO
- equivalence / mild_variation / structural_break

Interpretation:

- low distance -> same regime likely preserved
- medium distance -> drift
- high distance -> rupture

### 4.2 Irreversibility component

Measures whether the transition from S1 to S2 destroys recoverable structure.

Operational sources already partially present in the ecosystem:

- IRI
- break persistence
- inability to reconstruct a stable regime from later states

Interpretation:

- low irreversibility -> transition may still be absorbed
- high irreversibility -> regime loss is real

### 4.3 Purity / source coherence component

Measures whether the emerging state sequence is internally coherent enough to become a real baseline.

Operational sources already partially present in the ecosystem:

- candidate buffer consistency
- tau_commit
- tau_chaos
- purity-oriented layers from the wider ecosystem

Interpretation:

- high internal coherence -> candidate new regime
- high internal incoherence -> chaos, no commit

---

## 5. First operational form

The first honest formulation is therefore not a single number, but:

**U_v0(S1, S2) = (C, I, P)**

where:

- C = compatibility
- I = irreversibility
- P = purity / internal coherence

This is the first meaningful approximation of a structural state unit.

---

## 6. Why this is better than a single scalar

A single scalar would collapse different realities into one value.

Example:

- two states may be distant but still converge into a coherent new regime
- two states may be distant and also mutually chaotic
- two states may be close but structurally fragile

Therefore one scalar alone is too poor.

The correct first step is a vector-like unit.

---

## 7. Connection to Omniabase

Omniabase introduced the foundational intuition:

no single representation should be treated as privileged.

Therefore the true structural content of a state must be sought through:

- multiple representations
- multiple transformations
- invariance under perspective change

This means the structural unit must not depend on one encoding only.

The unit must emerge from what remains stable across valid representation changes.

---

## 8. Connection to OMNIA

OMNIA already provides the first operational skeleton of this unit:

- sigma -> structural signature
- dO -> distance between states
- protocol -> local classification
- memory -> temporal persistence
- post-break commit -> new regime confirmation
- tau_chaos -> refusal of false stabilization

Therefore the current system is not yet the final unit,
but already the first executable approximation of it.

---

## 9. Strongest correct claim

The strongest correct claim at this stage is:

**OMNIA already implements a first operational approximation of a structural compatibility unit between states.**

This does not yet mean:

- universal measurement
- final canonical metric
- theory closure

It means:

- the target object now has an executable skeleton

---

## 10. Next formal step

The next correct step is to define a computable prototype for:

**U_v1(S1, S2) = (C, I, P)**

using already existing OMNIA components.

That means:

- C from dO and transition zone
- I from break persistence and recovery failure
- P from candidate internal coherence and chaos refusal

Only after that should we test whether a scalar projection is possible.

---

## 11. Minimal conclusion

The original goal should no longer be described vaguely as
"finding the unit of measure".

It should now be described precisely as:

**building a structural compatibility unit between states.**

That is where the work has actually arrived.