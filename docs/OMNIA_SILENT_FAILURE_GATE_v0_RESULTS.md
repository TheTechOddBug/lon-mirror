# OMNIA Silent Failure Gate v0 - Toy Structural Sensitivity Demo

## Scope

This is a small reproducible toy demo.

It does **not** prove general semantic fragility.
It does **not** prove real-world failure prediction.
It does **not** establish a universal pre-collapse detector.

What it does show is narrower:

> Under a fixed transform family, some outputs that remain correct after simple normalization are structurally more sensitive than others.

---

## Core Question

Most evaluation pipelines ask:

- is the answer exactly correct?
- does it match the target string?

This demo asks a different question:

- how sensitive is the output structure under controlled representational perturbations?

This is a structural question, not a semantic one.

---

## Method

We evaluate each output under a fixed transformation family:

- identity
- whitespace collapse
- reversal
- vowel drop

From these perturbations, OMNIA computes:

- **Omega**: structural coherence
- **MAD**: dispersion of transform scores
- **IRI**: irreversibility proxy under mild perturbation
- **SEI**: extractability / efficiency signal

---

## Correctness Layers

We distinguish two notions:

### 1. Exact match
Strict string equality between `model_output` and `correct`.

### 2. Normalized match
A narrow task-aware normalization for this toy dataset only.

Examples:
- `"The capital of France is Paris"` -> `paris`
- `"World War II ended in 1945"` -> `1945`
- `"Yes, 17 is prime"` -> `yes`

This is still limited, but it is more informative than raw exact match.

---

## Structural Labels

These labels describe transform sensitivity only.

| Label | Meaning |
|------|---------|
| **Invariant** | high coherence, low dispersion, low irreversibility |
| **Sensitive** | intermediate transform sensitivity |
| **Degraded** | strong transform sensitivity or collapse under this transform family |

These are **not semantic truth labels**.

---

## What This Demo Can Support

This demo can support the following limited claim:

> Standard exact-match evaluation is too coarse to describe all output behavior. Some normalized-correct outputs are more structurally sensitive than others.

That is the result.

---

## What This Demo Cannot Yet Support

This demo cannot yet support:

- "OMNIA proves semantic fragility"
- "OMNIA predicts future failure"
- "OMNIA detects collapse before reasoning fails in general"
- "OMNIA measures truth"

Those claims require stronger datasets and stronger validation.

---

## Recommended Reading of the Output

The most relevant comparison is not:

- correct vs wrong

but:

- normalized-correct and structurally invariant
- normalized-correct but structurally sensitive
- clearly wrong and structurally degraded

This gives a three-level view that exact-match alone cannot provide.

---

## Example Interpretation Pattern

### Case A - Exact and structurally invariant
Example pattern:
- output is compact
- normalized match = true
- low MAD
- low IRI
- high Omega

Interpretation:
- under this transform family, the output is structurally robust

### Case B - Normalized-correct but structurally sensitive
Example pattern:
- output remains correct after normalization
- Omega lower
- MAD or IRI higher
- classified as sensitive

Interpretation:
- the answer survives normalization, but the representation is less transform-stable

### Case C - Normalized-wrong and degraded
Example pattern:
- normalized match = false
- low Omega
- high IRI or low SEI
- classified as degraded

Interpretation:
- the output is both task-wrong and structurally unstable under this setup

---

## Reproducibility

Dataset:
`examples/silent_failure_v0.jsonl`

Script:
`examples/omnia_silent_failure_gate_v0.py`

Output:
`examples/silent_failure_results_v0.json`

Run:

```bash
python examples/omnia_silent_failure_gate_v0.py


---

Limitations

very small toy dataset

narrow hand-built normalization

fixed transform family

no cross-model comparison

no out-of-sample failure forecasting

output-only measurement, not full question-output relational modeling



---

Correct Final Claim

A precise final statement for this version is:

> OMNIA v0 provides a toy, reproducible structural sensitivity demo showing that exact-match evaluation alone is too coarse, and that some normalized-correct outputs are more transform-sensitive than others.



That is a valid claim. Anything stronger would require a stronger experiment.

