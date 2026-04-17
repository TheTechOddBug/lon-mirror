# CROSS-MODEL PRECOLLAPSE REPLICATION v0

**Status:** Initial Cross-Model Real Comparison  
**Date:** 2026-04-17  
**Models:** gpt-4o-mini, Llama-3-8B Instruct  
**Domains:** Arithmetic Multiplication, Linear Algebra

---

## 1. Objective

Test whether the earlier consistency degradation pattern survives a model change under an identical protocol.

The protocol was held fixed across models:
- same task families
- same levels
- same prompt variants
- same normalization
- same metric (`consistency_v1`)

Only the model changed.

---

## 2. Comparison Table

| Model | Domain | First Consistency Drop | First Accuracy Drop | Lead Levels |
|---|---|---:|---:|---:|
| gpt-4o-mini | Arithmetic | L5 | L10 | 5 |
| gpt-4o-mini | Algebra | L5 | L10 | 5 |
| Llama-3-8B Instruct | Arithmetic | L4 | L7 | 3 |
| Llama-3-8B Instruct | Algebra | L3 | L5 | 2 |

---

## 3. Direct Reading

### Shared observation
In all 4 real runs:

- consistency degraded first
- accuracy dropped later
- lead remained positive

### Main difference
Lead magnitude varied by model:

- `gpt-4o-mini`: longer warning window
- `Llama-3-8B Instruct`: shorter warning window

---

## 4. Interpretation Boundary

What can be said:

> Under the same protocol, both models showed earlier structural degradation than accuracy loss.

What can also be said:

> The lead appears model-dependent in magnitude.

What cannot yet be said:

- that the same pattern holds for all LLMs
- that lead length is stable
- that a universal threshold exists
- that this is deployment-ready

---

## 5. Why This Matters

Standard evaluation usually reacts late:
- it sees failure when correctness is already gone

This protocol adds a different signal:
- consistency changes while correctness is still intact

That gap is the operational space of the pre-collapse hypothesis.

---

## 6. Minimal Conclusion

This replication does not prove universality.

It does show that the observed pattern is not confined to a single model.

That is enough to justify continued controlled replication.