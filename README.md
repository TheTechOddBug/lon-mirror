# OMNIA v1.0 - Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19488048.svg)](https://doi.org/10.5281/zenodo.19488048)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## New here

Start here: [START_HERE.md](./START_HERE.md)

If this repository feels broad at first glance, do not begin from the full architecture.

Use this short path first:

1. [docs/AT_A_GLANCE.md](./docs/AT_A_GLANCE.md)
2. [docs/RUN_OMNIA_NOW_RESULT.md](./docs/RUN_OMNIA_NOW_RESULT.md)
3. [docs/RUN_OMNIA_NOW_SECOND_RESULT.md](./docs/RUN_OMNIA_NOW_SECOND_RESULT.md)
4. [docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md)
5. [docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md)
6. [docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md](./docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md)
7. [docs/PROOF_CARD.md](./docs/PROOF_CARD.md)
8. [docs/ONE_EXAMPLE.md](./docs/ONE_EXAMPLE.md)
9. [docs/OMNIABASE_REVIEW_SENSOR_NOTE.md](./docs/OMNIABASE_REVIEW_SENSOR_NOTE.md)
10. [docs/PHASE6_FREEZE.md](./docs/PHASE6_FREEZE.md)
11. [docs/EXTERNAL_STATUS.md](./docs/EXTERNAL_STATUS.md)

That is the shortest current path from first contact to the strongest bounded claim supported by the repository.

---

## What OMNIA is

OMNIA is a post-hoc structural measurement engine.

It does not replace reasoning.  
It does not interpret semantics.  
It does not make final decisions.

It measures whether an output or state remains structurally stable under controlled transformations.

Core principle:

