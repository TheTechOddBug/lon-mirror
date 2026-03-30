## Canonical Index

- Ecosystem map: `ECOSYSTEM.md`
- Machine index: `repos.json`

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19318573.svg)](https://doi.org/10.5281/zenodo.19318573)

**DEMO**  
https://lon-reflect.emergent.host/

**MB-X.01**  
**Author:** Massimiliano Brighindi

**Core chain:** `Ω · Ω̂ · SEI · IRI · OMNIA-LIMIT · τ · SCI · CG · OPI · PV · INFERENCE · SI · GOV · SELF-MODEL ERROR`

---

## Canonical Ecosystem Map

This repository is part of the **MB-X.01 / OMNIA** ecosystem.

Canonical architecture and full ecosystem map:  
https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md

---

## Overview

**OMNIA** is a **post-hoc structural measurement engine**.

It measures **invariance, instability, compatibility, and limit conditions** under **independent, non-semantic transformations**.

OMNIA is designed to evaluate:

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

OMNIA is not a model, not a reasoning agent, and not a policy layer.

It is a **measurement instrument**.

Its role is to detect:

- what remains invariant when representation changes
- where continuation becomes structurally impossible
- how structure degrades under perturbation
- which inferential regime precedes collapse
- when two representations become structurally undecidable
- when a system diverges from its own internal model

**The output is measurement, never narrative.**

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

OMNIA does not define truth as semantic correctness, institutional authority, or interpretation.

It treats truth as **measured invariance under transformation**.

---

## Why This Repository Exists

This repository exists to formalize a strict architectural distinction:

**measurement ≠ cognition ≠ decision**

OMNIA occupies the **measurement layer only**.

Its purpose is to provide a deterministic, architecture-agnostic framework for evaluating structural behavior after outputs, transformations, or trajectories already exist.

That boundary is not secondary.  
It is the central design constraint.

---

## Quick Verification

A new visitor should be able to verify the repository through one compact example.

Suggested entry points:

### Minimal generic interface
- `examples/omnia_minimal_engine.py`

### Deterministic structural validation
- `examples/omnia_validation_demo.py`

### Multi-lens compatibility
- `examples/omnia_sci_engine.py`

Typical command pattern:

```bash
python examples/omnia_validation_demo.py

What to expect conceptually:

stable structures retain stronger coherence

unstable structures lose coherence faster under transformation

cross-lens disagreement lowers compatibility

false coherence can appear when one lens looks stable and another does not

structurally exhausted regimes approach limit conditions


The purpose of this quick verification step is not to prove every claim in the framework.

It is to make one point testable immediately:

OMNIA measures structural behavior under transformation rather than interpreting content.


---

Expected Structural Behavior

Across executable examples, the expected behavior is:

stable inputs retain higher Ω under perturbation

unstable inputs show faster Ω decay

cross-lens disagreement reduces SCI

structurally exhausted regimes push SEI toward zero

irreversible degradation yields positive IRI

high local coherence alone does not guarantee reliability

representational change does not necessarily destroy structure, but it reveals whether the structure was real or superficial


This matters because OMNIA should be readable as a measurement framework, not as a verbal claim.


---

Deterministic Diagnostic Principle

OMNIA does not assume that reality is deterministic.

It uses deterministic structure as a diagnostic principle.

Given:

x(t+1) = F(x(t))

Then:

same state + same law => same trajectory

If trajectories differ, then at least one of the following failed:

the state description is incomplete

hidden inputs exist

the governing law is non-deterministic


OMNIA does not force a metaphysical conclusion.

It treats divergence as a signal of unresolved structure.


---

Extended Principle — Self-Model Divergence

OMNIA also measures divergence between a system and its own internal model.

Define:

S(t) = real state

M(t) = internal model


Dynamics:

S(t+1) = F(S(t), A(M(t)))
M(t+1) = G(M(t), O(S(t)))

Metrics:

E(t)   = d(S(t), M(t))

E_p(t) = d(S(t+1), P(M(t)))

C(t)   = d(M(t+1), G̃(M(t)))


This introduces two distinct forms of instability:

dynamic instability

epistemic instability


Difference is treated as unresolved structure, not as narrative explanation.


---

Minimal Executable Systems

OMNIA includes minimal executable systems that convert:

theory -> executable process -> measurable structure

These systems are intentionally simple.

Their function is not scale, but clarity: they make the framework testable in compact, controlled settings.


---

1. Finite Structural Dynamics (mod 9)

File: examples/structural_dynamics_mod9.py

This system defines a finite dynamical space over residues modulo 9 and evaluates orbit behavior under multiplicative operators.

It demonstrates:

orbit cycles

stability vs collapse

separation between conservative and collapsing regimes

independence from surface representation


Key structural law:

gcd(k, 9) = 1 -> permutation cycles

gcd(k, 9) != 1 -> structural collapse



---

2. Generalized Dynamics (mod n)

File: examples/structural_dynamics_modn.py

This extends the same framework to arbitrary moduli and operators.

It adds:

orbit detection

regime classification

local coherence measurement through Ω


This is the first step from toy example to reusable structural analysis.


---

3. Global Structural Coherence

File: examples/structural_dynamics_modn_global.py

This adds a system-level coherence metric:

Ω_global


It distinguishes between:

fully cyclic systems

partially collapsing systems

strongly dissipative systems


This moves OMNIA from local trajectory inspection toward global regime characterization.


---

4. Non-Numeric Domain (Strings)

File: examples/structural_dynamics_strings.py

This example applies OMNIA-style measurement to strings.

It demonstrates:

structural analysis outside arithmetic domains

lens-based comparison

Ω measurement beyond numeric systems


This shows that the framework is not restricted to number-theoretic settings.


---

5. Multi-Lens Measurement (SCI)

File: examples/omnia_sci_engine.py

This example introduces multiple structural lenses and compares their outputs through centroid-level agreement.

It adds:

multi-lens evaluation

structural compatibility

SCI (Structural Compatibility Index)


SCI measures whether independent structural views agree or conflict.


---

6. Validation Demo

File: examples/omnia_validation_demo.py

This example combines Ω and SCI into a deterministic validation pipeline.

It produces structural regime classes such as:

stable_structure

false_coherence

instability

mixed


This matters because high coherence alone is not sufficient.
A system may appear coherent under one lens and fail under cross-lens comparison.


---

7. Minimal OMNIA Engine

File: examples/omnia_minimal_engine.py

This is the minimal domain-agnostic interface.

Unified entry point:

omnia_measure(x)

Supported example domains include:

mod-n systems

strings


This is the clearest compact demonstration of OMNIA as a generic structural measurement interface.


---

Emergent Structural Results

Across the executable systems, several stable results emerge:

1. Structure is not the same as representation


2. Dynamical regimes separate into:

conservative / invertible

dissipative / collapsing



3. Attractors and collapse basins can be measured structurally


4. Ω quantifies structural stability


5. SCI quantifies agreement across independent lenses


6. High Ω alone does not guarantee reliable structure
A system may exhibit false coherence



These results are intentionally small-scale, but they matter because they show that OMNIA is not merely conceptual.

It is an executable measurement framework.


---

The OMNIA Measurement Chain

The canonical measurement chain is:

OMNIA
-> Ω
-> Ω under transformations
-> Ω̂
-> ΔΩ / ΔC
-> SEI
-> cycles
-> IRI
-> INFERENCE states
-> OMNIA-LIMIT
-> SCI
-> CG
-> OPI
-> PV
-> SI
-> SELF-MODEL ERROR
-> GOV

This chain moves from local structural coherence to boundary detection, compatibility analysis, irreversibility, and regime certification.


---

Structural Lenses

OMNIA uses composable structural lenses.

Current canonical lenses include:

BASE — Omniabase

TIME — Omniatempo

CAUSA — Omniacausa

TOKEN

LCR


All lenses are:

deterministic

composable

non-semantic


Each lens measures structure through a different family of transformations.

Agreement across lenses is measured, not assumed.


---

Key Metrics

Ω — Structural Coherence

Measures the persistence of structure under transformation.

Ω̂ — Residual Invariance

Measures the invariant residue that remains after representational variation.

SEI — Saturation / Structural Exhaustion Index

Measures whether additional transformation still yields structural gain.

IRI — Irreversibility Index

Measures non-recoverable structural loss after transformation cycles.

SCI — Structural Compatibility Index

Measures agreement across independent structural lenses.

SI — Structural Indistinguishability

Measures when two representations become structurally undecidable.

SELF-MODEL ERROR

Measures divergence between a system and its own internal model.

τ — Structural Time

Measures regime progression in structural rather than wall-clock terms.

CG — Continuation Gate

Measures whether continuation remains structurally justified.

OPI / PV

Measure observer perturbation and the direction of perturbation-induced change.

GOV

Represents regime-level structural governance or certification logic.


---

OMNIA-LIMIT

OMNIA-LIMIT is the boundary condition of the framework.

The process stops when structural continuation is no longer justified.

Canonical stop conditions:

SEI -> 0

IRI > 0

Ω̂ stabilizes


At that point, continuation is not treated as deeper insight.
It is treated as structural exhaustion.

This is a stopping rule, not an interpretation layer.


---

What OMNIA Is Not

OMNIA is not:

a foundation model

a reasoning engine

a decision system

a learning system

a semantic interpreter

a policy layer

a generator of meaning


OMNIA does not explain content.

It measures structural persistence, degradation, compatibility, saturation, and limit conditions.


---

Positioning

OMNIA differs from standard evaluation or interpretability layers because it:

operates post hoc

does not depend on semantics

does not require retraining

does not decide

does not optimize

does not infer meaning from content

measures structural persistence across transformations

can detect saturation and irreversibility conditions


This repository should therefore be read as a structural measurement framework, not as a model claim.


---

Repository Structure

Main repository areas include:

omnia/

examples/

tests/

docs/

experiments/


Key executable examples include:

examples/structural_dynamics_mod9.py

examples/structural_dynamics_modn.py

examples/structural_dynamics_modn_global.py

examples/structural_dynamics_strings.py

examples/omnia_sci_engine.py

examples/omnia_minimal_engine.py

examples/omnia_validation_demo.py


Additional files define architectural boundaries, ecosystem structure, citation metadata, and integration logic.


---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror

