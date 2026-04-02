# Temporal Kernel (Δ / Structural Time)

## Definition

Structural time is not physical time.

It is defined as cumulative structural change:

T = Σ Δ_t

where:

Δ_t = structural difference between consecutive states

---

## Critical Clarification

TΔ is NOT time.

TΔ is the moment structural equivalence breaks.

It does not measure duration.  
It measures loss of invariance.

---

## Interpretation

Given two initially equivalent states:

S₀ ≈ S₀′

We track their evolution:

S(t), S′(t)

Structural divergence is defined as:

Δ(t) = distance(S(t), S′(t))

---

## Divergence Time (TΔ)

TΔ is the first t such that:

Δ(t) > ε

where ε is a structural tolerance threshold.

Meaning:

- before TΔ → structures are equivalent  
- after TΔ → equivalence is broken  

---

## Structural Regimes

### Stable

- Δ(t) remains bounded  
- no divergence  
- TΔ = ∅  

### Transitional

- Δ(t) grows slowly  
- delayed divergence  
- TΔ large  

### Collapse

- Δ(t) grows rapidly  
- early divergence  
- TΔ small  

### Immediate Collapse

- Δ(0) > ε  
- no structural equivalence  
- TΔ = 0  

---

## Irreversibility (IRI)

After divergence:

S(t) → S′(t)

Attempt recovery:

S′(t) → S″(t)

If:

S″(t) ≠ S(t)

then:

IRI > 0

Meaning:

- structure cannot be restored  
- information is lost  

---

## Resilience (R)

Resilience measures recovery capacity:

R = f(T_unstable, T_collapse, T_recovery)

Interpretation:

- high R → recovery possible  
- low R → persistent divergence  

---

## Key Properties

- non-semantic  
- deterministic  
- transformation-based  
- representation-invariant  

---

## What It Measures

Temporal Kernel detects:

- when two equivalent structures diverge  
- how fast divergence occurs  
- whether recovery is possible  
- whether collapse is irreversible  

---

## What It Does NOT Measure

- physical time  
- meaning  
- causality interpretation  
- prediction  

---

## Role in OMNIA

Temporal Kernel extends OMNIA from:

static measurement → dynamic structural diagnostics

It connects:

Ω → coherence  
TΔ → divergence  
IRI → irreversibility  
R → recovery  

---

## Minimal Implementation Reference

See:

- examples/divergence_time_demo_standalone.py  
- examples/divergence_benchmark.py  
- examples/resilience_benchmark.py  

---

## Summary

Structural time is not duration.

It is the accumulation of structural change.

TΔ marks the exact point where equivalence fails.

After TΔ:

- systems are no longer interchangeable  
- structure may degrade  
- recovery may or may not occur  

OMNIA does not track time.

It tracks the loss of structure across transformations.