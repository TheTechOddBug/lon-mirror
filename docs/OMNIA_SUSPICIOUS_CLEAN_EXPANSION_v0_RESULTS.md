# OMNIA Suspicious Clean Expansion v0 — Results

## Status

This document records the expanded suspicious-clean sandbox evaluation for the combined OMNIA gate policy using:

- a stronger handcrafted baseline
- the OMNIABASE auxiliary warning adapter
- a three-state decision policy:
  - `accept`
  - `review`
  - `retry`

This is not a production benchmark.
This is not deployment evidence.
This is not proof of general superiority.

It is the strongest sandbox result obtained so far for the current OMNIABASE integration path.

Correct state:

```text
expanded suspicious-clean sandbox executed
combined policy strongly improved over baseline in this sandbox
no degradation observed in this sandbox
external validity still unproven


---

Linked artifacts

Implementation files:

examples/omnia_suspicious_clean_expansion_v0.py

examples/omnia_end_to_end_sandbox_v0.py

examples/omnia_real_output_sandbox_v0.py

examples/omnia_base_gate_adapter_demo.py

omnia/lenses/base_lens.py


Related documents:

docs/OMNIA_END_TO_END_SANDBOX_v0_RESULTS.md

docs/OMNIA_REAL_OUTPUT_SANDBOX_v0_RESULTS.md

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Sandbox purpose

The purpose of this sandbox is narrow and important:

> stress-test the role of OMNIABASE on suspicious-clean outputs that are not obviously broken, but show soft repetition, rigid templating, low-diversity explanation patterns, or near-threshold structural regularity



This is the first sandbox designed specifically around OMNIABASE's most plausible operational niche.


---

Policy setup

Baseline policy

The stronger baseline uses explicit handcrafted warnings and maps:

warning -> retry

no warning -> accept


So baseline has only:

accept / retry


---

Combined policy

The combined policy preserves baseline authority and adds OMNIABASE as an auxiliary review layer:

baseline warning -> retry

baseline quiet + OMNIABASE warning -> review

no warnings -> accept


So combined policy becomes:

accept / review / retry

This remains the correct architecture.

OMNIABASE still does not replace the baseline. It only adds caution where the baseline stays silent.


---

Global metrics

Metric	Value	Interpretation

Baseline Correct Rate	0.5416	Baseline struggles on the soft suspicious-clean region
Combined Correct Rate	0.9166	Strong improvement on the current sandbox labels
Combined Better Than Baseline	0.3750	Combined policy improves on baseline in 37.5% of the set
Combined Worse Than Baseline	0.0000	No degradation observed in the current sandbox



---

Primary result

The main result is this:

the combined policy scales much better than the baseline on the expanded suspicious-clean sandbox

This is the strongest evidence so far that OMNIABASE has a real role when used as:

auxiliary structural warning

intermediate review trigger

detector of subtle suspiciousness beyond explicit pattern rules


This is not a claim of production readiness.

It is a strong sandbox proof of role usefulness.


---

Why the gain matters

The gain here is not marginal.

The baseline alone falls close to coin-flip quality on the expanded suspicious-clean set:

0.5416


The combined policy rises to:

0.9166


This means the addition of OMNIABASE materially improves the policy under the label structure of this sandbox.

That is a major result for the current phase.

The gain is not coming from obvious loops or explicit pattern spam. It is coming from softer, more ambiguous, more realistic suspiciousness.

That is exactly the region where OMNIABASE needed to prove value.


---

Subclass-level performance

Subclass	Better than Baseline	Note

soft_sentence_repetition	100%	OMNIABASE captures soft whole-sentence repetition missed by the baseline
light_paraphrase_repetition	66.6%	OMNIABASE retains signal even when wording changes slightly
low_diversity_explanation	100%	OMNIABASE helps on tautological or low-information explanatory forms
hybrid_suspicious	50%	Mixed text-number suspicious cases benefit partially
pattern_near_threshold	100%	OMNIABASE catches near-pattern cases the baseline leaves alone



---

Class-by-class interpretation

1. soft_sentence_repetition

Observed improvement:

combined better than baseline: 100%


Interpretation:

the baseline does not naturally capture repeated sentence-level content unless it fits one of its explicit syntactic triggers.

OMNIABASE improves strongly here by moving these cases into review.

This is one of the cleanest signals in the whole expansion.


---

2. light_paraphrase_repetition

Observed improvement:

combined better than baseline: 66.6%


Interpretation:

this is one of the most important findings.

The text is not literally repeated. The wording changes slightly.

That weakens explicit heuristic triggers, but the combined policy still gains substantial performance through OMNIABASE.

This suggests that OMNIABASE may be sensitive to low-diversity structure even when repetition becomes softer and less syntactically obvious.

This is still a projection-mediated effect, not a semantic proof. But it is a meaningful sandbox result.


---

3. low_diversity_explanation

Observed improvement:

combined better than baseline: 100%


Interpretation:

tautological or low-information explanatory forms are a strong success zone for the combined policy.

This matters because such outputs are often not visibly broken, yet they are operationally suspicious.

This subclass strongly supports the “review sensor” role.


---

4. hybrid_suspicious

Observed improvement:

combined better than baseline: 50%


Interpretation:

OMNIABASE adds partial value on cases where suspicious text structure mixes with numeric content.

This is useful because it suggests the signal is not limited to pure text repetition alone.

The gain is not perfect here, but it is real.


---

5. pattern_near_threshold

Observed improvement:

combined better than baseline: 100%


Interpretation:

this is another important result.

The baseline misses some near-threshold pattern cases because they do not cleanly satisfy its explicit pattern rules.

OMNIABASE still catches them often enough to produce full sandbox gain on this subclass.

That strengthens the claim that OMNIABASE can help exactly where explicit syntactic rules begin to lose sharpness.


---

What the numbers actually mean

Baseline Correct Rate = 0.5416

The stronger baseline performs poorly once the suspicious-clean set becomes broader and softer.

This is a real weakness.

It means explicit rules alone are not handling this region well.


---

Combined Correct Rate = 0.9166

The combined policy performs much better on the current sandbox labels.

That is a very strong sandbox result.

Correct interpretation:

strong fit on the current suspicious-clean sandbox

Not:

universal proof

deployment-level guarantee

final validation



---

Combined Better Than Baseline = 0.3750

This means the combined policy improved over the baseline on 37.5% of the examples in the expanded set.

This is the largest policy gain observed so far.

That makes this experiment the strongest sandbox evidence in favor of OMNIABASE's current role.


---

Combined Worse Than Baseline = 0.0000

This means no baseline-correct example was made worse by the combined policy in the current sandbox.

This is extremely encouraging.

But the correct wording remains:

no degradation observed in this sandbox


not:

impossible degradation or

guaranteed safety elsewhere



---

What this sandbox supports

The strongest justified claim is:

> In the expanded suspicious-clean sandbox, the combined policy substantially outperforms the stronger baseline by using OMNIABASE as an auxiliary review signal on soft repetition, low-diversity explanation, hybrid suspiciousness, and near-threshold pattern cases, without degrading baseline-correct decisions on the tested set.



That claim is supported.


---

What this sandbox does not support

The following claims remain unjustified:

OMNIABASE is production-ready

OMNIABASE proves semantic degeneration directly

OMNIABASE should replace handcrafted gates

the observed gain will generalize unchanged to live traffic

OMNIABASE provides a universal anomaly detector

Phase 6 is closed in a deployment sense


Those would still be too strong.


---

Structural interpretation

This expansion finally clarifies the current best role of OMNIABASE.

Weak role

OMNIABASE is still not the best primary detector for:

explicit pattern spam

obvious loops

syntactic repetition that handcrafted rules already catch well


Strong role

OMNIABASE is strongest as:

suspicious-clean detector

low-diversity structure detector

review escalator for outputs that remain superficially acceptable


This is the clearest role definition obtained so far.


---

Main strengths of the result

1. largest end-to-end policy gain so far

This is the most important milestone.

2. gain appears exactly in the target niche

The gain is not random. It concentrates in the soft suspicious-clean region.

3. no degradation observed on the tested set

This preserves trust in the auxiliary-review design.

4. role clarity is now strong

The evidence no longer points to “general gate replacement”. It points to a much sharper and more credible role.


---

Main limitations

1. sandbox is still hand-curated

The dataset is larger, but still designed by hand.

That makes it useful for role discovery, not final validation.

2. labels are sandbox policy labels

These are not large-scale human annotations or production outcomes.

So the result is policy evidence, not external ground truth.

3. projection bridge remains active

For text cases, OMNIABASE still depends on:

text -> deterministic integer projection -> OMNIABASE lens

This remains a core limitation.

4. no real traffic test yet

We still do not know how the gain behaves under:

real user prompts

actual model failures

distribution shift

operational cost constraints


Without that, the result remains bounded.


---

Why this result matters

This result matters because it is the first time the evidence is both:

strong in magnitude

aligned with a plausible operational role


That combination did not exist earlier.

Earlier steps showed signal. This step shows a narrow but strong policy use-case.

That is the first real candidate for moving OMNIABASE from “interesting module” to “plausible system component”.


---

Correct next step

The next technically correct move is not broad celebration and not full integration yet.

It is one of these:

1. small human-rated validation pass

Take this suspicious-clean set and have manual labels reviewed independently under the same policy space:

accept

review

retry


Then compare baseline vs combined again.

This would be much stronger than self-authored sandbox labels.

2. real model output collection

Build a small corpus of actual LLM outputs from real prompts, especially:

repetitive but paraphrased answers

low-diversity explanations

rigid templated summaries

suspiciously repetitive numeric-language hybrids


Then rerun the same combined-policy evaluation.

3. threshold calibration sweep

Stress the OMNIABASE thresholds and see whether the gain remains while avoiding review inflation.

This is necessary before deeper integration.


---

Minimal conclusion

The suspicious-clean expansion v0 is the strongest sandbox result obtained so far.

It shows that OMNIABASE, when used as an auxiliary review trigger rather than as a replacement gate, can substantially improve policy behavior over a stronger handcrafted baseline in the exact region where explicit heuristics become weakest: soft suspicious-clean outputs.

That is enough to justify continued development with confidence.

It is not enough to claim production completion.

