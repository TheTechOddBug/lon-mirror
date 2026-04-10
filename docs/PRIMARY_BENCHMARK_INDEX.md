# Primary Benchmark Index

This file defines the narrow public benchmark index for OMNIA v1.0.

It exists to keep the benchmark entry path short, readable, and externally usable.

OMNIA should be evaluated through a small evidence center, not through the full repository.

---

## Primary benchmark set

### 1. Factual stability benchmark

`OMNIA_FACT_BENCHMARK_v0.1.py`

Focus:
structural stability on factual-style outputs under controlled variation.

Role:
first entry point for basic structural separation.

---

### 2. Reasoning-output structural benchmark

`OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`

Focus:
structural behavior on reasoning-style outputs where surface plausibility and structural robustness may diverge.

Role:
main entry point for silent-failure style evaluation inside the tested perimeter.

---

### 3. Multi-model comparative benchmark

`OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

Focus:
same OMNIA runtime logic across the tested model pair under the same pipeline.

Role:
main entry point for bounded cross-model portability.

---

## Recommended reading order

Read in this order:

1. `OMNIA_FACT_BENCHMARK_v0.1.py`
2. `OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`
3. `OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

This order moves from simpler structural separation to stronger runtime evidence.

---

## How this index should be used

Use this index if the goal is to answer one of these questions quickly:

- Where is the main benchmark evidence for OMNIA?
- Which benchmark should be read first?
- Which file shows reasoning-output structural evaluation?
- Which file shows bounded cross-model portability?

This file is an index, not a benchmark report.

---

## Boundary of interpretation

These benchmarks support a bounded engineering claim only.

They support the view that, within the tested perimeter:

- OMNIA can act as a post-hoc structural measurement layer
- OMNIA can expose fragility signals beyond surface plausibility
- OMNIA can support runtime intervention logic in the tested setup

They do not support claims of:

- universal truth detection
- semantic understanding
- general reasoning replacement
- unrestricted portability
- universal model safety

---

## Related files

- `README.md`
- `docs/PRIMARY_BENCHMARKS.md`
- `docs/PRIMARY_ADOPTION_PATH.md`