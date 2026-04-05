# OMNIA v1.0 — Relational Fatigue Spectrometry (RFS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19420935.svg)](https://doi.org/10.5281/zenodo.19420935)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  

---

## Overview

OMNIA is a post-hoc structural measurement engine.

It does not analyze meaning or correctness.  
It measures how structure degrades under controlled perturbations.

Output = measurement only.

---

## Core Principle

Structure is what remains coherent under perturbation.

---

## Formalization

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

## Key Result

Δ_struct(structured) > Δ_struct(perturbed) > Δ_struct(random)

---

## Empirical Evidence

Datasets:

- B → stable separation  
- C → stable separation  
- D → stable separation  

Case studies:

- ZEH-1.1 → early warning signal  
- ZEH-2 → distributional robustness  

---

## Minimal Run

```bash
python examples/omnia_validation_demo.py
```

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

It measures structural stability only.

---

## License

MIT

---

## Citation

Brighindi, M.  
https://github.com/Tuttotorna/lon-mirror