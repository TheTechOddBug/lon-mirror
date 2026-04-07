# OMNIA x GSM-Symbolic — Mini Validation Protocol v0

Status: executable public mini-validation
Scope: small, falsifiable, externally readable
Goal: test whether OMNIA detects structural fragility on controlled mathematical variants

---

## 1. Claim

OMNIA measures structural fragility across near-equivalent GSM-Symbolic problem instances.

More precisely:

Given groups of questions generated from the same symbolic template, OMNIA should assign:

- higher structural stability to base instances
- lower structural stability to number-perturbed instances
- equal or lower structural stability to clause-augmented instances

if the model behavior becomes less stable under those controlled variations.

This is not a claim about solving mathematics.
It is a claim about detecting structural instability in model outputs.

---

## 2. Boundary

OMNIA does not:

- solve the math problem
- explain the reasoning semantically
- replace accuracy
- claim truth from meaning

OMNIA only measures structural behavior across transformed outputs.

measurement != cognition != decision

---

## 3. Score convention

The protocol uses one single fixed convention.

### 3.1 `omnia_score`

`omnia_score` = structural stability score

Interpretation:
- higher score = more stable
- lower score = more fragile

This convention is fixed for the entire protocol.

### 3.2 `fragility_rank`

`fragility_rank` is assigned within each 3-instance template group.

Rank definition:
- rank 1 = least fragile = highest stability
- rank 2 = intermediate
- rank 3 = most fragile = lowest stability

If two instances have exactly the same `omnia_score`, they are treated as tied and the expected ordering for that template is marked as non-conforming.

---

## 4. Minimal hypothesis

For a fixed model and a fixed prompting setup:

- base variants should show the highest structural stability
- number-only perturbations should reduce stability
- clause-augmented variants should reduce stability further, or at least not improve it systematically

Expected direction:

base > num_perturbed >= clause_augmented

where the comparison refers to `omnia_score`.

If OMNIA cannot separate these groups better than noise, the claim fails.

---

## 5. Dataset slice

Use a very small public slice first.

Recommended v0 slice:

- 10 symbolic templates total
- for each template, select:
  - 1 base instance
  - 1 number-perturbed instance
  - 1 clause-augmented instance

Total:
- 30 questions

Why this size:
- small enough to inspect manually
- large enough to avoid single-example cherry-picking
- public and reproducible

---

## 6. Model protocol

Use a single model only in v0.

Required invariants:
- same model
- same prompt template
- same decoding settings
- same final-answer extraction rule
- same run conditions across all 30 cases

No multi-model expansion in v0.
No parameter sweep in v0.

The first goal is not breadth.
It is one clean falsifiable signal.

---

## 7. Scoring mode

This point is fixed.

OMNIA produces one **individual `omnia_score` per instance**.

That means:
- each of the 30 outputs receives its own stability score
- scores are computed independently at the instance level
- comparison is performed afterward at the template level

Then, within each template:
- the 3 instance scores are ordered
- `fragility_rank` is derived from that ordering

So the protocol is:

individual score first  
template comparison second

No pairwise scoring is used in v0 as the primary reported quantity.
No reference-output scoring is used in v0 as the public-facing primary protocol.

---

## 8. Input/output artifacts

For each of the 30 questions, store:

- `template_id`
- `variant_type`
- `question`
- `expected_answer`
- `model_raw_output`
- `model_final_extracted_answer`
- `is_correct`
- `omnia_score`
- `fragility_rank`

Suggested filenames:

- `examples/gsm_symbolic_v0_questions.jsonl`
- `examples/gsm_symbolic_v0_model_outputs.jsonl`
- `examples/gsm_symbolic_v0_omnia_scores.jsonl`

---

## 9. Variant labels

Use exactly these labels:

- `base`
- `num_perturbed`
- `clause_augmented`

Do not introduce extra categories in v0.

---

## 10. Success criterion

The experiment is considered successful if all of the following hold.

### S1. Group ordering

Mean `omnia_score` follows this direction:

base > num_perturbed >= clause_augmented

This is the primary aggregate signal.

### S2. Template consistency

The expected direction above appears in a clear majority of templates,
not just in the aggregate mean.

Minimum acceptable rule for v0:

- at least 7 out of 10 templates follow the expected ordering direction exactly

A template counts as conforming only if:

base_score > num_score >= clause_score

If this exact relation does not hold, that template is non-conforming.

### S3. Non-triviality

OMNIA must provide signal beyond raw correctness.

Minimum operational test:

- recompute group comparison using only cases where `is_correct = true`

If, inside the correct-only subset, `base` still tends to have higher `omnia_score` than `clause_augmented`, OMNIA is not merely copying correctness.

