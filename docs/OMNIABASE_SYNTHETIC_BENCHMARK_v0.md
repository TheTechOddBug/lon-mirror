# OMNIABASE Synthetic Benchmark v0

## Status

This document defines the first synthetic benchmark layer for the OMNIABASE lens.

It is not external validation.
It is not a real-world benchmark.
It is not proof of superiority.

It is the first controlled class-separation test.

Its purpose is simple:

test whether the current OMNIABASE lens emits measurably different structural profiles for different synthetic input families.

---

## Linked files

Implementation:

- `omnia/lenses/base_lens.py`

Benchmark script:

- `examples/omnia_base_lens_synthetic_benchmark.py`

Interpretation layer:

- this file

---

## Purpose

The benchmark exists to answer one narrow question:

> Does the current OMNIABASE lens produce different output distributions for controlled input classes?

This is the first meaningful test.

If the answer is no,
the lens is currently weak or badly specified.

If the answer is yes,
the lens becomes at least testable as a structural discriminator.

That still does not imply usefulness in real domains.
But it is the first non-trivial checkpoint.

---

## Benchmark design

The benchmark uses synthetic integer families.

Current classes:

1. `random`
2. `repeated_pattern`
3. `powers_of_two`
4. `arithmetic_construction`
5. `prime_subset`
6. `logistic_mapped`

Each class is designed to expose a different structural regime.

The goal is not realism.
The goal is controlled contrast.

---

## Why these classes were chosen

### 1. random

Purpose:

- baseline irregularity
- no intended privileged visible structure

Expected role:

- reference class for unstructured variation

---

### 2. repeated_pattern

Examples:

- repeated digit seeds
- repeated string-like constructions

Purpose:

- create numbers that may look structurally special in decimal form
- stress-test representation dependence

Expected role:

- likely higher base sensitivity
- possible collapse outside privileged encodings

---

### 3. powers_of_two

Purpose:

- include a mathematically regular family
- test whether a regular generative law leaves a recognizable cross-base signature

Expected role:

- possible relative stability
- possible distinct profile family

No stronger claim is licensed.

---

### 4. arithmetic_construction

Purpose:

- provide a simple deterministic linear family
- test whether orderly additive construction differs from random and repeated forms

Expected role:

- intermediate behavior
- possible lower variance than random

---

### 5. prime_subset

Purpose:

- include a mathematically important but heterogeneous class
- test whether the current shallow feature family sees anything stable or not

Expected role:

- uncertain
- useful as a falsification pressure point

This class is important because weak or mixed results here are acceptable.
They help prevent overclaiming.

---

### 6. logistic_mapped

Purpose:

- create a deterministic but irregular family derived from a nonlinear map
- approximate a synthetic structured-irregular regime

Expected role:

- higher drift than simple deterministic families
- possible distinction from purely random samples

This class is not a chaos proof.
It is only a controlled irregular generator.

---

## What the benchmark measures

The benchmark aggregates four outputs from the current lens:

1. `cross_base_stability`
2. `representation_drift`
3. `base_sensitivity`
4. `collapse_count`

For each class it reports:

- mean
- median
- min
- max

These are descriptive statistics only.

No inferential statistics are included in v0.

---

## What counts as success in v0

The benchmark counts as minimally successful only if at least one of the following occurs clearly:

### A. distribution separation

At least some classes show visibly different central tendency across one or more metrics.

Example:

- repeated-pattern class has higher base sensitivity than random
- powers-of-two have lower drift than repeated-pattern inputs

The exact classes matter less than the existence of consistent separation.

---

### B. class ordering stability

A class ranking appears consistently across metrics.

Example:

- one class remains systematically more fragile
- one class remains systematically more stable

This matters because it suggests the lens is not emitting arbitrary noise.

---

### C. bounded heterogeneity

Some classes remain mixed while others separate.

This is actually a good sign.

Why:
a lens that separates everything too cleanly in v0 is suspicious.
Reality usually includes ambiguous intermediate behavior.

