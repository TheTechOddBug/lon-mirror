## Canonical Index

- Ecosystem map: `ECOSYSTEM.md`
- Machine index: `repos.json`

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19318573.svg)](https://doi.org/10.5281/zenodo.19318573)

**DEMO**  
https://lon-reflect.emergent.host/

**Ω · Ω̂ · SEI · IRI · OMNIA-LIMIT · τ · SCI · CG · OPI · PV · INFERENCE · SI · GOV · SELF-MODEL ERROR**  
**MB-X.01**

**Author:** Massimiliano Brighindi

---

## Canonical Ecosystem Map

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

Canonical architecture and full ecosystem map:  
https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md

---

## Overview

**OMNIA** is a **post-hoc structural measurement engine**.

It is designed to measure structural properties of systems, outputs, trajectories, and representations under **independent, non-semantic transformations**.

OMNIA measures:

- structural coherence
- instability
- compatibility
- irreversibility
- saturation limits
- perturbation cost
- inference regimes
- structural indistinguishability
- self-model divergence

OMNIA does **not**:

- interpret meaning
- decide
- optimize
- learn
- explain

OMNIA is not a model and not a policy layer.

It is a **measurement instrument**.

Its function is to detect:

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

OMNIA does not treat truth as semantic correctness or authority.
It treats truth as **measured invariance under transformation**.

---

## Deterministic Diagnostic Principle

OMNIA does not assume that reality is deterministic.

It uses deterministic structure as a **diagnostic principle**.

Given:

x(t+1) = F(x(t))

Then:

**same state + same law ⇒ same trajectory**

If trajectories differ, at least one of the following failed:

- the state description is incomplete
- hidden inputs exist
- the law is non-deterministic

OMNIA does not force a metaphysical conclusion.
It treats divergence as a sign of **unresolved structure**.

---

## Extended Principle — Self-Model Divergence

OMNIA also measures the divergence between a system and its own internal model.

Define:

- S(t) = real state
- M(t) = internal model

Dynamics:

S(t+1) = F(S(t), A(M(t)))  
M(t+1) = G(M(t), O(S(t)))

Metrics:

- E(t)   = d(S(t), M(t))
- E_p(t) = d(S(t+1), P(M(t)))
- C(t)   = d(M(t+1), G̃(M(t)))

This introduces two additional layers of instability:

- **dynamic instability**
- **epistemic instability**

Difference is treated as unresolved structure, not as narrative explanation.

---

## Minimal Executable Systems

OMNIA includes minimal executable systems that turn:

**theory → executable process → measurable structure**

These systems are intentionally simple.
Their role is not scale, but clarity.

---

### 1. Finite Structural Dynamics (mod 9)

**File:** `examples/structural_dynamics_mod9.py`

This system defines a finite dynamical space over residues modulo 9 and evaluates orbit behavior under multiplicative operators.

It shows:

- orbit cycles
- stability vs collapse
- independence from surface representation

Key structural law:

- `gcd(k, 9) = 1` → permutation cycles
- `gcd(k, 9) ≠ 1` → structural collapse

---

### 2. Generalized Dynamics (mod n)

**File:** `examples/structural_dynamics_modn.py`

This extends the same framework to arbitrary moduli and operators.

It adds:

- orbit detection
- regime classification
- local coherence measurement through Ω

This is the first general step from toy example to reusable structural analysis.

---

### 3. Global Structural Coherence

**File:** `examples/structural_dynamics_modn_global.py`

This adds a system-level coherence measure:

- `Ω_global`

It distinguishes between:

- fully cyclic systems
- partially collapsing systems
- strongly dissipative systems

This moves OMNIA from local trajectory inspection to global regime characterization.

---

### 4. Non-Numeric Domain (Strings)

**File:** `examples/structural_dynamics_strings.py`

This example applies OMNIA-style measurement to strings.

It demonstrates:

- structural analysis outside arithmetic domains
- lens-based comparison
- Ω measurement beyond numeric systems

This matters because it shows that the framework is not tied to number theory.

---

### 5. Multi-Lens Measurement (SCI)

**File:** `examples/omnia_sci_engine.py`

This example introduces multiple structural lenses and compares their outputs through centroid-level agreement.

It adds:

- multi-lens evaluation
- structural compatibility
- `SCI` (Structural Compatibility Index)

SCI measures whether independent structural views agree or conflict.

---

### 6. Validation Demo

**File:** `examples/omnia_validation_demo.py`

This example combines Ω and SCI into a deterministic validation pipeline.

It produces regime classes such as:

- `stable_structure`
- `false_coherence`
- `instability`
- `mixed`

This is useful because high coherence alone is not sufficient.
A system can appear coherent in one lens and fail under cross-lens agreement.

---

### 7. Minimal OMNIA Engine

**File:** `examples/omnia_minimal_engine.py`

This is the minimal domain-agnostic interface.

Unified entry point:

`omnia_measure(x)`

Supported examples include:

- mod-n systems
- strings

This is the clearest demonstration of OMNIA as a generic structural measurement interface.

---

## Emergent Structural Results

Across the executable systems, several stable results emerge:

1. **Structure is not the same as representation**
2. Dynamical regimes split into:
   - conservative / invertible
   - dissipative / collapsing
3. Attractors and collapse basins can be measured structurally
4. `Ω` quantifies structural stability
5. `SCI` quantifies agreement across independent lenses
6. High `Ω` alone does not imply reliable structure  
   A system may exhibit **false coherence**

These results are small-scale but important:
they show that OMNIA is not only a conceptual layer, but an executable measurement framework.

---

## The OMNIA Measurement Chain

The full measurement chain is:

**OMNIA**  
→ **Ω**  
→ **Ω under transformations**  
→ **Ω̂**  
→ **ΔΩ / ΔC**  
→ **SEI**  
→ **cycles**  
→ **IRI**  
→ **INFERENCE states**  
→ **OMNIA-LIMIT**  
→ **SCI**  
→ **CG**  
→ **OPI**  
→ **PV**  
→ **SI**  
→ **SELF-MODEL ERROR**  
→ **OMNIA-GOV**

This chain moves from local structural coherence to global boundary detection and regime certification.

---

## Structural Lenses

OMNIA uses composable structural lenses.

Current canonical lenses include:

- **BASE** — Omniabase
- **TIME** — Omniatempo
- **CAUSA** — Omniacausa
- **TOKEN**
- **LCR**

All lenses are:

- deterministic
- composable
- non-semantic

Each lens measures structure from a different transformation family.
Agreement across lenses is measured, not assumed.

---

## Key Metrics

### Ω — Structural Coherence
Measures the persistence of structure under transformation.

### Ω̂ — Residual Invariance
Measures the invariant residue that remains after representational variation.

### SEI — Saturation / Structural Exhaustion Index
Measures whether additional transformation still yields structural gain.

### IRI — Irreversibility Index
Measures non-recoverable structural loss after transformation cycles.

### SCI — Structural Compatibility Index
Measures agreement across independent structural lenses.

### SI — Structural Indistinguishability
Measures when two representations become structurally undecidable.

### SELF-MODEL ERROR
Measures divergence between a system and its own internal model.

---

## OMNIA-LIMIT

`OMNIA-LIMIT` is the boundary condition of the framework.

The process stops when structural continuation is no longer justified.

Canonical stop conditions:

- `SEI → 0`
- `IRI > 0`
- `Ω̂` stabilizes

At that point, continuation is not treated as deeper insight.
It is treated as structural exhaustion.

This is a stopping rule, not a narrative interpretation.

---

## Repository Structure

Main areas of the repository include:

- `omnia/`
- `examples/`
- `tests/`
- `docs/`
- `experiments/`

Key executable examples include:

- `examples/structural_dynamics_mod9.py`
- `examples/structural_dynamics_modn.py`
- `examples/structural_dynamics_modn_global.py`
- `examples/structural_dynamics_strings.py`
- `examples/omnia_sci_engine.py`
- `examples/omnia_minimal_engine.py`
- `examples/omnia_validation_demo.py`

Additional files define boundaries, ecosystem structure, citation metadata, and integration logic.

---

## What OMNIA Is Not

OMNIA is **not**:

- a foundation model
- a reasoning engine
- a decision system
- a learning system
- a semantic interpreter
- a policy layer

OMNIA does not generate meaning.
It measures structural persistence, degradation, compatibility, and limit conditions.

---

## Why This Repository Exists

This repository exists to formalize a strict distinction:

**measurement ≠ cognition ≠ decision**

OMNIA occupies the measurement layer only.

Its purpose is to provide a deterministic, architecture-agnostic framework for evaluating structural behavior after outputs, transformations, or trajectories already exist.

That boundary is not secondary.
It is the central design constraint.

---

## License

MIT License

---

## Citation

**Brighindi, M.**  
**OMNIA — Unified Structural Measurement Engine (MB-X.01)**  
https://github.com/Tuttotorna/lon-mirror

