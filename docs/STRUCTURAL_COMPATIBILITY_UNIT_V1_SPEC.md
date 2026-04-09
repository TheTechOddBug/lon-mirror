# OMNIA — Structural Compatibility Unit v1 Spec

## Status

This document defines the first computable prototype of the structural compatibility unit introduced in v0.

Target object:

**U_v1(S1, S2) = (C, I, P)**

where:

- C = compatibility
- I = irreversibility
- P = purity / coherence

This is not yet a final canonical unit.
It is the first executable specification.

---

## 1. Objective

Transform the conceptual bundle defined in `STRUCTURAL_COMPATIBILITY_UNIT_V0.md`
into a directly computable output built from already existing OMNIA components.

The purpose is to measure not only distance,
but the structural status of a transition.

---

## 2. Input

Given a transition between two states:

- S1 = reference state
- S2 = observed state

and, when available, the trajectory context after rupture.

---

## 3. Output object

The first executable form is:

**U_v1(S1, S2) = (C, I, P)**

Each component must be bounded in [0, 1].

Interpretation:

- 0 = absence of the property
- 1 = maximal expression of the property

---

## 4. Component C — Compatibility

### Definition

C measures how much S2 remains structurally compatible with S1.

### Operational source

C is derived from the already available transition metric:

- dO
- transition zone

### First prototype

**C = 1 - dO**

with clamp into [0, 1].

### Interpretation

- C close to 1 -> same regime likely preserved
- C intermediate -> drift
- C low -> rupture

This is the most mature component and already operational.

---

## 5. Component I — Irreversibility

### Definition

I measures whether the transition indicates loss of recoverable regime continuity.

### Operational source

I is derived from break behavior and persistence:

- structural_break events
- consecutive break count
- inability to recover into equivalence
- failure of post-break commit

### First prototype

For v1, define:

- if assigned_zone != structural_break -> I = 0
- if assigned_zone == structural_break and no trajectory context yet -> I = 0.5
- if post-break sequence converges to a committed regime -> I = 0.5
- if post-break sequence remains chaotic -> I = 1.0

### Interpretation

- I = 0 -> no irreversibility detected
- I = 0.5 -> rupture exists, but final recoverability unresolved
- I = 1.0 -> rupture confirmed as structurally non-recoverable within the observed window

This is still a coarse component.
It is the least mature part of the bundle.

---

## 6. Component P — Purity / internal coherence

### Definition

P measures whether the emerging state or post-break candidate sequence has enough internal coherence to deserve stabilization.

### Operational source

P is derived from:

- candidate buffer coherence
- tau_commit
- tau_chaos
- candidate_internal_score

### First prototype

Outside candidate evaluation:

- if no candidate regime is active -> P = 0.5 by default neutrality

Inside candidate evaluation:

- if candidate_internal_score <= tau_commit -> P = 1.0
- if candidate_internal_score >= tau_chaos -> P = 0.0
- otherwise:
  P decreases linearly between tau_commit and tau_chaos

### Interpretation

- P close to 1 -> emerging structure is internally coherent
- P close to 0 -> emerging structure is chaotic
- P around 0.5 -> unresolved

This is the most direct expression of the post-break judgment layer.

---

## 7. Why U_v1 is a vector

A scalar would confuse distinct situations.

Examples:

### Case A
High distance, high purity:
- old regime is broken
- new regime is coherent

### Case B
High distance, low purity:
- old regime is broken
- no new regime exists

### Case C
Low distance, medium purity:
- system still near continuity
- emerging instability not yet resolved

These cases must not collapse into the same value.

Therefore v1 remains vectorial.

---

## 8. First readable semantics

The bundle can be read as:

- **C** -> "How much is the old regime still alive?"
- **I** -> "How irreversible is the rupture?"
- **P** -> "How much structural dignity does the new pattern have?"

This is not poetic language.
It is a readable interpretation of the three operational axes.

---

## 9. First implementation rule

For any tested transition, OMNIA should be able to emit:

```json
{
  "U_v1": {
    "C": 0.82,
    "I": 0.00,
    "P": 0.50
  }
}

or, after post-break observation:

{
  "U_v1": {
    "C": 0.12,
    "I": 1.00,
    "P": 0.00
  }
}

or:

{
  "U_v1": {
    "C": 0.18,
    "I": 0.50,
    "P": 1.00
  }
}


---

10. Strongest correct claim for v1

The strongest correct claim is:

U_v1 is the first executable approximation of a structural compatibility unit between states, implemented as a 3-axis bounded bundle.

It does not yet claim:

universality

canonical finality

theoretical closure


It claims only:

executable operational approximation



---

11. Immediate next step

Implement U_v1 in the benchmark engine so that every transition emits:

dO

zone

trajectory status

U_v1 = (C, I, P)


This is the next correct bridge between concept and code.

