# OMNIA Primary Benchmark Index
## Canonical benchmark entry points

Status: active
Purpose: define the exact benchmark files that represent the public evidence layer of OMNIA

---

## 1. Rule

This file identifies the exact benchmark entry points that should represent OMNIA publicly.

These are not necessarily the only benchmark-related files in the repo.
They are the files that should be treated as the main evidence path for external readers.

---

## 2. Primary benchmark entry points

### A. Factual stability benchmark

Canonical files:

- `OMNIA_FACT_BENCHMARK_v0.1.py`

Role:
measure structural stability or fragility signals on factual-style outputs.

Why it is primary:
this is one of the clearest bridges between OMNIA and real reliability use cases.

Public function:
show that OMNIA can operate on outputs where external readers immediately understand the value of stability assessment.

---

### B. Reasoning-output structural benchmark

Canonical files:

- `OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`

Role:
measure structural behavior on reasoning-like outputs without claiming semantic reasoning or mathematical solving ability.

Why it is primary:
it connects OMNIA to a known evaluation territory while preserving the measurement-only boundary.

Public function:
show that OMNIA can detect signals around fragility, instability, or structural inconsistency in chain-like outputs.

---

### C. Multi-model comparative benchmark

Canonical files:

- `OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

Role:
compare outputs across different models using OMNIA as an external measurement layer.

Why it is primary:
this supports the strongest architecture claim in the project:
OMNIA is model-agnostic and sits outside the model.

Public function:
show that OMNIA can be used comparatively, not only internally on one stream.

---

## 3. Supporting benchmark materials

These files may support the main benchmark story, but they are not the first public entry points unless explicitly needed.

Possible examples:

- benchmark reports
- benchmark notes
- result summaries
- case-study documents linked to the primary benchmark files
- standardized test outputs
- reproducibility helpers

Rule:
supporting material supports.
It does not replace the canonical benchmark entry file.

---

## 4. Public reading order

External readers should encounter benchmarks in this order:

1. factual benchmark
2. reasoning-output benchmark
3. multi-model benchmark

This order maximizes clarity and minimizes dispersion.

---

## 5. Interpretation rule

These benchmarks support the following claim only:

OMNIA provides post-hoc structural measurement signals that may help detect coherence, fragility, instability, or related properties across outputs and models.

These benchmarks do NOT support claims of:

- semantic understanding
- superior reasoning
- universal truth detection
- proof generation
- replacement of model inference

---

## 6. Maintenance rule

If a stronger benchmark replaces one of the above, this file must be updated explicitly.

No benchmark should become publicly central by accident.

---

## 7. Final rule

The benchmark center of OMNIA must remain narrow, explicit, and reproducible.

Three strong benchmark entry points are better than ten scattered ones.