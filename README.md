## Canonical Index

- Ecosystem map: [ECOSYSTEM.md](ECOSYSTEM.md)
- Machine index: [repos.json](repos.json)

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19318573.svg)](https://doi.org/10.5281/zenodo.19318573)

**DEMO**  
https://lon-reflect.emergent.host/

**MB-X.01**  
**Author:** Massimiliano Brighindi

---

## Overview

OMNIA is a **post-hoc structural measurement engine**.

It measures:

- invariance
- instability
- compatibility
- saturation
- irreversibility

under **independent, non-semantic transformations**.

OMNIA detects:

- what remains invariant when representation changes
- where structure degrades
- where continuation becomes unjustified
- when systems become irreversibly altered
- when representations become indistinguishable

OMNIA does NOT:

- interpret meaning  
- decide  
- optimize  
- learn  
- explain  

**Output = measurement only**

---

## Core Principle

**Truth = invariance under transformation**

Not:

- semantics  
- authority  
- interpretation  

---

## Architectural Boundary

Strict constraint:

**measurement ≠ cognition ≠ decision**

OMNIA:

- does not generate outputs  
- does not modify models  
- does not choose actions  

It measures structure only.

---

## Quick Verification

Run:

```bash
python examples/omnia_validation_demo.py

Expected behavior:

stable inputs → higher Ω

unstable inputs → faster Ω decay

disagreement → lower SCI

saturation → SEI → 0

irreversibility → IRI > 0



---

Quick Experiment — Structural Divergence (TΔ)

Standalone demo:

python examples/divergence_time_demo_standalone.py

What it does:

generates two nearby trajectories

computes Δ(t)

measures structural degradation over time

detects divergence point


Output:

TΔ unstable

TΔ collapse


Note:

no dependencies

not OMNIA

implementation-sensitive


Purpose:

minimal reproducibility

demonstration of structural divergence



---

Minimal Executable Systems

Examples:

examples/omnia_validation_demo.py

examples/omnia_minimal_engine.py

examples/omnia_sci_engine.py

examples/divergence_time_demo_standalone.py


Additional structural demos:

examples/structural_dynamics_mod9.py

examples/structural_dynamics_modn.py

examples/structural_dynamics_modn_global.py

examples/structural_dynamics_strings.py


These convert:

theory → execution → measurable structure


---

Key Metrics

Ω — Structural Coherence
Persistence under transformation

SCI — Structural Compatibility
Agreement across lenses

SEI — Saturation Index
Remaining structural gain

IRI — Irreversibility Index
Non-recoverable loss

OMNIA-LIMIT
Formal stop condition


---

Structural Lenses

Canonical lenses:

BASE (Omniabase)

TIME (Omniatempo)

CAUSA (Omniacausa)

TOKEN

LCR


Properties:

deterministic

composable

non-semantic


Agreement is measured, not assumed.


---

OMNIA-LIMIT

Stop conditions:

SEI → 0

IRI > 0

Ω̂ stable


Interpretation:

no further structural extraction possible

continuation = non-informative



---

Positioning

OMNIA is not:

a model

an evaluator

an interpreter


OMNIA is:

post-hoc

model-agnostic

semantics-free

transformation-based


It measures:

structural persistence

structural collapse

structural limits



---

Repository Structure

omnia/ → measurement core

examples/ → executable demos

tests/ → verification

docs/ → formal definitions

experiments/ → exploratory modules



---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror