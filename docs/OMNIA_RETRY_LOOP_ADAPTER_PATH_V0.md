# OMNIA Retry Loop Adapter Path v0
## Minimal runtime integration specification

Status: active  
Priority: high  
Scope: define the first realistic adapter-mediated execution path for OMNIA after the calibrated retry-loop example

---

## 1. Purpose

This document defines the first runtime-oriented integration path for OMNIA.

Goal:

move from a controlled retry-loop benchmark to a minimal execution wrapper that behaves like a real middleware component.

This step does not change OMNIA's role.

OMNIA remains:

- post-hoc
- structural
- bounded
- external to model cognition
- external to final decision ownership

What changes here is the environment:

the gate is no longer evaluated only against pre-baked candidate pairs,
but inserted into an execution path that manages retries, escalation, and audit trail.

---

## 2. Core question

The key question at this stage is no longer:

"Can OMNIA detect fragility?"

That has already been demonstrated inside the tested perimeter.

The key question now is:

"Can OMNIA be inserted into a live-like workflow without creating more operational friction than safety value?"

This is the purpose of the Adapter Path.

---

## 3. Architectural role

The Adapter Path is not a new intelligence layer.

It is a connector between:

- upstream generation
- OMNIA structural measurement
- downstream workflow action

Its job is not to interpret truth.
Its job is to manage intervention flow under bounded rules.

---

## 4. Canonical boundary

The runtime path must preserve the same rule as the rest of the project:

```text
measurement != inference != decision

Interpretation:

the model generates

OMNIA measures

the adapter routes

the host system owns final policy


The adapter may apply bounded local rules such as retry once or escalate, but it must not turn OMNIA into a semantic reasoner.


---

5. Minimal runtime workflow

The minimal adapter-mediated workflow is:

1. receive input


2. generate candidate_1


3. run surface acceptance check


4. run OMNIA gate


5. branch:

pass -> accept

low_confidence_flag -> accept with warning

retry -> generate candidate_2

escalate -> stop and route to higher control



6. if retry occurred:

re-run surface check

re-run OMNIA gate

emit final action



7. save audit trail


8. emit final workflow result



This is the smallest path that counts as a runtime integration.


---

6. Adapter responsibilities

The adapter must do only four things:

A. Normalize input/output shape

Convert host-system output into the form expected by the gate.

B. Manage retry state

Track whether a retry has already been used.

C. Route intervention

Map the gate result to a bounded workflow action.

D. Preserve audit trail

Record the decision path in a machine-readable form.

It must not:

rewrite meaning

perform hidden semantic correction

silently override OMNIA signals

become a second evaluator



---

7. Minimal interface concept

The adapter v0 should expose a small callable path such as:

run_with_omnia_retry_loop(input_payload, generator, max_retries=1) -> RuntimeResult

Where:

input_payload is the original task/input

generator is the upstream generation function or mock

max_retries=1 keeps the loop bounded

RuntimeResult contains both the final decision and the audit trace


This keeps the path importable and reusable.


---

8. Required runtime objects

The adapter v0 should define at least these result objects.

RuntimeAttempt

Represents one generation attempt.

Suggested fields:

attempt_index

model_output

surface_accept

gate_action

triggered_rules

signals

rationale


RuntimeResult

Represents the full workflow result.

Suggested fields:

input_payload

attempts

final_action

final_output

retry_count

escalated

accepted

audit_label

metrics



---

9. Required runtime actions

The adapter must preserve the action semantics established by the gate:

pass

low_confidence_flag

retry

escalate


Additionally, the runtime wrapper may emit final consolidated outcomes such as:

accepted

accepted_flagged

accepted_after_retry

accepted_after_retry_flagged

escalated

retry_failed

reject_surface


This is a workflow-level vocabulary, not a sensor-level vocabulary.


---

10. Retry policy

The retry policy must remain intentionally narrow.

v0 policy

max_retries = 1


Reason:

keeps cost measurable

keeps behavior interpretable

prevents infinite uncertainty loops

preserves auditability


Retry should only occur if:

surface validation passed

OMNIA action is retry


Retry should not occur if:

OMNIA action is escalate

surface validation failed



---

11. Escalation policy

Escalation means:

the output should not be trusted automatically and should be routed to a higher-control path.

Possible higher-control paths include:

human review

stronger model

external validator

stop condition


The adapter v0 does not need to implement the external escalation target. It only needs to emit the escalation state clearly.


---

12. Audit trail requirement

This artifact is worthless without a good audit trail.

Every execution must record:

what candidate was produced

which rules fired

whether retry happened

whether retry improved the result

why the final branch was taken


The audit trail must make it possible to reconstruct:

what happened

why it happened

what OMNIA contributed


This is the minimum standard for operational credibility.


---

13. New metric family: operational efficiency

This phase introduces metrics that do not belong to the earlier static gate benchmark.

Safety Dividend

How many harmful accepts were avoided relative to baseline.

Operational Overhead

How many retries were triggered.

Retry Yield

How many retries produced a better final result.

Retry Waste

How many retries did not improve the outcome.

Escalation Precision

How often escalate was used on genuinely harmful outputs.

Over-Defensive Cost

How often a structurally healthy output was penalized unnecessarily.

These metrics are required because the adapter path is about intervention economics, not only fragility detection.


---

14. Success criterion for Adapter Path v0

The adapter path is successful if all of the following hold:

1. it preserves the OMNIA boundary cleanly


2. it reduces harmful acceptance relative to baseline


3. retry produces some measurable positive yield


4. over-defensive cost remains low


5. the runtime history is audit-ready



This is enough to justify the next stage of integration work.


---

15. Failure criterion for Adapter Path v0

The adapter path fails if any of the following happens:

retry adds cost without meaningful safety dividend

the wrapper hides too much of the decision logic

healthy outputs are over-penalized

escalation is triggered too broadly

the path becomes semantically tangled and stops being interpretable


A failed runtime path is still useful if it shows where intervention economics break.


---

16. Minimal implementation artifact set

The minimal artifact set for this phase is:

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_V0.md

examples/omnia_retry_loop_adapter_path_v0.py

data/omnia_retry_loop_adapter_path_v0_results.jsonl

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_V0_RESULTS.md


Optional:

data/omnia_retry_loop_adapter_path_v0_inputs.jsonl



---

17. Suggested implementation scope

The first implementation should use a mock or controlled generator interface before touching a real external API.

Reason:

isolates logic first

keeps test conditions reproducible

avoids mixing API noise with adapter logic bugs


Only after the wrapper is stable should it be attached to a real generation backend.


---

18. Non-goals

This phase does NOT aim to prove:

universal runtime safety

production deployment readiness

broad domain generalization

semantic truth adjudication

model replacement


It aims only to prove:

OMNIA can function as a bounded runtime intervention layer in a realistic execution path.


---

19. Final rule

The Adapter Path is the first test of whether OMNIA can survive contact with workflow reality.

If it works, OMNIA becomes more than a benchmarked measurement engine. It becomes a usable control component.

If it fails, the failure will be more informative than another round of offline calibration.

