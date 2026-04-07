# OMNIA x GSM-Symbolic — Mini Validation Protocol v0

Status: external-facing minimal validation
Scope: small, falsifiable, public
Goal: test whether OMNIA detects structural fragility on controlled mathematical variants

---

## 1. Claim

OMNIA measures structural fragility across near-equivalent GSM-Symbolic problem instances.

More precisely:

Given groups of questions generated from the same symbolic template, OMNIA should assign:

- lower fragility to base instances
- higher fragility to number-perturbed instances
- equal or higher fragility to clause-augmented instances

if the model behavior becomes less stable under those controlled variations.

This is not a claim about solving mathematics.
It is a claim about detecting structural instability in model outputs.

---

## 2. Why GSM-Symbolic

GSM-Symbolic is a public benchmark built from symbolic templates that generate multiple controlled variants of the same underlying problem.

This makes it a good target for OMNIA because OMNIA is not meant to judge semantic truth directly.
It is meant to measure stability under controlled transformations.

So the fit is direct:

- GSM-Symbolic provides controlled structural variants
- the model produces outputs
- OMNIA measures how stable or fragile those outputs are across the variants

---

## 3. Boundary

OMNIA does not:

- solve the math problem
- explain the reasoning semantically
- replace accuracy
- claim truth from meaning

OMNIA only measures structural behavior across transformed outputs.

measurement != cognition != decision

---

## 4. Minimal hypothesis

For a fixed model and a fixed prompting setup:

- base variants should show the highest structural stability
- number-only perturbations should reduce stability
- clause-augmented variants should reduce stability further, or at least not improve it systematically

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
- large enough to avoid a single cherry-picked example
- public and reproducible

---

## 6. Model protocol

Use a single model only in v0.

Recommended rule:
- same model
- same prompt template
- same decoding settings
- same extraction rule for final answer across all 30 cases

No multi-model expansion in v0.
No parameter sweep in v0.

The first goal is not breadth.
It is one clean falsifiable signal.

---

## 7. Input/output artifacts

For each of the 30 questions, store:

- template_id
- variant_type
- question
- expected_answer
- model_raw_output
- model_final_extracted_answer
- is_correct
- omnia_score
- omnia_fragility_rank

Suggested filenames:

- `examples/gsm_symbolic_v0_questions.jsonl`
- `examples/gsm_symbolic_v0_model_outputs.jsonl`
- `examples/gsm_symbolic_v0_omnia_scores.jsonl`

---

## 8. Variant labels

Use exactly these labels:

- `base`
- `num_perturbed`
- `clause_augmented`

Do not introduce extra categories in v0.

---

## 9. Success criterion

The experiment is considered successful if all of the following hold:

### S1. Group ordering

Mean fragility follows this direction:

base < num_perturbed <= clause_augmented

or, if stability is used instead of fragility:

base > num_perturbed >= clause_augmented

### S2. Template consistency

The ordering above appears in a clear majority of templates,
not just in the aggregate mean.

Minimum acceptable rule for v0:

- at least 7 out of 10 templates follow the expected ordering direction

### S3. Non-triviality

OMNIA must provide more than raw correctness.

That means:
even among answers with the same correctness label,
OMNIA should still show a meaningful difference in structural fragility between the variant groups.

If OMNIA only mirrors correct/incorrect labels, the result is weak.

---

## 10. Failure criterion

The experiment is considered failed if any of the following happens:

### F1. No separation

Mean OMNIA fragility is approximately the same across all three groups.

### F2. Wrong direction

Base instances are scored as equally or more fragile than the perturbed groups without a clear reason.

### F3. Template collapse

The expected ordering appears in too few templates to be credible.

### F4. Pure accuracy shadow

OMNIA adds no signal beyond correct vs incorrect.

If correct answers always get one pattern and incorrect answers always get another,
with no extra structure inside those buckets,
then the result is not strong enough.

---

## 11. Baseline

Use only one minimal baseline in v0:

### Baseline A: raw model correctness

For each instance:
- correct or incorrect

### Baseline B: answer consistency within template

For each 3-instance group:
- do the answers stay aligned across variants or not

OMNIA does not need to beat accuracy.
It needs to reveal structural instability that accuracy alone does not describe well.

---

## 12. Public result format

The result must be readable without reading the repo.

Produce one table with 30 rows and these columns:

| template_id | variant_type | final_answer | is_correct | omnia_score | fragility_rank |
|-------------|--------------|--------------|------------|-------------|----------------|

Then produce one summary table:

| group | n | mean_accuracy | mean_omnia_score | std_omnia_score |
|-------|---|---------------|------------------|-----------------|

And one final template-level table:

| template_id | base_score | num_score | clause_score | expected_order_respected |
|-------------|------------|-----------|--------------|--------------------------|

---

## 13. Visual output

Use only one plot in v0.

Recommended:
- bar plot of mean OMNIA score by variant group
- error bars = standard deviation

Optional second plot only if needed:
- per-template line plot showing score drift from base -> num_perturbed -> clause_augmented

No more than two plots.

---

## 14. Interpretation rules

Allowed interpretation:

"OMNIA detects structural fragility under controlled symbolic perturbations on GSM-Symbolic."

Not allowed:

- "OMNIA solves mathematical reasoning"
- "OMNIA proves truth"
- "OMNIA outperforms all evaluation methods"
- "OMNIA understands logic semantically"

Stay inside the boundary.

---

## 15. Strong version of the result

A strong v0 result would look like this:

- base questions have the highest structural stability
- changing only numbers already lowers OMNIA stability
- adding a non-essential clause lowers it further
- this trend appears repeatedly across templates
- the effect is visible even before giving a semantic explanation

That would be enough for the first public claim.

---

## 16. Weak version of the result

A weak but still usable result would be:

- OMNIA separates clause-augmented from base
- but number-only perturbations are noisy
- or the effect exists only on some templates

That would still be publishable as:
"partial signal, not full validation"

---

## 17. Why this matters

If this works, OMNIA stops being only a framework described inside its own repo.

It becomes a system that demonstrates one visible external behavior on a public benchmark.

That is the first threshold that matters.

Not completeness.
Not architecture.
Not theory.

Visible external behavior.

---

## 18. Deliverables

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

## 19. Final compression

The only thing this validation tries to show is:

Can OMNIA detect instability where GSM-Symbolic already shows that near-equivalent math problems destabilize LLM behavior?

If yes, OMNIA has produced its first small external signal.
If no, the claim must be reduced or abandoned.

That is the correct standard.