Optional secondary check:
- if there are enough incorrect cases, repeat the same comparison inside the incorrect-only subset

This secondary check is optional in v0.
The correct-only check is mandatory.

---

## 11. Failure criterion

The experiment is considered failed if any of the following happens.

### F1. No separation

Mean `omnia_score` is approximately the same across all three groups.

### F2. Wrong direction

Base instances are scored as equally or less stable than the perturbed groups without a consistent interpretable pattern.

### F3. Template collapse

Fewer than 7 out of 10 templates satisfy:

base_score > num_score >= clause_score

### F4. Pure correctness shadow

Inside the correct-only subset, OMNIA shows no meaningful group separation.

In that case, OMNIA is not adding structural signal beyond correct vs incorrect.

---

## 12. Tie rule

The tie rule is fixed and explicit.

### 12.1 Score ties

If two instances inside the same template have exactly the same `omnia_score`, the template is marked as non-conforming for the purposes of expected-order validation.

### 12.2 No epsilon threshold in v0

No epsilon tolerance is introduced in v0.

The protocol uses the raw numerical value directly.

This is intentionally strict.

Reason:
- easier to read
- easier to reproduce
- no ambiguity from threshold tuning

If later versions need tolerance handling, that belongs to v1 or later, not to v0.

---

## 13. Baselines

Use only minimal baselines in v0.

### Baseline A: raw correctness

For each instance:
- correct or incorrect

### Baseline B: within-template answer consistency

For each 3-instance template:
- whether the model answer stays aligned across variants or not

OMNIA does not need to beat accuracy.
OMNIA needs to reveal structural instability that raw correctness alone does not describe well.

---

## 14. Public result format

The result must be readable without reading the full repo.

### Table 1: instance-level results

| template_id | variant_type | final_answer | is_correct | omnia_score | fragility_rank |
|-------------|--------------|--------------|------------|-------------|----------------|

### Table 2: group summary

| group | n | mean_accuracy | mean_omnia_score | std_omnia_score |
|-------|---|---------------|------------------|-----------------|

### Table 3: template-level ordering

| template_id | base_score | num_score | clause_score | expected_order_respected |
|-------------|------------|-----------|--------------|--------------------------|

Where:

- `expected_order_respected = true` only if  
  `base_score > num_score >= clause_score`

Otherwise:
- `expected_order_respected = false`

---

## 15. Visual output

Use only one plot in v0.

Recommended:
- bar plot of mean `omnia_score` by variant group
- error bars = standard deviation

Optional second plot only if necessary:
- per-template line plot showing score drift from `base` to `num_perturbed` to `clause_augmented`

Do not exceed two plots.

---

## 16. Interpretation rules

Allowed interpretation:

"OMNIA detects structural fragility under controlled symbolic perturbations on GSM-Symbolic."

Allowed stronger version if results support it:

"OMNIA preserves a stability ordering across base, number-perturbed, and clause-augmented symbolic variants."

Not allowed:

- "OMNIA solves mathematical reasoning"
- "OMNIA proves truth"
- "OMNIA outperforms all evaluation methods"
- "OMNIA understands logic semantically"

Stay inside the boundary.

---

## 17. Strong result profile

A strong v0 result would look like this:

- base questions have the highest mean `omnia_score`
- changing only numbers already lowers `omnia_score`
- adding a non-essential clause lowers it further, or at least does not restore stability
- the trend appears in at least 7 out of 10 templates
- the trend remains visible inside the correct-only subset

That is enough for a first public external claim.

---

## 18. Weak result profile

A weak but still usable result would be:

- OMNIA separates `base` from `clause_augmented`
- but `num_perturbed` is noisy
- or the aggregate signal exists but template-level consistency is weak
- or the correct-only non-triviality check is only partially positive

This would support a reduced claim:

"Partial structural signal detected, not full validation."

---

## 19. Why this matters

If this works, OMNIA stops being only a framework described inside its own repo.

It becomes a system that demonstrates one visible external behavior on a public benchmark.

That is the first threshold that matters.

Not completeness.
Not architecture.
Not theory.

Visible external behavior.

---

## 20. Deliverables

Minimum deliverables for v0:

1. this protocol file
2. one question slice file
3. one model outputs file
4. one OMNIA scoring file
5. one 30-row result table
6. one summary plot
7. one short external post showing the result

If all 7 exist, v0 is real.

If not, it is still only intention.

---

## 21. Final compression

This validation asks only one thing:

Can OMNIA detect instability where controlled symbolic variants destabilize model behavior?

If yes, OMNIA has produced its first small public external signal.

If no, the claim must be reduced or abandoned.

That is the correct standard.