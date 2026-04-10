# Primary Benchmarks

This file defines the main public evidence path for OMNIA v1.0.

OMNIA should be evaluated through a narrow benchmark center, not through the entire repository.

---

## Benchmark 1 - Factual stability

`OMNIA_FACT_BENCHMARK_v0.1.py`

Purpose:
measure structural stability on factual-style outputs under controlled variation.

Use this to inspect whether OMNIA separates stable outputs from structurally weak ones inside the tested perimeter.

---

## Benchmark 2 - Reasoning-output structural evaluation

`OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`

Purpose:
measure structural behavior on reasoning-style outputs, especially where surface plausibility and structural robustness may diverge.

Use this to inspect silent-failure sensitivity in the tested reasoning-output perimeter.

---

## Benchmark 3 - Multi-model comparative evaluation

`OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

Purpose:
measure whether the same OMNIA runtime logic remains usable across the tested model pair under the same pipeline.

Use this to inspect bounded cross-model portability inside the tested runtime setup.

---

## Recommended order

Read and run in this order:

1. `OMNIA_FACT_BENCHMARK_v0.1.py`
2. `OMNIA_TOTALE_GSM8K_EVAL_v0.1.py`
3. `OMNIA_TOTALE_MULTIMODEL_EVAL_v0.2.py`

This order moves from simpler structural separation to stronger runtime evidence.

---

## What these benchmarks support

Within the tested perimeter, these benchmarks support a bounded claim:

- OMNIA can act as a post-hoc structural measurement layer
- OMNIA can expose fragility signals not reducible to surface plausibility alone
- OMNIA can support runtime intervention logic in the tested setup

---

## What these benchmarks do not support

These benchmarks do not support claims of:

- universal truth detection
- semantic understanding
- general reasoning replacement
- universal model safety
- unrestricted portability

The benchmark center is evidence of bounded engineering behavior, not universality.