```text
structural truth = invariance under transformation

OMNIA is designed to detect:

structural stability

fragility

instability

saturation

irreversibility

compatibility shifts


It is not a generative model.
It is not a semantic classifier.
It is not a decision layer.

Output remains:

measurement only


---

Architectural boundary

The architectural boundary is non-negotiable:

measurement != inference != decision

OMNIA measures structure.
Another layer may reason.
Another layer may decide.

OMNIA itself does not collapse these roles.

This boundary matters because it prevents the system from being misread as:

a truth oracle

a semantic validator

a policy engine

a universal gate by itself


That would be false.


---

What OMNIA currently measures

The current ecosystem includes structural diagnostics such as:

coherence under transformation

compatibility between outputs or states

instability under perturbation

saturation / exhaustion behavior

irreversibility of structural loss

divergence time and resilience

bounded post-hoc gate signals


These measurements answer one narrow question:

> what remains structurally stable when representation, perturbation, or viewpoint changes?




---

Current role of OMNIABASE

OMNIABASE is currently positioned as an auxiliary structural review sensor inside the broader OMNIA measurement architecture.

Its best-supported role is not primary rejection and not replacement of strong handcrafted gate rules.

Instead, it is used to add a bounded review signal on outputs that are still superficially acceptable but structurally suspicious, especially in the suspicious-clean region:

soft repetition

low-diversity explanation

rigid templating

near-threshold structural regularity


In the current Phase 6 sandbox results, OMNIABASE showed its strongest value when used in a layered policy such as:

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept

This role is supported by:

synthetic benchmark evidence

gate adapter and sandbox comparisons

end-to-end sandbox policy tests

human-rated sandbox evidence


Shortest role documents:

docs/OMNIABASE_REVIEW_SENSOR_NOTE.md

docs/PHASE6_FREEZE.md


Important boundary:

OMNIABASE is not currently claimed as a production-ready replacement for strong rule-based gates, and it is not presented as a direct retry/reject engine.


---

Why this repository exists

This repository exists to make structural diagnostics executable, testable, and bounded.

The goal is not to produce broader narratives.

The goal is to freeze a usable architecture where:

measurement remains distinct from reasoning

structural diagnostics remain reproducible

instability can be detected before obvious collapse

auxiliary gate signals can be attached without breaking the boundary


This makes OMNIA useful as a structural layer inside broader AI or analysis pipelines.


---

Current repository focus

The current stable direction of the repository is:

Dual-Echo / OMNIAMIND lineage
-> OMNIA measurement
-> bounded post-hoc gate behavior
-> OMNIABASE auxiliary review sensing

This means the repository is no longer only conceptual.

It now contains:

measurement logic

executable sandbox experiments

adapter experiments

gate-policy experiments

bounded evidence for a review-sensor role



---

Minimal practical interpretation

OMNIA should currently be read as a layered structural toolkit.

Baseline layer

Handles obvious failures well, such as:

loops

repeated tokens

repeated characters

explicit syntactic pattern spam

brittle numeric structures when explicitly encoded


OMNIABASE layer

Adds review-level caution on outputs that are not clearly broken but still look structurally suspicious.

Decision layer

Must remain external.

That is the correct current interpretation.


---

Current best-supported use case

The strongest currently supported use case is:

auxiliary review sensing for suspicious-clean outputs

These are outputs that:

still look readable

are not obviously degenerate

may still pass a shallow gate

but show rigidity, low diversity, soft repetition, or suspicious structural regularity


That is where the current evidence is strongest.


---

Minimal executable policy split

The current entry-point demo already shows two minimal readable regimes.

Case 1 - suspicious-clean output

INPUT: The answer seems correct. The answer seems correct. The answer seems correct.
BASELINE: no warning
OMNIA: review
ACTION: review

Case 2 - obvious failure

INPUT: retry retry retry retry retry
BASELINE: warning
OMNIA: review
ACTION: retry

These two cases are enough to expose the current bounded policy split:

suspicious-clean case -> review

obvious failure case -> retry


This does not prove a universal gate.

It shows that the layered policy is at least executable, readable, and behaviorally distinct across two short cases.


---

Minimal executable results

Two minimal executable results are now available:

docs/RUN_OMNIA_NOW_RESULT.md

docs/RUN_OMNIA_NOW_SECOND_RESULT.md


Observed demo patterns:

CASE 1
INPUT: The answer seems correct. The answer seems correct. The answer seems correct.
BASELINE: no warning
OMNIA: review
ACTION: review

CASE 2
INPUT: retry retry retry retry retry
BASELINE: warning
OMNIA: review
ACTION: retry

This is not a universal proof.

It is a bounded executable demonstration that the current layered policy produces two distinct readable regimes:

suspicious-clean case -> review

obvious failure case -> retry



---

Damage-proxy results

Three bounded proxy tests are now available:

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md


V0

N_EXAMPLES: 12
BASELINE_FALSE_ACCEPTS: 4
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 4
EXTRA_REVIEWS_FROM_OMNIA: 4

V1

N_EXAMPLES: 20
BASELINE_FALSE_ACCEPTS: 6
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 6
EXTRA_REVIEWS_FROM_OMNIA: 6

REALISH V0

N_EXAMPLES: 15
BASELINE_FALSE_ACCEPTS: 5
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 5
EXTRA_REVIEWS_FROM_OMNIA: 5

This is the first readable result linking OMNIA to a realistic cost pattern:

false accept reduction under a layered policy

This does not prove deployment performance.

It shows that OMNIA can already be evaluated against a bounded damage proxy rather than architecture alone.


---

One concrete example

A readable output is not automatically a structurally safe output.

Example:

The answer seems correct. The answer seems correct. The answer seems correct.

This is not a catastrophic failure.

It is readable.
It is superficially acceptable.
It may even pass shallow checks.

But structurally it is suspicious enough to justify review.

That is exactly the regime where OMNIABASE currently adds value.

For a compressed walkthrough, read:

docs/ONE_EXAMPLE.md



---

External status

For the clearest statement of what has and has not been shown, read:

docs/EXTERNAL_STATUS.md


The external claim boundary is intentionally narrow.

The strongest current claim that remains technically honest is:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.



Anything stronger than that is premature.


---

What OMNIA is not claiming

This repository does not currently claim that OMNIA or OMNIABASE is:

a production-ready universal gate

a replacement for strong handcrafted baselines

a semantic truth engine

a correctness oracle

a final decision system

a completed deployment layer


Those claims would exceed the current evidence.


---

Repository guide

A good short path through the current repository is:

1. README.md


2. START_HERE.md


3. docs/AT_A_GLANCE.md


4. docs/RUN_OMNIA_NOW_RESULT.md


5. docs/RUN_OMNIA_NOW_SECOND_RESULT.md


6. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md


7. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md


8. docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md


9. docs/PROOF_CARD.md


10. docs/ONE_EXAMPLE.md


11. docs/OMNIABASE_REVIEW_SENSOR_NOTE.md


12. docs/PHASE6_FREEZE.md


13. docs/OMNIA_END_TO_END_SANDBOX_v0_RESULTS.md


14. docs/OMNIA_SUSPICIOUS_CLEAN_EXPANSION_v0_RESULTS.md


15. docs/EXTERNAL_STATUS.md



If the goal is the shortest explanation of the OMNIABASE role, start with:

docs/AT_A_GLANCE.md

docs/RUN_OMNIA_NOW_RESULT.md

docs/RUN_OMNIA_NOW_SECOND_RESULT.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md

docs/PROOF_CARD.md

docs/ONE_EXAMPLE.md

docs/EXTERNAL_STATUS.md


If the goal is the frozen conclusion of the current phase, read:

docs/PHASE6_FREEZE.md



---

Phase 6 summary

Phase 6 established a narrow but credible result:

> OMNIABASE is useful when treated as an auxiliary review trigger, not as a replacement gate.



The current evidence shows:

weak baseline comparison: OMNIABASE adds signal

strong baseline comparison: explicit heuristics remain stronger on obvious pattern classes

real-output sandbox: OMNIABASE adds signal on suspicious-clean outputs

end-to-end policy sandbox: review is the correct action

suspicious-clean expansion: strongest sandbox gain so far

human-rated sandbox pass: combined policy improves over baseline in the tested set


This is enough to define a stable role.

It is not enough to claim full external validation.


---

Example policy sketch

The current best sandbox policy is intentionally simple:

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept

This preserves the right hierarchy:

baseline handles obvious failures

OMNIABASE handles subtle suspiciousness

neither becomes a universal judge



---

Canonical examples

Example 1 - baseline is sufficient

retry retry retry retry retry

A strong handcrafted baseline already catches this.

Example 2 - OMNIABASE adds useful caution

The answer seems correct. The answer seems correct. The answer seems correct.

This may not always be strong enough for explicit heuristics, but it is structurally suspicious enough to justify review.

Example 3 - OMNIABASE can be stricter than needed

12121213

Near-threshold structures can trigger caution even when a human might still accept them.

This is a calibration issue, not something to hide.

It is one reason why OMNIABASE should currently remain a review sensor rather than a direct rejection trigger.


---

Current limitations

The current phase still has active limitations.

1. Projection bridge

For text behavior, OMNIABASE currently depends on:

text -> deterministic integer projection -> OMNIABASE lens

This is useful, but still a limitation.

2. Sandbox evidence

Most current evidence is still sandbox evidence.

3. Human validation is still limited

The current human-rated pass is useful, but not yet independent enough to count as strong external validation.

4. No live deployment evidence

There is still no real traffic or deployment benchmark.

5. Threshold calibration remains open

Useful thresholds exist, but they are not yet final.

6. Damage-proxy scope is still small

The current false-accept results come from 12-example, 20-example, and 15-example support-style evaluations.

They are useful as first external anchors, but still far from broad validation.


---

Current file landmarks

Core and role documents

docs/OMNIABASE_REVIEW_SENSOR_NOTE.md

docs/PHASE6_FREEZE.md


Entry documents

START_HERE.md

docs/AT_A_GLANCE.md

docs/RUN_OMNIA_NOW_RESULT.md

docs/RUN_OMNIA_NOW_SECOND_RESULT.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md

docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md

docs/PROOF_CARD.md

docs/ONE_EXAMPLE.md

docs/EXTERNAL_STATUS.md


Phase 6 result documents

docs/OMNIABASE_SYNTHETIC_BENCHMARK_v0_RESULTS.md

docs/OMNIA_GATE_BASELINE_VS_OMNIABASE_v0_RESULTS.md

docs/OMNIA_GATE_STRONGER_BASELINE_VS_OMNIABASE_v0_RESULTS.md

docs/OMNIA_REAL_OUTPUT_SANDBOX_v0_RESULTS.md

docs/OMNIA_END_TO_END_SANDBOX_v0_RESULTS.md

docs/OMNIA_SUSPICIOUS_CLEAN_EXPANSION_v0_RESULTS.md


Example scripts

RUN_OMNIA_NOW.py

examples/omnia_support_false_accept_miniset_v0.py

examples/omnia_support_false_accept_miniset_v1.py

examples/omnia_support_false_accept_realish_v0.py

examples/omnia_base_gate_adapter_demo.py

examples/omnia_gate_baseline_vs_omniabase_v0.py

examples/omnia_gate_stronger_baseline_vs_omniabase_v0.py

examples/omnia_real_output_sandbox_v0.py

examples/omnia_end_to_end_sandbox_v0.py

examples/omnia_suspicious_clean_expansion_v0.py

examples/omnia_human_rated_validation_pack_v0.py

examples/omnia_human_validation_compare_v0.py


Core lens

omnia/lenses/base_lens.py



---

Current claim level

The strongest current claim that remains technically honest is:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.



Anything stronger than that is premature.


---

What should happen next

The next correct directions are:

1. independent human rating


2. threshold calibration


3. small corpus of real LLM outputs


4. deployment-like review pipeline test



The wrong direction would be to inflate OMNIABASE back into universal claims.


---

Final statement

The value of the current repository state is not that it proved everything.

The value is that it reduced a broad and unstable idea into a role that is:

specific

testable

operationally plausible

architecturally bounded

technically honest


That is stronger than a larger claim that cannot survive contact with data.