# FORMAL_METRICS.md

## Scope

This file defines the canonical structural metrics used in the L.O.N. / OMNIA measurement frame.

These metrics are proposed structural measurements.

They are not established scientific standards.

They are not truth claims, decisions, semantic judgments, or proofs.

Their function is to measure how a structure behaves under controlled transformation.

---

## Core Boundary

```text
measurement != inference != decision

This system measures structural behavior.

It does not:

interpret semantic truth

decide correctness

replace reasoning

prove claims

act as an oracle



---

Core Principle

Structural stability is defined as:

invariance under controlled transformation

A structure is considered more stable when its relevant structural features remain invariant under admissible transformations.


---

Formal Objects

Let:

x      = observed object
T      = {t1, ..., tn} controlled transformation set
f      = structural feature map
d      = bounded structural distance, d in [0,1]
theta  = divergence threshold
tau    = transformation step or observation time

Where:

f(x) = structural representation of x
d(f(x), f(y)) = measured structural distance between x and y

All metrics below depend on the choice of:

domain
transformation set
feature map
distance function
thresholds

Therefore, no metric is universal without its measurement context.


---

1. Ω — Structural Invariance

Meaning

Ω measures how much of a structure remains stable under controlled transformation.

It is the primary invariance signal.

Definition

Given:

T = {t1, ..., tn}

Define:

Ω(x) = 1 - (1/n) * sum_i d( f(x), f(ti(x)) )

Range

Ω(x) in [0,1]

Interpretation

Ω → 1  high structural invariance
Ω → 0  high structural fragility

Notes

Ω does not measure truth.

It measures preservation of structural features under transformation.


---

2. IRI — Irreversibility Index

Meaning

IRI measures how much structural information is lost after a transformation and attempted reversal.

A reversible transformation should return close to the original structure.

An irreversible transformation leaves residual damage.

Definition

For each transformation ti, let ti^-1 be an attempted inverse or recovery operation.

IRI(x) = (1/n) * sum_i d( f(x), f(ti^-1(ti(x))) )

Range

IRI(x) in [0,1]

Interpretation

IRI → 0  transformation is structurally reversible
IRI → 1  transformation is structurally irreversible

Notes

IRI requires an explicit recovery or inverse operation.

If no inverse operation is defined, IRI is not computable.


---

3. SEI — Saturation Index

Meaning

SEI measures whether repeated transformations stop producing meaningful new structural information.

A saturated system shows little additional change under continued transformation.

Definition

Let:

Ω_tau(x)

be the invariance signal measured across transformation steps or observation time.

Let:

Var_norm({Ω_tau(x)})

be the normalized variance of the invariance signal.

Define:

SEI(x) = 1 - Var_norm({Ω_tau(x)})

Range

SEI(x) in [0,1]

Interpretation

SEI → 1  saturated / little new structural change
SEI → 0  unstable / continuing structural variation

Notes

SEI is a stop-condition signal.

High SEI can indicate that further transformation is no longer producing meaningful new structural information.


---

4. TΔ — Divergence Time

Meaning

TΔ measures the first point at which structural divergence becomes significant.

It captures when a structure crosses a defined instability threshold.

Definition

Given a trajectory:

x0, x1, x2, ..., xt

Define:

TΔ(x) = min t such that d( f(x0), f(xt) ) >= theta

Range

TΔ(x) >= 0

or undefined if the threshold is never crossed.

Interpretation

small TΔ  rapid structural divergence
large TΔ  delayed structural divergence
undefined TΔ  no detected divergence within observed horizon

Notes

TΔ depends directly on the threshold theta.

Different thresholds produce different divergence times.


---

5. R — Resilience

Meaning

R measures the capacity of a structure to recover after perturbation.

It compares damage caused by perturbation with recovery after correction, reversal, or stabilization.

Definition

Let:

P(x) = perturbed state
C(P(x)) = corrected or recovered state

Define perturbation damage:

D_p = d( f(x), f(P(x)) )

Define residual damage after recovery:

D_r = d( f(x), f(C(P(x))) )

Then:

R(x) = 1 - (D_r / D_p)

when:

D_p > 0

If D_p = 0, R is undefined or set by convention.

Range

R(x) in [0,1]

after clamping.

Interpretation

R → 1  strong recovery
R → 0  poor recovery

Notes

R is meaningful only when a perturbation and recovery procedure are explicitly defined.


---

6. Ω̂ — Residual Invariant Set

Meaning

Ω̂ identifies which structural features remain invariant across transformations.

Unlike Ω, which is a scalar score, Ω̂ is a set.

It answers:

what survived the transformations?

Definition

Let:

Q(f(x)) = set of structural features extracted from x

Then:

Ω̂(x) = { q in Q(f(x)) | q remains stable across all ti in T }

Equivalent condition:

q in Ω̂(x) iff for all ti in T, q(f(x)) = q(f(ti(x)))

or, with tolerance epsilon:

q in Ω̂(x) iff for all ti in T, d_q(q(f(x)), q(f(ti(x)))) <= epsilon

Interpretation

large Ω̂  many residual invariants
small Ω̂  few residual invariants
empty Ω̂  no detected invariant structure

Notes

Ω̂ is often more informative than Ω because it identifies the surviving structural components.


---

7. Score⁺ — Aggregate Bounded Score

Meaning

Score⁺ is a bounded aggregate signal.

It combines multiple structural measurements into a single operational score.

It is not a truth score.

It is not a decision score.

Definition

Let:

wΩ, wI, wS, wR >= 0

and:

wΩ + wI + wS + wR = 1

Define:

Score⁺(x) =
    wΩ * Ω(x)
  + wI * (1 - IRI(x))
  + wS * SEI(x)
  + wR * R(x)

Range

Score⁺(x) in [0,1]

after clamping.

Interpretation

Score⁺ → 1  high aggregate structural stability
Score⁺ → 0  high aggregate structural fragility

Notes

Score⁺ is valid only if all included component metrics are defined.

If a component metric is not computable, it must be excluded and the weights must be renormalized.


---

Optional Local Metric: Co⁺

Status

Co⁺ is retained as a local coherence proxy, not as a core canonical metric.

Meaning

Co⁺ measures internal consistency among structural components.

Definition

Given:

f(x) = (c1, ..., ck)

Define:

Co⁺(x) = 1 - [2 / (k * (k - 1))] * sum_{i<j} d(ci, cj)

Range

Co⁺(x) in [0,1]

Notes

Co⁺ can be useful inside specific implementations, but it is not the main L.O.N. metric.

The core system is:

Ω, IRI, SEI, TΔ, R, Ω̂, Score⁺


---

Metric Relationships

Stability

high Ω
low IRI
high SEI
high R
large Ω̂
high Score⁺

suggest stronger structural stability.

Fragility

low Ω
high IRI
low SEI
low R
small Ω̂
low Score⁺

suggest stronger structural fragility.

Divergence

small TΔ

suggests rapid structural divergence.


---

Required Properties

For a metric to be operationally meaningful, it must satisfy:

1. Reproducibility

Same input, same transformation set, same feature map, same distance function:

same output

2. Falsifiability

There must exist cases where the metric can fail.

A metric that always returns the same value is not informative.

3. Sensitivity

Controlled perturbations should produce measurable changes.

4. Boundedness

All scalar metrics should remain within defined bounds.

5. Context Declaration

Every use must declare:

domain
T
f
d
thresholds
weights

without these, the metric is incomplete.


---

Transformation Constraints

Transformations must be controlled.

They may include:

reordering
format changes
encoding changes
base representation changes
controlled perturbations
compression / decompression
translation between representations

Invalid transformations include:

undefined semantic changes
uncontrolled rewriting
meaning-altering substitution without declaration
hidden human correction


---

Validation Status

These metrics are proposed structural measurements.

Current status:

Ω       formalized and experimentally exercised
IRI     formalized, requires explicit reversibility tests
SEI     formalized, requires trajectory tests
TΔ      formalized, requires temporal / stepwise trajectories
R       formalized, requires perturbation-recovery tests
Ω̂       formalized, requires invariant extraction
Score⁺  formalized as bounded aggregation
Co⁺     optional local proxy

They are not established external standards.

They become operational only when implemented, tested, and reported with full measurement context.


---

Final Constraint

These metrics measure structure.

They do not assert truth.

They do not decide correctness.

They do not replace reasoning.

They expose structural stability, fragility, irreversibility, saturation, divergence, resilience, and residual invariance under controlled transformation.

