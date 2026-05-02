# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19857066.svg)](https://doi.org/10.5281/zenodo.19857066)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

# New Here

Start here:

- [START_HERE.md](./START_HERE.md)

If the repository feels broad at first glance, do not begin from the full architecture.

Use this short path first:

1. [CANONICAL_EVIDENCE.md](./CANONICAL_EVIDENCE.md)
2. [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)
3. [FORMAL_METRICS.md](./FORMAL_METRICS.md)
4. [AT_A_GLANCE.md](./docs/AT_A_GLANCE.md)
5. [OMNIA_10_SECONDS_DEMO_RESULT.md](./docs/OMNIA_10_SECONDS_DEMO_RESULT.md)
6. [RUN_OMNIA_NOW_RESULT.md](./docs/RUN_OMNIA_NOW_RESULT.md)
7. [RUN_OMNIA_NOW_SECOND_RESULT.md](./docs/RUN_OMNIA_NOW_SECOND_RESULT.md)
8. [OMNIABASE_REVIEW_SENSOR_NOTE.md](./docs/OMNIABASE_REVIEW_SENSOR_NOTE.md)
9. [PHASE6_FREEZE.md](./docs/PHASE6_FREEZE.md)
10. [EXTERNAL_STATUS.md](./docs/EXTERNAL_STATUS.md)

That path is currently the shortest route from first contact to the strongest bounded claim supported by the repository.

---

# Quick External Run

To execute the current canonical evidence cases:

```bash
python RUN_ALL_CANONICAL_CASES.py
```

Runner file:

- [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)

This runner executes the current canonical structural cases:

1. suspicious-clean review signal
2. correctness vs structural stability
3. irreversibility
4. saturation
5. divergence timing
6. resilience
7. residual invariant extraction

The purpose is not to prove universal structural truth.

The purpose is to expose the framework to quick external inspection.

Expected interpretation:

```text
the framework separates multiple structural properties under controlled tests
```

Not more.

---

# What OMNIA Is

OMNIA is a post-hoc structural measurement engine.

It does not replace reasoning.  
It does not interpret semantics.  
It does not make final decisions.

Its role is:

```text
measurement only
```

OMNIA measures whether outputs, states, or trajectories remain structurally stable under controlled transformations.

Core principle:

```text
structural truth = invariance under transformation
```

This is a measurement principle, not a claim of semantic truth.

---

# Architectural Boundary

The architectural boundary is strict:

```text
measurement != inference != decision
```

OMNIA measures structure.

Another layer may:

- reason
- interpret
- decide
- apply policy

OMNIA itself does not collapse these roles.

This prevents the framework from being misread as:

- a semantic truth engine
- a correctness oracle
- a universal gate
- a policy engine
- a final decision layer

Those interpretations would be false.

---

# Core Contribution

The current contribution of this repository is not a universal intelligence system.

It is a bounded structural measurement framework.

The framework separates structural behavior into distinct measurable properties:

```text
change
irreversibility
saturation
divergence timing
recovery
residual invariants
```

This separation is the main point.

OMNIA does not reduce structural behavior to a single vague score.

---

# Structural Metric Layer

The repository includes a formal structural metric layer.

Current metrics include:

```text
Omega      structural invariance
IRI        irreversibility
SEI        saturation
TDelta     divergence time
R          resilience
Omega-hat  residual invariant set
```

ASCII aliases are used where needed for compatibility:

```text
Omega      = Ω
TDelta     = TΔ
Omega-hat  = Ω̂
```

---

# Current Metric Interpretation

```text
Omega      = how much structure changes
IRI        = how much structure cannot be recovered
SEI        = whether structural behavior stabilizes
TDelta     = when divergence crosses a critical threshold
R          = how effectively structure recovers
Omega-hat  = which structural components survive
```

These metrics are intentionally separated.

The framework does not compress all structural behavior into one global interpretation.

---

# Current Metric Status

The repository currently includes:

- formal metric definitions
- executable minimal implementations
- controlled local validation tests
- explicit limitations
- a single-entry canonical runner

Current status:

```text
operationally coherent under controlled tests
```

Not externally validated.

Not deployment-grade.

Not scientifically established.

---

# Current Formal Metric Documents

Formal definitions:

- [FORMAL_METRICS.md](./FORMAL_METRICS.md)

Canonical evidence:

- [CANONICAL_EVIDENCE.md](./CANONICAL_EVIDENCE.md)

External test pack:

