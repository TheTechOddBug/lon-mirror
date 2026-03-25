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

It measures **structural coherence, instability, compatibility, limits, perturbations,
inference regimes, structural indistinguishability, and self-model divergence** of representations under
**independent, non-semantic transformations**.

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
- which inferential regime is active before collapse  
- when different internal codifications are structurally undecidable  
- when a system diverges from its own internal model  

**The output is measurement, never narrative.**

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

---

## Extended Principle — Self-Model Divergence

Determinism is not prediction.

It is diagnosis of difference.

A system evolves:

S(t+1) = F(S(t))

But real systems act on internal models:

S(t+1) = F(S(t), A(M(t)))  
M(t+1) = G(M(t), O(S(t)))

Divergence does not require randomness.

It can emerge from:

- incomplete observation  
- internal model mismatch  

Define:

E(t) = d( φ(S(t)), M(t) )  
E_p(t+1) = d( φ(S(t+1)), P(M(t)) )  
C(t) = d( M(t+1), G̃(M(t)) )

This introduces a second axis of instability:

- dynamic instability (Lyapunov)  
- epistemic instability (self-model error)  

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

Toy Self-Model Experiment (NEW)

Minimal operational system implementing:

real state S(t)

internal model M(t)

partial observation O(S(t))

self-model error E(t)

predictive error E_p(t)

internal coherence C(t)


Run:

python experiments/self_model_toy.py

This produces:

real trajectory

model trajectory

divergence metrics


Purpose:

convert theory → measurement

expose epistemic instability

isolate model-driven divergence



---

Stress Framework (Iriguchi Integration)

OMNIA includes a formal stress methodology.

Stress is not “more tests”.
Stress is controlled exposure of structural limits.

Failures are preserved as frozen boundary artifacts.

Official taxonomy:

docs/STRESS_TAXONOMY.md


---

The OMNIA Measurement Chain

OMNIA
→ Ω
→ Ω under transformations
→ Ω̂ (Omega-set)
→ ΔΩ / ΔC
→ SEI (Saturation)
→ A → B → A′
→ IRI (Irreversibility)
→ Inference State (S1–S5)
→ OMNIA-LIMIT (STOP)
→ SCI (Structural Compatibility)
→ CG (Runtime STOP / CONTINUE)
→ OPI (Observer Perturbation Index)
→ PV (Perturbation Vector)
→ SI (Structural Indistinguishability)
→ SELF-MODEL ERROR (E, E_p, C)
→ OMNIA-GOV (Trajectory Certification)

Each step is measured, never inferred.


---

1. Ω — Structural Coherence Score

Ω is the aggregated structural score produced by OMNIA lenses.

It reflects internal structural consistency, not correctness, usefulness, or semantic truth.

Ω is model-agnostic and semantics-free.


---

2. Structural Lenses

OMNIA operates through independent, composable lenses:

BASE — Omniabase
TIME — Omniatempo
CAUSA — Omniacausa
TOKEN
LCR — Logical Coherence Reduction

All lenses are deterministic, composable, and non-semantic.


---

3. APERSPECTIVE — Aperspective Invariance

Measures invariants that persist under transformations without a privileged observer.


---

4. Ω̂ — Omega-set (Residual Invariance)

Ω̂ is deduced by subtraction, not assumed.


---

5. SEI — Saturation / Exhaustion Index

SEI = ΔΩ / ΔC

SEI → 0 indicates structural saturation.


---

6. IRI — Irreversibility / Hysteresis Index

Measures irrecoverable structural loss:

A → B → A′


---

7. Pre-Limit Inference States — INFERENCE

S1 — RIGID_INVARIANCE
S2 — ELASTIC_INVARIANCE
S3 — META_STABLE
S4 — COHERENT_DRIFT
S5 — PRE_LIMIT_FRAGMENTATION


---

8. OMNIA-LIMIT — Epistemic Boundary

STOP when:

SEI → 0
IRI > 0
Ω̂ stable


---

9. Structural Time (τ)

Advances only when structure changes.


---

10. Structural Compatibility — SCI

Measures coexistence without contradiction.


---

11. Compatibility Guard — CG

Strict STOP / CONTINUE layer.

No policy. No semantics.


---

12. Observer Perturbation Index — OPI

OPI = Ω_ap − Ω_obs

Measures structural cost of observation.


---

13. Perturbation Vector — PV

Captures direction and intensity of structural loss.


---

14. Structural Indistinguishability — SI

If all structural relations are invariant → systems are undecidable.


---

15. SELF-MODEL ERROR — Epistemic Divergence Layer

Measures divergence between:

real state

internal model

predicted evolution


Detects:

internal misrepresentation

predictive failure

epistemic drift



---

16. OMNIA-GOV — Trajectory Certification Layer

Outputs:

ALLOW
BOUNDARY_ONLY
REFUSE

No semantics. No learning.


---

17. Experimental Module — Prime Regime Sensor

Non-semantic structural sensor on primes.


---

18. Repository Structure

omnia/
examples/
tests/
docs/
experiments/


---

19. What OMNIA Is Not

Not a model.
Not a policy.
Not a decision system.

OMNIA is a measurement instrument.


---

20. License

MIT License.


---

21. Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror