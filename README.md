# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19420935.svg)](https://doi.org/10.5281/zenodo.19420935)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  

---

## Overview

OMNIA is a post-hoc structural measurement engine.

It does not analyze meaning, correctness, or intent.  
It measures how structure behaves under controlled transformations.

Output = measurement only.

---

## Core Principle

Structural truth is defined as invariance under transformation.

What remains stable across perturbations is structure.  
What collapses is representation.

---

## Architecture

OMNIA is a multi-layer system:

```text
Dual-Echo → OMNIAMIND → OMNIA → OMNIA-LIMIT → Decision Layer (external)
```

Strict boundary:

```text
measurement ≠ cognition ≠ decision
```

OMNIA operates only at the measurement layer.

---

## Structural Lenses

OMNIA applies independent transformations through multiple lenses:

- BASE → multi-representation / multi-base invariance  
- TIME → structural drift and temporal instability  
- CAUSA → relational / lagged dependencies  
- TOKEN → sequence-level perturbations  
- LCR → logical coherence reduction  

Each lens produces independent structural measurements.

---

## Core Metrics

### Ω (Omega)

Local structural coherence under perturbation.

---

### Ω̂ (Omega-set)

Residual structural invariance across transformations.

Represents what cannot be removed.

---

### SEI (Structural Extractability Index)

Measures remaining extractable structure.

```text
SEI → 0 ⇒ no additional structure can be extracted
```

---

### IRI (Irreversibility Index)

Measures structural loss that cannot be recovered.

```text
IRI > 0 ⇒ irreversible transformation occurred
```

---

### TΔ (Divergence Time)

Point where structural equivalence breaks.

---

### R (Resilience)

Ability of a structure to recover after perturbation.

---

## Local Method — RFS (Relational Fatigue Spectrometry)

RFS is a local probe inside OMNIA.

Sequence representation:

A(S) = {(t_i, t_{i+1})}

Perturbation impact:

D = |A(S) Δ A(S')|  
I = D / |A(S)|  

Volatility:

σ = std(I across trials)

Stability:

V = 1 / (1 + α·σ)

Structural score:

Ω = 0.7·V + 0.3·I

---

## Structural Isolation

Δ_struct = Ω_raw − Ω_shuffle

Removes statistical artifacts.  
Retains structural signal.

---

## OMNIA-LIMIT (STOP Condition)

A system reaches structural saturation when:

```text
SEI → 0  
IRI > 0  
Ω̂ stable
```

At this point:

```text
no further structure can be extracted
```

Continuation becomes non-informative.

---

## Key Result

Δ_struct(structured) > Δ_struct(perturbed) > Δ_struct(random)

---

## Empirical Evidence

Datasets:

- B → stable separation  
- C → stable separation  
- D → stable separation  

Case studies:

- ZEH-1.1 → early-warning signal  
- ZEH-2 → distributional robustness  

---

## Minimal Run

Requires: Python 3.10+

```bash
python examples/omnia_validation_demo.py
```

---

## Expected Output

Running the demo should produce:

- higher Ω for structured sequences  
- lower Ω for perturbed sequences  
- near-zero Δ_struct for random data  

This demonstrates structural separation.

---

## Repository Structure

- omnia/ → core engine  
- examples/ → runnable demos  
- tests/ → validation  
- docs/ → formal notes  
- data/ → datasets  

---

## Position

OMNIA is a structural measurement system.

- Not semantic  
- Not predictive  
- Not generative  
- Not a model  

It is a diagnostic layer.

---

## License

MIT

---

## Citation

Brighindi, M.  
https://github.com/Tuttotorna/lon-mirror