- [OMNIA_EXTERNAL_TEST_PACK_V0.md](./OMNIA_EXTERNAL_TEST_PACK_V0.md)
- [RUN_EXTERNAL_TEST_PACK_V0.md](./RUN_EXTERNAL_TEST_PACK_V0.md)
- [RUN_ALL_CANONICAL_CASES.md](./RUN_ALL_CANONICAL_CASES.md)
- [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)

Controlled validation documents:

- [RESULTS_IRI_VALIDATION_V2.md](./RESULTS_IRI_VALIDATION_V2.md)
- [RESULTS_SEI_VALIDATION_V0.md](./RESULTS_SEI_VALIDATION_V0.md)
- [RESULTS_TDELTA_VALIDATION_V0.md](./RESULTS_TDELTA_VALIDATION_V0.md)
- [RESULTS_R_VALIDATION_V0.md](./RESULTS_R_VALIDATION_V0.md)
- [RESULTS_OMEGA_HAT_VALIDATION_V0.md](./RESULTS_OMEGA_HAT_VALIDATION_V0.md)

---

# Canonical Evidence

For a compressed view of the strongest currently readable evidence slices, see:

- [CANONICAL_EVIDENCE.md](./CANONICAL_EVIDENCE.md)

This file collects the current canonical cases where surface validity and structural stability separate.

It includes examples covering:

```text
suspicious-clean review
correctness vs stability
irreversibility
saturation
divergence timing
resilience
residual invariant extraction
```

The purpose is not to prove universal structural truth.

The purpose is to provide a small, inspectable, rerunnable evidence surface for the current framework.

---

# What OMNIA Currently Measures

The current ecosystem includes structural diagnostics such as:

- coherence under transformation
- compatibility between outputs or states
- instability under perturbation
- saturation / exhaustion behavior
- irreversibility of structural loss
- divergence time
- resilience after perturbation
- residual invariant extraction
- bounded post-hoc gate signals

These measurements answer one narrow question:

> what remains structurally stable when representation, perturbation, or viewpoint changes?

---

# Current Role of OMNIABASE

OMNIABASE is currently positioned as:

```text
an auxiliary structural review sensor
```

inside the broader OMNIA measurement architecture.

Its strongest current role is:

```text
bounded review sensing for suspicious-clean outputs
```

not:

- universal rejection
- semantic validation
- production-grade gating
- replacement for strong handcrafted baselines

---

# Suspicious-Clean Regime

The strongest current OMNIABASE evidence exists in the suspicious-clean region.

Examples include:

- soft repetition
- low-diversity explanations
- rigid templating
- near-threshold structural regularity

Example:

```text
The answer seems correct. The answer seems correct. The answer seems correct.
```

This is readable.

It is superficially acceptable.

It may pass shallow checks.

But structurally it is suspicious enough to justify review.

That is where OMNIABASE currently adds value.

---

# Current Layered Policy

The current bounded policy sketch is intentionally simple:

```python
if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept
```

This preserves the intended hierarchy:

```text
baseline   obvious failures
OMNIABASE  subtle suspiciousness
decision   external
```

Neither OMNIABASE nor OMNIA acts as a universal judge.

---

# Current Strongest Supported Claim

The strongest technically honest claim currently supported by the repository is:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.

Nothing stronger is currently justified.

---

# Current Repository Direction

The broader repository trajectory points toward:

```text
a bounded runtime structural trust layer
inside the tested perimeter
```

This is a trajectory.

Not a proven deployment claim.

The repository does not currently establish:

- universal runtime safety
- production readiness
- deployment-scale validation
- replacement of strong baselines
- final decision autonomy

---

# Current Repository Focus

The current stable direction is:

```text
Dual-Echo / OMNIAMIND lineage
-> OMNIA structural measurement
-> bounded post-hoc gate behavior
-> OMNIABASE auxiliary review sensing
-> formal structural metric layer
-> canonical evidence
-> external reproducibility path
```

The repository is no longer purely conceptual.

It now includes:

- formal metric definitions
- executable experiments
- sandbox evaluations
- gate-policy experiments
- invariant extraction tests
- bounded review-sensor evidence
- canonical evidence compression
- single-entry canonical execution

---

# Minimal Practical Interpretation

OMNIA should currently be interpreted as:

```text
a layered structural measurement toolkit
```

---

## Baseline Layer

Handles obvious failures well:

- loops
- repeated tokens
- repeated characters
- explicit syntactic spam
- brittle encoded numeric structures

---

## OMNIABASE Layer

Adds bounded review-level caution on outputs that:

