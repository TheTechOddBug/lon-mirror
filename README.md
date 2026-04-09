# OMNIA v1.0 — Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19484594.svg)](https://doi.org/10.5281/zenodo.19484594)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## What OMNIA is

Systems often look stable until they fail.

OMNIA is a structural measurement layer designed to detect instability, fragility, and regime change before they become obvious at the surface level.

It does **not** interpret meaning.  
It does **not** evaluate semantic truth.  
It does **not** decide policy.  
It does **not** act as a model.

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

measurement != cognition != memory != decision

OMNIA does not decide.
OMNIA measures, classifies, and maintains structural state within a bounded operational policy.

Canonical chain:

Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-LIMIT -> Decision Layer (external)


---

Current validated operational stack

OMNIA is now validated, within the tested perimeter, across five layers:

1. Metric
Detects structural deviation through the signature sigma and dO.


2. Protocol
Classifies transitions as:

equivalence

mild_variation

structural_break



3. Memory
Consolidates a new regime when post-break states become internally coherent.


4. Chaos refusal
Refuses to normalize persistent incoherence as a false stable regime.


5. SCU v1
Emits a first operational structural compatibility unit between states:

U_v1(S1, S2) = (C, I, P)

where:

C = compatibility

I = irreversibility within the observed window

P = purity / internal coherence




This means OMNIA now supports:

structural measurement

transition classification

regime consolidation

refusal of false stabilization

first bounded structural compatibility output between states


within the currently validated datasets.


---

Reproducibility

Clone and run:

git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py

Expected behavior:

structured   -> high Omega
perturbed    -> Omega drop
random       -> Delta_struct approx 0

If this separation appears, the system is working as intended.

Example reference files:

examples/model_outputs_gemini_2plus2.json

examples/model_outputs_gemini_bones.json

examples/model_outputs_gemini_logic.json



---

Validation perimeter reached so far

OMNIA has been validated, within controlled or semi-controlled settings, across:

synthetic pair discrimination

temporal numeric streams

multi-stream numeric monitoring

structured logs

controlled free-text operational logs

chaotic console-like logs with volatile token normalization

post-break recovery

post-break chaos refusal

SCU v1 emission on validated transition scenarios


This is a real operational perimeter, not a universality claim.


---

Structural lenses

Independent transformation families currently used in the project:

BASE  -> multi-representation invariance

TIME  -> drift / instability over time

CAUSA -> relational dependencies

TOKEN -> sequence perturbation

LCR   -> logical coherence reduction


Each lens emits an independent structural signal.


---

Core metrics

Omega      -> structural coherence under perturbation

Omega-set  -> residual invariance across transformations

SEI        -> remaining extractable structure

IRI        -> irreversible structural loss

TDelta     -> divergence point

R          -> recovery capacity

dO         -> structural distance between consecutive states


SBC-specific engine fields:

omega_raw

omega_adjusted

structural_bias_meta.bias_penalty_raw

structural_bias_meta.bias_penalty_norm

structural_bias_meta.lambda_value



---

Structural isolation

Delta_struct = Omega_raw - Omega_shuffle

This removes statistical artifacts and preserves only structure-dependent signal.

Minimal validation rule:

Delta_struct(structured) > Delta_struct(perturbed) > Delta_struct(random)

If this ordering fails, either:

the system is misconfigured, or

the input contains no meaningful structure.



---

Operational transition logic

At runtime, OMNIA classifies transitions into three zones:

equivalence

Variation is representational only.

mild_variation

Drift exists, but continuity remains structurally compatible.

structural_break

Continuity is no longer structurally justified.

This transition layer is integrated with trajectory memory.


---

Memory policy and regime handling

The memory layer currently supports:

STABLE

DRIFTING

CANDIDATE

CHAOTIC


What this means

After rupture, OMNIA no longer remains trapped in permanent alarm mode.

It can now:

open a post-break candidate window

evaluate internal coherence of post-break states

confirm a new stable regime if coherence is high enough

refuse the commit if post-break states remain structurally incoherent


This is the key difference between:

adaptation

when a new regime is coherent

and

auto-deception

when chaos is incorrectly promoted to normality


---

Structural Compatibility Unit (SCU v1)

OMNIA now emits a first executable approximation of a structural compatibility unit between states:

U_v1(S1, S2) = (C, I, P)

where:

C = compatibility

I = irreversibility within the observed window

P = purity / internal coherence


Interpretation

C asks: how much is the previous regime still alive

I asks: how irreversible is the rupture within the observed window

P asks: how much structural dignity does the emerging pattern have


This unit is not yet universal and not yet canonical.
It is the first operational bundle that compresses a transition into a bounded structural object.

Relevant files:

docs/STRUCTURAL_COMPATIBILITY_UNIT_V0.md

docs/STRUCTURAL_COMPATIBILITY_UNIT_V1_SPEC.md

docs/STRUCTURAL_COMPATIBILITY_UNIT_V1_RESULTS.md

examples/do_structural_compatibility_unit_v1.jsonl



---

Validation highlights

1. Synthetic / controlled pair validation

Initial validation separated:

equivalent pairs

mild variations

structural breaks


This established the first operational dO baseline.

Relevant files:

docs/STATE_DISTANCE_FOUNDATION.md

docs/DO_MINI_VALIDATION_RESULTS_v0.md

docs/DO_MINI_VALIDATION_RESULTS_v2.md

examples/do_mini_validation_pairs_v0.jsonl

examples/do_mini_validation_pairs_v1.jsonl



---

2. Real numeric stream validation

OMNIA was validated on a simple ordered numeric series containing:

stability

drift

shock

stabilization at a new level


This proved that OMNIA can operate as a temporal monitoring engine, not only as a pairwise comparator.

Relevant files:

examples/real_series_demo_v1.jsonl

docs/REAL_SERIES_DEMO_RESULTS_V1.md



---

3. Multi-stream validation

OMNIA then validated strict memory isolation across interleaved streams.

This proved that:

drift accumulation remains stream-local

break counters remain stream-local

alerts remain stream-local

no cross-stream contamination occurs


Relevant files:

docs/MULTI_TRAJECTORY_V1.md

examples/multi_stream_demo_v1.jsonl

docs/MULTI_STREAM_DEMO_RESULTS_V1.md



---

4. Structured logs validation

OMNIA was validated on structured operational logs where messages still preserved explicit field-like organization.

This demonstrated:

drift detection under mixed numeric/symbolic change

break detection under schema change

preserved stream isolation


Relevant files:

examples/structured_logs_demo_v1.jsonl



---

5. Free-text operational validation

OMNIA was then validated on controlled free-text logs.

This demonstrated that the engine can:

tolerate limited linguistic noise

detect drift embedded in prose

detect rupture without rigid schema

remain stable under minor wording changes


Relevant files:

examples/free_text_logs_demo_v1.jsonl

examples/do_free_text_results_v1.jsonl

docs/FREE_TEXT_VALIDATION_V1.md



---

6. Chaotic console validation

OMNIA was then stressed on console-like logs containing:

timestamps

thread ids

pid values

hex tokens

volatile counters


A stronger precanonicalization layer normalized these volatile tokens so that OMNIA measured the message topology rather than incidental identifiers.

This demonstrated:

strong suppression of superficial noise

preserved break sensitivity

preserved stability on structurally unchanged noisy streams


Relevant files:

examples/chaotic_console_logs_demo_v1.jsonl

examples/do_chaotic_console_results_v1.jsonl

docs/CHAOTIC_CONSOLE_VALIDATION_V1.md



---

7. Post-break recovery validation

OMNIA was then validated on the first successful post-break regime crystallization scenario.

This demonstrated that after rupture, the system can:

buffer post-break states

evaluate their internal coherence

commit a new stable regime when coherence is sufficiently high

reset legacy drift correctly


Relevant files:

examples/post_break_recovery_test.jsonl

examples/do_post_break_recovery_results_v1.jsonl

docs/MEMORY_POLICY_POST_BREAK_RESULTS_V1.md



---

8. Post-break chaos refusal validation

OMNIA was then validated against the opposite condition:

post-break states remain mutually incoherent.

This demonstrated that OMNIA can:

refuse a false commit

remain in CHAOTIC

preserve the previous stable regime identity

avoid normalizing persistent disorder


This is the current safeguard against false stabilization.

Relevant files:

examples/post_break_chaos_test.jsonl

examples/do_post_break_chaos_results_v1.jsonl



---

9. SCU v1 validation

SCU v1 was then validated as the first bounded structural state-relation bundle.

This demonstrated that OMNIA can compress a transition into:

C -> compatibility

I -> irreversibility within observed window

P -> purity / internal coherence


The currently archived perimeter includes:

continuity

first rupture

chaos refusal behavior

alignment with recovery logic already validated by the same pipeline


Relevant files:

docs/STRUCTURAL_COMPATIBILITY_UNIT_V0.md

docs/STRUCTURAL_COMPATIBILITY_UNIT_V1_SPEC.md

docs/STRUCTURAL_COMPATIBILITY_UNIT_V1_RESULTS.md

examples/do_structural_compatibility_unit_v1.jsonl



---

Prime candidate ranking — validated result

OMNIA was also tested on real integer candidate sets, not only on text or LLM outputs.

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

top 5%  -> density 58.33% | lift 1.6280x

top 10% -> density 58.33% | lift 1.6280x

top 20% -> density 50.00% | lift 1.3953x

top 25% -> density 48.33% | lift 1.3488x

top 50% -> density 42.50% | lift 1.1860x


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

Omega_adjusted = Omega_raw - lambda * regularity_penalty_norm

Current validated variant:

Structural Bias Correction

internal tag: SBC-Regularity v1


The correction uses a regularity penalty based on:

inverse mean entropy

dominant-character ratio

max run ratio

palindrome closeness


Current best balanced value from the lambda sweep:

lambda = 0.03


Important:

Omega_raw is preserved

Omega_adjusted is exposed

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


Adjusted OMNIA (lambda = 0.03):

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

Positive Gain

Negative Impact

Sacrifice Ratio

Spread Widening


Million-range monitoring result:

Positive Gain count: 18

Negative Impact count: 2

Sacrifice Ratio: 9.000000

Spread widening: 37.521258


This means that, in the monitored batch, SBC removed nine dangerous composite traps for each materially harmed prime.

See:

examples/sbc_shadow_mode_report_results.md



---

Fragility Display — public-facing result

OMNIA was also tested on a minimal public-facing reasoning display based on three near-equivalent math variants.

Triplet used:

A_base

B_symbolic_pressure

C_distractor_added


All three variants were answered correctly by the model.

OMNIA ranking:

A_base -> 0.924150

B_symbolic_pressure -> 0.881230

C_distractor_added -> 0.741200


Public interpretation:

A is correct and structurally solid

B is correct but already stressed

C is still correct on the surface, but structurally fragile


This supports a public and readable claim:

OMNIA detects fragility before visible failure, even when correctness still looks intact.

See:

docs/OMNIA_FRAGILITY_DISPLAY_v1.md

examples/fragility_display_triplets_v1_scores.jsonl

examples/sbc_fragility_monitor_results.md



---

GSM-style mini validation

OMNIA was also tested on a small GSM-style reasoning set with controlled variants:

base

num_perturbed

clause_augmented


The repeated effect was simple:

clause_augmented consistently showed lower structural stability than base.

This supports a narrow claim:

OMNIA detects structural fragility when extra reasoning burden is injected into an otherwise similar chain.

Relevant files:

docs/OMNIA_x_GSM_SYMBOLIC_MINI_VALIDATION_v0.md

examples/gsm_symbolic_v0_questions.jsonl

examples/gsm_symbolic_v0_model_outputs.jsonl

examples/gsm_symbolic_v0_omnia_scores.jsonl



---

Experimental evidence already recorded

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

Delta_struct(correct)   = 0.1284

Delta_struct(incorrect) = 0.0912


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

Delta_struct decreases as temperature increases.

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

Delta_struct decreases as context length increases.

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

operational monitoring -> drift / break / regime consolidation



---

What you get

early signal of structural instability

model-independent diagnostics

sequence-level robustness measurement

ranking signal on structured candidates

structural comparison across transformations

practical filtering signal for candidate reduction

monitored structural bias correction for numeric ranking

public-facing fragility display for reasoning outputs

multi-stream structural monitoring

post-break regime confirmation

refusal of false stabilization under persistent chaos

first bounded structural compatibility bundle between states


Works on:

text

code

numeric sequences

logs

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

readable fragility display where correctness and stability diverge

regime confirmation after break

chaos refusal when no coherent baseline exists

a first operational structural compatibility unit between states



---

Limits

Current limits remain explicit:

controlled + semi-controlled datasets

mean-based evaluation

limited distributional analysis

mostly single-model experiments

no universality claim

ranking correlation is not equivalent to proof

false positives remain part of the observed behavior

SBC is validated and integrated, but still shadow-monitored

omega_adjusted is not yet the public default score

memory policy is validated within tested scenarios, not all real environments

SCU v1 is validated within the tested perimeter, not as a universal unit

threshold values may still require tuning on wider real datasets



---

Current claim

The strongest correct claim at this stage is:

OMNIA is a structural stability measurement engine with validated transition classification, bounded regime memory, chaos refusal, and a first operational structural compatibility unit between states within the tested perimeter.

It is not a universal intelligence layer.
It is not a semantic reasoner.
It is not a proof engine.
It is a structural measurement and monitoring system.


---

Repository layout

omnia/     -> engine

examples/  -> runnable demos and experiments

tests/     -> validation

docs/      -> formalization and reports

data/      -> datasets



---

Position

OMNIA is not:

a model

a predictor

a semantic analyzer

a primality test

a decision layer


OMNIA is:

a structural stability measurement layer

a ranking mechanism over structured representations

a detector of fragility and invariance

a filtering aid for candidate prioritization

a bounded regime-memory engine

a chaos-resistant structural monitoring layer

a first executable structural compatibility framework between states



---

Next steps

The next technically correct steps are:

1. longer and less controlled streams


2. noisier real operational datasets


3. threshold tuning (tau_commit, tau_chaos)


4. wider distributional validation


5. stricter comparison against external baselines




---

License

MIT


---

Citation

Brighindi, M.
https://github.com/Tuttotorna/lon-mirror