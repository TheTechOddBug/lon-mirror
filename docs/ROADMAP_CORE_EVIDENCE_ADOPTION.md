# OMNIA Roadmap
## Core / Evidence / Adoption

Status: active roadmap
Scope: compression of the existing project
Rule: no expansion of identity, only increase of clarity, reproducibility, and adoption

---

## 0. Mission

OMNIA is a post-hoc structural measurement layer.

It does not interpret semantics.
It does not replace model cognition.
It does not make final decisions.

Its role is narrower and stronger:

- measure structural coherence
- detect fragility and instability
- estimate saturation / irreversibility signals
- support filtering, supervision, and evaluation

Everything in the project must reinforce this perimeter.

---

## 1. Core

Goal:
stabilize the technical identity of OMNIA around the actual reusable core.

Primary assets:

- `omnia/`
- `ARCHITECTURE_BOUNDARY.md`
- `INFERENCE_FREEZE.md`
- `INTERFACE.md`
- `OMNIA_MINIMAL_INTERFACE.md`

Core rule:

If a component does not strengthen the measurement layer, it is not core.

Core tasks:

1. keep the package boundary clean
2. make the minimal interface explicit
3. reduce duplication between root historical scripts and package logic
4. define which modules are canonical and which are legacy
5. protect the distinction:
   measurement != inference != decision

Success condition:

A new reader must understand OMNIA's function in under 3 minutes without reading historical files.

---

## 2. Evidence

Goal:
turn OMNIA from coherent architecture into externally credible evidence.

Primary assets:

- `benchmarks/`
- `tests/`
- `case_studies/`
- `OMNIA_TOTALE_BENCHMARK_v1.0.py`
- `OMNIA_TOTALE_BENCHMARK_REPORT_v1.0.md`
- `OMNIA_FACT_BENCHMARK_v0.1.py`
- `OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`
- `OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

Evidence rule:

No new claim without a benchmark path.

Evidence tasks:

1. identify the 2 or 3 strongest benchmark stories only
2. remove secondary benchmark noise from public positioning
3. standardize result format
4. ensure reproducibility path is visible
5. define baseline comparisons clearly
6. separate exploratory results from stable evidence

Success condition:

An external evaluator can answer:
- what OMNIA measures
- on which tasks it was tested
- against which baselines
- with what reproducible outputs

---

## 3. Adoption

Goal:
make OMNIA usable by others as a layer, not only readable as a theory.

Primary assets:

- `integrations/`
- `adapters/`
- `INTERFACE.md`
- `OMNIA_MINIMAL_INTERFACE.md`
- selected case studies

Adoption rule:

Integration matters more than conceptual expansion.

Adoption tasks:

1. define one minimal input/output contract
2. show one or two concrete integration paths
3. keep adapters thin
4. keep the measurement role separate from host-system logic
5. produce one case study that shows where OMNIA changes an actual pipeline decision

Success condition:

Another developer can plug OMNIA into a workflow without first studying the whole repo history.

---

## 4. What moves to archive or experiments

Anything that does not directly strengthen Core, Evidence, or Adoption should move to:

- `archive/`
- `experiments/`

Examples:

- speculative branches
- one-off numeric side paths
- historical versions kept only for provenance
- interesting but non-transferable internal explorations

Rule:

Interesting is not enough.
Transferable value is required.

---

## 5. Public positioning rule

Public description of OMNIA must stay compressed.

Allowed positioning:

"OMNIA is a post-hoc structural measurement layer for detecting coherence, fragility, instability, and related signals under controlled transformations."

Avoid:

- broad intelligence claims
- open-problem mathematics framing
- claims that imply semantic understanding
- claims that blur measurement with reasoning or decision

---

## 6. Immediate execution order

Step 1:
create this roadmap file

Step 2:
mark canonical files for Core

Step 3:
select the top benchmark set for Evidence

Step 4:
select the top integration path for Adoption

Step 5:
move side material out of the main narrative

---

## 7. Final rule

OMNIA does not need more identities.

It needs:

- less dispersion
- stronger evidence
- clearer integration