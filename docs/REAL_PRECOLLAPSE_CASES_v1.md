# REAL PRECOLLAPSE CASES v1

**Status:** Initial Multi-Domain Real Evidence  
**Date:** 2026-04-17  
**Model Coverage:** gpt-4o-mini, Llama-3-8B Instruct  
**Domains:** Arithmetic Multiplication, Linear Algebra  
**Protocol:** Fixed prompting structure, fixed normalization, fixed consistency metric

---

## 1. Scope

This document records initial multi-domain real evidence compatible with a pre-collapse pattern under a fixed protocol.

The objective was not to prove a universal law, but to test a narrower question:

> Can structural consistency degrade before the first observed accuracy loss on real model outputs, under controlled prompt variation?

The answer, in the cases reported here, is yes.

---

## 2. Protocol

### Models
- `gpt-4o-mini`
- `Llama-3-8B Instruct`

### Domains
- `arithmetic_multiplication_real`
- `algebra_linear_real`

### Structure
- 10 ordered complexity levels per domain
- 5 near-isomorphic prompt variants per level
- same prompt protocol across models
- same normalization protocol across runs
- same consistency metric across runs

### Measures
- **accuracy**: fraction of normalized outputs matching ground truth
- **consistency_v1**: structural stability metric combining:
  - lexical backbone
  - numeric proximity
  - morphological fingerprint
  - dispersion penalty

---

## 3. Prompt Protocol

Prompt variants were intentionally kept near-isomorphic in order to test model stability rather than prompt-engineering sensitivity.

Examples:

### Arithmetic
1. `What is A * B?`
2. `A * B = ?`
3. `Compute A times B.`
4. `Multiply A and B.`
5. `A multiplied by B?`

### Algebra
1. `Solve: EQ`
2. `Find x: EQ`
3. `What is x if EQ?`
4. `Solve EQ`
5. `Equation: EQ`

---

## 4. Case A — arithmetic_multiplication_real

### Summary table

| Segment | Levels | Accuracy | Consistency_v1 | Interpretation |
|---|---:|---:|---:|---|
| Stable | L1-L4 | 1.00 | high / flat | no observed degradation |
| Gray Zone | L5-L9 | 1.00 | declining | early structural weakening before error |
| Breakdown | L10 or earlier depending on model | < 1.00 | degraded | first observed accuracy loss |

### gpt-4o-mini

| Level | Accuracy | Consistency_v1 |
|---|---:|---:|
| L1 | 1.00 | 0.8432 |
| L2 | 1.00 | 0.8432 |
| L3 | 1.00 | 0.8432 |
| L4 | 1.00 | 0.8432 |
| L5 | 1.00 | 0.7485 |
| L6 | 1.00 | 0.7485 |
| L7 | 1.00 | 0.6930 |
| L8 | 1.00 | 0.6930 |
| L9 | 1.00 | 0.6120 |
| L10 | 0.80 | 0.5186 |

- **First consistency drop:** L5
- **First accuracy drop:** L10
- **Lead levels:** 5

### Llama-3-8B Instruct

| Segment | Observation |
|---|---|
| Baseline | stable through early levels |
| First drop | L4 |
| First accuracy loss | L7 |
| Lead levels | 3 |

Interpretation:
- same qualitative pattern as gpt-4o-mini
- shorter warning window
- lower resilience under increasing multiplication complexity

---

## 5. Case B — algebra_linear_real

### Summary table

| Segment | Levels | Accuracy | Consistency_v1 | Interpretation |
|---|---:|---:|---:|---|
| Stable | L1-L4 | 1.00 | high / flat | baseline symbolic stability |
| Gray Zone | L5-L9 | 1.00 | declining | format/logical stability weakens before error |
| Breakdown | L10 or earlier depending on model | < 1.00 | degraded | first observed accuracy loss |

### gpt-4o-mini

| Level | Accuracy | Consistency_v1 |
|---|---:|---:|
| L1 | 1.00 | 0.8840 |
| L2 | 1.00 | 0.8840 |
| L3 | 1.00 | 0.8840 |
| L4 | 1.00 | 0.8840 |
| L5 | 1.00 | 0.7932 |
| L6 | 1.00 | 0.7932 |
| L7 | 1.00 | 0.7420 |
| L8 | 1.00 | 0.7420 |
| L9 | 1.00 | 0.6925 |
| L10 | 0.80 | 0.5560 |

- **First consistency drop:** L5
- **First accuracy drop:** L10
- **Lead levels:** 5

### Llama-3-8B Instruct

| Segment | Observation |
|---|---|
| Baseline | stable through early levels |
| First drop | L3 |
| First accuracy loss | L5 |
| Lead levels | 2 |

Interpretation:
- pre-error degradation persists outside pure multiplication
- symbolic formatting noise does not destroy the signal
- lead remains positive, but shorter than in gpt-4o-mini

---

## 6. Shared Pattern

Across both closed-form domains and both models, the same qualitative pattern appeared:

1. normalized accuracy remained at `1.0`
2. structural consistency declined earlier
3. the first observed accuracy loss happened later

Compressed form:

> Structural consistency weakened before correctness failed.

This is the central observed result.

---

## 7. Cross-Model Comparison

| Model | Domain | First Consistency Drop | First Accuracy Drop | Lead Levels |
|---|---|---:|---:|---:|
| gpt-4o-mini | Arithmetic | L5 | L10 | 5 |
| gpt-4o-mini | Algebra | L5 | L10 | 5 |
| Llama-3-8B Instruct | Arithmetic | L4 | L7 | 3 |
| Llama-3-8B Instruct | Algebra | L3 | L5 | 2 |

Interpretation:
- the pattern is not confined to a single model
- lead magnitude varies across models
- this suggests model-dependent resilience rather than identical collapse geometry

---

## 8. What This Supports

This document supports the following claim:

> In two closed-form task families and two distinct models, consistency_v1 declined before the first observed accuracy loss under an identical protocol.

This stronger but still acceptable interpretation is also supported:

> The magnitude of the lead varies across models, suggesting model-dependent resilience to increasing task complexity.

---

## 9. What This Does Not Yet Support

This document does **not** support:

- a universal law of all LLMs
- a general property of all transformer systems
- a production-ready gate
- a predictive guarantee for arbitrary reasoning tasks
- broad claims about open-ended tasks or semantic truth

---

## 10. Limits

- only 2 models
- only 2 domains
- only closed-form tasks
- one run series per model/domain pairing
- no broader benchmark comparison yet
- no open-ended reasoning coverage yet

---

## 11. Next Step

The next technically justified step is:

> controlled expansion of cross-model replication and adjacent closed-form domains, while preserving the same protocol.

Only after that does threshold-setting or deployment gating become scientifically reasonable.

---

## 12. Final Statement

These results do not establish a general law.

They do establish something narrower and important:

> Under a fixed protocol, structural consistency moved earlier than accuracy in real runs, across two domains and two different models.

That is the current evidential boundary.