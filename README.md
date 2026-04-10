# OMNIA v1.0 - Structura Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19497026.svg)](https://doi.org/10.5281/zenodo.19497026)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What OMNIA is

Systems often appear stable until failure is already visible.

OMNIA is a post-hoc structural measurement engine designed to detect coherence, fragility, instability, and regime change before these effects become obvious at the surface level.

It does not interpret semantics.  
It does not replace model cognition.  
It does not make final decisions.  
It does not act as a proof engine.  
It does not act as a primality test.

OMNIA measures only:

```text
output = measurement only
structural behavior under controlled transformations


---

Core principle

Structural truth = invariance under transformation

If a structure remains stable under perturbation, it carries durable signal.
If it collapses under mild transformation, it was representation-dependent.


---

Architectural boundary

measurement != inference != decision

OMNIA is a bounded measurement layer.

It may emit structural signals, rankings, compatibility values, instability indicators, or stop conditions.

It does not decide what a host system should do with them.

Canonical chain:

Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-LIMIT -> Decision Layer (external)


---

What OMNIA currently does

Within the tested perimeter, OMNIA currently supports:

structural measurement

transition classification

regime tracking after drift or rupture

refusal of false stabilization under persistent incoherence

bounded structural compatibility output between states

post-hoc ranking and filtering on structured candidates

monitored structural bias correction in numeric ranking

public-facing fragility display where correctness and stability diverge

runtime retry and escalation intervention on structured LLM outputs inside the tested example perimeter

adapter-mediated workflow control with measurable safety dividend in tested runtime scenarios

cross-model runtime portability inside the tested structured-output perimeter


This is a real tested perimeter.
It is not a universality claim.


---

Structural lenses

Independent transformation families currently used in the project:

BASE -> multi-representation invariance

TIME -> drift and instability over time

CAUSA -> relational dependencies

TOKEN -> sequence perturbation

LCR -> logical coherence reduction


Each lens emits an independent structural signal.


---

Core metrics

Primary structural metrics:

Omega -> structural coherence under perturbation

Omega-set -> residual invariance across transformations

SEI -> remaining extractable structure

IRI -> irreversible structural loss

TDelta -> divergence point

R -> recovery capacity

dO -> structural distance between consecutive states


Numeric ranking and SBC-related exposed fields:

omega_raw

omega_adjusted

structural_bias_meta.bias_penalty_raw

structural_bias_meta.bias_penalty_norm

structural_bias_meta.lambda_value



---

Transition logic

At runtime, OMNIA classifies transitions into three zones:

equivalence

mild_variation

structural_break


This transition layer can be combined with memory and regime policy inside the tested scenarios.


---

Memory and regime policy

The current memory layer supports these states:

STABLE

DRIFTING

CANDIDATE

CHAOTIC


This means OMNIA can:

open a post-break candidate window

evaluate internal coherence of post-break states

confirm a new stable regime when coherence is high enough

refuse the commit if post-break states remain incoherent


This is the difference between adaptation and false normalization of chaos.


---

Structural Compatibility Unit

OMNIA emits a bounded structural compatibility bundle between states:

U_v1(S1, S2) = (C, I, P)

where:

C = compatibility

I = irreversibility within the observed window

P = purity / internal coherence


This is an operational bundle within the tested perimeter, not a universal final object.


---

Reproducibility

Clone and run:

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected behavior:

structured -> high Omega
perturbed  -> Omega drop
random     -> low stable structure / near-null structural consistency

If this separation appears, the system is behaving as intended inside the demo perimeter.


---

Current evaluated status

OMNIA v1.0 has been evaluated, within the tested perimeter, across:

controlled structural benchmarks

calibrated silent-failure gate behavior

retry-loop workflow intervention

adapter-path runtime integration

expanded structured-output runtime dataset

real backend execution

cross-model portability under the same runtime pipeline


Inside this perimeter, OMNIA has shown behavior consistent with a post-hoc structural runtime safety layer for structured LLM outputs.

This means it has demonstrated:

positive safety dividend

bounded retry waste

low over-defensive cost

stable preservation of healthy outputs

portability across the tested model pair

auditable intervention behavior under runtime conditions


This remains a bounded engineering result, not a universality claim.


---

Primary evidence

OMNIA should be read through a narrow benchmark center.

Primary benchmark entry points:

OMNIA_FACT_BENCHMARK_v0.1.py

OMNIA_TOTALE_GSM8K_EVAL_v0.1.py

OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py


These are the main public evidence path.

Additional reports, notes, and side validations may support them, but should not replace them as the public center.


---

Runtime external-impact path

The main external-impact path of OMNIA v1.0 is now:

1. calibrated silent-failure detection


2. bounded retry / escalate intervention


3. adapter-mediated runtime workflow control


4. real backend execution


5. cross-model portability under the same pipeline



Core runtime validation artifacts include:

docs/OMNIA_SILENT_FAILURE_GATE_v0.md

docs/OMNIA_SILENT_FAILURE_GATE_v0_RESULTS.md

docs/OMNIA_SILENT_FAILURE_GATE_v0_2_RESULTS.md

docs/OMNIA_SILENT_FAILURE_RETRY_LOOP_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0.md

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0.md

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0.md

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0.md

docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0_RESULTS.md


These artifacts define the most advanced validated runtime branch of the project.


---

Numeric ranking perimeter

OMNIA was also tested on real integer candidate sets using multi-base structural representations.

This supports a narrow claim only:

OMNIA can produce a non-random ranking signal on tested prime candidate sets

OMNIA can support search-space reduction on tested candidate sets

OMNIA does not prove primality

OMNIA does not solve open mathematical problems


A correction layer was then introduced to handle structurally regular false positives:

Omega_adjusted = Omega_raw - lambda * regularity_penalty_norm

Current validated balanced value:

lambda = 0.03

This correction is currently integrated in shadow mode.

It exists to improve ranking purity while preserving raw score visibility.

Numeric ranking is part of the experimental measurement perimeter.
It is not the central public identity of OMNIA.


---

Where OMNIA applies

OMNIA can be used on systems where ordered representation matters, including:

AI outputs

logs

code

numeric sequences

monitoring streams

structured operational traces

candidate ranking and filtering tasks


The project is strongest when treated as a post-hoc measurement layer, not as a semantic or decision engine.

The currently strongest demonstrated use case is:

structured JSON-like LLM outputs

silent-failure interception

retry / escalation control

runtime auditability



---

Primary adoption path

The narrow adoption path of OMNIA is:

1. OMNIA_MINIMAL_INTERFACE.md


2. INTERFACE.md


3. adapters/llm_output_adapter.py


4. integrations/caios/



This is the shortest readable path for an external integrator.

OMNIA adoption means external usability as a structural measurement layer.
It does not mean conceptual expansion.


---

Repository reading order

For a new external reader, the recommended order is:

1. README.md


2. ARCHITECTURE_BOUNDARY.md


3. INTERFACE.md


4. OMNIA_MINIMAL_INTERFACE.md


5. docs/ROADMAP_CORE_EVIDENCE_ADOPTION.md


6. docs/CANONICAL_FILES.md


7. docs/PRIMARY_BENCHMARKS.md


8. docs/PRIMARY_BENCHMARK_INDEX.md


9. docs/PRIMARY_ADOPTION_PATH.md


10. docs/PRIMARY_ADOPTION_INDEX.md



If the reader wants the strongest runtime branch after that, the next documents should be the Silent Failure Gate, Retry Loop, Adapter Path, Real Backend, and Cross-Model result files listed above.


---

What makes OMNIA different

OMNIA is not positioned as a model, a guardrail, or a semantic evaluator.

Its role is narrower:

measure structural fragility before visible collapse

isolate structure-dependent signal from representational noise

detect instability and regime change

provide external measurement usable by host systems

support bounded retry and escalation intervention in tested runtime workflows


The project is built around one hard rule:

measurement first
decision external


---

Limits

Current limits remain explicit:

controlled and semi-controlled datasets

limited distributional analysis

mostly narrow tested perimeters

benchmark-dependent evidence

no universality claim

ranking correlation is not proof

false positives remain part of observed behavior

omega_adjusted is monitored and exposed, but not treated as universal default truth

SCU v1 is bounded to the tested perimeter

adoption is still early and selective

real backend validation is still bounded to the tested structured-output runtime setup

cross-model portability is demonstrated only for the tested model pair and pipeline



---

Canonical project rule

OMNIA does not need more identities.

It needs:

less dispersion

stronger evidence

clearer integration

external reproducibility



---

Final v1.0 status

OMNIA v1.0 should now be treated as a completed foundational cycle.

It is not complete because no more ideas exist.

It is complete because the architectural uncertainty required to define the v1.0 perimeter has been exhausted.

What now exists is:

stable

measured

auditable

runtime-tested

real-backend-tested

cross-model-tested

bounded by explicit limits


That is the correct end state of OMNIA v1.0.