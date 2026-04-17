# OMNIA Real-Output Sandbox v0 — Results

## Status

This document records the first real-output-style sandbox comparison between:

- a stronger handcrafted baseline
and
- the OMNIABASE auxiliary warning adapter

This is not a production benchmark.
This is not deployment evidence.
This is not proof of end-to-end system improvement.

It is a controlled sandbox intended to test whether OMNIABASE adds any useful warning signal on outputs that are closer to realistic LLM behavior than the previous synthetic class tests.

Correct state:

```text
real-output sandbox executed
bounded incremental signal observed
operational value suggested but not proven


---

Linked artifacts

Implementation files:

examples/omnia_real_output_sandbox_v0.py

examples/omnia_gate_stronger_baseline_vs_omniabase_v0.py

examples/omnia_base_gate_adapter_demo.py

omnia/lenses/base_lens.py


Related documents:

docs/OMNIA_GATE_STRONGER_BASELINE_VS_OMNIABASE_v0_RESULTS.md

docs/OMNIABASE_GATE_ADAPTER_EVAL_v0_RESULTS.md

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Sandbox purpose

The purpose of this sandbox is narrow:

> test whether OMNIABASE adds warning signal on outputs that look closer to real model behavior, especially on cases that are superficially acceptable but structurally suspicious



This is the first step beyond pure synthetic class benchmarking.

The target is not proof. The target is operational relevance screening.


---

Comparison setup

Stronger baseline

The stronger baseline emits warnings from explicit handcrafted rules such as:

repeated character runs

repeated token loops

power-of-two numeric cases

alternating short-cycle patterns

repeated substring blocks

repeated numeric block structures


This baseline is intentionally stronger than the weak sandbox baseline.


---

OMNIABASE side

The OMNIABASE adapter remains unchanged.

It projects candidate outputs into deterministic integers, runs the OMNIABASE lens, and emits:

cross_base_fragility_warning

when at least one of the following holds:

ob_cross_base_stability < 0.72

ob_collapse_count >= 12

ob_base_sensitivity >= 0.40


This remains an auxiliary warning only.

It is not a rejection signal.


---

Summary table

Dataset Class	Baseline Warn	OMNIABASE Warn	OMNIABASE Only	Agreement

Clean Numeric	0%	0%	0%	100%
Brittle Numeric	100%	100%	0%	100%
Clean Explanations	0%	0%	0%	100%
Loop-like	100%	100%	0%	100%
Pattern Heavy	100%	40%	0%	40%
Suspicious Clean	60%	80%	20%	80%
Natural Mixed	0%	0%	0%	100%



---

Primary result

The most important result is this:

OMNIABASE adds bounded extra warning signal on the suspicious-clean class

That is the first place where the real-output sandbox shows incremental value beyond the stronger handcrafted baseline.

This matters more than the earlier synthetic gain because the class is closer to plausible model behavior: outputs that look superficially acceptable but may already be drifting toward degeneracy.


---

Class-by-class interpretation

1. Clean Numeric

Observed behavior:

baseline warning: 0%

OMNIABASE warning: 0%

agreement: 100%


Interpretation:

ordinary clean numeric answers remain quiet for both systems.

This is good. It suggests that neither side is overfiring on normal numeric outputs in this sandbox.


---

2. Brittle Numeric

Observed behavior:

baseline warning: 100%

OMNIABASE warning: 100%

agreement: 100%


Interpretation:

both systems reliably detect this class.

This confirms continuity with previous results: OMNIABASE remains aligned with known cross-base fragile numeric structures, especially power-of-two style cases.


---

3. Clean Explanations

Observed behavior:

baseline warning: 0%

OMNIABASE warning: 0%

agreement: 100%


Interpretation:

clean explanatory text does not trigger the OMNIABASE warning in this sandbox.

This is operationally important because it suggests that the projection bridge is not trivially punishing normal explanatory language.


---

4. Loop-like

Observed behavior:

baseline warning: 100%

OMNIABASE warning: 100%

agreement: 100%


Interpretation:

both systems identify obvious loop-like degeneration.

This is expected.

It does not prove superiority, but it confirms that OMNIABASE does not miss the clearest repetitive failures in this sandbox.


---

5. Pattern Heavy

Observed behavior:

baseline warning: 100%

OMNIABASE warning: 40%

agreement: 40%


Interpretation:

the stronger baseline remains better at explicit pattern detection.

This is an important limitation.

For clearly syntactic repetition families such as patterned strings, well-designed handcrafted rules still dominate raw coverage in this sandbox.

That is not a failure of the experiment. It is a boundary condition.


---

6. Suspicious Clean

Observed behavior:

baseline warning: 60%

OMNIABASE warning: 80%

OMNIABASE-only: 20%

agreement: 80%


Interpretation:

this is the most important class in the sandbox.

It represents outputs that are not obviously broken, but begin to show signs of structural rigidity, repetition, or suspicious regularity while remaining superficially acceptable.

Here OMNIABASE adds warning signal beyond the stronger handcrafted baseline.

This is the first meaningful operational foothold for the system.

It does not prove that OMNIABASE is right in every such case. But it does show that OMNIABASE is not merely duplicating the stronger baseline.


---

7. Natural Mixed

Observed behavior:

baseline warning: 0%

OMNIABASE warning: 0%

agreement: 100%


Interpretation:

natural-looking mixed outputs remain quiet for both systems.

This matters because it suggests that OMNIABASE is not expanding warnings indiscriminately when the output is varied and language-like.

Important boundary: this is not proof of low false positives in general. It is only a positive sandbox outcome on this controlled class.


---

What this sandbox supports

The strongest justified claim is:

> In this real-output-style sandbox, OMNIABASE adds auxiliary warning signal on some superficially clean but structurally suspicious outputs that a stronger handcrafted baseline does not always catch, while remaining quiet on the controlled clean-language classes.



That claim is supported by the current results.


---

What this sandbox does not support

The following claims remain unjustified:

OMNIABASE is production-ready

OMNIABASE should replace strong handcrafted gates

OMNIABASE provides a rejection criterion

OMNIABASE proves hidden semantic inconsistency

OMNIABASE guarantees reduced user-facing failure

OMNIABASE outperforms stronger baselines in general


Those would still be premature or false.


---

Structural interpretation

This sandbox reveals three practical zones.

Zone A — shared obvious cases

Both systems agree on:

brittle numeric

loop-like

clean numeric

clean explanations

natural mixed


This is the stable overlap region.


---

Zone B — handcrafted baseline dominance on explicit syntax

On:

pattern heavy


the stronger baseline remains more aggressive and more complete.

This confirms that explicit pattern rules remain highly effective when the failure mode is overtly syntactic.


---

Zone C — OMNIABASE incremental signal on subtle suspiciousness

On:

suspicious clean


OMNIABASE emits more warnings than the stronger baseline.

This is the most relevant result in the sandbox, because it points toward the niche where OMNIABASE may actually matter: not obvious ugliness, but subtle structural degeneration under superficially acceptable form.


---

Main strengths of the result

1. bounded incremental signal exists in the most relevant class

This is the key practical outcome.

2. no warning expansion on the clean classes in this sandbox

This is a good boundedness signal.

3. OMNIABASE remains coherent with previous numeric fragility findings

The brittle numeric class still behaves as expected.

4. the experiment narrows the real niche of OMNIABASE

This is useful because it reduces ambiguity.

The system is not strongest on obvious patterns. It may be strongest on subtle suspicious structure.


---

Main limitations

1. sandbox size remains small

The number of examples is still too small for strong statistical claims.

2. projection bridge remains a central uncertainty

For text inputs, the warning still depends on:

text -> deterministic integer projection -> OMNIABASE lens

This means some of the observed signal may still be projection-mediated rather than native text understanding.

3. no end-to-end outcome metric exists yet

This sandbox does not show improvement in:

retry success

escalation quality

user-facing failure rate

final correctness


Without that, operational value remains suggestive, not established.

4. stronger baseline is still manually designed

The comparison is informative, but still bounded by the handcrafted nature of the baseline and the chosen sandbox classes.


---

Why this result matters

This result matters because it identifies the first plausible use-case niche for OMNIABASE.

Not:

obvious loops

explicit pattern spam

trivial syntactic failures


But rather:

outputs that look acceptable on the surface

yet show structural rigidity or suspicious repetition below the threshold of obvious handcrafted detection


That is the narrowest truthful description of the current value.


---

Correct next step

The next technically correct move is not full integration.

It is one of these two:

1. enlarge the suspicious-clean set

Build a more diverse controlled set of outputs such as:

repeated but paraphrased claims

soft looping with token variation

structurally rigid numeric-language hybrids

superficially coherent but low-diversity explanations


Goal: see whether OMNIABASE keeps adding signal in the same niche.

2. add a tiny end-to-end sandbox

Take a small batch of candidate outputs and simulate:

baseline only

baseline + OMNIABASE auxiliary warning


Then measure whether OMNIABASE changes any downstream sandbox decision in a way that looks useful.

Only that begins to test actual operational contribution.


---

Minimal conclusion

The real-output sandbox v0 shows that OMNIABASE does not outperform a stronger handcrafted baseline on obvious syntactic pattern classes, but it does add bounded extra warning signal on a more interesting class: superficially clean yet structurally suspicious outputs.

That is enough to keep going.

It is not enough to claim that the system is fully validated or ready for final gate integration.

