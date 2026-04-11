# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19505644.svg)](https://doi.org/10.5281/zenodo.19505644)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What OMNIA is

OMNIA is a post-hoc structural measurement engine.

It measures whether an output remains structurally stable under controlled transformations.

It does not interpret semantics.  
It does not replace reasoning.  
It does not make decisions.

Its role is narrower and harder:

- detect structural fragility before visible collapse
- separate durable structure from representation-dependent behavior
- expose measurable instability signals for downstream systems

**Core principle:** structural truth = invariance under transformation  
**Architectural boundary:** measurement != inference != decision

---

## Canonical position in the ecosystem

OMNIA belongs to the MB-X.01 ecosystem and remains the canonical post-hoc structural measurement layer.

Canonical chain:

```text
Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-LIMIT -> Decision Layer (external)

Within this chain:

OMNIAMIND measures pre-output structural dynamics

OMNIA measures post-hoc output stability under controlled transformations

OMNIA-LIMIT defines structural stop / saturation conditions

Decision Layer remains external


Canonical ecosystem map:
https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md


---

What OMNIA currently does

Within the tested perimeter, OMNIA currently supports:

structural measurement

transition classification

regime tracking after drift or rupture

post-hoc ranking and filtering on structured candidates

runtime retry and escalation intervention on structured LLM outputs

adapter-mediated workflow control in tested runtime scenarios

cross-model runtime portability inside the tested structured-output perimeter


This is a real tested perimeter.
It is not a universality claim.


---

Primary demonstrated use case

The strongest demonstrated public use case currently exposed in the repository is:

structured LLM outputs

silent-failure interception

bounded retry / escalation support

runtime auditability within the tested perimeter


This is the current external-impact center of the project.


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

Primary evidence center

OMNIA should be read through a narrow evidence center, not through the entire repository.

The main public evidence path is:

1. OMNIA_FACT_BENCHMARK_v0.1.py


2. OMNIA_TOTALE_GSM8K_EVAL_v0.1.py


3. OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py



These three entry points define the primary benchmark center of the project.

Additional reports, notes, and side validations may support them, but should not replace them as the public center.


---

Primary runtime path

The strongest runtime branch currently exposed in the project is:

1. silent-failure detection


2. bounded retry / escalation intervention


3. adapter-mediated workflow control


4. real backend execution


5. cross-model portability under the same tested pipeline



Core runtime artifacts:

docs/OMNIA_SILENT_FAILURE_GATE_v0.md
docs/OMNIA_SILENT_FAILURE_GATE_v0_RESULTS.md
docs/OMNIA_SILENT_FAILURE_RETRY_LOOP_v0_RESULTS.md
docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0.md
docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0_RESULTS.md
docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0.md
docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0_RESULTS.md
docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0.md
docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0_RESULTS.md
docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0.md
docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0_RESULTS.md

This is the most advanced external-impact branch currently documented in the repository.


---

Silent Failure Gate (offline demonstrator)

The repository also contains a synthetic offline demonstrator for bounded routing logic:

PASS

RETRY

ESCALATE


This branch does not replace runtime validation. It exists to show how structural signals can drive a bounded action surface without requiring external dependencies.

Core artifacts:

docs/SILENT_FAILURE_GATE_OFFLINE_v0.md
data/gate_cases_v0.json
silent_failure_gate_demo.py
report_generator_silent_failure_gate.py
STATUS_SILENT_FAILURE_GATE.md

This is an offline architectural demonstrator only.


---

Primary adoption path

For an external integrator, the shortest usable path is:

1. OMNIA_MINIMAL_INTERFACE.md


2. INTERFACE.md


3. adapters/llm_output_adapter.py


4. integrations/caios/



OMNIA adoption means external usability as a structural measurement layer.
It does not mean full conceptual immersion in the entire MB-X.01 ecosystem.


---

What makes OMNIA different

OMNIA is not positioned as:

a model

a guardrail

a semantic evaluator

a decision engine


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

Relationship to OMNIAMIND

OMNIAMIND is an upstream analytical extension of the OMNIA ecosystem.

OMNIA remains the canonical post-hoc structural measurement engine.

Difference in role:

OMNIAMIND: pre-output structural dynamics

OMNIA: post-hoc structural stability under transformation

OMNIA-LIMIT: structural stop / saturation boundary


OMNIAMIND does not replace OMNIA.
It extends structural visibility before final emission.


---

Current limits

Current limits remain explicit:

controlled and semi-controlled datasets

limited distributional analysis

mostly narrow tested perimeters

benchmark-dependent evidence

no universality claim

ranking correlation is not proof

false positives remain part of observed behavior

adoption is still early and selective

real backend validation is still bounded to the tested structured-output runtime setup

cross-model portability is demonstrated only for the tested model pair and pipeline


These limits are part of the architecture, not an afterthought.


---

Current repository state

The repository currently contains two different but compatible states:

Branch	Status	Note

OMNIA runtime branch	FOUNDATIONALLY STABILIZED	Real backend, retry-loop, adapter path, and cross-model perimeter documented.
OMNIAMIND analytical branch	OPERATIONAL OFFLINE	Synthetic proxy engine, formalization, and offline comparison package available, but no real trace ingestion yet.


This means the repository is stronger on post-hoc structural measurement than on upstream empirical pre-output measurement.

That asymmetry is real and explicitly declared.


---

Final v1.0 status

OMNIA v1.0 should be treated as a completed foundational cycle.

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


---

Minimal conclusion

OMNIA v1.0 is a bounded structural measurement engine.

It is strongest where the project currently has real tested perimeter:

structured LLM outputs

silent-failure interception

bounded retry / escalation

runtime auditability

tested cross-model path inside the declared setup


It is not a universality claim.
It is a completed foundational engineering layer inside MB-X.01.

The correct current state is:

OMNIA: canonical post-hoc structural measurement engine
OMNIAMIND: upstream analytical extension
OMNIA-LIMIT: downstream structural boundary
v1.0: foundationally stabilized