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

It operates strictly on outputs and measures:

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

Truth is:

- not semantic  
- not interpretative  
- not authority-based  

Truth is what remains **structurally stable under transformation**.

---

## Architectural Boundary

\[
\text{measurement} \neq \text{cognition} \neq \text{decision}
\]

OMNIA:

- does not generate  
- does not optimize  
- does not learn  
- does not interpret  
- does not decide  

\[
\boxed{\text{Output = measurement only}}
\]

---

## Structural Time

OMNIA replaces physical time with structural time:

\[
T = \sum \Delta_t
\]

\[
\Delta_t = \text{structural change between states}
\]

Time is treated as:

\[
\boxed{\text{divergence, not clock progression}}
\]

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
Point of structural break  

### R — Resilience  
Recovery capacity after perturbation  

---

## Structural Dynamics

OMNIA detects:

- divergence onset  
- collapse thresholds  
- recovery regimes  
- instability  
- indistinguishability  
- trajectory bifurcation  

Reference:

- `docs/TDELTA_IRI_FORMALISM_MINIMAL.md`

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
- independent  
- composable  
- non-semantic  

Agreement is measured, not assumed.

---

## OMNIA-LIMIT

Stop condition:

\[
SEI \rightarrow 0,\quad IRI > 0,\quad \hat{\Omega} \text{ stable}
\]

Interpretation:

- no additional structure extractable  
- continuation is non-informative  
- structural boundary reached  

\[
\boxed{\text{STOP}}
\]

---

## K-Framework Integration (Structural Gap)

OMNIA incorporates the **K-Framework** as a structural classification layer.

### Structural Triple

\[
\mathfrak T=(\mathcal S,\mathcal G,d)
\]

### Residual

\[
\Delta([S],[T])=\inf_{U\in\mathcal G} d(US,T)
\]

### Structural Gap

\[
k=\inf_{[S]\neq[T]} \Delta([S],[T])
\]

---

## Regime Classification

\[
\boxed{
\text{All systems fall into one of three regimes}
}
\]

- **Case A**: \(k > 0\) (uniform separation)  
- **Case B**: \(k = 0\), zero realized  
- **Case C**: \(k = 0\), zero not realized  

\[
\boxed{
\text{Classification depends on } (\mathcal S,\mathcal G,d),\ \text{not on the system alone}
}
\]

---

## Physical Results

### Quantum Harmonic Oscillator (full space)

\[
\boxed{\text{Case C}}
\]

- compact orbits  
- minimum exists  
- no collapse  

---

### Spectral Representation

\[
\boxed{\text{Case A}}
\]

- discrete states  
- group action trivial  
- \(\Delta = d\)  

---

### Free Particle

\[
\boxed{\text{Case C (under non-collapse assumption)}}
\]

---

## Structural Consequence

\[
\boxed{
\text{Full quantum state spaces } \rightarrow \text{Case C}
}
\]

\[
\boxed{
\text{Discreteness emerges from structural reduction}
}
\]

---

## Proper-Time Minimum Principle (k)

\[
\Delta \tau_{\min} = k
\]

Interpretation:

- minimum distinguishable increment in proper time  
- not coordinate time  
- not a clock unit  

Implications:

\[
f_{0,\max} \sim \frac{1}{k}, \quad E_{\max} \sim \frac{\hbar}{k}
\]

Status:

- structurally consistent  
- not experimentally validated  

References:

- `docs/PROPER_TIME_MINIMUM_PRINCIPLE.md`  
- `docs/K_FALSIFIABILITY.md`  
- `docs/WHY_K_IS_NOT_A_MARKET_SIGNAL.md`  

---

## Minimal Execution

```bash
python examples/omnia_validation_demo.py

Expected:

stable → high Ω

unstable → Ω decay

disagreement → low SCI

saturation → SEI → 0

irreversibility → IRI > 0



---

Experiments

Divergence

python examples/divergence_time_demo_standalone.py

Benchmark

python examples/divergence_benchmark.py

Resilience

python examples/resilience_benchmark.py


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



---

Repository Structure

omnia/ → core engine

examples/ → execution

tests/ → validation

docs/ → formal definitions

experiments/ → extensions



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

limits

breakdown


OMNIA does not:

predict

interpret

explain

decide



---

Boundary Statement

\boxed{
\text{Complete internal structure + partial external validation}
}

\boxed{
\text{No universal classification theorem}
}


---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror