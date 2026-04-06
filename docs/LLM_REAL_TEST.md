# OMNIA — Real LLM Output Test (TruthfulQA)

## Status

PASS

---

## Objective

Evaluate whether OMNIA can distinguish structurally stronger and weaker outputs on a real non-controlled LLM dataset.

Dataset used:

- TruthfulQA

Classes:

- correct
- incorrect

---

## Method

Engine:

- semantic_decoupling_v10_0

Signal:

- Δ_struct

OMNIA does not evaluate semantic correctness directly.  
It measures structural stability under controlled transformations.

---

## Results

Δ_struct (correct)   = 0.1284  
Δ_struct (incorrect) = 0.0912  

Expected invariant:

```text
correct > incorrect

Result:

PASS


---

Interpretation

The measured separation is positive but narrower than in controlled stress tests.

This indicates:

real incorrect outputs are not random

fluent falsehoods can preserve partial structure

correct outputs remain, on average, more structurally stable



---

Why this matters

This is not a manual synthetic test.

It is the first recorded pass on non-controlled LLM outputs.

OMNIA distinguishes output quality without reading semantic truth directly,
but by measuring structural stability under transformation.


---

Limits

mean separation only

no full variance / overlap analysis included here

single dataset

single evaluation layer


This is a real-data pass, not a universal proof.


---

Conclusion

OMNIA shows positive structural discrimination on TruthfulQA outputs:

Δ_struct(correct) > Δ_struct(incorrect)

This moves the system beyond controlled laboratory tests and into non-controlled output evaluation.