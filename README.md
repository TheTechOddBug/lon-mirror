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

OMNIA does not assume determinism.

It uses deterministic structure as a diagnostic tool.

Given:

x(t+1) = F(x(t))

Then:

Same state + same law ⇒ same trajectory

If trajectories differ:

⇒ incomplete description  
⇒ hidden inputs  
⇒ non-deterministic dynamics  

OMNIA does not resolve which.

It detects divergence as **unresolved structure**.

---

## Extended Principle — Self-Model Divergence

Define:

S(t) = real state  
M(t) = internal model  

Dynamics:

S(t+1) = F(S(t), A(M(t)))  
M(t+1) = G(M(t), O(S(t)))

Metrics:

- E(t)   = d(S(t), M(t))  
- E_p(t) = d(S(t+1), P(M(t)))  
- C(t)   = d(M(t+1), G̃(M(t)))  

This introduces:

- dynamic instability  
- epistemic instability  

**Difference is unresolved structure.**

---

## Minimal Executable Systems (NEW)

OMNIA now includes **minimal deterministic systems** that convert:

theory → executable → measurable

---

### 1. Finite Structural Dynamics (mod 9)

File:

examples/structural_dynamics_mod9.py

System:

- space: residues mod 9  
- operator: x → kx (via digital root encoding)  
- output: orbit cycles  

Results:

- stable cycles exist  
- collapse vs permutation separation  
- independence from base representation  

Key law:

- gcd(k, 9) = 1 → permutation cycles  
- gcd(k, 9) ≠ 1 → structural collapse  

---

### 2. Generalized Dynamics (mod n)

File:

examples/structural_dynamics_modn.py

Extends system to:

- any n  
- any k  

Adds:

- orbit detection  
- regime classification  
- Ω (local coherence)

---

### 3. Global Structural Coherence

File:

examples/structural_dynamics_modn_global.py

Adds:

- Ω_global (system-level coherence)

Distinguishes:

- fully cyclic systems  
- partially collapsing systems  
- strongly dissipative systems  

---

### 4. Non-Numeric Domain (Strings)

File:

examples/structural_dynamics_strings.py

System:

- transformations on strings  
- structural lenses  
- Ω measurement  

Demonstrates:

- transfer of structure beyond mathematics  
- independence from numeric domain  

---

### 5. Multi-Lens Measurement (SCI)

File:

examples/omnia_sci_engine.py

Adds:

- multiple structural lenses  
- centroid comparison  
- SCI (Structural Compatibility Index)

SCI measures:

- agreement between independent structural views  

---

### 6. Validation Demo

File:

examples/omnia_validation_demo.py

Provides:

- deterministic classification  
- Ω + SCI combined interpretation  

Categories:

- stable_structure  
- false_coherence  
- instability  
- mixed  

---

### 7. Minimal OMNIA Engine

File:

examples/omnia_minimal_engine.py

Unified interface:

omnia_measure(x)

Supports:

- mod-n systems  
- strings  

This is the first **domain-agnostic measurement interface**.

---

## Emergent Structural Results

From the executable systems:

1. Structure ≠ representation  
2. Dynamics split into:
   - conservative (invertible)  
   - dissipative (collapsing)  
3. Existence of attractors  
4. Ω quantifies structural stability  
5. SCI quantifies inter-lens agreement  
6. High Ω does not imply agreement (false coherence)

---

## The OMNIA Measurement Chain

OMNIA  
→ Ω  
→ Ω under transformations  
→ Ω̂  
→ ΔΩ / ΔC  
→ SEI  
→ cycles  
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

---

## Structural Lenses

- BASE — Omniabase  
- TIME — Omniatempo  
- CAUSA — Omniacausa  
- TOKEN  
- LCR  

All lenses:

- deterministic  
- composable  
- non-semantic  

---

## Key Metrics

- Ω — structural coherence  
- Ω̂ — residual invariance  
- SEI — saturation  
- IRI — irreversibility  
- SCI — compatibility  
- SI — indistinguishability  
- SELF-MODEL ERROR — divergence  

---

## OMNIA-LIMIT

STOP when:

- SEI → 0  
- IRI > 0  
- Ω̂ stabilizes  

No continuation beyond structural exhaustion.

---

## Repository Structure

omnia/ examples/ structural_dynamics_mod9.py structural_dynamics_modn.py structural_dynamics_modn_global.py structural_dynamics_strings.py omnia_sci_engine.py omnia_minimal_engine.py omnia_validation_demo.py tests/ docs/ experiments/

---

## What OMNIA Is Not

- Not a model  
- Not a decision system  
- Not a learning system  

OMNIA is a **measurement instrument**.

---

## License

MIT License

---

## Citation

Brighindi, M.  
OMNIA — Unified Structural Measurement Engine (MB-X.01)  
https://github.com/Tuttotorna/lon-mirror




