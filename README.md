# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19657788.svg)](https://doi.org/10.5281/zenodo.19657788)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

# New Here

Start here:

```text
START_HERE.md

If the repository feels broad at first glance, do not begin from the full architecture.

Use this short path first:

1. docs/AT_A_GLANCE.md


2. docs/OMNIA_10_SECONDS_DEMO_RESULT.md


3. docs/RUN_OMNIA_NOW_RESULT.md


4. docs/RUN_OMNIA_NOW_SECOND_RESULT.md


5. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md


6. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md


7. docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md


8. docs/OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md


9. docs/PROOF_CARD.md


10. docs/ONE_EXAMPLE.md


11. docs/OMNIABASE_REVIEW_SENSOR_NOTE.md


12. docs/PHASE6_FREEZE.md


13. docs/EXTERNAL_STATUS.md



That path is currently the shortest route from first contact to the strongest bounded claim supported by the repository.


---

What OMNIA Is

OMNIA is a post-hoc structural measurement engine.

It does not replace reasoning.
It does not interpret semantics.
It does not make final decisions.

Its role is:

measurement only

OMNIA measures whether outputs, states, or trajectories remain structurally stable under controlled transformations.

Core principle:

structural truth = invariance under transformation


---

Architectural Boundary

The architectural boundary is strict:

measurement != inference != decision

OMNIA measures structure.

Another layer may:

reason

interpret

decide

apply policy


OMNIA itself does not collapse these roles.

This prevents the framework from being misread as:

a semantic truth engine

a correctness oracle

a universal gate

a policy engine

a final decision layer


Those interpretations would be false.


---

Structural Metric Layer

The repository now includes a formal structural metric layer.

The framework separates multiple independent structural properties instead of collapsing them into a single scalar score.

Current metrics include:

Ω   → structural invariance
IRI → irreversibility
SEI → saturation
TΔ  → divergence time
R   → resilience
Ω̂   → residual invariant set


---

Current Metric Interpretation

Ω   = how much structure changes
IRI = how much structure cannot be recovered
SEI = whether structural behavior stabilizes
TΔ  = when divergence crosses a critical threshold
R   = how effectively structure recovers
Ω̂   = which structural components survive

These metrics are intentionally separated.

The framework does not compress all structural behavior into a single score.


---

Current Metric Status

The repository currently includes:

formal metric definitions

executable minimal implementations

controlled local validation tests

explicit limitations


Current status:

operationally coherent under controlled tests

Not externally validated.

Not deployment-grade.

Not scientifically established.


---

Current Formal Metric Documents

Formal definitions:

FORMAL_METRICS.md

Controlled validation documents:

RESULTS_IRI_VALIDATION_V2.md
RESULTS_SEI_VALIDATION_V0.md
RESULTS_TDELTA_VALIDATION_V0.md
RESULTS_R_VALIDATION_V0.md
RESULTS_OMEGA_HAT_VALIDATION_V0.md


---

What OMNIA Currently Measures

The current ecosystem includes structural diagnostics such as:

coherence under transformation

compatibility between outputs or states

instability under perturbation

saturation / exhaustion behavior

irreversibility of structural loss

divergence time

resilience after perturbation

residual invariant extraction

bounded post-hoc gate signals


These measurements answer one narrow question:

> what remains structurally stable when representation, perturbation, or viewpoint changes?




---

Current Role of OMNIABASE

OMNIABASE is currently positioned as:

an auxiliary structural review sensor

inside the broader OMNIA measurement architecture.

Its strongest current role is:

bounded review sensing for suspicious-clean outputs

not:

universal rejection

semantic validation

production-grade gating

replacement for strong handcrafted baselines



---

Suspicious-Clean Regime

The strongest current evidence exists in the suspicious-clean region.

Examples include:

soft repetition

low-diversity explanations

rigid templating

near-threshold structural regularity


Example:

The answer seems correct. The answer seems correct. The answer seems correct.

This is readable.

It is superficially acceptable.

It may pass shallow checks.

But structurally it is suspicious enough to justify review.

That is where OMNIABASE currently adds value.


---

Current Layered Policy

The current bounded policy sketch is intentionally simple:

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept

This preserves the intended hierarchy:

baseline   → obvious failures
OMNIABASE  → subtle suspiciousness
decision   → external

Neither OMNIABASE nor OMNIA acts as a universal judge.


---

Current Strongest Supported Claim

The strongest technically honest claim currently supported by the repository is:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.



Nothing stronger is currently justified.


---

Current Repository Direction

The broader repository trajectory points toward:

a bounded runtime structural trust layer
inside the tested perimeter

This is a trajectory.

Not a proven deployment claim.

The repository does NOT currently establish:

universal runtime safety

production readiness

deployment-scale validation

replacement of strong baselines

final decision autonomy



---

Current Repository Focus

The current stable direction is:

Dual-Echo / OMNIAMIND lineage
→ OMNIA structural measurement
→ bounded post-hoc gate behavior
→ OMNIABASE auxiliary review sensing

The repository is no longer purely conceptual.

It now includes:

formal metric definitions

executable experiments

sandbox evaluations

gate-policy experiments

invariant extraction tests

bounded review-sensor evidence



---

Minimal Practical Interpretation

OMNIA should currently be interpreted as:

a layered structural measurement toolkit


---

Baseline Layer

Handles obvious failures well:

loops

repeated tokens

repeated characters

explicit syntactic spam

brittle encoded numeric structures



---

OMNIABASE Layer

Adds bounded review-level caution on outputs that:

still look readable

are not obviously broken

may still pass shallow gates

remain structurally suspicious



---

Decision Layer

Must remain external.

That boundary is intentional.


---

Fastest Visible Entry Point

Shortest demonstrations:

docs/OMNIA_10_SECONDS_DEMO_RESULT.md
docs/RUN_OMNIA_NOW_RESULT.md
docs/RUN_OMNIA_NOW_SECOND_RESULT.md

Observed pattern:

BASELINE: no warning
OMNIA: review
ACTION: review

This is not proof of universal gating.

It is a bounded executable demonstration of distinct policy behavior.


---

Damage-Proxy Results

Current bounded proxy tests:

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md
docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md
docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md
docs/OMNIA_LLM_SUPPORT_SET_v0_RESULTS.md

Observed pattern:

baseline false accepts ↓
combined review policy improves

This does not prove deployment performance.

It shows bounded operational usefulness under tested conditions.


---

Relation Between Metrics

The framework intentionally separates structural properties.

Examples:

high Ω  + low R
high SEI + low Ω
low IRI + small Ω̂

These are different structural states.

The framework avoids collapsing them into a single global interpretation.


---

Current Limits

The repository still has major limitations.


---

1. Sandbox Scope

Most evidence remains sandbox-level.


---

2. Projection Bridge

Current text behavior often depends on:

text → deterministic integer projection → OMNIABASE lens

This remains a limitation.


---

3. Limited Human Validation

Current human-rated tests are still limited in scale and independence.


---

4. No Real Deployment Evidence

There is currently:

no live traffic evidence

no production benchmark

no deployment-scale validation



---

5. Metric Dependency

Current metrics still depend heavily on:

f(x)
d(x,y)
thresholds
weights

Metric forms are therefore not yet canonical.


---

6. Small Damage-Proxy Scope

Current evaluations remain small-scale.

Useful as bounded anchors.

Not broad validation.


---

Current File Landmarks

Core documents:

FORMAL_METRICS.md
docs/OMNIABASE_REVIEW_SENSOR_NOTE.md
docs/PHASE6_FREEZE.md
docs/EXTERNAL_STATUS.md

Metric validation documents:

RESULTS_IRI_VALIDATION_V2.md
RESULTS_SEI_VALIDATION_V0.md
RESULTS_TDELTA_VALIDATION_V0.md
RESULTS_R_VALIDATION_V0.md
RESULTS_OMEGA_HAT_VALIDATION_V0.md

Entry documents:

START_HERE.md
docs/AT_A_GLANCE.md
docs/OMNIA_10_SECONDS_DEMO_RESULT.md
docs/RUN_OMNIA_NOW_RESULT.md
docs/RUN_OMNIA_NOW_SECOND_RESULT.md
docs/PROOF_CARD.md
docs/ONE_EXAMPLE.md


---

Current Claim Level

Current strongest bounded claim:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.



Anything substantially stronger would exceed current evidence.


---

What Should Happen Next

Correct next directions:

1. independent human evaluation


2. threshold calibration


3. real LLM output datasets


4. deployment-like review pipelines


5. large-scale structural benchmarking


6. stronger invariant extraction systems



Wrong direction:

inflating bounded results into universal claims


---

Final Statement

The value of the current repository state is not that it proved universal structural truth.

The value is that it reduced broad structural claims into:

bounded

executable

testable

structurally differentiated

architecturally constrained


measurements.

The repository now contains a coherent structural measurement framework with explicit limits rather than unconstrained conceptual claims.