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
| 03 | recoverable vs non-recoverable transformations | IRI separates temporary deformation from irreversible loss | lossy deletion produces maximal residue while recoverable type drift does not | `RESULTS_IRI_VALIDATION_V2.md` |
| 04 | stable vs oscillating trajectories | SEI separates saturation from continued instability | saturated trajectory scores near 1 while oscillating trajectory drops | `RESULTS_SEI_VALIDATION_V0.md` |
| 05 | rapid vs slow divergence | TΔ separates early threshold crossing from delayed crossing | rapid divergence crosses θ at step 2, slow divergence at step 6 | `RESULTS_TDELTA_VALIDATION_V0.md` |
| 06 | recovery paths | R separates perfect, partial, and failed recovery | resilience decreases from 1.0 to 0.0 across recovery quality | `RESULTS_R_VALIDATION_V0.md` |
| 07 | invariant extraction | Ω̂ returns surviving components instead of a scalar score | `active` and `id` survive while `name` and `score` fail | `RESULTS_OMEGA_HAT_VALIDATION_V0.md` |
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

# Case 03 — Irreversible Structural Loss

## Context

This case comes from the IRI v2 validation.

IRI measures irreversible structural residue after a transformation and attempted recovery.

The important point is that not all structural damage is equal:

```text
temporary deformation
!=
irreversible loss
```

---

## Tested Transformations

```text
reorder
type_recoverable
type_nonrecoverable
lossy
```

---

## Results

```text
reorder             : 0.000000
type_recoverable    : 0.000000
type_nonrecoverable : 0.700000
lossy               : 1.000000
```

---

## Surface Status

All cases are controlled transformations of the same simple structure.

Some transformations visibly change the object, but the key distinction is whether recovery restores the original structure.

---

## Structural Signal

IRI separates:

```text
recoverable deformation
```

from:

```text
irreversible structural residue
```

Recoverable type drift returns:

```text
IRI = 0.000000
```

Lossy deletion returns:

```text
IRI = 1.000000
```

---

## Why This Matters

This case shows that structural change and irreversible structural loss are not the same phenomenon.

A structure may change temporarily and still fully recover.

Another structure may lose information that cannot be reconstructed.

IRI captures that difference.

---

## Supported Claim

```text
Change does not imply irreversible loss.
Irreversible loss requires residual damage after attempted recovery.
```

---

## Source

```text
RESULTS_IRI_VALIDATION_V2.md
```

---

# Case 04 — Saturation vs Instability

## Context

This case comes from the SEI validation.

SEI measures whether a structural trajectory stabilizes or continues to oscillate.

It does not measure correctness.

It measures saturation of structural behavior.

---

## Tested Trajectories

```text
saturated:
[0.92, 0.91, 0.91, 0.90, 0.91, 0.91]

unstable:
[0.95, 0.40, 0.88, 0.35, 0.90, 0.30]

converging:
[0.55, 0.68, 0.76, 0.82, 0.84, 0.85]
```

---

## Results

```text
SEI(saturated)  = 0.999840
SEI(converging) = 0.945600
SEI(unstable)   = 0.617600
```

---

## Surface Status

All trajectories are valid bounded Ω sequences.

The difference is not validity.

The difference is dynamic behavior.

---

## Structural Signal

SEI separates:

```text
stable / saturated behavior
```

from:

```text
continued oscillation
```

The saturated trajectory scores near 1.

The oscillating trajectory drops.

---

## Why This Matters

A system can keep producing bounded outputs while remaining dynamically unstable.

SEI measures stabilization, not correctness.

---

## Supported Claim

```text
Stability over time is different from instantaneous correctness.
```

---

## Source

```text
RESULTS_SEI_VALIDATION_V0.md
```

---

# Case 05 — Divergence Timing

## Context

This case comes from the TΔ validation.

TΔ measures the first point where structural divergence crosses a declared threshold.

It does not measure total instability.

It measures timing of threshold crossing.

---

## Threshold

```text
θ = 0.30
```

---

## Tested Trajectories

```text
rapid_divergence:
[0.05, 0.18, 0.35, 0.50, 0.72]

slow_divergence:
[0.02, 0.05, 0.10, 0.15, 0.21, 0.28, 0.31, 0.40]

no_divergence:
[0.03, 0.05, 0.08, 0.10, 0.12, 0.14]
```

---

## Results

```text
TΔ(rapid_divergence) = 2
TΔ(slow_divergence)  = 6
TΔ(no_divergence)    = undefined
```

---

## Surface Status

All trajectories remain valid bounded distance sequences.

The important difference is when the declared threshold is crossed.

---

## Structural Signal

TΔ separates:

```text
early structural divergence
```

from:

```text
late structural divergence
```

and from:

```text
no detected divergence
```

---

## Why This Matters

Two systems can both diverge, but not at the same time.

TΔ captures this temporal difference.

---

## Supported Claim

```text
Structural divergence is not only a magnitude.
It also has a time of threshold crossing.
```

---

## Source

```text
RESULTS_TDELTA_VALIDATION_V0.md
```

---

# Case 06 — Recovery Efficiency

## Context

This case comes from the R validation.

R measures recovery efficiency after perturbation.

It does not measure the initial amount of damage.

It measures how much damage remains after recovery.

---

## Results

```text
perfect_recovery:
Dp = 0.700000
Dr = 0.000000
R  = 1.000000

partial_recovery:
Dp = 0.850000
Dr = 0.500000
R  = 0.411765

failed_recovery:
Dp = 0.850000
Dr = 0.850000
R  = 0.000000
```

---

## Surface Status

All cases use controlled perturbation and recovery paths.

The important distinction is how much residual damage remains after recovery.

---

## Structural Signal

R separates:

```text
perfect recovery
```

from:

```text
partial recovery
```

and from:

```text
failed recovery
```

---

## Why This Matters

Perturbation alone does not define structural weakness.

A system can be strongly perturbed but still resilient if recovery restores the original structure.

---

## Supported Claim

```text
Damage and recovery capability are different structural properties.
```

---

## Source

```text
RESULTS_R_VALIDATION_V0.md
```

---

# Case 07 — Residual Invariant Extraction

## Context

This case comes from the Ω̂ validation.

Ω̂ does not return a scalar score.

It returns the structural components that survive all tested transformations.

---

## Base Object

```json
{
  "id": 42,
  "name": "Alice",
  "score": 100,
  "active": true
}
```

---

## Result

```text
Ω̂ = ['active', 'id']
```

---

## Surface Status

All tested variants are controlled transformations of the same object.

The important question is not whether the object remains parseable.

The important question is:

```text
which features survived?
```

---

## Structural Signal

Ω̂ identifies the surviving invariant set:

```text
active
id
```

The following features fail invariance:

```text
name
score
```

Reasons:

```text
name  → null insertion
score → type drift
```

---

## Why This Matters

Scalar metrics say how much structure survives.

Ω̂ identifies what survives.

This moves the framework from scoring toward invariant extraction.

---

## Supported Claim

```text
Structural measurement can identify residual invariant components, not only aggregate scores.
```

---

## Source

```text
RESULTS_OMEGA_HAT_VALIDATION_V0.md
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