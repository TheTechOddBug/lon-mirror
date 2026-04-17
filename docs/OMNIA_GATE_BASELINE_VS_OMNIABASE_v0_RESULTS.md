# OMNIA Gate Sandbox — Baseline vs OMNIABASE v0 Results

## Status

This document records the first sandbox comparison between:

- a minimal heuristic baseline
and
- the OMNIABASE auxiliary warning adapter

This is not a production benchmark.
This is not deployment evidence.
This is not proof that OMNIABASE should replace all manual heuristics.

It is a controlled comparison intended to answer one narrow question:

> does OMNIABASE add any warning signal beyond a shallow handcrafted baseline?

Correct state:

```text
sandbox comparison executed
incremental warning signal observed
external operational value not yet validated


---

Linked artifacts

Implementation files:

examples/omnia_base_gate_adapter_demo.py

examples/omnia_gate_baseline_vs_omniabase_v0.py

omnia/lenses/base_lens.py


Related documents:

docs/OMNIABASE_GATE_ADAPTER_EVAL_v0_RESULTS.md

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Comparison setup

Baseline

The baseline is intentionally simple and transparent.

It emits warnings from three shallow rules:

repeated character run warning

repeated token loop warning

numeric power-of-two warning


This is not meant to be a strong system. It is meant to be a clear reference point.


---

OMNIABASE side

The OMNIABASE adapter projects inputs into deterministic integers, runs the OMNIABASE lens, and emits:

cross_base_fragility_warning

when at least one of the following conditions holds:

ob_cross_base_stability < 0.72

ob_collapse_count >= 12

ob_base_sensitivity >= 0.40


This remains an auxiliary warning only.

It is not a rejection decision.


---

Evaluated classes

The sandbox comparison includes controlled classes such as:

simple numeric

power numeric

repeated numeric

repetitive text

token loop text

patterned text

mixed text


The purpose of these classes is contrast, not realism.


---

Summary table

Dataset Class	Baseline Warn	OMNIABASE Warn	OMNIABASE Only Rate	Agreement

Simple Numeric	0%	0%	0%	100%
Power Numeric	100%	100%	0%	100%
Repeated Numeric	0%	20%	20%	80%
Repetitive Text	100%	100%	0%	100%
Token Loop Text	100%	100%	0%	100%
Patterned Text	0%	40%	40%	60%
Mixed Text	0%	0%	0%	100%



---

Primary result

The main result is simple:

OMNIABASE is not pure redundancy in this sandbox

It agrees with the baseline on obvious fragile cases, but also emits additional warnings on some classes that the shallow baseline does not catch.

That is the first evidence of incremental signal.


---

Where OMNIABASE adds signal

1. repeated numeric class

Observed behavior:

baseline warning rate: 0%

OMNIABASE warning rate: 20%

OMNIABASE-only rate: 20%


Interpretation:

the shallow baseline does not treat decimal repetition as suspicious unless it matches one of its explicit heuristics.

OMNIABASE, instead, detects some cases as representation-fragile under cross-base analysis.

This does not prove correctness. But it does show non-redundant sensitivity.


---

2. patterned text class

Observed behavior:

baseline warning rate: 0%

OMNIABASE warning rate: 40%

OMNIABASE-only rate: 40%


Interpretation:

this is the most important incremental result in the sandbox.

The baseline misses these cases because they do not satisfy its explicit handcrafted triggers.

OMNIABASE still flags some of them through its projection plus cross-base fragility analysis.

This is the clearest evidence, in this controlled comparison, that OMNIABASE may detect some forms of structural regularity or instability that shallow heuristics do not cover.

That is a bounded but real result.


---

Where OMNIABASE agrees with the baseline

1. power numeric class

Observed behavior:

baseline warning rate: 100%

OMNIABASE warning rate: 100%

agreement: 100%


Interpretation:

both systems identify this class as fragile.

This is useful because it shows OMNIABASE is at least compatible with an obvious handcrafted check in a known unstable regime.


---

2. repetitive text class

Observed behavior:

baseline warning rate: 100%

OMNIABASE warning rate: 100%

agreement: 100%


Interpretation:

both systems react strongly to extreme repetition.

Again, this is not enough to prove superiority, but it confirms that OMNIABASE does not miss an obvious low-diversity failure mode in this sandbox.


---

3. token loop text class

Observed behavior:

baseline warning rate: 100%

OMNIABASE warning rate: 100%

agreement: 100%


Interpretation:

the adapter remains aligned with clear repetitive-loop behavior under this controlled setup.

This is positive because agreement on obvious cases is necessary before disagreement on subtle cases becomes interesting.


---

Where OMNIABASE stays quiet

1. simple numeric class

Observed behavior:

baseline warning rate: 0%

OMNIABASE warning rate: 0%


Interpretation:

OMNIABASE does not introduce extra warnings on ordinary simple numeric examples in this set.


---

2. mixed text class

Observed behavior:

baseline warning rate: 0%

OMNIABASE warning rate: 0%


Interpretation:

OMNIABASE remains quiet on the natural-language-like mixed class in this controlled evaluation.

This matters because it suggests the auxiliary warning is not firing indiscriminately.

Important constraint: this is not proof of zero false positives. It is only a no-warning outcome on this limited sandbox class.


---

What this comparison supports

The strongest justified claim is:

> In this controlled sandbox, OMNIABASE adds non-redundant warning signal beyond a shallow heuristic baseline, especially on repeated numeric and patterned text classes, while remaining aligned with the baseline on obvious fragile cases.



That claim is supported.


---

What this comparison does not support

The following claims remain unjustified:

OMNIABASE replaces handcrafted heuristics

OMNIABASE has zero false positives

OMNIABASE is production-ready

OMNIABASE understands semantic loops

OMNIABASE is superior to well-engineered gate systems

OMNIABASE should directly drive rejection or escalation by itself


Those would still be premature or false.


---

Structural interpretation

The comparison suggests three useful zones.

Zone A — obvious shared fragility

Classes where both systems fire:

power numeric

repetitive text

token loop text


These are shared detections.


---

Zone B — OMNIABASE-only sensitivity

Classes where OMNIABASE adds signal:

repeated numeric

patterned text


This is the most important zone in the current sandbox.

If this effect survives broader testing, it becomes the main argument for including OMNIABASE as an auxiliary layer.


---

Zone C — shared quiet regime

Classes where both systems remain quiet:

simple numeric

mixed text


This is also useful, because it suggests OMNIABASE is not currently degenerating into universal warning behavior.


---

Main strengths of the result

1. incremental signal exists

This is the central point.

OMNIABASE is not just reproducing the baseline.

2. agreement on obvious cases remains high

This reduces the risk that OMNIABASE is merely eccentric or disconnected.

3. no extra warnings on the quiet classes in this sandbox

This is a positive sign for boundedness.

Again: not proof of low false positives in general, only a useful controlled result.


---

Main limitations

1. baseline is intentionally weak

This matters.

A stronger handcrafted baseline might reduce OMNIABASE-only gains.

So the current result demonstrates incremental value over a shallow baseline, not over all plausible baselines.


---

2. sandbox classes are small and controlled

The dataset is narrow. It does not represent real failure distributions from deployed LLM systems.


---

3. projection bridge remains a core uncertainty

For text inputs, the warning depends on:

text -> deterministic integer projection -> OMNIABASE lens

This means some observed signal may reflect projection artifacts.

That limitation remains active.


---

4. no end-to-end outcome metric yet

This comparison measures warning behavior only.

It does not yet show improvement in:

retry success

escalation quality

downstream correctness

user-facing failure reduction


Without that, operational value remains suggestive, not established.


---

Why this result matters

This result matters because it answers the first hard practical objection:

> why not just use regexes and simple rules?



Current answer:

because in this sandbox, simple rules miss some cases that OMNIABASE flags.

That is not the final answer. But it is the first legitimate answer.


---

Correct next step

The next technically correct move is:

test OMNIABASE against a stronger sandbox baseline

Two good directions:

1. strengthened heuristic baseline

Add handcrafted checks for:

alternating pattern repetition

short-cycle motifs

repeated numeric block structure


Then compare again.

This tests whether OMNIABASE still adds signal after baseline improvement.

2. small real-output sandbox

Use a small set of actual model outputs, including:

normal answers

loops

near-loops

brittle numeric outputs

superficially clean but structurally suspicious outputs


Then compare:

baseline

baseline + OMNIABASE


Only that begins to test practical value.


---

Minimal conclusion

The sandbox comparison v0 shows that OMNIABASE provides incremental warning signal beyond a shallow heuristic baseline in a controlled setting, especially on patterned text and repeated numeric classes, while remaining aligned on obvious fragile cases and quiet on the controlled natural-language-like class.

That is enough to justify stronger testing.

It is not enough to claim general gate superiority.

