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

This introduces a second axis of instability:

- dynamic instability (sensitivity to initial conditions)  
- epistemic instability (model divergence)  

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

Toy Self-Model Experiment

Minimal executable system implementing:

real state S(t)

internal model M(t)

partial observation

measurable divergence


Run:

python experiments/self_model_toy.py

Outputs:

real trajectory

model trajectory

E(t), E_p(t), C(t)


Purpose:

convert theory → measurement

expose epistemic instability

isolate model-driven divergence



---

Stress Framework

OMNIA includes a formal stress methodology.

Stress is not repetition.

Stress is controlled exposure of structural limits.

Failures are preserved as boundary artifacts.

Reference:

docs/STRESS_TAXONOMY.md


---

The OMNIA Measurement Chain

OMNIA
→ Ω
→ Ω under transformations
→ Ω̂ (Omega-set)
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
→ SELF-MODEL ERROR (E, E_p, C)
→ OMNIA-GOV

Each step is measured, never inferred.


---

1. Ω — Structural Coherence

Aggregated structural consistency.

Semantics-free.


---

2. Structural Lenses

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

3. APERSPECTIVE

Invariance without privileged observer.


---

4. Ω̂ — Residual Invariance

Computed by subtraction.


---

5. SEI — Saturation

SEI = ΔΩ / ΔC

SEI → 0 ⇒ structural exhaustion


---

6. IRI — Irreversibility

Measures loss across cycles.


---

7. INFERENCE States

S1 → rigid
S2 → elastic
S3 → meta-stable
S4 → drift
S5 → fragmentation


---

8. OMNIA-LIMIT

STOP condition:

SEI → 0

IRI > 0

Ω̂ stable



---

9. Structural Time (τ)

Advances only with structural change.


---

10. SCI — Compatibility

Coexistence without contradiction.


---

11. CG — Guard

Binary STOP / CONTINUE.


---

12. OPI — Observer Cost

OPI = Ω_ap − Ω_obs


---

13. PV — Perturbation

Direction + intensity of loss.


---

14. SI — Indistinguishability

No structural distinction possible.


---

15. SELF-MODEL ERROR

Measures divergence between:

real state

internal representation

predicted evolution


Detects:

misrepresentation

predictive failure

epistemic drift



---

16. OMNIA-GOV

Trajectory certification:

ALLOW

BOUNDARY_ONLY

REFUSE



---

17. Repository Structure

omnia/
examples/
tests/
docs/
experiments/


---

18. What OMNIA Is Not

Not a model

Not a decision system

Not a learning system


OMNIA is a measurement instrument.


---

19. License

MIT License


---

20. Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror

