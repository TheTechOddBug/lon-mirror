# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19488048.svg)](https://doi.org/10.5281/zenodo.19488048)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What OMNIA is

Systems often look stable until they fail.

OMNIA is a post-hoc structural measurement layer designed to detect coherence, fragility, instability, and regime change before they become obvious at the surface level.

It does not interpret semantics.  
It does not replace model cognition.  
It does not make final decisions.  
It does not act as a proof engine or a primality test.

It measures only:

```text
output = measurement only
structural behavior under controlled transformations


---

Core principle

Structural truth = invariance under transformation

If a structure survives perturbation, it carries stable signal.
If it collapses under mild transformation, it was representation-dependent.


---

Architectural boundary

measurement != inference != decision

OMNIA is a bounded measurement layer.

It may emit structural signals, rankings, compatibility values, instability indicators, or stop conditions.

It does not decide what the host system should do with them.

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

post-hoc ranking / filtering on structured candidates

monitored structural bias correction in numeric ranking

public-facing fragility display where correctness and stability diverge


This is a real tested perimeter.
It is not a universality claim.


---

Structural lenses

Independent transformation families currently used in the project:

BASE -> multi-representation invariance

TIME -> drift / instability over time

CAUSA -> relational dependencies

TOKEN -> sequence perturbation

LCR -> logical coherence reduction


Each lens emits an independent structural signal.


---

Core metrics

Omega -> structural coherence under perturbation

Omega-set -> residual invariance across transformations

SEI -> remaining extractable structure

IRI -> irreversible structural loss

TDelta -> divergence point

R -> recovery capacity

dO -> structural distance between consecutive states


Numeric ranking / SBC-related fields currently exposed:

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


This transition layer can be combined with memory / regime policy in the tested scenarios.


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
random     -> Delta_struct approx 0

If this separation appears, the system is working as intended.


---

Primary evidence

OMNIA should be read through a narrow benchmark center.

Primary benchmark entry points:

Factual stability benchmark
OMNIA_FACT_BENCHMARK_v0.1.py

Reasoning-output structural benchmark
OMNIA_TOTALE_GSM8K_EVAL_v0.1.py

Multi-model comparative benchmark
OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py


These are the main public evidence path.

Additional reports, notes, and side validations may support them, but should not replace them as the public center.


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

candidate ranking / filtering tasks


The project is strongest when treated as a post-hoc measurement layer, not as a semantic or decision engine.


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




---

What makes OMNIA different

OMNIA is not positioned as a model, a guardrail, or a semantic evaluator.

Its role is narrower:

measure structural fragility before visible collapse

isolate structure-dependent signal from representational noise

detect instability and regime change

provide external measurement usable by host systems


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



---

Canonical project rule

OMNIA does not need more identities.

It needs:

less dispersion

stronger evidence

clearer integration

external reproducibility

