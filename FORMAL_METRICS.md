# FORMAL_METRICS.md

## Scope

This file defines the minimal formalization of:

TruthΩ → Co⁺ → Score⁺

These are **structural measurements**, not truth claims, not decisions, not semantic judgments.

---

## Core Principle

Structural truth is defined as:

> invariance under controlled transformation

---

## Definitions

### 1. TruthΩ (Ω)

TruthΩ measures **structural invariance**.

Given:
- input `x`
- transformation set `T = {t₁, ..., tₙ}`
- structural mapping `f(x)`
- distance function `d(a,b) ∈ [0,1]`

Definition:

Ω(x) = 1 - (1/n) * Σ d( f(x), f(tᵢ(x)) )

Interpretation:
- Ω → 1 → stable structure
- Ω → 0 → fragile structure

Constraint:
- transformations must preserve semantics

---

### 2. Co⁺ (Structural Coherence)

Measures **internal consistency**.

Given:
- `f(x) = (c₁, ..., c_k)`

Definition:

Co⁺(x) = 1 - [ 2 / (k*(k-1)) ] * Σ d(cᵢ, cⱼ)  for i < j

Interpretation:
- high → coherent components
- low → internal contradiction

---

### 3. Score⁺ (Bounded Aggregation)

Score⁺(x) = α * Ω(x) + (1 - α) * Co⁺(x)

Where:
- α ∈ [0,1]
- output ∈ [0,1]

No interpretation layer is included.

---

## Required Properties

For validity, the system must satisfy:

### 1. Reproducibility
Same input → same output

### 2. Falsifiability
There exist cases where:
- output looks correct
- Ω detects instability

### 3. Sensitivity
Small structural perturbations → measurable change

### 4. Boundary Condition (OMNIA Principle)

measurement != inference != decision

This system:
- does NOT interpret meaning
- does NOT validate truth
- does NOT make decisions

---

## Transformations T

Transformations must be **non-semantic**.

Examples:
- reordering
- formatting changes
- encoding variations
- base representation changes (OMNIABASE)

Invalid:
- meaning-altering transformations

---

## Minimal Reference Implementation

```python
def omega(x, transforms, f, d):
    base = f(x)
    deltas = []
    for t in transforms:
        xt = t(x)
        deltas.append(d(base, f(xt)))
    return 1 - sum(deltas) / len(deltas)


def coherence_plus(x, f, d):
    comps = f(x)
    k = len(comps)
    if k < 2:
        return 1.0

    total = 0
    count = 0
    for i in range(k):
        for j in range(i+1, k):
            total += d(comps[i], comps[j])
            count += 1

    return 1 - (2 / (k*(k-1))) * total


def score_plus(x, transforms, f, d, alpha=0.5):
    o = omega(x, transforms, f, d)
    c = coherence_plus(x, f, d)
    return alpha * o + (1 - alpha) * c


---

Minimal Test Protocol

A valid test must include:

1. Original input x


2. Set of transformations T


3. Computed:

Ω(x)

Co⁺(x)

Score⁺(x)




And at least one case where:

output is superficially valid

Ω detects instability



---

Final Constraint

These metrics measure structure.
They do not assert truth.


---

Status

Experimental
Not validated
Requires empirical testing

---

Messaggio commit:

Add formal definition of structural metrics (TruthΩ, Co⁺, Score⁺)