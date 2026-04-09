# OMNIA — State Distance Foundation v0.2

## Status

This document defines the second operational notion of structural distance between states in OMNIA.

Version v0.2 extends v0.1 after falsification on the expanded synthetic validation set.

The main changes are:

- explicit local transition sensitivity
- explicit run-length sensitivity
- explicit local numeric delta sensitivity
- explicit transformation cost

Architectural boundary remains unchanged:

measurement != cognition != decision

OMNIA does not interpret meaning.
OMNIA does not decide.
OMNIA measures residual structural difference under admissible transformations.

---

## 1. Goal

Given two states S1 and S2, define a measurable quantity that answers:

- how much structural difference remains
- after admissible representational variation is accounted for
- while penalizing transformations that themselves alter structure

This quantity is called:

Delta_Omega(S1, S2)

and its operational unit is:

dO = delta-Omnia

1 dO is one normalized unit of residual structural difference.

---

## 2. State

A state S is any object convertible to a structural representation compatible with OMNIA.

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
  order_sensitivity,
  transition_frequency,
  run_length_irregularity,
  local_delta_pattern
)

where:

- omega: global structural coherence
- omega_variance: local stability dispersion
- sei: saturation index
- drift: accumulated deviation
- drift_vector: directional deviation
- order_sensitivity: dependence on ordering
- transition_frequency: rate of adjacent state change
- run_length_irregularity: structure of contiguous runs
- local_delta_pattern: local pattern of adjacent numeric differences

This signature is not truth.
It is a structural fingerprint.

---

## 4. Admissible transformations

Let G be the set of admissible transformations.

The default canonical transformation set for v0.2 is:

G_v0.2 = {
  identity,
  controlled_perturbation,
  compression,
  representation_preserving_rewrite,
  permutation
}

A transformation g belongs to G only if it satisfies all of the following:

1. reproducibility
2. explicit declaration in the protocol
3. bounded intensity or parameterization
4. no hidden semantic reinterpretation
5. compatibility with the OMNIA architectural boundary

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
+ w7 * abs(transition_frequency1 - transition_frequency2)
+ w8 * abs(run_length_irregularity1 - run_length_irregularity2)
+ w9 * abs(local_delta_pattern1 - local_delta_pattern2)

subject to:

- wi >= 0
- sum_i wi = 1
- each component normalized to [0,1]

---

## 5bis. Canonical weights v0.2

The default canonical weights are:

- w1 = 0.20 for omega
- w2 = 0.10 for omega_variance
- w3 = 0.15 for sei
- w4 = 0.10 for drift
- w5 = 0.05 for drift_vector
- w6 = 0.10 for order_sensitivity
- w7 = 0.10 for transition_frequency
- w8 = 0.10 for run_length_irregularity
- w9 = 0.10 for local_delta_pattern

These weights are operational defaults only.

---

## 5ter. Normalization constraint

Before computing d_sigma, all signature components must be normalized to [0,1].

Default rule:

x_norm = (x - x_min) / (x_max - x_min)

with clipping to [0,1].

Distance values are invalid if normalization is omitted.

---

## 6. Transformation cost

Admissible transformations are not free.

Define a transformation cost:

C_transform(g, S) in [0,1]

Default canonical costs for v0.2:

- identity = 0.00
- controlled_perturbation = 0.03
- compression = 0.04
- representation_preserving_rewrite = 0.05
- permutation = 0.25

These values are operational defaults only.

---

## 7. Canonical state distance

Define the OMNIA residual state distance as:

Delta_Omega(S1, S2) =
inf_{g in G} [
  d_sigma( sigma(g(S1)), sigma(S2) ) + lambda * C_transform(g, S1)
]

where lambda is the transformation-cost coefficient.

Default canonical value:

lambda = 0.50

Interpretation:

- transform S1 through admissible transformations
- compare structural signatures
- penalize transformations according to structural cost
- keep the minimal residual total distance

This removes superficial representational variation without making strong structural transformations free.

---

## 8. Operational unit

The operational unit is:

dO = delta-Omnia

Interpretation:

- 0 dO: structural equivalence under low-cost admissible transformations
- small dO: mild residual variation
- large dO: strong structural mismatch
- threshold crossing: regime change candidate

dO is not an SI unit.
It is a normalized internal structural unit.

---

## 9. Derived diagnostics

The scalar Delta_Omega is primary.

The following are derived diagnostics:

### 9.1 Alignment

kappa(S1, S2) = 1 - Delta_Omega(S1, S2)

### 9.2 Drift

epsilon(S1 -> S2) measures persistent directional deviation across ordered transitions.

### 9.3 Break / Drift decomposition

For trajectories x(t), y(t), define:

K(t) = (k_break(t), k_drift(t))

### 9.4 First divergence time

T_Delta = inf { t : Delta_Omega(S_ref(t), S_obs(t)) > epsilon_crit }

### 9.5 Irreversibility

IRI measures non-recoverable residual divergence after threshold crossing.

### 9.6 Resilience

R measures capacity to return below threshold after perturbation.

---

## 10. Interpretation rules

High structural proximity does not imply semantic equality.
Low structural proximity does not imply falsity.

Delta_Omega measures only:

residual structural difference under admissible transformation and transformation cost

Nothing more.

---

## 11. Falsifiability

This definition fails if one or more of the following occur:

1. equivalent states repeatedly produce high Delta_Omega
2. local real variations collapse into equivalence
3. ordering-regime changes collapse into equivalence or mild variation
4. transformation cost does not prevent over-cleaning
5. repeated identical evaluation is unstable

Therefore the metric is valid only together with:

- explicit transformation set G
- explicit transformation costs
- explicit normalization rules
- explicit component weights
- reproducible evaluation protocol

---

## 12. Scope

This definition transfers across domains only when the domain admits:

- state representation
- admissible transformations
- structural signature extraction
- normalized comparison

It is not universal by declaration.
It is transferable only across structurally representable domains.

---

## 13. Minimal claim

OMNIA can define a second operational unit of distance between states.

That unit remains:

dO

and its canonical quantity is:

Delta_Omega(S1, S2)

This is a measurement primitive.
Not a theory of meaning.
Not a theory of truth.
Not a decision function.