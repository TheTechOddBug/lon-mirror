# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19401583.svg)](https://doi.org/10.5281/zenodo.19401583)

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

\[
\boxed{\text{Time = divergence}}
\]

---

## Core Metrics

- Ω — Structural Coherence  
- SCI — Structural Compatibility  
- SEI — Saturation Index  
- IRI — Irreversibility Index  
- TΔ — Divergence Time  
- R — Resilience  

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
`docs/TDELTA_IRI_FORMALISM_MINIMAL.md`

---

## Structural Lenses

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

---

## OMNIA-LIMIT

\[
SEI \rightarrow 0,\quad IRI > 0,\quad \hat{\Omega} \text{ stable}
\]

\[
\boxed{\text{STOP}}
\]

---

## K-Framework Integration

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
\text{Every structural triple } (\mathcal S,\mathcal G,d) \text{ belongs to exactly one regime}
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

### Quantum Harmonic Oscillator (full projective space)

\[
\boxed{\text{Case C}}
\]

- compact orbits  
- minimum attained  
- no collapse  

---

### Spectral Representation

\[
\boxed{\text{Case A}}
\]

\[
\boxed{
\Delta = d_{\mathrm{spec}} \quad
\text{(since the group action does not identify distinct eigenstates)}
}
\]

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

## Proper-Time Minimum Principle

\[
\Delta \tau_{\min} = k
\]

- invariant in proper time  
- not coordinate time  
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

python examples/divergence_time_demo_standalone.py
python examples/divergence_benchmark.py
python examples/resilience_benchmark.py


---

Repository Structure

omnia/ → core engine

examples/ → execution

tests/ → validation

docs/ → formal definitions

experiments/ → extensions



---

Empirical Evidence (Micro-Benchmark v1)

A minimal benchmark has been introduced to evaluate OMNIA against a rule-based baseline.

Baseline

Rule:

flag error if final_answer != last_computed_step


Limitation:

detects only explicit mismatches

cannot detect hidden structural inconsistencies



---

OMNIA Detection

OMNIA detects structural instability using:

TDelta (break point)

Omega decay

SCI divergence

SEI pre-saturation

IRI positive


Detection occurs before the final observable error.


---

Benchmark Summary

case	class	baseline	OMNIA	decisive

case_01	narrative_override	true	true	no
case_02	narrative_override	true	true	no
case_03	narrative_override	true	true	no
case_04	hidden_inconsistency	true	true	no
case_05	hidden_inconsistency	false	true	yes



---

Note:

baseline detects only explicit mismatch

OMNIA detects structural break even when no mismatch is present (case_05)



---

Decisive Case

Case_05 demonstrates:

no arithmetic error

no mismatch between reasoning and final answer

baseline does not detect any issue


But:

a structural constraint is violated

OMNIA detects the break (TDelta < final_answer)


\boxed{
\text{baseline = false, OMNIA = true}
}


---

Status

\boxed{
\text{true\_early\_detection = PROVEN\_AT\_LOCAL\_SCALE}
}


---

Epistemic Scope

This benchmark establishes:

first minimal comparative evidence

local proof-of-function


This does NOT establish:

generalization

robustness

superiority over stronger baselines



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

\boxed{\text{Complete internal structure + partial external validation}}

\boxed{\text{No universal classification theorem}}


---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror