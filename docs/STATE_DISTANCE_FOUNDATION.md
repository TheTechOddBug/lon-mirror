# OMNIA — State Distance Foundation v0.1

## Status

This document defines the first operational notion of structural distance between states in OMNIA.

It is not a universal final metric.
It is the canonical minimal definition compatible with the current OMNIA architecture.

Architectural boundary remains unchanged:

measurement != cognition != decision

OMNIA does not interpret meaning.
OMNIA does not decide.
OMNIA measures structural difference under admissible transformations.

---

## 1. Goal

Given two states S1 and S2, define a measurable quantity that answers:

- how much structural difference remains
- after removing admissible representational variation

This quantity is called:

Delta_Omega(S1, S2)

and its operational unit is named:

dO = delta-Omnia

1 dO is one normalized unit of residual structural difference.

---

## 2. State

A state S is any object convertible to a sequence or structural representation compatible with OMNIA.

Examples:

- text
- token stream
- numeric sequence
- model output
- trajectory
- encoded signal

No semantic assumption is required.

---

## 3. Structural signature

Each state S is mapped to a structural signature:

sigma(S) =
(
  omega,
  omega_variance,
  sei,
  drift,
  drift_vector,
  order_sensitivity
)

where:

- omega: structural coherence
- omega_variance: local stability or coherence dispersion
- sei: saturation index
- drift: accumulated deviation
- drift_vector: directional deviation
- order_sensitivity: dependence on ordering

This signature is not truth.
It is a structural fingerprint.

---

## 4. Admissible transformations

Let G be the set of admissible transformations.

Typical examples:

- identity
- base change
- encoding change
- permutation class
- compression / decompression
- controlled perturbation
- representation-preserving rewrite

Only transformations consistent with the measurement protocol are allowed.

The default canonical transformation set for v0.1 is:

G_v0.1 = {
  identity,
  permutation,
  controlled_perturbation,
  compression,
  representation_preserving_rewrite
}

### 4.1 Transformation constraints

A transformation g belongs to G only if it satisfies all of the following:

1. reproducibility
2. explicit declaration in the protocol
3. bounded intensity or parameterization
4. no hidden semantic re-interpretation layer
5. compatibility with the OMNIA architectural boundary

If these conditions are not met, the transformation is invalid for Delta_Omega evaluation.

---

## 5. Primitive distance on signatures

Define a normalized distance d_sigma between two signatures:

d_sigma(sigma1, sigma2)
=
w1 * abs(omega1 - omega2)
+ w2 * abs(omega_variance1 - omega_variance2)
+ w3 * abs(sei1 - sei2)
+ w4 * abs(drift1 - drift2)
+ w5 * D_vec(drift_vector1, drift_vector2)
+ w6 * abs(order_sensitivity1 - order_sensitivity2)

subject to:

- wi >= 0
- sum_i wi = 1
- each component normalized to [0,1]

D_vec is a normalized vector distance.

---

## 5bis. Canonical weights v0.1

The default canonical weights for the primitive signature distance are:

- w1 = 0.30 for omega
- w2 = 0.15 for omega_variance
- w3 = 0.20 for sei
- w4 = 0.15 for drift
- w5 = 0.10 for drift_vector
- w6 = 0.10 for order_sensitivity

These weights satisfy:

- wi >= 0
- sum_i wi = 1

Rationale:

- omega is primary because it captures global structural coherence
- sei is secondary because it captures residual structural capacity
- omega_variance and drift capture stability and deviation
- drift_vector and order_sensitivity are informative but more domain-dependent

These weights are not final.
They are the canonical operational default for v0.1.

---

## 5ter. Normalization constraint

Before computing d_sigma, all signature components must be normalized to [0,1].

Default rule:

x_norm = (x - x_min) / (x_max - x_min)

with clipping to [0,1].

If empirical bounds are unavailable, explicit protocol bounds must be declared.

Distance values are invalid if normalization is omitted.

---

## 6. Canonical state distance

Define the OMNIA residual state distance as:

Delta_Omega(S1, S2) = inf_{g in G} d_sigma( sigma(g(S1)), sigma(S2) )

Interpretation:

- transform S1 through all admissible transformations
- compare structural signatures
- keep the minimal residual difference

This removes representational variation and preserves only non-eliminable structural difference.

---

## 7. Operational unit

The operational unit is:

dO = delta-Omnia

Interpretation:

- 0 dO: structural equivalence under admissible transformations
- small dO: mild residual variation
- large dO: strong structural mismatch
- threshold crossing: regime change candidate

dO is not an SI unit.
It is an internal normalized structural unit.

---

## 8. Derived diagnostics

The scalar Delta_Omega is primary.

The following are derived diagnostics.

### 8.1 Alignment

kappa(S1, S2) = 1 - Delta_Omega(S1, S2)

High kappa means strong structural compatibility.

### 8.2 Drift

epsilon(S1 -> S2) measures persistent directional deviation across ordered transitions.

### 8.3 Break / Drift decomposition

For trajectories x(t), y(t), define:

K(t) = (k_break(t), k_drift(t))

where:

- k_break detects rapid local rupture
- k_drift detects slow persistent deviation

### 8.4 First divergence time

T_Delta = inf { t : Delta_Omega(S_ref(t), S_obs(t)) > epsilon_crit }

### 8.5 Irreversibility

IRI measures non-recoverable residual divergence after threshold crossing.

### 8.6 Resilience

R measures capacity to return below threshold after perturbation.

---

## 9. Interpretation rules

High structural proximity does not imply semantic equality.
Low structural proximity does not imply falsity.

Delta_Omega measures only:

residual structural difference under admissible transformation

Nothing more.

---

## 10. Falsifiability

This definition fails if one or more of the following occur:

1. equivalent states under admissible transformation produce systematically high Delta_Omega
2. structurally distinct states produce systematically low Delta_Omega
3. Delta_Omega is unstable under repeated identical evaluation
4. component normalization makes cross-case comparison impossible
5. the choice of G dominates the result arbitrarily

Therefore the metric is valid only together with:

- explicit transformation set G
- explicit normalization rules
- explicit component weights
- reproducible evaluation protocol

---

## 11. Scope

This definition is expected to transfer across domains only when the domain admits:

- state representation
- admissible transformations
- structural signature extraction
- normalized comparison

This is not universal by declaration.
It is universal only over structurally representable domains.

---

## 12. Minimal claim

OMNIA can define a first operational unit of distance between states.

That unit is:

dO

and its canonical quantity is:

Delta_Omega(S1, S2)

This is a measurement primitive.
Not a theory of meaning.
Not a theory of truth.
Not a decision function.