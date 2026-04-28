# CANONICAL_EVIDENCE_20

## Scope

This document compresses the strongest currently readable evidence slices across the OMNIA / OMNIABASE ecosystem.

The goal is not to prove universal structural truth.

The goal is to expose small, repeatable cases where:

```text
surface validity
!=
structural stability
```

The focus is intentionally narrow.

These cases are designed to be:

- small
- executable
- inspectable
- rerunnable
- difficult to dismiss as pure narrative

---

# Core Claim

The current ecosystem suggests that:

> structural instability may become measurable before obvious visible failure.

This is still a bounded working claim.

Not a universal proof.

---

# Architectural Boundary

The framework explicitly separates:

```text
measurement != inference != decision
```

OMNIA measures structure.

It does not:

- determine semantic truth
- replace reasoning
- make final decisions

---

# What Is Being Measured

Current measurements include:

```text
Ω   → structural invariance
IRI → irreversibility
SEI → saturation
TΔ  → divergence time
R   → resilience
Ω̂   → residual invariant structure
```

These measurements attempt to separate:

- change
- irreversibility
- stabilization
- divergence timing
- recovery
- surviving invariants

instead of collapsing structural behavior into a single scalar.

---

# Canonical Evidence Cases

| Case | Surface Status | Structural Signal | Observed Consequence | Source |
|---|---|---|---|---|
| 01 | readable / superficially acceptable | OMNIABASE review signal where baseline gives no warning | suspicious-clean output escalated to review instead of accept | `docs/OMNIA_10_SECONDS_DEMO_RESULT.md` |
| 02 | formally correct answer | Ω and Score⁺ degrade under controlled clause augmentation | correctness preserved while structural stability drops | `RESULTS_GSM_FORMAL_METRICS_V0.md` |
| 03 | pending | pending | pending | pending |
| 04 | pending | pending | pending | pending |
| 05 | pending | pending | pending | pending |
| 06 | pending | pending | pending | pending |
| 07 | pending | pending | pending | pending |
| 08 | pending | pending | pending | pending |
| 09 | pending | pending | pending | pending |
| 10 | pending | pending | pending | pending |
| 11 | pending | pending | pending | pending |
| 12 | pending | pending | pending | pending |
| 13 | pending | pending | pending | pending |
| 14 | pending | pending | pending | pending |
| 15 | pending | pending | pending | pending |
| 16 | pending | pending | pending | pending |
| 17 | pending | pending | pending | pending |
| 18 | pending | pending | pending | pending |
| 19 | pending | pending | pending | pending |
| 20 | pending | pending | pending | pending |

---

# Case 01 — Suspicious-Clean Repetition

## Input

```text
The answer seems correct. The answer seems correct. The answer seems correct.
```

## Surface Status

The output is readable.

It is not catastrophic spam.

It is not malformed.

A shallow baseline may accept it because it does not look like an obvious failure.

---

## Structural Signal

OMNIABASE detects suspicious structural regularity.

Observed pattern:

```text
BASELINE: no warning
OMNIA: review
ACTION: review
```

---

## Why This Matters

This case separates:

```text
obvious failure detection
```

from:

```text
suspicious-clean structural review
```

The point is not that the output is definitely wrong.

The point is that the output is structurally rigid enough to justify review.

---

## Supported Claim

```text
Readable output does not imply structural safety.
```

---

## Source

```text
docs/OMNIA_10_SECONDS_DEMO_RESULT.md
```

---

# Case 02 — Correct Answer, Degraded Structure

## Context

This case comes from the GSM symbolic v0 formal metrics run.

The important point is that the model answer remains correct, but structural stability decreases under a controlled variant.

---

## Base Case

```text
template_id:  gsmsym_001
variant_type: base
is_correct:   true
omega:        1.000000
score_plus:   0.800641
rank:         stable
```

---

## Controlled Variant

```text
template_id:  gsmsym_001
variant_type: clause_augmented
is_correct:   true
omega:        0.826667
score_plus:   0.658337
rank:         watch
```

---

## Structural Drop

```text
score_drop: 0.142304
omega_drop: 0.173333
```

---

## Surface Status

The final answer is still correct.

A correctness-only evaluator would likely mark both cases as acceptable.

---

## Structural Signal

The controlled clause augmentation produces a measurable degradation:

```text
Ω decreases
Score⁺ decreases
fragility_rank changes toward watch
```

---

## Why This Matters

This case separates:

```text
answer correctness
```

from:

```text
structural stability
```

The output can remain formally correct while the structural signal becomes weaker.

---

## Supported Claim

```text
Correctness does not imply structural stability.
```

---

## Source

```text
RESULTS_GSM_FORMAL_METRICS_V0.md
```

---

# Why These Cases Matter

Most systems primarily evaluate:

- correctness
- confidence
- semantic similarity
- formatting validity
- policy compliance

The current experiments suggest that structural instability may appear before visible collapse.

If true, structural measurement may provide:

```text
early warning signals
```

before obvious failure emerges.

This is the central hypothesis currently under investigation.

---

# Important Limits

The current evidence remains limited.

Current limitations include:

- sandbox-heavy evidence
- synthetic cases
- small evaluation sets
- non-canonical thresholds
- handcrafted transformations
- limited independent validation
- no deployment-scale proof

Nothing in this document should be interpreted as proof of universal structural validity.

---

# Current Strongest Supported Claim

The strongest currently defensible claim remains:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs under controlled conditions.

Anything substantially stronger would exceed the current evidence.

---

# Repository Links

GitHub:

```text
https://github.com/Tuttotorna/lon-mirror
https://github.com/Tuttotorna/OMNIA
https://github.com/Tuttotorna/omnia-limit
https://github.com/Tuttotorna/OMNIA-RADAR
```

DOI:

```text
https://doi.org/10.5281/zenodo.19857066
```

---

# Final Observation

The important point is not that the framework already solved structural measurement.

The important point is that structural behavior has now been separated into independently measurable properties with executable tests and explicit limits.

That makes the framework testable.

And therefore falsifiable.