## Canonical Index

- Ecosystem map: [ECOSYSTEM.md](ECOSYSTEM.md)
- Machine index: [repos.json](repos.json)

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19356116.svg)](https://doi.org/10.5281/zenodo.19356116)

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
- divergence over structural time  

under **independent, non-semantic transformations**.

OMNIA detects:

- what remains invariant when representation changes  
- where structure degrades  
- where continuation becomes unjustified  
- when systems become irreversibly altered  
- when representations become indistinguishable  
- when structural trajectories diverge  

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

## Structural Dynamics

Minimal formalism:

- Ω(t) — Local Structural Coherence  
- TΔ — Structural Divergence Time  
- IRI — Irreversibility Index  
- R — Structural Resilience  

Extended dynamics:

- divergence detection  
- collapse detection  
- recovery detection  

See:

docs/TDELTA_IRI_FORMALISM_MINIMAL.md

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

Temporal Kernel (Δ Structural Time)

Core addition:

Temporal Kernel introduces time as structural divergence, not physical time.

Definition:

T = Σ Δ_t

Δ_t = structural change between states


Capabilities:

detects divergence onset

identifies collapse thresholds

measures trajectory instability

distinguishes stable vs chaotic regimes


Implementation:

docs/TEMPORAL_KERNEL.md
examples/divergence_time_demo_standalone.py
examples/divergence_benchmark.py
examples/resilience_benchmark.py


---

Quick Experiment — Structural Divergence (TΔ)

python examples/divergence_time_demo_standalone.py

What it does:

generates two nearby trajectories

computes Δ(t)

detects structural divergence


Output:

TΔ unstable

TΔ collapse


Properties:

deterministic

minimal

no dependencies


Purpose:

isolate structural divergence independently from OMNIA



---

Benchmark — Divergence Across Systems

python examples/divergence_benchmark.py

What it does:

compares multiple systems

computes TΔ

computes IRI

classifies regimes


Systems:

logistic (stable / transitional / chaotic)

linear contraction

random sequences


Example:

System: logistic_r3.9
TΔ: 18
IRI: 0.92
Regime: COLLAPSE

System: linear_0.8
TΔ: None
IRI: 0.00
Regime: STABLE

System: random
TΔ: 0
IRI: 1.00
Regime: IMMEDIATE COLLAPSE

Interpretation:

stable systems resist divergence

chaotic systems collapse rapidly

random systems have no continuity



---

Benchmark — Structural Resilience (R)

python examples/resilience_benchmark.py

What it does:

measures divergence and recovery


Metrics:

T_unstable

T_collapse

T_recovery

R


Interpretation:

high R → structure preserved or restored

low R → persistent divergence

adaptive systems delay collapse



---

Minimal Executable Systems

Core:

examples/omnia_validation_demo.py

examples/omnia_minimal_engine.py

examples/omnia_sci_engine.py


Temporal:

examples/divergence_time_demo_standalone.py

examples/divergence_benchmark.py

examples/resilience_benchmark.py


Additional:

examples/structural_dynamics_mod9.py

examples/structural_dynamics_modn.py

examples/structural_dynamics_modn_global.py

examples/structural_dynamics_strings.py



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

TΔ — Structural Divergence Time
Time until equivalence breaks

R — Resilience Score
Recovery capacity

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

no further structure extractable

continuation becomes non-informative



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

temporal divergence



---

Repository Structure

omnia/ → core engine

examples/ → executable systems

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