# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19356116.svg)](https://doi.org/10.5281/zenodo.19356116)

**DEMO**  
https://lon-reflect.emergent.host/

**MB-X.01**  
**Author:** Massimiliano Brighindi

---

## Canonical Index

- Ecosystem map: [ECOSYSTEM.md](ECOSYSTEM.md)
- Machine index: [repos.json](repos.json)

---

## Definition

OMNIA is a **post-hoc structural measurement engine**.

It operates on outputs and measures:

- invariance  
- compatibility  
- divergence  
- saturation  
- irreversibility  
- resilience  

under **independent, non-semantic transformations**.

---

## Core Principle

\[
\text{Truth} = \text{invariance under transformation}
\]

Truth is not:

- semantic  
- interpretative  
- authority-based  

Truth is what **remains stable across transformations**.

---

## Architectural Boundary

Strict constraint:

\[
\text{measurement} \neq \text{cognition} \neq \text{decision}
\]

OMNIA:

- does not generate  
- does not optimize  
- does not learn  
- does not interpret  
- does not decide  

**Output = measurement only**

---

## Structural Time

OMNIA does not use physical time.

It defines:

\[
T = \sum \Delta_t
\]

where:

\[
\Delta_t = \text{structural change between states}
\]

Time is **divergence**, not clock progression.

---

## Core Metrics

### Ω — Structural Coherence
Persistence under transformation

### SCI — Structural Compatibility
Agreement across independent lenses

### SEI — Saturation Index
Remaining structural extractability

### IRI — Irreversibility Index
Non-recoverable structural loss

### TΔ — Divergence Time
Point where structural equivalence breaks

### R — Resilience
Capacity to recover structure

---

## Structural Dynamics

OMNIA detects:

- divergence onset  
- collapse thresholds  
- recovery regimes  
- structural instability  
- indistinguishability  
- trajectory bifurcation  

Formal reference:

docs/TDELTA_IRI_FORMALISM_MINIMAL.md

---

## Structural Lenses

Canonical lenses:

- BASE (Omniabase)  
- TIME (Omniatempo)  
- CAUSA (Omniacausa)  
- TOKEN  
- LCR  

Properties:

- deterministic  
- composable  
- independent  
- non-semantic  

Agreement is **measured**, not assumed.

---

## OMNIA-LIMIT

Stop condition:

\[
SEI \rightarrow 0,\quad IRI > 0,\quad \hat{\Omega} \text{ stable}
\]

Interpretation:

- no further structure extractable  
- continuation becomes non-informative  
- system reached structural boundary  

OMNIA does not proceed beyond this point.

---

## Proper-Time Minimum Principle (k)

\[
\Delta \tau \ge k
\]

k is defined as:

> minimum distinguishable proper-time increment for timelike physical processes

Properties:

- invariant (proper time)  
- not coordinate time  
- not a clock unit  
- not applied to null trajectories  

Implications:

\[
f_{\max} \sim \frac{1}{k}, \quad E_{\max} \sim \frac{\hbar}{k}
\]

Interpretation:

- physical evolution may not be infinitely distinguishable  
- k is a constraint on **state resolution**, not time itself  

Status:

- structurally consistent  
- not experimentally validated  

---

## Minimal Execution

Run:

```bash
python examples/omnia_validation_demo.py

Expected:

stable inputs → higher Ω

unstable inputs → faster Ω decay

disagreement → lower SCI

saturation → SEI → 0

irreversibility → IRI > 0



---

Structural Time Experiments

Divergence Detection

python examples/divergence_time_demo_standalone.py

Detects:

divergence onset

collapse threshold



---

System Benchmark

python examples/divergence_benchmark.py

Classifies:

stable systems

chaotic systems

random systems



---

Resilience Measurement

python examples/resilience_benchmark.py

Measures:

instability

collapse

recovery

resilience score (R)



---

Minimal Systems

Core:

examples/omnia_validation_demo.py

examples/omnia_minimal_engine.py

examples/omnia_sci_engine.py


Temporal:

examples/divergence_time_demo_standalone.py

examples/divergence_benchmark.py

examples/resilience_benchmark.py


Additional:

structural_dynamics_mod*.py

structural_dynamics_strings.py



---

Positioning

OMNIA is:

post-hoc

model-agnostic

semantics-free

deterministic

bounded


OMNIA measures:

structure

breakdown

limits

divergence


OMNIA does not:

predict

interpret

explain

decide



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
