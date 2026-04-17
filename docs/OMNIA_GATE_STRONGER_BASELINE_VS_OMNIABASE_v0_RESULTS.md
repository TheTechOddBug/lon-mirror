# OMNIA Gate Sandbox — Stronger Baseline vs OMNIABASE v0 Results

## Status

This document records the second sandbox comparison between:

- a stronger handcrafted baseline
and
- the OMNIABASE auxiliary warning adapter

This is not a production benchmark.
This is not deployment evidence.
This is not proof that OMNIABASE should replace a stronger rule-based gate.

It is a controlled comparison intended to answer a narrower question than before:

> does OMNIABASE still add useful signal once the handcrafted baseline is strengthened with explicit pattern rules?

Correct state:

```text
stronger sandbox comparison executed
incremental signal reduced versus the weak baseline
behavioral difference between baseline and OMNIABASE remains visible
external operational value still not validated


---

Linked artifacts

Implementation files:

examples/omnia_gate_stronger_baseline_vs_omniabase_v0.py

examples/omnia_gate_baseline_vs_omniabase_v0.py

examples/omnia_base_gate_adapter_demo.py

omnia/lenses/base_lens.py


Related documents:

docs/OMNIA_GATE_BASELINE_VS_OMNIABASE_v0_RESULTS.md

docs/OMNIABASE_GATE_ADAPTER_EVAL_v0_RESULTS.md

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Comparison setup

Stronger baseline

The stronger baseline extends the original heuristic baseline with explicit checks for:

repeated character runs

repeated token loops

numeric powers of two

alternating short-cycle patterns

repeated substring blocks

repeated numeric block structures


This is still a handcrafted system, but it is materially stronger than the first baseline.


---

OMNIABASE side

The OMNIABASE adapter remains unchanged.

It projects inputs into deterministic integers, runs the OMNIABASE lens, and emits:

cross_base_fragility_warning

when at least one of the following holds:

ob_cross_base_stability < 0.72

ob_collapse_count >= 12

ob_base_sensitivity >= 0.40


This remains an auxiliary warning only.

It is not a rejection decision.


---

Summary table

Dataset Class	Stronger Baseline Warn	OMNIABASE Warn	OMNIABASE Only Rate	Agreement

Simple Numeric	0%	0%	0%	100%
Power Numeric	100%	100%	0%	100%
Repeated Numeric	100%	20%	0%	20%
Repetitive Text	100%	100%	0%	100%
Token Loop Text	100%	100%	0%	100%
Patterned Text	100%	40%	0%	40%
Mixed Text	0%	0%	0%	100%



---

Primary result

The main result is this:

the incremental advantage seen against the weak baseline mostly disappears against the stronger baseline

This matters.

Against the first shallow baseline, OMNIABASE showed non-redundant warning behavior on some classes.

Against the stronger handcrafted baseline, that advantage is largely absorbed by explicit rules.

So the correct conclusion is not that OMNIABASE wins. The correct conclusion is:

OMNIABASE captures a different warning logic

but a stronger procedural baseline can recover much of the previously observed gap


That is the true result.


---

Where the stronger baseline absorbs OMNIABASE's previous edge

1. repeated numeric class

Observed behavior:

stronger baseline warning rate: 100%

OMNIABASE warning rate: 20%

OMNIABASE-only rate: 0%

agreement: 20%


Interpretation:

the stronger baseline now catches repeated numeric structures directly through explicit numeric repetition rules.

OMNIABASE no longer provides incremental warning advantage on this class.

This is a genuine reduction in relative value versus the earlier sandbox.


---

2. patterned text class

Observed behavior:

stronger baseline warning rate: 100%

OMNIABASE warning rate: 40%

OMNIABASE-only rate: 0%

agreement: 40%


Interpretation:

the stronger baseline now captures short-cycle and repeated-block patterns explicitly.

This removes the main OMNIABASE-only effect previously seen on patterned text.

Again, this is a real erosion of incremental advantage.


---

Where OMNIABASE still behaves differently

1. OMNIABASE is more conservative on some pattern classes

The strongest contrast is now not additional coverage, but selective restraint.

For example:

stronger baseline flags all patterned_text

OMNIABASE flags only 40%


and:

stronger baseline flags all repeated_numeric

OMNIABASE flags only 20%


Interpretation:

the stronger baseline reacts to explicit form. OMNIABASE reacts only when the projected structure crosses its cross-base fragility thresholds.

This means the two systems are no longer differing mainly by coverage. They are differing by warning philosophy.

That is the important shift.


---

Where both systems still agree

1. simple numeric class

stronger baseline: 0%

OMNIABASE: 0%

agreement: 100%


2. power numeric class

stronger baseline: 100%

OMNIABASE: 100%

agreement: 100%


3. repetitive text class

stronger baseline: 100%

OMNIABASE: 100%

agreement: 100%


4. token loop text class

stronger baseline: 100%

OMNIABASE: 100%

agreement: 100%


5. mixed text class

stronger baseline: 0%

OMNIABASE: 0%

agreement: 100%


Interpretation:

there remains a broad shared zone where both systems are aligned on obvious fragile or obvious quiet cases.

That is useful, but not enough by itself to justify OMNIABASE as a replacement.


---

What this comparison supports

The strongest justified claim is:

> Against a stronger handcrafted baseline, OMNIABASE no longer shows the same incremental warning advantage seen against the weaker baseline, but it still exhibits a distinct and more conservative warning behavior on some pattern-heavy classes.



That claim is supported by the current comparison.


---

What this comparison does not support

The following claims remain unjustified:

OMNIABASE replaces strong handcrafted heuristics

OMNIABASE reduces heuristic debt in production

OMNIABASE should directly reject outputs

OMNIABASE is ready for final gate integration

OMNIABASE is superior in raw detection coverage

OMNIABASE captures all pattern failures that regex-style rules miss


Those claims would be too strong for the evidence currently available.


---

Structural interpretation

This comparison reveals three important zones.

Zone A — shared obvious behavior

Both systems agree on:

power numeric

repetitive text

token loop text

simple numeric

mixed text


This is the stable overlap zone.


---

Zone B — stronger baseline dominates coverage

On:

repeated numeric

patterned text


the stronger baseline captures more cases than OMNIABASE.

This means explicit procedural rules are still highly effective for known pattern families.


---

Zone C — warning philosophy divergence

OMNIABASE is not simply weaker. It is more selective.

The stronger baseline flags explicit pattern presence. OMNIABASE flags only the subset that crosses its structural fragility thresholds.

This is the most important qualitative distinction in this comparison.


---

Main strengths of the result

1. honesty under pressure

This comparison is useful precisely because it reduces earlier optimism.

It shows where OMNIABASE loses ground against stronger heuristics.

That is scientifically valuable.

2. behavioral distinction remains real

Even where OMNIABASE loses coverage, it still behaves differently rather than randomly.

3. no expansion of warnings on quiet classes

mixed_text and simple_numeric remain quiet for both systems.

That preserves boundedness in this sandbox.


---

Main limitations

1. stronger baseline is still handcrafted for the test classes

This baseline was improved specifically in directions relevant to the sandbox. So this is still not a general comparison.

2. OMNIABASE text path still depends on projection

For text classes, warning behavior still passes through:

text -> deterministic integer projection -> OMNIABASE lens

This remains a structural uncertainty.

3. no end-to-end utility metric yet

We still do not know whether OMNIABASE improves:

retry success

escalation quality

downstream correctness

real LLM failure reduction


Without that, operational value remains open.

4. sandbox classes remain limited

The comparison is controlled and small. It is useful for structure, not for broad deployment claims.


---

Why this result matters

This result matters because it answers a harder objection than the previous sandbox:

> what happens when the baseline is no longer naive?



Current answer:

a stronger baseline can recover most of the incremental warning advantage previously shown by OMNIABASE on these controlled pattern classes.

That is a real constraint. It narrows the argument.

But it also reveals something else:

OMNIABASE is not merely duplicating handcrafted rules. It is applying a stricter structural criterion and therefore warning less aggressively on some explicitly patterned classes.

That may become useful later, but it is not yet a proven advantage.


---

Correct next step

The next technically correct move is not "final integration".

It is one of these two:

1. real-output sandbox

Collect a small set of actual model outputs, including:

clean answers

loop-like outputs

patterned but acceptable outputs

brittle numeric outputs

superficially acceptable but suspicious outputs


Then compare:

stronger baseline

stronger baseline + OMNIABASE


This is the right next stress test.

2. calibration study

Tune OMNIABASE thresholds and inspect whether it can recover more useful coverage without exploding warnings on quiet classes.

Only after that does it make sense to talk about deeper integration.


---

Minimal conclusion

The stronger-baseline sandbox shows that OMNIABASE does not currently outperform a strengthened handcrafted detector in raw coverage on the tested pattern classes.

Its earlier incremental edge largely disappears once the baseline is upgraded.

However, OMNIABASE still expresses a distinct, more selective warning logic based on cross-base fragility rather than explicit pattern matching.

That is enough to continue testing.

It is not enough to justify final gate integration.