---

## What counts as failure in v0

The benchmark counts as weak or failed if one or more of the following happens:

### 1. total overlap

All classes produce nearly indistinguishable summaries across all metrics.

Interpretation:
the current feature family may be too shallow.

---

### 2. arbitrary inversion

Class order changes erratically across runs or depends mostly on sample accident.

Interpretation:
the lens may not be stable enough as a diagnostic instrument.

---

### 3. trivial domination by scale

If outputs are driven mostly by size effects rather than structural family,
the benchmark is contaminated.

Interpretation:
feature normalization is insufficient.

---

### 4. repeated-pattern no different from random

If visibly representation-bound constructions do not differ from random at all,
the current lens may be missing its main target.

That would be a bad sign.

---

## Correct interpretation discipline

This benchmark must be read under hard constraints.

### Constraint 1

Synthetic separation is not real-world validation.

A synthetic benchmark only shows that the lens can respond differently under controlled construction.

It does not prove external usefulness.

---

### Constraint 2

Separation is not explanation.

Even if one class separates,
the lens may still not explain why at a deeper structural level.

---

### Constraint 3

No domain leap is allowed.

From this benchmark alone one cannot conclude:

- financial predictive value
- causal access
- mathematical truth extraction
- LLM robustness advantage
- superiority over OMNIA's other lenses

Any such leap would be false.

---

## Main limitations of v0

### Limitation 1 - shallow profile family

The lens uses simple profile statistics.
This makes the system auditable.
It also limits depth.

---

### Limitation 2 - no inferential testing

There are no significance tests, no confidence intervals, no effect sizes.

So v0 is descriptive, not statistically conclusive.

---

### Limitation 3 - integer-only sandbox

The benchmark works on positive integers only.

This is much narrower than OMNIA's intended ecosystem.

---

### Limitation 4 - synthetic generation choices matter

The classes are design choices.
Different generators could shift the results.

Therefore the benchmark is reproducible, but not exhaustive.

---

### Limitation 5 - no comparison against alternative methods

There is no baseline competitor yet.

So even if separation appears, we still do not know whether this lens adds anything unique.

---

## Why v0 still matters

Despite the limitations, this benchmark matters for one reason:

it is the first point where the OMNIABASE lens can fail visibly.

That is good.

A system that cannot fail cleanly cannot be validated cleanly.

v0 makes the lens falsifiable at the class-separation level.

That is the minimum scientific threshold.

---

## Reading guide for the first run

When the benchmark is executed, read the output in this order:

### Step 1 - compare means and medians

Look for obvious class differences in:

- `cross_base_stability`
- `representation_drift`
- `base_sensitivity`
- `collapse_count`

If means differ but medians do not, the effect may be driven by outliers.

---

### Step 2 - inspect min and max spread

Wide spread may indicate:

- unstable class signature
- insufficient feature precision
- heterogeneous generator behavior

This is informative, not automatically bad.

---

### Step 3 - compare repeated_pattern against random

This is the first pressure test.

If repeated-pattern constructions show no increase in representation sensitivity or collapse behavior compared to random,
the current lens is likely underpowered.

---

### Step 4 - compare powers_of_two against random and repeated_pattern

If powers-of-two show relatively lower drift or lower collapse,
the lens may be detecting some cross-base persistence.

This would be a positive result, but still bounded.

---

### Step 5 - inspect ambiguous classes

Prime subset and logistic-mapped inputs may remain mixed.
That is acceptable.

What matters is whether the lens produces structured ambiguity rather than uniform noise.

---

## Expected next step after first run

Once the first run exists, the next action is not publicity.

The next action is one of these two:

### Path A - if separation is weak

Upgrade the feature family.

Possible additions:

- compressibility proxy
- local motif counts
- digit entropy
- symmetry scores
- transition irregularity
- multi-scale run statistics

---

### Path B - if separation is visible

Run two strengthening tests:

1. threshold sensitivity sweep
2. class