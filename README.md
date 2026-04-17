# lon-mirror — Historical and Operational Core of the OMNIA Diagnostics Lineage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19513076.svg)](https://doi.org/10.5281/zenodo.19513076)

**Author:** Massimiliano Brighindi  
**Contact:** brighissimo@gmail.com  
**Project:** MB-X.01

---

## First Real Operational Result

The first narrow operational result in this repository is:

**OMNIA Silent Failure Gate v0**

A minimal post-hoc structural gate applied to LLM outputs improved final accuracy through selective retry:

- **Baseline:** 78.0%
- **Gate + Retry:** 86.5%
- **Net gain:** +8.5%
- **Hard tasks:** +14% / +15%
- **Retry rate:** 26.0%

Full result:

- [`docs/OMNIA_SILENT_FAILURE_GATE_REAL_RESULT_v0.md`](./docs/OMNIA_SILENT_FAILURE_GATE_REAL_RESULT_v0.md)

Minimal executable artifact:

- `run_omnia_gate.py`

This is the first clear practical result in the repository:
a bounded software artifact with measurable operational gain.

---

## Position in the Ecosystem

This repository is part of the **MB-X.01 / OMNIABASE / OMNIA** ecosystem.

- **[OMNIABASE](https://github.com/Tuttotorna/OMNIABASE)** = general multirepresentational framework
- **[OMNIA](https://github.com/Tuttotorna/OMNIA)** = canonical diagnostics / structural measurement branch
- **lon-mirror** = historical, operational, and research core of the OMNIA diagnostics lineage

Canonical ecosystem map:

- **[ECOSYSTEM.md](https://github.com/Tuttotorna/lon-mirror/blob/main/ECOSYSTEM.md)**

Compressed identity:

```text
OMNIABASE = framework
OMNIA = canonical measurement branch
lon-mirror = operational core and historical archive of that branch


---

What This Repository Is

lon-mirror is the deepest public operational repository in the OMNIA diagnostics lineage.

It preserves:

operational artifacts

benchmark material

retry / escalation pathways

structural gate experiments

real-run traces

cross-model diagnostics material

bounded runtime evidence

early pre-collapse evidence under fixed protocols


In practical terms:

if OMNIA is the cleaner branch-facing repository,
then lon-mirror is the deeper engineering and evidence-preserving core behind that branch.


---

What OMNIA Is, Here

Within this repository, OMNIA should be read as a post-hoc structural measurement layer.

Its role is narrow:

measure structural fragility in outputs that may look acceptable on the surface

expose instability before visible collapse

support bounded retry / escalation decisions in host systems

separate durable structure from representation-dependent behavior


It does not:

interpret semantics

replace reasoning

act as an autonomous agent

decide goals

serve as a truth oracle


Core principle:

structural truth = invariance under transformation

Architectural boundary:

measurement != inference != decision


---

Why This Repository Matters

Many systems are checked only for explicit wrongness.

That is not enough.

A system can fail even when an output:

looks coherent

sounds correct

matches the expected format

passes superficial inspection

is still structurally unstable underneath


This repository matters because it preserves the deepest public material for detecting exactly that class of failure.

Not just claims.
Operational path.

Not just theory.
Measured artifacts.


---

Canonical Chain

Within the broader MB-X.01 / OMNIABASE ecosystem, the canonical chain is:

Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-RADAR -> OMNIA-LIMIT -> Decision Layer (external)

Repository roles:

dual-echo-perception = theoretical origin

OMNIAMIND = upstream structural dynamics / pre-output analysis

OMNIA = post-hoc structural measurement

OMNIA-RADAR = residual structural opportunity detection

omnia-limit = structural stop / saturation boundary

decision layer = always external


Non-negotiable rule:

measurement != cognition != decision


---

Current Strongest Public Use Cases

The strongest public use cases currently exposed here are:

1. Structured-output runtime diagnostics

silent-failure interception

bounded retry / escalation support

adapter-mediated workflow intervention

runtime auditability inside the tested perimeter


2. Early structural degradation analysis

consistency decline before first observed accuracy loss

fixed-protocol real runs

cross-model comparison on closed-form domains

bounded pre-collapse evidence


The first is the strongest current runtime engineering branch.
The second is the strongest current diagnostic branch for early instability.


---

Current Evaluated Status

Within the tested perimeter, the material in this repository documents evaluation across:

controlled structural benchmarks

calibrated silent-failure gate behavior

retry-loop intervention

adapter-path runtime integration

expanded structured-output datasets

real backend execution

cross-model portability under the same pipeline

synthetic pre-collapse sweeps

initial real pre-collapse cases

initial cross-model real replication


Inside this perimeter, the OMNIA lineage has shown behavior consistent with a bounded post-hoc structural diagnostics layer for structured LLM outputs.

This includes documented evidence of:

measurable retry benefit

bounded retry waste

low over-defensive cost

preservation of healthy outputs

portability across the tested model pair

auditable intervention behavior

early structural degradation preceding first observed accuracy drop in bounded runs


This remains a bounded engineering result, not a universality claim.


---

Primary Evidence Center

This repository should be read through a narrow evidence center, not through the full archive at once.

Main benchmark / evaluation entry points include:

OMNIA_FACT_BENCHMARK_v0.1.py

OMNIA_TOTALE_GSM8K_EVAL_v0.1.py

OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py


Primary operational result:

docs/OMNIA_SILENT_FAILURE_GATE_REAL_RESULT_v0.md


These form the main public evidence center of the diagnostics lineage.


---

Primary Runtime Path

The strongest runtime branch currently documented here is:

1. silent-failure detection


2. bounded retry / escalation


3. adapter-mediated workflow control


4. real backend execution


5. cross-model portability inside the tested pipeline



Core runtime artifacts include:

docs/OMNIA_SILENT_FAILURE_GATE_v0.md

docs/OMNIA_SILENT_FAILURE_GATE_v0_RESULTS.md

docs/OMNIA_SILENT_FAILURE_GATE_REAL_RESULT_v0.md

docs/OMNIA_SILENT_FAILURE_RETRY_LOOP_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0.md

docs/OMNIA_RETRY_LOOP_ADAPTER_PATH_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0.md

docs/OMNIA_RETRY_LOOP_DATASET_EXPANSION_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0.md

docs/OMNIA_RETRY_LOOP_REAL_BACKEND_v0_RESULTS.md

docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0.md

docs/OMNIA_RETRY_LOOP_CROSS_MODEL_v0_RESULTS.md


This is the most advanced externally legible runtime branch currently documented in the repository.


---

Real Pre-Collapse Evidence

The repository also preserves an early real-evidence branch focused on structural consistency degradation before the first observed accuracy loss under fixed protocols.

This branch should be read narrowly.

It does not claim a universal law.

It documents an observed pattern under:

fixed prompting

fixed normalization

fixed metric

closed-form tasks

real model outputs

cross-model comparison


Core artifacts:

docs/REAL_PRECOLLAPSE_CASES_v1.md

docs/CROSS_MODEL_PRECOLLAPSE_REPLICATION_v0.md

examples/consistency_metric_v1.py

examples/real_llm_precollapse_suite_v0.py


Archived real-run artifacts are stored under:

examples/real_runs/


Current evidence boundary:

> In two closed-form task families and two distinct models, consistency_v1 declined before the first observed accuracy loss under an identical protocol.




---

Reproducibility

Clone and run:

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected qualitative behavior:

structured -> high Omega

perturbed -> Omega drop

random -> low stable structure / near-null structural consistency


Minimal operational gate form:

python run_omnia_gate.py --input sample.jsonl --output gated.jsonl --print-summary


---

Primary Adoption Path

For an external integrator, the shortest usable path is:

1. OMNIA_MINIMAL_INTERFACE.md


2. INTERFACE.md


3. adapters/llm_output_adapter.py


4. integrations/caios/



Adoption here means external usability as a structural measurement layer.
It does not require immersion in the full archive.


---

Related Repositories

For the shortest functional reading of the broader lineage:

OMNIABASE — umbrella framework

OMNIA — diagnostics / structural measurement branch

observer-suspension — epistemic pre-layer

omniabase-coordinate-discovery — coordinate discovery branch

omega-translator — cross-representation translation branch

OMNIA-RADAR — residual structural opportunity detection

omnia-limit — structural boundary / saturation layer

Pre-Deployment-Structural-Gate — deployment-facing diagnostics extension



---

Current Limits

Current limits remain explicit:

controlled and semi-controlled datasets

bounded evaluated perimeters

benchmark-dependent evidence

no universality claim

false positives remain part of observed behavior

adoption is still early and selective

real backend validation remains bounded to the tested structured-output setup

cross-model portability remains bounded to the tested model pair and pipeline

real pre-collapse evidence currently covers only two models and two closed-form domains

no claim yet on open-ended reasoning, broad semantic tasks, or production thresholds


These limits are part of the architecture, not an afterthought.


---

Current Repository State

This repository currently contains two compatible but asymmetrical states:

Branch	Status	Note

OMNIA runtime branch	FOUNDATIONALLY STABILIZED	real backend, retry-loop, adapter path, and cross-model perimeter documented
OMNIAMIND analytical branch	OPERATIONAL OFFLINE	synthetic proxy engine, formalization, and offline comparison package available, but no real trace ingestion yet
Pre-collapse evidence branch	INITIAL REAL POSITIVE EVIDENCE	multi-domain real cases and initial cross-model replication under fixed protocol


This means the repository is currently strongest on:

post-hoc structural measurement

runtime diagnostics

bounded trust routing

initial real evidence of early structural degradation


That asymmetry is real and explicitly declared.


---

Why lon-mirror Still Matters

Now that OMNIABASE exists as the umbrella framework and OMNIA exists as the cleaner branch-facing repository, lon-mirror preserves what those repositories do not try to contain all at once:

the deeper operational archive

the richer benchmark context

the experimental breadth of the diagnostics lineage

the engineering path that led to the current stabilized perimeter

the canonical ecosystem memory of this branch

the real-run artifacts behind current pre-collapse evidence


It is therefore not the umbrella framework.

It is the deepest public operational core of one of its most mature branches.


---

Final v1.0 Status

The OMNIA diagnostics lineage documented here should be treated as a completed foundational cycle.

It is not complete because no more ideas exist.

It is complete because the architectural uncertainty required to define the current foundational perimeter has been exhausted.

What now exists is:

stable

measured

auditable

runtime-tested

real-backend-tested

cross-model-tested inside the declared runtime perimeter

explicitly bounded

extended by initial real multi-domain pre-collapse evidence


This is the correct state of the current foundational cycle.


---

Minimal Conclusion

lon-mirror preserves the historical and operational core of the OMNIA diagnostics lineage inside the OMNIABASE ecosystem.

Externally, the clearest way to understand the work preserved here is this:

> the OMNIA lineage is a structural trust and diagnostics layer for plausible but fragile outputs.



It is strongest where the project currently has a real tested perimeter:

structured LLM outputs

silent-failure interception

bounded retry / escalation

runtime auditability

tested cross-model path inside the declared setup

initial cross-model real evidence that structural consistency can move earlier than accuracy in closed-form tasks


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

