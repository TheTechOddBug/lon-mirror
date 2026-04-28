# JSON Structural Stability — v1 Results

## Scope

This document reports a controlled test of structural stability metrics applied to JSON objects.

Goal:

> Verify whether structural metrics can distinguish between:
- harmless transformations (e.g., key reordering)
- structurally degrading transformations (e.g., type drift, null corruption)

All tested variants are syntactically valid JSON.

---

## Test Setup

### Base Object

```json
{
  "name": "Alice",
  "age": 30,
  "balance": 1000,
  "active": true
}

Variants

Variant 1 — Reordering (benign)

{
  "balance": 1000,
  "active": true,
  "name": "Alice",
  "age": 30
}

Expected behavior:

No structural degradation



---

Variant 2 — Type Drift (critical)

{
  "name": "Alice",
  "age": "30",
  "balance": "1000",
  "active": "yes"
}

Expected behavior:

Strong structural degradation



---

Variant 3 — Null Corruption (partial)

{
  "name": "Alice",
  "age": null,
  "balance": 1000,
  "active": true
}

Expected behavior:

Partial structural degradation



---

Metrics

Defined signals:

Ω (Omega): structural invariance across variants

Co⁺: structural coherence relative to base object

Score⁺: bounded aggregation


Score⁺ = α * Ω + (1 - α) * Co⁺


---

Results

Omega (invariance): 0.666667

Variant Scores

Variant 1 (reorder)
  coherence_variant: 1.000000
  score:             0.833333

Variant 2 (type drift)
  coherence_variant: 0.250000
  score:             0.458333

Variant 3 (null corruption)
  coherence_variant: 0.750000
  score:             0.708333


---

Interpretation

Observed behavior:

Reordering preserves full structural alignment

Type drift produces strong structural divergence

Null corruption produces moderate degradation


Key result:

Valid JSON ≠ structurally stable JSON


---

Key Insight

A syntactically valid JSON object can still be:

structurally inconsistent

type-unstable

semantically degraded


Standard validation does not detect this.

Structural metrics can.


---

Implication

This has direct relevance for:

API validation

LLM JSON outputs

data pipelines

schema drift detection



---

Limits

Single base object

handcrafted variants

heuristic weighting

no large-scale validation



---

Status

experimental v1
not validated
requires real-world testing


---

Final Statement

Syntax validation guarantees format correctness.

It does not guarantee structural stability.

Structural metrics provide an additional signal
that can detect degradation invisible to syntax checks.

