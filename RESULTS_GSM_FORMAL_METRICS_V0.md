# GSM Symbolic v0 — Formal Metrics Results

## Scope

This document reports the first empirical run of:

TruthΩ → Co⁺ → Score⁺

applied to the GSM-symbolic v0 protocol.

The goal is not to validate correctness, but to test:

> whether structural stability varies under controlled transformations even when answers remain correct.

---

## Dataset

- total cases: 30  
- templates: 10  
- variants per template:
  - base
  - num_perturbed
  - clause_augmented

Each case includes:
- model output
- extracted final answer
- correctness label
- Ω (structural invariance)
- Co⁺ (structural coherence)
- Score⁺ (aggregated signal)

---

## Global Summary

omega: min:  0.750490 max:  1.000000 mean: 0.936966

coherence_plus: min:  0.480350 max:  0.805556 mean: 0.690568

score_plus: min:  0.658337 max:  0.894253 mean: 0.813767

Correctness:

correct:   27 incorrect: 3

---

## Summary by Variant Type

base: omega_mean:     1.000000 score_mean:     0.838671

num_perturbed: omega_mean:     0.948534 score_mean:     0.828977

clause_augmented: omega_mean:     0.862365 score_mean:     0.773654

Observation:

- base cases show maximal invariance
- clause augmentation produces the strongest structural degradation

---

## Fragility Distribution

stable: 20 watch:  10 fragile: 0 unstable: 0

---

## Correct but Structurally Degraded

count: 7 / 27 ≈ 25.9%

These cases satisfy:

- correct final answer
- reduced Ω and/or Score⁺
- fragility_rank ∈ {watch}

Example:

template_id:    gsmsym_001 variant_type:   clause_augmented

expected:       20 model_answer:   20

omega:          0.826667 coherence_plus: 0.490007 score_plus:     0.658337

fragility_rank: watch

Interpretation:

The model produces a correct answer, but its structural stability decreases under controlled transformation.

---

## Template Degradation

Largest observed drops:

template_id:    gsmsym_001 variant_type:   clause_augmented

score_drop:     0.142304 omega_drop:     0.173333

Pattern:

- clause augmentation produces the largest drops
- numerical perturbation produces smaller but consistent drops

---

## Core Observation

correct_degraded_ratio = 0.259259

Meaning:

> ~26% of correct outputs show measurable structural degradation.

---

## Interpretation

This experiment shows:

1. Correctness is not sufficient to guarantee structural stability  
2. Structural invariance (Ω) reacts to controlled perturbations  
3. Stability signals can diverge from correctness signals  

---

## Limits

- v0 feature space is simple (token-based)
- distance metric is heuristic
- transformations are limited
- no external validation

---

## Status

experimental evidence (v0) not validated not generalizable

---

## Final Statement

These metrics do not measure truth.

They measure structural stability under transformation.

In this run: correct answers can remain stable or become structurally fragile.

Therefore:

correctness ≠ structural stability



