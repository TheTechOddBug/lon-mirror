## Canonical Index

- Ecosystem map: `ECOSYSTEM.md`
- Machine index: `repos.json`

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19217482.svg)](https://doi.org/10.5281/zenodo.19217482)

DEMO  
https://lon-reflect.emergent.host/

**Ω · Ω̂ · SEI · IRI · OMNIA-LIMIT · τ · SCI · CG · OPI · PV · INFERENCE · SI · GOV · SELF-MODEL ERROR**  
**MB-X.01**

**Author:** Massimiliano Brighindi

---

## Canonical Ecosystem Map

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

Canonical architecture and full map:  
https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md

---

## Overview

**OMNIA** is a **post-hoc structural measurement engine**.

It measures:

- structural coherence  
- instability  
- compatibility  
- irreversibility  
- saturation limits  
- perturbation cost  
- inference regimes  
- structural indistinguishability  
- self-model divergence  

under **independent, non-semantic transformations**.

OMNIA:

- does **not** interpret meaning  
- does **not** decide  
- does **not** optimize  
- does **not** learn  
- does **not** explain  

OMNIA measures:

- what remains invariant when representation changes  
- where continuation becomes structurally impossible  
- how structure degrades under perturbation  
- which inferential regime precedes collapse  
- when representations become undecidable  
- when a system diverges from its own internal model  

**The output is measurement, never narrative.**

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

---

## Deterministic Diagnostic Principle

OMNIA does not assume that reality is deterministic.

It uses deterministic structure as a diagnostic tool.

Given a system:

x(t+1) = F(x(t))

Then:

Same state + same law ⇒ same trajectory

If trajectories differ:

⇒ the observed description is incomplete  
⇒ or the system includes unmodeled inputs  
⇒ or the dynamics are non-deterministic  

OMNIA does not resolve which case is true.

It detects divergence as **unresolved structure**.

---

## Extended Principle — Self-Model Divergence

Real systems do not act directly on reality.

They act on internal representations.

Define:

S(t) = real state  
M(t) = internal model  

Dynamics:

S(t+1) = F(S(t), A(M(t)))  
M(t+1) = G(M(t), O(S(t)))

Divergence emerges from:

- incomplete observation  
- model mismatch  
- internal inconsistency  

Define:

E(t)   = d( S(t), M(t) )  
E_p(t) = d( S(t+1), P(M(t)) )  
C(t)   = d( M(t+1), G̃(M(t)) )

Where:

- E(t)   = self-model error  
- E_p(t) = predictive error  
- C(t)   = internal coherence  

**Difference is not noise.  
It is unresolved structure.**

---

## Quickstart

Run the full test suite:

```bash
pytest tests/ -v

Run the prime regime demo:

python examples/prime_gap_knn_demo.py


---

Minimal Structural Example (NEW)

File:

examples/structural_dynamics_mod9.py

This is the first minimal executable system demonstrating:

structure vs representation

invariance under transformation

finite-state structural dynamics


System:

space: residues mod 9

operator: ( x \rightarrow kx ) (via digital root encoding)

output: orbit cycles


What it shows:

existence of stable cycles

separation between invertible and collapsing dynamics

independence from base-10 representation


Key structural result:

if gcd(k, 9) = 1 → permutation cycles

if gcd(k, 9) ≠ 1 → collapse toward fixed point (9)


This file is:

deterministic

reproducible

representation-independent (structure preserved)


It is a minimal bridge between:

theory → executable system


---

Toy Self-Model Experiment

Run:

python experiments/self_model_toy.py

Outputs:

real trajectory

model trajectory

E(t), E_p(t), C(t)


Purpose:

expose epistemic instability

measure divergence

convert theory → measurement



---

Stress Framework

Reference:

docs/STRESS_TAXONOMY.md

Stress = controlled exposure of structural limits.

Failures are preserved as boundary artifacts.


---

The OMNIA Measurement Chain

OMNIA
→ Ω
→ Ω under transformations
→ Ω̂
→ ΔΩ / ΔC
→ SEI
→ trajectory cycles
→ IRI
→ INFERENCE states
→ OMNIA-LIMIT
→ SCI
→ CG
→ OPI
→ PV
→ SI
→ SELF-MODEL ERROR
→ OMNIA-GOV

Each step is measured, never inferred.


---

Structural Lenses

BASE — Omniabase

TIME — Omniatempo

CAUSA — Omniacausa

TOKEN

LCR


All lenses are:

deterministic

composable

non-semantic



---

Key Metrics

Ω — structural coherence

Ω̂ — residual invariance

SEI — saturation (ΔΩ / ΔC)

IRI — irreversibility

SCI — compatibility

SI — indistinguishability

SELF-MODEL ERROR — divergence



---

OMNIA-LIMIT

STOP condition when:

SEI → 0

IRI > 0

Ω̂ stabilizes


No continuation beyond structural exhaustion.


---

Repository Structure

omnia/
examples/
  └── structural_dynamics_mod9.py
tests/
docs/
experiments/


---

What OMNIA Is Not

Not a model

Not a decision system

Not a learning system


OMNIA is a measurement instrument.


---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror

