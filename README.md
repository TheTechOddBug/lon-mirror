# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19436307.svg)](https://doi.org/10.5281/zenodo.19436307)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What this does

Systems often look stable until they fail.

OMNIA is a structural measurement layer designed to detect instability signals before they become obvious at the surface level.

It does not interpret meaning.  
It does not evaluate correctness.  
It does not decide.

It measures only:

```text
output = measurement only
structural stability under controlled transformations


---

Core principle

Structural truth = invariance under transformation

If a structure survives perturbation, it carries stable signal.
If it collapses under mild transformation, it was representation-dependent.


---

Architectural boundary

measurement ≠ cognition ≠ decision

OMNIA does not decide.
It measures.

Canonical chain:

Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-LIMIT -> Decision Layer (external)


---

Reproducibility

Example files:

examples/model_outputs_gemini_2plus2.json

examples/model_outputs_gemini_bones.json

examples/model_outputs_gemini_logic.json


Quick demo:

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected behavior:

structured   -> high Ω
perturbed    -> Ω drop
random       -> Δ_struct ≈ 0

If this separation appears, the system is working as intended.


---

Prime candidate ranking — validated result

OMNIA was tested on real integer candidate sets, not only on text or LLM outputs.

Three disjoint intervals were scored using multi-base structural representations:

1000–1200

1200–1400

2000–2200


Across the combined 240-candidate set:

total primes: 86

natural prime density: 35.8333%

OMNIA top 10 prime concentration: 70%

OMNIA top 20 prime concentration: 60%


Compared to a random baseline:

top 10 lift: 1.951709x

top 20 lift: 1.673944x


Compared to a trivial deterministic baseline based on decimal digit sum:

OMNIA top 10 primes: 7

digit-sum top 10 primes: 4


Mean rank comparison on the full set:

OMNIA mean prime rank: 33.151163

random baseline mean prime rank: 120.504210

digit-sum baseline mean prime rank: 120.726744


This supports a narrow but real claim:

OMNIA produces a replicated, non-random ranking signal on prime candidates.

It does not prove primality.
It does not solve an open problem.
It does show a structural correlation strong enough to enrich primes near the top of the ranking.

See:

examples/prime_candidates_1000_1200_results.md

examples/prime_candidates_1200_1400_results.md

examples/prime_candidate_runs_summary_final.md

examples/prime_candidate_random_baseline_comparison.md

examples/prime_candidate_validation_block_final.md



---

Prime candidate cutoff analysis — practical filtering result

The prime-ranking result was also evaluated as a search-space reduction tool.

Using the merged 240-candidate set:

natural prime density: 35.8333%


OMNIA cutoff behavior:

top 5%  -> density 58.33%  | lift 1.6280x

top 10% -> density 58.33%  | lift 1.6280x

top 20% -> density 50.00%  | lift 1.3953x

top 25% -> density 48.33%  | lift 1.3488x

top 50% -> density 42.50%  | lift 1.1860x


This supports a second narrow claim:

OMNIA enables non-trivial search-space reduction on tested prime candidate sets.

See:

examples/prime_candidate_cutoff_analysis_results.md



---

Structural Bias Correction (SBC) — current state

During numeric validation, a recurring failure mode was isolated:

some composite numbers were ranked too highly because they were too symbolically regular across bases.

Examples:

1007

2047

30031

1000001


This led to the design of a correction layer:

Ω_adjusted = Ω_raw - λ * regularity_penalty_norm

Current validated variant:

Structural Bias Correction

internal tag: SBC-Regularity v1


The correction uses a regularity penalty based on:

inverse mean entropy

dominant-character ratio

max run ratio

palindrome closeness


Current best balanced value from the lambda sweep:

λ = 0.03


Important:

Ω_raw is preserved

Ω_adjusted is exposed

legacy default behavior is still preserved in engine


See:

docs/OMNIA_STRUCTURAL_BIAS_CORRECTION.md

examples/high_false_positive_regularity_probe_results.md

examples/regularity_penalty_rerank_results.md

examples/regularity_penalty_lambda_sweep_results.md



---

Million-range validation — correction generalization

SBC was then tested on the interval:

1,000,000–1,002,000


Results:

total candidates: 800

total primes: 145

natural prime density: 18.125%


Raw OMNIA:

top 10 primes: 3

top 20 primes: 7


Adjusted OMNIA (λ = 0.03):

top 10 primes: 8

top 20 primes: 15


Tracked critical case:

1,000,001

raw rank: 2

adjusted rank: 112

penalty norm: 1.0000


This supports a stronger claim:

The regularity correction generalizes successfully to a substantially harder regime with much lower prime density.

See:

examples/prime_candidates_1m_1m002_results.md



---

Shadow Mode — current release policy

SBC is now integrated into the engine in shadow mode.

This means:

omega_total still preserves legacy behavior

omega_raw is exposed explicitly

omega_adjusted is computed when numeric context exists

structural_bias_meta is exposed for inspection

the corrected score is monitored before any default switch


This is a deliberate release policy, not a partial integration.

Reason:

a validated correction should be observed under live-like conditions before replacing the public default score.

See:

examples/structural_bias_correction_smoke_test_results.md

examples/engine_structural_bias_adapter_test_results.md



---

Shadow Mode monitoring

The correction is not only measured by ranking gains, but also by explicit cost accounting.

Current monitor tracks:

Positive Gain: high-confidence composites declassified by SBC

Negative Impact: real primes losing more than a configured rank threshold

Sacrifice Ratio: declassified traps divided by materially harmed primes

Spread Widening: increase in prime vs composite separation after correction


Million-range monitoring result:

Positive Gain count: 18

Negative Impact count: 2

Sacrifice Ratio: 9.000000

Spread widening: 37.521258


This means that, in the monitored batch, SBC removed nine dangerous composite traps for each materially harmed prime.

See:

examples/sbc_shadow_mode_report_results.md



---

GSM-style mini validation

OMNIA was also tested on a small GSM-style reasoning set with controlled variants:

base

num_perturbed

clause_augmented


The main repeated effect was simple:

clause_augmented consistently showed lower structural stability than base.

This supports a narrow claim:

OMNIA detects structural fragility when extra reasoning burden is injected into an otherwise similar chain.

Relevant files:

docs/OMNIA_x_GSM_SYMBOLIC_MINI_VALIDATION_v0.md

examples/gsm_symbolic_v0_questions.jsonl

examples/gsm_symbolic_v0_model_outputs.jsonl

examples/gsm_symbolic_v0_omnia_scores.jsonl



---

Structural lenses

Independent transformation families:

BASE   -> multi-representation invariance

TIME   -> drift / instability over time

CAUSA  -> relational dependencies

TOKEN  -> sequence perturbation

LCR    -> logical coherence reduction


Each lens produces an independent signal.


---

Core metrics

Ω   (Omega)      -> structural coherence under perturbation

Ω̂  (Omega-set)  -> residual invariance across transformations

SEI              -> remaining extractable structure (-> 0 = saturation)

IRI              -> irreversible structural loss (> 0 = non-recoverable)

TΔ               -> divergence point

R                -> recovery capacity


SBC-specific fields now available in engine-level integration:

omega_raw

omega_adjusted

structural_bias_meta.bias_penalty_raw

structural_bias_meta.bias_penalty_norm

structural_bias_meta.lambda_value



---

Structural isolation

Δ_struct = Ω_raw − Ω_shuffle

This removes statistical artifacts and preserves only structure-dependent signal.


---

Minimal validation rule

Δ_struct(structured) > Δ_struct(perturbed) > Δ_struct(random)

If this ordering fails, either the system is misconfigured or the input does not contain meaningful structure.


---

Experimental evidence (current)

Natural text (controlled)

Invariant verified.

See:

docs/PUBLIC_PROOF.md


LLM stress test (manual, controlled)

logic_strong         = 0.1654
hallucination_fluent = 0.0821
degenerated_loop     = 0.0114

Invariant:

logic > hallucination > loop

Interpretation:

fluency is not structure

hallucination loses relational stability

loops collapse structural diversity


Status:

pre-validation (manual dataset)

See:

docs/LLM_STRESS_TEST.md

data/llm_stress_test_results.json


Real LLM test (TruthfulQA)

Δ_struct(correct)   = 0.1284
Δ_struct(incorrect) = 0.0912

Invariant:

correct > incorrect

Status:

PASS (non-controlled outputs)

See:

docs/LLM_REAL_TEST.md

data/llm_real_results.json


Temperature decay test

T=0.2 -> 0.1482
T=0.5 -> 0.1215
T=0.8 -> 0.0984
T=1.0 -> 0.0812
T=1.2 -> 0.0543

Invariant:

Δ_struct decreases as temperature increases

Status:

PASS

See:

docs/TEMPERATURE_TEST.md

data/temperature_results.json


Context length test

short   -> 0.1524
medium  -> 0.1310
long    -> 0.0942
v_long  -> 0.0618

Invariant:

Δ_struct decreases as context length increases

Status:

PASS

See:

docs/CONTEXT_LENGTH_TEST.md



---

Where this applies

OMNIA can be used on any structured system where ordered representation matters.

Examples:

code -> hidden fragility detection

finance -> regime shifts / pre-collapse signals

cybersecurity -> anomaly pattern detection

AI outputs -> reasoning stability measurement

knowledge systems -> invariance testing

decision pipelines -> robustness measurement

numeric sequences -> structural ranking and instability screening



---

What you get

early signal of structural instability

model-independent diagnostics

sequence-level robustness measurement

ranking signal on structured candidates

structural comparison across transformations

practical filtering signal for candidate reduction

monitored structural bias correction for numeric ranking


Works on:

text

code

numeric sequences

any ordered representation



---

Why this is different

System	Behavior

Guardrails	block output
Eval tools	measure after failure
Observability	track metrics
OMNIA	measure structural fragility before visible collapse


OMNIA now also supports:

explicit separation between raw and adjusted structural score

monitored bias correction instead of blind score replacement



---

Limits

controlled + semi-controlled datasets

mean-based evaluation

limited distributional analysis

mostly single-model experiments

no universality claim

ranking correlation is not equivalent to proof

false positives remain part of the observed behavior

SBC is validated and integrated, but still shadow-monitored

omega_adjusted is not yet the public default score



---

Repository layout

omnia/     -> engine
examples/  -> runnable demos and numeric experiments
tests/     -> validation
docs/      -> formalization
data/      -> datasets


---

Position

OMNIA is not:

a model

a predictor

a semantic analyzer

a primality test


OMNIA is:

a structural stability measurement layer

a ranking mechanism over structured representations

a detector of fragility and invariance

a filtering aid for candidate prioritization

a shadow-monitored bias-correctable measurement engine



---

License

MIT


---

Citation

Brighindi, M.
https://github.com/Tuttotorna/lon-mirror

