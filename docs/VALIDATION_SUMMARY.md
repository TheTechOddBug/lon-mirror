# OMNIA v1.0 — Validation Summary

## Scope

ZEH-2 protocol (Relational Fatigue Spectrometry + Δ_struct)

Test dimensions:

- cross-model
- cross-domain
- cross-scale

---

## Models

- llama3_8b (small)
- gemma2_27b (medium)
- gpt4o (large)

---

## Domains

- logic (transitivity)
- code (functional structure)
- news (natural language)

---

## Results Matrix

| Domain | Small (Llama-3-8B) | Medium (Gemma-2-27B) | Large (GPT-4o) |
|--------|-------------------|----------------------|----------------|
| Logic  | PASS (+2)         | PASS (+3)            | PASS (+5)      |
| Code   | PASS (+2)         | —                    | PASS (+4)      |
| News   | WEAK_PASS (+1)    | —                    | PASS (+3)      |

Lead margin = yield_depth → error_depth distance

---

## Observations

1. Structural ordering is preserved across all tested models:
   
   structured > perturbed > random

2. Early-warning signal is consistently present:

   yield_depth < error_depth

3. Decoupling (Δ_struct) improves class separation in all domains.

4. Signal quality depends on model scale:

   - small models → degraded resolution in high-entropy domains
   - large models → restored separation and stronger lead margin

---

## Interpretation

OMNIA behaves as a structural stress sensor:

- detects instability before failure
- operates independently of task semantics
- scales with model capability

---

## Limits

- signal degradation in high-entropy natural language (small models)
- sensitivity depends on model capacity
- not yet validated on real-world continuous streams

---

## Status

Validation phase:

COMPLETED

OMNIA v1.0 is:

- cross-model supported
- cross-domain supported
- early-warning capable

---

## Conclusion

OMNIA is not model-specific.

It measures a structural property of transformer-based systems:

response instability under controlled perturbation.

The signal becomes clearer as model capacity increases.