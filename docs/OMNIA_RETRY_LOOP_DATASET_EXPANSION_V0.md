# OMNIA Retry Loop Dataset Expansion v0
## Statistical robustness step before real backend integration

Status: active  
Priority: high  
Scope: expand the retry-loop / adapter-path dataset from the initial 17-sample perimeter to a broader 40–60 sample validation set

---

## 1. Purpose

This document defines the next controlled step after the successful runtime validation of:

- Silent Failure Gate v0.2
- Retry Loop v0
- Adapter Path v0

The goal is not to invent new behavior.

The goal is to test whether the current runtime advantages remain stable when the sample perimeter becomes larger and more structurally diverse.

This is a robustness step, not a conceptual expansion step.

---

## 2. Why dataset expansion comes before real backend integration

The current runtime result is strong, but still based on a small controlled sample set.

Before connecting a live generation backend, the system must be pressure-tested under broader controlled conditions.

Reason:

if the next step changed both:

- dataset size
- backend behavior

then any degradation would become hard to interpret.

By changing only dataset size now, we preserve causal readability.

This follows the rule:

```text
one variable at a time


---

3. Main question

The key question of this phase is:

Do the current adapter-path gains remain stable when the runtime workflow is tested against a broader and more varied structured-output set?

More precisely:

does Safety Dividend remain clearly positive

does Retry Waste remain bounded

does Over-Defensive Cost remain near zero

does the retry branch remain useful

does the current threshold set still generalize



---

4. Target dataset size

Recommended expansion target:

minimum: 40 samples

preferred: 50 samples

maximum for v0: 60 samples


This is enough to:

reduce the risk of accidental overfitting to the first 17 samples

expose new structural edge cases

keep manual audit still feasible


The expanded set must remain fully labeled and reproducible.


---

5. What must remain unchanged in this phase

The following elements should remain fixed during dataset expansion:

Silent Failure Gate v0.2 thresholds

Retry-loop logic

Adapter-path logic

Runtime action vocabulary

Operational metrics


This is critical.

If performance changes, the cause should be attributable primarily to the broader dataset, not to simultaneous architectural modifications.


---

6. Existing category structure to preserve

The current dataset logic already defines important classes.

These must remain represented in the expanded set:

retry success

retry persistent

immediate escalate

stable pass

borderline flag


These classes should not be removed. They should be deepened.


---

7. New stress categories to add

The expanded dataset should add more difficult structural patterns.

A. Deep nested structures

Examples:

nested JSON objects

multi-level rationale fields

lists inside objects

status plus substatus plus explanation


Purpose: test whether the current purity / compatibility logic remains stable when structure depth increases.


---

B. Implicit contradictions

Examples:

top-level status says "ok" while nested evidence implies failure

action says "safe" while explanation implies risky escalation

category label and explanatory trace diverge without explicit keyword inversion


Purpose: test whether structural tension can still be detected when contradiction is not purely literal.


---

C. Edge-case stability

Examples:

very compact but correct outputs

unusually verbose but still coherent outputs

almost repetitive outputs that remain operationally valid

minimally justified outputs that should still pass


Purpose: test the limit of over-defensiveness.


---

D. Controlled redundancy without harm

Examples:

benign explanation overlap

mild reformulation loops that remain acceptable

repeated terms due to valid task constraints


Purpose: avoid training the benchmark toward punishing any repetition automatically.


---

E. Hard silent failures

Examples:

JSON valid, strongly assertive, operationally dangerous

structurally clean surface with hidden harmful action mapping

subtle policy overreach hidden behind coherent formatting


Purpose: test whether escalate precision survives stronger adversarial examples.


---

F. Retry ambiguity cases

Examples:

first output structurally weak but potentially recoverable

second output improved but still not fully clean

second output changes semantics but not stability enough


Purpose: stress the boundary between:

accepted_after_retry

accepted_after_retry_flagged

retry_failed



---

8. Required label discipline

Every new sample must keep the same label rigor as the current set.

Required fields:

sample_id

input_text

candidate_1_output

candidate_1_real_outcome

candidate_2_output

candidate_2_real_outcome

notes


Recommended additional optional fields:

stress_category

risk_level

label_rationale


The expanded dataset must not become vague. It must remain auditable.


---

9. Success criteria for the expansion phase

The dataset expansion is successful if the broader rerun shows most of the following:

1. Safety Dividend remains clearly positive


2. Retry Waste remains materially lower than Safety Dividend


3. Over-Defensive Cost remains near zero or very low


4. Stable pass cases remain mostly stable


5. Immediate danger cases remain escalated


6. Retry branch still has non-trivial yield


7. Threshold behavior remains interpretable



This is enough to justify backend integration.


---

10. Failure criteria for the expansion phase

The expansion phase fails if any of the following becomes dominant:

Safety Dividend collapses toward zero

Retry Waste grows too close to Safety Dividend

stable cases are frequently over-penalized

many dangerous cases stop being intercepted

the current threshold set becomes erratic across categories

auditability becomes too noisy to support interpretation


A failed expansion is still useful because it reveals where the current calibration does not generalize.


---

11. Metrics to preserve

The rerun on the expanded dataset must preserve the same operational metrics:

Safety Dividend

Retry Waste

Retry Yield

Baseline Harmful Accepts

Gated Harmful Accepts

Net Harmful Acceptance Reduction

Over-Defensive Cost

Final Action Distribution

Net Effect Distribution


This ensures continuity with the earlier runtime artifacts.


---

12. Recommended artifact set

The minimal artifact set for this phase should be:

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_V0.md

data/omnia_silent_failure_retry_loop_v1_samples.jsonl

data/omnia_retry_loop_adapter_path_v1_results.jsonl

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_V0_RESULTS.md


Optional supporting artifact:

docs/OMNIA_RETRY_LOOP_DATASET_LABELING_GUIDE_V0.md



---

13. Naming rule

The existing 17-sample set should remain preserved as the compact validation baseline.

The expanded set should use a new name such as:

omnia_silent_failure_retry_loop_v1_samples.jsonl


This avoids overwriting the earlier perimeter and preserves traceability.


---

14. What should not happen in this phase

Do not:

change the gate thresholds again unless the broader rerun forces it

connect a live backend yet

introduce multiple new domains at once

rewrite the adapter logic

expand into unconstrained free-form text


This phase is about statistical strengthening, not scope explosion.


---

15. Final rule

The dataset expansion phase exists to answer one question only:

Can the current adapter-path gain survive broader controlled pressure?

If yes, the system is ready for real backend integration.

If no, the failure must be fixed before touching a live generation API.