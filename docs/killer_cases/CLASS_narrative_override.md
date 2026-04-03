file: docs/killer_cases/CLASS_narrative_override.md

# OMNIA — Structural Class Definition
## Class: narrative_override

---

## Definition

A failure mode where:

- a **correct computation path is fully established**
- the system **abandons the computed result**
- replaces it with a **heuristic / non-derived value**

\[
\boxed{\text{correct structure → overridden by non-structural substitution}}
\]

---

## Core Properties

- local reasoning: coherent
- arithmetic: correct
- transformation chain: valid up to break point
- failure: introduced at final stage

---

## Structural Signature (Invariant)

### Omega
- stable during reasoning
- sharp decay at override

### SCI
- local: high
- global: broken

### SEI
- high on correct structure
- false saturation before override

### IRI
- positive (irreversible deviation)

### TDelta
- located at override point
- strictly precedes final error

---

## Break Mechanism

Type:
- substitution of computed value with heuristic estimate

Forms:
- "approximation reasoning"
- "intuitive correction"
- "back-to-original bias"
- "rounding intuition"

---

## Necessary Conditions

1. correct derivation exists
2. no arithmetic error in core path
3. override occurs after valid result
4. replacement value is not derived
5. final answer remains plausible

---

## Failure Pattern

\[
\text{Exact Result} \rightarrow \text{Override} \rightarrow \text{Plausible Error}
\]

---

## Detection Rule (OMNIA)

Detect when:

- Omega drops after stable phase
- SCI divergence appears (local vs global)
- SEI saturates on pre-override state
- IRI becomes positive at override
- TDelta < final_error

---

## Canonical Examples

### killer_case_01
- discount + tax
- override: 70.4 → 80

### killer_case_02
- total price with discount
- override: 95 → 100

### killer_case_03
- discount + tax
- override: 107.1 → 120

---

## Class Status

\[
\boxed{\text{STRUCTURALLY CONSISTENT CLASS}}
\]

- pattern repeated ≥ 3 times
- invariant metric behavior observed
- early detection confirmed

---

## Epistemic Boundary

- no semantic interpretation
- no domain knowledge
- purely structural measurement

---

## Operational Use

This class is:

- reproducible
- detectable early (TDelta)
- non-trivial (plausible final answers)

---

## System Role

First confirmed class demonstrating:

\[
\boxed{\text{early structural instability detection on plausible reasoning}}
\]

---

## Status

[CLASS FROZEN]
[READY FOR MULTI-CLASS EXPANSION]