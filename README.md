# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19420935.svg)](https://doi.org/10.5281/zenodo.19420935)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  

---

## What this does

AI systems fail suddenly.  
OMNIA detects structural collapse **before it becomes visible as an error**.

It does not interpret meaning.  
It does not evaluate correctness.  

It measures **structural stability under controlled transformations**.

```text
output = measurement only


---

Run it (10 seconds)

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected behavior

structured   → high Ω
perturbed    → Ω drop
random       → Δ_struct ≈ 0

If this separation appears, the system is working.


---

What you get

early signal of structural instability

model-independent diagnostics

sequence-level robustness measurement


Works on:

text

code

numeric sequences

any ordered representation



---

Why this is different

System	Behavior

Guardrails	block output
Eval tools	measure after failure
Observability	track metrics
OMNIA	detects collapse before it



---

Core principle

Structural truth = invariance under transformation

If a structure survives perturbations → it is real
If it collapses → it was representation


---

Architecture

Dual-Echo → OMNIAMIND → OMNIA → OMNIA-LIMIT → Decision Layer (external)

Boundary condition:

measurement ≠ cognition ≠ decision

OMNIA does not decide.
It measures.


---

Structural lenses

Independent transformation families:

BASE   → multi-representation invariance

TIME   → drift / instability over time

CAUSA  → relational dependencies

TOKEN  → sequence perturbation

LCR    → logical coherence reduction


Each lens produces an independent signal.


---

Core metrics

Ω (Omega)
Structural coherence under perturbation

Ω̂ (Omega-set)
Residual invariance across transformations

SEI
Remaining extractable structure
→ SEI → 0 = saturation

IRI
Irreversible structural loss
→ IRI > 0 = non-recoverable

TΔ
Divergence point

R
Recovery capacity after perturbation


---

Local probe (RFS)

Relational Fatigue Spectrometry measures sequence degradation:

A(S) = {(t_i, t_{i+1})}
D = |A(S) Δ A(S')|
I = D / |A(S)|
σ = std(I)
V = 1 / (1 + α·σ)

Ω = 0.7·V + 0.3·I


---

Structural isolation

Δ_struct = Ω_raw − Ω_shuffle

Removes statistical artifacts.
Keeps only structure.


---

STOP condition (OMNIA-LIMIT)

SEI → 0
IRI > 0
Ω̂ stable

Result:

no additional structure can be extracted

Continuation is non-informative.


---

Minimal validation

Observed invariant:

Δ_struct(structured) > Δ_struct(perturbed) > Δ_struct(random)

If violated → system failure or bad data.


---

Repository

omnia/ → engine

examples/ → runnable demos

tests/ → validation

docs/ → formalization

data/ → datasets



---

Position

OMNIA is not:

a model

a predictor

a semantic analyzer


It is:

a structural diagnostic layer


---

License

MIT


---

Citation

Brighindi, M.
https://github.com/Tuttotorna/lon-mirror
