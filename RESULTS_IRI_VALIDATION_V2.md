# IRI Validation v2 — Irreversibility Index

## Scope

This document reports a controlled validation test for:

```text
IRI — Irreversibility Index

IRI measures irreversible structural loss after a transformation and attempted recovery.

It does not measure temporary deformation if the original structure can be recovered.


---

Formal Definition

Given:

x      = original object
t(x)   = transformed object
t⁻¹    = attempted inverse / recovery operation
f      = structural feature map
d      = bounded structural distance

IRI is defined as:

IRI(x) = d( f(x), f(t⁻¹(t(x))) )

For multiple transformations:

IRI(x) = mean_i d( f(x), f(t_i⁻¹(t_i(x))) )


---

Test Object

Base object:

{
  "a": 10,
  "b": 20
}


---

Tested Transformations

1. Reorder

Transformation:

{
  "b": 20,
  "a": 10
}

Recovery restores the original key order and structure.

Expected result:

IRI ≈ 0


---

2. Recoverable Type Drift

Transformation:

{
  "a": "10",
  "b": "20"
}

Recovery converts the string values back into integers.

Expected result:

IRI ≈ 0

Reason:

The deformation is temporary and structurally recoverable.


---

3. Non-Recoverable Type Drift

Transformation:

{
  "a": "ten",
  "b": "twenty"
}

Recovery cannot reconstruct the original numeric structure.

Expected result:

IRI > 0


---

4. Lossy Structural Deletion

Transformation:

{
  "a": 10
}

The key b is lost and cannot be recovered.

Expected result:

IRI = high


---

Distance Design

v2 uses key-loss dominance.

This means:

structural key loss > value/type mismatch

Weights:

KEY_LOSS_WEIGHT = 2.0
TYPE_WEIGHT     = 0.7
NULL_WEIGHT     = 0.3

Final distance is clamped to:

[0, 1]


---

Results

reorder             : 0.000000
type_recoverable    : 0.000000
type_nonrecoverable : 0.700000
lossy               : 1.000000


---

Observed Ordering

reorder ≈ type_recoverable < type_nonrecoverable < lossy

This matches the expected behavior.


---

Interpretation

IRI correctly separates:

reversible structural deformation

from:

irreversible structural loss

Key findings:

1. Reordering is structurally reversible.


2. Recoverable type drift is structurally reversible.


3. Non-recoverable type drift produces irreversible residue.


4. Lossy deletion produces maximal irreversible residue.




---

Core Claim Supported

IRI measures irreversible structural loss after attempted recovery.

It does not penalize transformations that can be fully reversed.


---

Relation to Ω

Ω measures immediate structural change under transformation.

IRI measures residual structural damage after attempted recovery.

Therefore:

Ω  = how much the structure changes
IRI = how much cannot be restored

They are complementary metrics.


---

Limits

This is a minimal controlled validation.

Limitations:

toy JSON object

handcrafted transformations

manually defined inverse functions

heuristic distance weights

no large-scale empirical validation



---

Status

IRI v2: formally coherent in controlled test

Not yet externally validated.

Not yet general-purpose.

Requires additional testing on:

larger JSON objects

schema drift

API responses

LLM-generated structured outputs

lossy compression / recovery tasks



---

Final Statement

IRI is not a measure of surface change.

IRI is a measure of irreversible structural residue.

A temporary deformation has low IRI if recovery restores the original structure.

A lossy transformation has high IRI because lost structure cannot be recovered.

