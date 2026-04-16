# lon-mirror — Historical and Operational Core of the OMNIA Diagnostics Lineage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19513076.svg)](https://doi.org/10.5281/zenodo.19513076)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com  
**Project:** MB-X.01

---

## Position in the Ecosystem

This repository is part of the **MB-X.01 / OMNIABASE / OMNIA** ecosystem.

- **[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** = the general multirepresentational framework
- **[OMNIA](https://github.com/Tuttotorna/OMNIA)** = the Diagnostics / Structural Measurement branch
- **lon-mirror** = the historical, operational, and research core of the OMNIA diagnostics lineage

Canonical ecosystem map:  
**[lon-mirror / ECOSYSTEM.md](https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md)**

This repository should not be read as the umbrella framework itself.

Its role is different:

**lon-mirror preserves the deepest operational, experimental, and architectural material of the OMNIA branch.**

Ω · Ω̂ · SEI · IRI · OMNIA-LIMIT  
**MB-X.01**

---

## Overview

**lon-mirror** is the historical and operational core repository of the **OMNIA diagnostics lineage**.

It contains the deepest implementation, documentation, experiments, reports, adapters, and benchmark material connected to the OMNIA branch.

Its center of gravity is:

- post-hoc structural measurement
- structural trust gating
- silent-failure interception
- bounded retry / escalation support
- structural drift, saturation, and collapse analysis
- runtime-oriented diagnostics on structured outputs

In practical terms:

if **[OMNIA](https://github.com/Tuttotorna/OMNIA)** is the clean public branch-facing repository,  
then **lon-mirror** is the deeper engineering and research core behind that lineage.

---

## What OMNIA Is, in This Repository

Within this repository, **OMNIA** should be understood as a **post-hoc structural measurement engine**.

More precisely, it is a **structural trust gate**:
a layer that detects when an output looks acceptable on the surface but is not stable enough to be trusted as-is.

LLM failures are not only obvious failures.  
They also appear as outputs that seem plausible, pass too easily, and remain structurally fragile underneath.

OMNIA exists to catch those cases before trust turns into error.

It does **not** interpret semantics.  
It does **not** replace reasoning.  
It does **not** decide goals.  
It does **not** act as an autonomous agent.

Its role is narrower and harder:

- detect structural fragility before visible collapse
- separate durable structure from representation-dependent behavior
- expose measurable instability signals for downstream systems
- support bounded trust decisions by host systems inside the tested perimeter

**Core principle:** structural truth = invariance under transformation  
**Architectural boundary:** measurement != inference != decision

---

## Why This Repository Matters

Most systems are checked only for explicit wrongness.

That is not enough.

A system can still fail when an output:

- looks coherent
- sounds correct
- fits the expected format
- passes superficial inspection
- is still structurally unstable underneath

This is the practical target of the OMNIA diagnostics lineage.

This repository matters because it preserves the deepest public material for that work:
not only the clean statement of the branch, but also the surrounding operational path that made it testable.

---

## Canonical Chain

Within the broader MB-X.01 / OMNIABASE ecosystem, the canonical chain is:

```text
Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-RADAR -> OMNIA-LIMIT -> Decision Layer (external)

Within this chain:

Dual-Echo = theoretical origin

OMNIAMIND = pre-output structural dynamics

OMNIA = post-hoc structural measurement

OMNIA-RADAR = residual structural opportunity detection

OMNIA-LIMIT = structural stop / saturation boundary

Decision Layer = any action-taking layer, always external


Non-negotiable rule:

measurement != cognition != decision


---

What This Repository Currently Supports

Within the tested perimeter, the material preserved here currently supports:

structural measurement

transition classification

regime tracking after drift or rupture

post-hoc ranking and filtering on structured candidates

runtime retry / escalation support on structured LLM outputs

adapter-mediated workflow control in tested runtime scenarios

cross-model runtime portability inside the tested structured-output perimeter


This is a real tested perimeter.

It is not a universality claim.


---

Current Strongest Public Use Case

The strongest public use case currently exposed in this repository is:

structured LLM outputs

silent-failure interception

bounded retry / escalation support

runtime auditability inside the tested perimeter


This is the current external-impact center of the documented work.

In practical terms:

the OMNIA lineage is strongest where an output can look acceptable, yet still be too fragile to pass without an additional structural check.


---

What Makes the Lineage Different

The OMNIA diagnostics lineage is not positioned as:

a model

a general-purpose agent

a semantic evaluator

a truth oracle

a decision engine


Its role is narrower:

measure structural fragility before visible collapse

isolate durable signal from representational noise

detect instability and regime change

expose measurement usable by host systems

support bounded retry / escalation flows inside the tested runtime perimeter


The project is built around one hard rule:

measurement first
decision external

That restriction is not a weakness.
It is part of the architecture.


---

Reproducibility

Clone and run:

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected behavior:

structured -> high Omega

perturbed -> Omega drop

random -> low stable structure / near-null structural consistency


If this separation appears, the system is behaving as intended inside the demo perimeter.


---

Current Evaluated Status

Within the tested perimeter, the material in this repository documents evaluation across:

controlled structural benchmarks

calibrated silent-failure gate behavior

retry-loop workflow intervention

adapter-path runtime integration

expanded structured-output runtime dataset

real backend execution

cross-model portability under the same runtime pipeline


Inside this perimeter, the OMNIA lineage has shown behavior consistent with a post-hoc structural runtime safety layer for structured LLM outputs.

This includes evidence of:

positive safety dividend

bounded retry waste

low over-defensive cost

stable preservation of healthy outputs

portability across the tested model pair

auditable intervention behavior under runtime conditions


This remains a bounded engineering result, not a universality claim.


---

Primary Evidence Center

This repository should be read through a narrow evidence center, not through the entire repository at once.

Main public benchmark entry points:

1. OMNIA_FACT_BENCHMARK_v0.1.py


2. OMNIA_TOTALE_GSM8K_EVAL_v0.1.py


3. OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py



These define the main benchmark center of the diagnostics lineage.

Additional reports, notes, and side validations may support them, but should not replace them as the public center of gravity.


---

Primary Runtime Path

The strongest runtime branch currently exposed in the repository is:

1. silent-failure detection


2. bounded retry / escalation intervention


3. adapter-mediated workflow control


4. real backend execution


5. cross-model portability under the same tested pipeline



Core runtime artifacts include:

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


This is the most advanced externally legible branch currently documented in the repository.


---

Silent Failure Gate (Offline Demonstrator)

The repository also contains a synthetic offline demonstrator for bounded routing logic:

PASS

RETRY

ESCALATE


This branch does not replace runtime validation.

It exists to show how structural signals can drive a bounded action surface without requiring external dependencies.

Core artifacts include:

docs/SILENT_FAILURE_GATE_OFFLINE_v0.md

data/gate_cases_v0.json

silent_failure_gate_demo.py

report_generator_silent_failure_gate.py

STATUS_SILENT_FAILURE_GATE.md


This is an offline architectural demonstrator only.


---

Primary Adoption Path

For an external integrator, the shortest usable path is:

1. OMNIA_MINIMAL_INTERFACE.md


2. INTERFACE.md


3. adapters/llm_output_adapter.py


4. integrations/caios/



Adoption here means external usability as a structural measurement layer.

It does not require full immersion in the entire MB-X.01 history.


---

Relationship to OMNIAMIND

OMNIAMIND is an upstream analytical extension of the same ecosystem.

OMNIA remains the canonical post-hoc structural measurement engine.

Difference in role:

OMNIAMIND = pre-output structural dynamics

OMNIA = post-hoc structural stability under transformation

OMNIA-LIMIT = structural stop / saturation boundary


OMNIAMIND does not replace OMNIA.
It extends structural visibility before final emission.


---

Current Limits

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

Current Repository State

This repository currently contains two compatible but asymmetrical states:

Branch	Status	Note

OMNIA runtime branch	FOUNDATIONALLY STABILIZED	Real backend, retry-loop, adapter path, and cross-model perimeter documented
OMNIAMIND analytical branch	OPERATIONAL OFFLINE	Synthetic proxy engine, formalization, and offline comparison package available, but no real trace ingestion yet


This means the repository is currently stronger on post-hoc structural measurement than on upstream empirical pre-output measurement.

That asymmetry is real and explicitly declared.


---

Why lon-mirror Still Matters

Now that OMNIABASE exists as the umbrella framework and OMNIA exists as the cleaner branch-facing repository, lon-mirror should be understood as preserving what those repositories do not try to contain all at once:

the deeper operational archive

the richer benchmark context

the experimental breadth of the diagnostics lineage

the engineering path that led to the current stabilized perimeter

the canonical ecosystem memory of this branch


It is therefore not the umbrella framework.

It is the deepest public operational core of one of its most mature branches.


---

Final v1.0 Status

The OMNIA diagnostics lineage documented here should be treated as a completed foundational cycle.

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


That is the correct end state of this foundational cycle.


---

Minimal Conclusion

lon-mirror preserves the historical and operational core of the OMNIA diagnostics lineage inside the OMNIABASE ecosystem.

Externally, the clearest way to understand the work preserved here is this:

the OMNIA lineage is a structural trust gate for plausible but fragile outputs.

It is strongest where the project currently has real tested perimeter:

structured LLM outputs

silent-failure interception

bounded retry / escalation

runtime auditability

tested cross-model path inside the declared setup


It is not a universality claim.
It is not another agent.
It is not a semantic judge.

It is a bounded, completed, foundational diagnostics lineage inside MB-X.01 / OMNIABASE.

Current correct state:

OMNIABASE   = general multirepresentational framework
OMNIA       = canonical Diagnostics / Structural Measurement branch
lon-mirror  = historical and operational core of that branch
OMNIAMIND   = upstream analytical extension
OMNIA-LIMIT = downstream structural boundary
v1.0        = foundationally stabilized