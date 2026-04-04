# OMNIA v1.0 — Relational Fatigue Spectrometry (RFS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19420935.svg)](https://doi.org/10.5281/zenodo.19420935)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  

---

## Definition

OMNIA is a **dynamic structural measurement engine**.

It does not analyze content.  
It measures how a system **responds to controlled perturbations**.

---

## Core Principle

> Structure is not what is present.  
> Structure is what resists.

---

## Method (RFS Core)

OMNIA applies repeated micro-perturbations (multi-swap stress) to a sequence and observes the response.

Each sequence is treated as a graph of local adjacencies.

For each perturbation:

- adjacency structure is altered  
- the **symmetric difference** between original and perturbed graph is computed  

---

### Signals Extracted

- **Impact** → mean structural disruption  
- **Volatility** → variance of disruption across trials  

---

## Omega Score

Omega = 0.7 × Volatility Score + 0.3 × Impact

Where:

- Volatility Score = inverse of response variance  
- Impact = normalized graph disruption  

---

## Interpretation

OMNIA treats information as a material under stress:

| System Type | Response |
|------------|---------|
| Structured | stable |
| Perturbed  | partially unstable |
| Random     | volatile |

---

## Properties

- Token-agnostic  
- Non-semantic  
- Fully dynamic  
- Differential (response-based)  
- Deterministic (given seed)  

OMNIA does not read meaning.  
It measures relational coherence.

---

## Validation

OMNIA v1.0 has been validated across three regimes:

| Dataset | Regime | Result |
|--------|--------|-------|
| B | Cyclic redundancy | ✔ |
| C | Aperiodic linear sequences | ✔ |
| D | Semantic noise | ✔ |

### Key Result

Structural integrity remains detectable even under semantic interference.

---

## What OMNIA Measures

- relational coherence  
- structural stability  
- breakdown under stress  
- consistency of response  

---

## What OMNIA Does NOT Do

OMNIA:

- does not interpret  
- does not predict  
- does not classify semantics  
- does not optimize  
- does not learn

Output = measurement only

---

## Use Cases

- logical coherence analysis  
- code structure validation  
- pipeline integrity verification  
- detection of hidden inconsistencies  

---

## Limitations

OMNIA v1.0 measures **total structural response**, including:

- topological structure  
- statistical-linguistic patterns  

It does not separate these layers.

---

## Roadmap

Next step:

v10.x → Semantic Decoupling Layer

Goal:

- isolate topological structure  
- remove linguistic interference  

---

## Minimal Execution

```bash
python examples/omnia_validation_demo.py

Expected behavior:

stable systems → high Omega

unstable systems → Omega decay



---

Repository Structure

omnia/        → core engine  
examples/     → demos  
tests/        → validation  
docs/         → formal notes  
experiments/  → research extensions


---

Positioning

OMNIA is:

post-hoc

model-agnostic

non-semantic

bounded

structural


OMNIA is NOT a pattern detector.

It is a structural integrity sensor.


---

Statement

> OMNIA v1.0
Structure is not what you see.
It is what resists.




---

License

MIT License


---

Citation

Brighindi, M.
OMNIA v1.0 — Relational Fatigue Spectrometry Core
https://github.com/Tuttotorna/lon-mirror