- still look readable
- are not obviously broken
- may still pass shallow gates
- remain structurally suspicious

---

## Metric Layer

Separates structural behavior into measurable properties:

- invariance
- irreversibility
- saturation
- divergence timing
- resilience
- residual invariant extraction

---

## Runner Layer

Provides a single-entry reproduction path:

```bash
python RUN_ALL_CANONICAL_CASES.py
```

Runner file:

- [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)

This lowers external inspection friction.

---

## Decision Layer

Must remain external.

That boundary is intentional.

---

# Fastest Visible Entry Points

Shortest demonstrations:

- [CANONICAL_EVIDENCE.md](./CANONICAL_EVIDENCE.md)
- [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)
- [OMNIA_10_SECONDS_DEMO_RESULT.md](./docs/OMNIA_10_SECONDS_DEMO_RESULT.md)
- [RUN_OMNIA_NOW_RESULT.md](./docs/RUN_OMNIA_NOW_RESULT.md)
- [RUN_OMNIA_NOW_SECOND_RESULT.md](./docs/RUN_OMNIA_NOW_SECOND_RESULT.md)

Observed policy pattern:

```text
BASELINE: no warning
OMNIA: review
ACTION: review
```

This is not proof of universal gating.

It is a bounded executable demonstration of distinct policy behavior.

---

# Damage-Proxy Results

Current bounded proxy tests:

- [OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md)
- [OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md)
- [OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md)
- [OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md](./docs/OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md)

Observed pattern:

```text
baseline false accepts decrease
combined review policy improves
```

This does not prove deployment performance.

It shows bounded operational usefulness under tested conditions.

---

# Structural Separations Already Demonstrated

The repository currently contains controlled examples separating:

```text
readability       != structural safety
correctness       != structural stability
change            != irreversible loss
stabilization     != correctness
divergence amount != divergence timing
damage            != recovery capability
score             != surviving invariant structure
```

These separations are the central technical value of the current framework.

---

# Relation Between Metrics

The framework intentionally separates structural properties.

Examples:

```text
high Omega + low R
high SEI   + low Omega
low IRI    + small Omega-hat
```

These are different structural states.

The framework avoids collapsing them into a single global interpretation.

---

# What OMNIA Is Not Claiming

This repository does not claim that OMNIA or OMNIABASE is:

- a production-ready universal gate
- a replacement for strong handcrafted baselines
- a semantic truth engine
- a correctness oracle
- a final decision system
- a completed deployment layer
- a proof of universal structural truth

Those claims would exceed the current evidence.

---

# Current Limits

The repository still has major limitations.

---

## 1. Sandbox Scope

Most evidence remains sandbox-level.

---

## 2. Projection Bridge

Current text behavior often depends on:

```text
text -> deterministic integer projection -> OMNIABASE lens
```

This remains a limitation.

---

## 3. Limited Human Validation

Current human-rated tests are still limited in scale and independence.

---

## 4. No Real Deployment Evidence

There is currently:

- no live traffic evidence
- no production benchmark
- no deployment-scale validation

---

## 5. Metric Dependency

Current metrics still depend heavily on:

```text
f(x)
d(x,y)
thresholds
weights
```

Metric forms are therefore not yet canonical.

---

## 6. Small Damage-Proxy Scope

Current evaluations remain small-scale.

Useful as bounded anchors.

Not broad validation.

---

# Current File Landmarks

Core documents:

- [README.md](./README.md)
- [START_HERE.md](./START_HERE.md)
- [CANONICAL_EVIDENCE.md](./CANONICAL_EVIDENCE.md)
- [FORMAL_METRICS.md](./FORMAL_METRICS.md)
- [OMNIA_EXTERNAL_TEST_PACK_V0.md](./OMNIA_EXTERNAL_TEST_PACK_V0.md)
- [RUN_EXTERNAL_TEST_PACK_V0.md](./RUN_EXTERNAL_TEST_PACK_V0.md)
- [RUN_ALL_CANONICAL_CASES.md](./RUN_ALL_CANONICAL_CASES.md)
- [RUN_ALL_CANONICAL_CASES.py](./RUN_ALL_CANONICAL_CASES.py)
- [AT_A_GLANCE.md](./docs/AT_A_GLANCE.md)
- [OMNIABASE_REVIEW_SENSOR_NOTE.md](./docs/OMNIABASE_REVIEW_SENSOR_NOTE.md)
- [PHASE6_FREEZE.md](./docs/PHASE6_FREEZE.md)
- [EXTERNAL_STATUS.md](./docs/EXTERNAL_STATUS.md)

Metric validation documents:

- [RESULTS_IRI_VALIDATION_V2.md](./RESULTS_IRI_VALIDATION_V2.md)
- [RESULTS_SEI_VALIDATION_V0.md](./RESULTS_SEI_VALIDATION_V0.md)
- [RESULTS_TDELTA_VALIDATION_V0.md](./RESULTS_TDELTA_VALIDATION_V0.md)
- [RESULTS_R_VALIDATION_V0.md](./RESULTS_R_VALIDATION_V0.md)
- [RESULTS_OMEGA_HAT_VALIDATION_V0.md](./RESULTS_OMEGA_HAT_VALIDATION_V0.md)

Entry and proof documents:

- [OMNIA_10_SECONDS_DEMO_RESULT.md](./docs/OMNIA_10_SECONDS_DEMO_RESULT.md)
- [RUN_OMNIA_NOW_RESULT.md](./docs/RUN_OMNIA_NOW_RESULT.md)
- [RUN_OMNIA_NOW_SECOND_RESULT.md](./docs/RUN_OMNIA_NOW_SECOND_RESULT.md)
- [PROOF_CARD.md](./docs/PROOF_CARD.md)
- [ONE_EXAMPLE.md](./docs/ONE_EXAMPLE.md)

Damage-proxy documents:

- [OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md)
- [OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md)
- [OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md)
- [OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md](./docs/OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md)

---

# Current Claim Level

Current strongest bounded claim:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.

Anything substantially stronger would exceed current evidence.

---

# What Should Happen Next

Correct next directions:

1. independent human evaluation
2. threshold calibration
3. real LLM output datasets
4. deployment-like review pipelines
5. large-scale structural benchmarking
6. stronger invariant extraction systems
7. cross-metric evidence cases
8. improved external reproducibility

Wrong direction:

```text
inflating bounded results into universal claims
```

---

# Final Statement

The value of the current repository state is not that it proved universal structural truth.

The value is that it reduced broad structural claims into:

- bounded
- executable
- testable
- structurally differentiated
- architecturally constrained
- externally inspectable

measurements.

The repository now contains a coherent structural measurement framework with explicit limits rather than unconstrained conceptual claims.

---

```text
LON-MIRROR
|
├── CORE
|   ├── OMNIA
|   ├── OMNIA-INVARIANCE
|   ├── omnia-limit
|   └── OMNIA-RADAR
|
├── RESEARCH
|   ├── OMNIA-CONSTANT
|   └── OMNIA-THREE-BODY
|
├── REPRESENTATION
|   └── OMNIABASE
|
└── APPLICATIONS
    ├── OMNIA-SECURITY
    ├── OMNIA-CRYPTO
    └── OMNIAMIND

Root

LON-MIRROR


Canonical ecosystem hub, lineage map, navigation layer, and coordination entry point.


---

Core

OMNIA


Core structural measurement framework.

OMNIA-INVARIANCE


Core validation and invariance-testing repository.
Focuses on structural invariance, perturbation behavior, and controlled evidence around Ω under transformation.

omnia-limit


Structural stopping conditions, saturation, irreducibility, and limit behavior.

OMNIA-RADAR


Structural drift surfacing and trajectory visualization layer.


---

Research

OMNIA-CONSTANT


Post-analysis and falsification repository for Ω-region behavior.
Current focus: whether observed Ω corridors behave as structural transition regimes or collapse as measurement artifacts.
No universal structural constant is declared.

OMNIA-THREE-BODY


Experimental dynamics repository for multi-body structural interaction tests.
Focuses on instability, trajectory interaction, and non-trivial structural behavior under interacting perturbations.


---

Representation

OMNIABASE


Multi-base structural representation and invariance exploration layer.


---

Applications

OMNIA-SECURITY


Bounded structural diagnostics for security-relevant systems.

OMNIA-CRYPTO


Bounded structural diagnostics for cryptographic behavior.

OMNIAMIND


Bounded structural diagnostics for cognitive and reasoning-related behavior.


---

Architectural Separation

LON-MIRROR
=
ecosystem hub

OMNIA
=
core structural measurement layer

OMNIA-INVARIANCE
=
core invariance validation layer

OMNIA-CONSTANT
=
post-analysis / falsification layer for Ω-region behavior

OMNIA-THREE-BODY
=
experimental structural dynamics layer

Other repositories
=
representation layers,
limit layers,
visualization layers,
or bounded domain verticalizations.


---

Core Boundary

measurement != inference != decision
---

