# Ω̂ Validation v0 — Residual Invariant Set

## Scope

This document reports a controlled validation test for:

```text
Ω̂ — Residual Invariant Set

Ω̂ identifies which structural features remain invariant across a set of controlled transformations.

Unlike scalar metrics such as:

Ω

IRI

SEI

TΔ

R


Ω̂ does not return a score.

It returns:

the surviving invariant structure


---

Formal Definition

Given:

x      = original object
T      = {t1, ..., tn} transformation set
f(x)   = structural feature representation
Q      = set of extracted structural features

Define:

Ω̂(x) = { q in Q(f(x)) | q remains invariant across all ti in T }

Equivalent condition:

q in Ω̂(x)
iff
for all ti in T:
    q(f(x)) = q(f(ti(x)))

Or with tolerance:

d_q(q(f(x)), q(f(ti(x)))) <= epsilon


---

Key Difference From Previous Metrics

Previous metrics return scalar measurements:

Ω   → amount of structural change
IRI → irreversible structural residue
SEI → saturation of dynamics
TΔ  → divergence threshold crossing time
R   → recovery efficiency

Ω̂ instead returns:

which structural components survived

This makes Ω̂ the first explicit invariant extraction metric in the framework.


---

Test Object

Base object:

{
  "id": 42,
  "name": "Alice",
  "score": 100,
  "active": true
}


---

Tested Transformations

1. Reordering

{
  "score": 100,
  "active": true,
  "id": 42,
  "name": "Alice"
}


---

2. Type Drift

{
  "id": 42,
  "name": "Alice",
  "score": "100",
  "active": true
}


---

3. Null Insertion

{
  "id": 42,
  "name": null,
  "score": 100,
  "active": true
}


---

4. Key Deletion

{
  "id": 42,
  "score": 100,
  "active": true
}


---

Structural Feature Extraction

For each feature:

type(v)
is_null(v)

were extracted and compared across transformations.


---

Result

Residual invariant set:

Ω̂ = ['active', 'id']


---

Interpretation

The following features remained structurally invariant across all tested transformations:

active
id

The following features did not survive:

name
score

Reasons:

name

Lost invariance because:

null insertion changed structural state

score

Lost invariance because:

type drift changed feature signature


---

Core Observation

Ω̂ depends on the transformation set.

Therefore:

invariance is transformation-relative

A feature may remain invariant under one transformation family and fail under another.


---

Key Claim Supported

Ω̂ extracts surviving structural invariants across controlled transformations.

It does not measure:

semantic meaning

correctness

importance


It measures only:

structural persistence


---

Relation to Ω

Ω measures the amount of aggregate invariance.

Ω̂ identifies which specific components remain invariant.

Therefore:

Ω  = how much structure survives
Ω̂ = what structure survives


---

Relation to IRI

IRI measures irreversible loss after recovery.

Ω̂ measures residual surviving structure.

Therefore:

IRI = residual damage
Ω̂  = residual invariants

They are complementary.


---

Limits

This validation is minimal and synthetic.

Limitations:

toy JSON object

handcrafted transformations

simple feature extraction

no semantic invariants

no tolerance hierarchy

no weighted invariant importance



---

Status

Ω̂ v0: operationally coherent in controlled invariant extraction tests

Not externally validated.

Requires future testing on:

symbolic systems

LLM outputs

schema evolution

multibase representations

structured trajectories

semantic-preserving transformations



---

Final Statement

Ω̂ is not a score.

Ω̂ is a residual structural invariant extractor.

It identifies which structural components persist across controlled transformations.

