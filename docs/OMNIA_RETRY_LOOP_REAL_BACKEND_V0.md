# OMNIA Retry Loop Real Backend v0
## First live API integration specification

Status: active  
Priority: high  
Scope: define the first real-backend execution path for OMNIA after the successful adapter-path and dataset-expansion phases

---

## 1. Purpose

This document defines the first real backend integration step for OMNIA.

Goal:

connect the validated retry-loop adapter path to a live generation API while preserving:

- auditability
- bounded intervention
- cost visibility
- latency visibility
- architectural separation

This phase exists to test whether the current runtime gains survive contact with a real, non-deterministic generator.

---

## 2. Why this phase exists

The project has already demonstrated, inside controlled conditions:

- structural detection
- gate calibration
- retry-loop intervention
- runtime adapter behavior
- statistical robustness under dataset expansion

The next unanswered question is:

Can OMNIA maintain a positive safety dividend when the generator is no longer deterministic?

This is the purpose of the Real Backend phase.

---

## 3. Canonical boundary

The same rule remains non-negotiable:

```text
measurement != inference != decision

Interpretation:

the backend model generates

OMNIA measures

the runtime wrapper routes

the host system owns final policy


The real backend wrapper must not turn OMNIA into:

a semantic evaluator

a hidden prompt engineer

a self-correcting reasoning engine


OMNIA remains a bounded post-hoc intervention layer.


---

4. Why a mid-tier model is the correct first target

The first backend should not be:

the strongest model available

the weakest model available

an unstable local experiment

a multi-provider comparison


The correct first target is:

a general-purpose model

stable enough to produce structured output

imperfect enough to expose fragile outputs

cheap enough to support repeated runtime testing


Reason:

A top-tier model may hide OMNIA's value by making too few mistakes. A weak model may saturate the gate with low-value noise.

A middle layer is the correct pressure point.


---

5. Recommended real backend profile

The first backend profile should be:

provider with clean API surface

structured output support

predictable request/response metadata

manageable cost

low implementation friction


Recommended generation profile:

structured JSON output

temperature in the range 0.2 to 0.3

bounded token budget

one retry maximum

same task family already validated in the controlled dataset


This keeps the first live integration interpretable.


---

6. Core runtime flow

The real backend workflow is:

1. receive input payload


2. call live generator for candidate_1


3. run surface acceptance check


4. run OMNIA gate


5. branch:

pass -> accept

low_confidence_flag -> accept with warning

retry -> call live generator again for candidate_2

escalate -> stop and route to higher control



6. if retry occurred:

re-run surface acceptance

re-run OMNIA gate

emit final action



7. record full runtime trace


8. record cost / latency / retry burden


9. compare baseline vs gated workflow



This is the first real transactional form of OMNIA.


---

7. Minimal implementation principle

The first backend integration must remain narrow.

Do not introduce:

multiple models

multiple providers

broad domain variation

dynamic threshold tuning

hidden prompt rewriting loops


The first job is not optimization.

The first job is to test whether the current adapter-path logic survives live stochastic generation.


---

8. Generation wrapper requirements

The real backend wrapper must do the following:

A. Send request

Call the live generation API with the selected model and fixed settings.

B. Receive response

Extract structured output as raw text for the gate.

C. Preserve metadata

Record at least:

provider

model

temperature

token usage if available

latency if available

finish status if available


D. Handle errors

Catch:

network failures

timeout failures

malformed responses

provider-side errors


E. Stay transparent

The wrapper must not silently rewrite output content before OMNIA sees it.


---

9. Retry policy for real backend v0

The retry policy remains intentionally strict.

v0 policy

max_retries = 1


Reason:

cost stays measurable

latency stays bounded

audit trail stays readable

comparison with controlled artifacts remains easy


Retry should happen only when:

candidate_1 passed surface validation

OMNIA emitted retry


Retry should not happen when:

OMNIA emitted escalate

candidate_1 failed surface validation

backend request failed in a way that makes retry meaningless



---

10. Prompt stability rule

The retry must not be a hidden semantic rewrite engine.

The first real backend phase should keep prompt changes minimal.

Allowed retry differences:

identical prompt with fresh generation

minimal system-level reminder to preserve structured output

optional metadata field indicating "second attempt"


Disallowed retry behavior:

long corrective coaching

semantic decomposition

answer hint injection

hidden truth repair logic


Reason:

The test is about OMNIA's intervention value, not about prompt engineering tricks.


---

11. Structured output requirement

The real backend should be asked for structured JSON output.

Reason:

keeps baseline surface validation clear

preserves continuity with prior artifacts

reduces ambiguity in what counts as acceptance

isolates structural quality from formatting chaos


This phase should not yet move into unconstrained prose.


---

12. Runtime state objects

The live backend path should preserve the same audit discipline as the mock adapter path.

Suggested runtime objects:

BackendAttempt

Fields:

attempt_index

request_payload

raw_response_text

surface_accept

gate_action

triggered_rules

signals

rationale

latency_ms

token_usage

provider_metadata


BackendRuntimeResult

Fields:

sample_id

input_payload

attempts

final_action

final_output

accepted

retry_count

escalated

audit_label

cost_metrics

notes


This is required to keep the runtime phase auditable.


---

13. New metric family for real backend phase

In addition to the existing runtime metrics, the real backend phase must measure live operational cost.

Existing metrics to preserve

Safety Dividend

Retry Waste

Retry Yield

Baseline Harmful Accepts

Gated Harmful Accepts

Net Harmful Acceptance Reduction

Over-Defensive Cost

Final Action Distribution

Net Effect Distribution


New real-backend metrics

Request Count

Total live API calls made.

Retry Rate

Fraction of samples that triggered a second API call.

Mean Latency

Average request latency per attempt.

Retry Latency Overhead

Extra latency introduced by OMNIA-triggered retries.

Token Cost

Total token usage if available.

Safety Dividend per Retry

How much safety gain is obtained per additional retry.

Safety Dividend per Unit Cost

How much harmful acceptance reduction is obtained relative to cost.

These metrics are necessary because real integration is not judged only by correctness, but by economics.


---

14. Baseline comparison rule

The real backend phase still needs a baseline.

Baseline means:

candidate_1 only

surface validation only

no OMNIA routing

no retry unless the host system would already retry by default


The gated workflow must always be compared to that baseline.

Without this comparison, the live phase loses interpretability.


---

15. Success criterion for Real Backend v0

The real backend phase is successful if most of the following hold:

1. Safety Dividend remains clearly positive


2. Retry Waste remains materially lower than Safety Dividend


3. Stable outputs remain mostly untouched


4. Real retry still produces some useful recoveries


5. Cost and latency remain bounded enough to justify the intervention


6. The audit trail stays fully readable


7. The gain is not destroyed by live stochasticity



This is enough to justify deeper backend work.


---

16. Failure criterion for Real Backend v0

The real backend phase fails if any of the following dominates:

Safety Dividend collapses toward zero

Retry Waste becomes too close to Safety Dividend

live retry mostly regenerates the same fragility

stable outputs begin to suffer over-defensive penalties

cost/latency overhead makes the intervention economically irrational

runtime logs become too noisy to interpret


A failed live phase is still useful because it reveals whether the barrier is:

model instability

gate design

adapter policy

intervention economics



---

17. Minimal implementation artifact set

The minimal artifact set for this phase should be:

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_V0.md

examples/omnia_retry_loop_real_backend_v0.py

data/omnia_retry_loop_real_backend_v0_results.jsonl

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_V0_RESULTS.md


Optional:

data/omnia_retry_loop_real_backend_v0_inputs.jsonl

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_V0_CONFIG.md



---

18. Minimal first live sample size

The first live backend run should stay small.

Recommended first range:

minimum: 10 samples

preferred: 12 to 20 samples


Reason:

enough to reveal whether runtime stochasticity destroys the gain

small enough to keep cost and audit burden manageable

fast enough to debug before scaling


The first live phase should not jump directly to the 50-sample set.


---

19. Sample selection rule for the first live phase

The first live sample batch should include a balanced mix of:

stable pass cases

borderline fragile cases

retry-success-like tasks

immediate escalate-like tasks

one or two deep nested cases

one or two implicit contradiction cases


This creates a compact but meaningful live pressure test.


---

20. What should not happen in this phase

Do not:

change thresholds again before evidence forces it

expand to multiple providers immediately

compare many models at once

broaden into free-form text

add semantic correctness heuristics

hide failures through aggressive prompt engineering


The goal is realism with interpretability, not maximum benchmark theater.


---

21. Final rule

The real backend phase is the first true contact test between OMNIA and live generation reality.

If the gain survives here, OMNIA stops being only a validated prototype and becomes a defensible runtime safety component.

If the gain does not survive here, the failure must be treated as structural evidence, not as a reason to add narrative complexity.