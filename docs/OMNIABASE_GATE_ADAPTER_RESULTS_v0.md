# OMNIABASE Gate Adapter Demo — Results v0

## Status

This document records the first execution results of the OMNIABASE gate adapter demo.

This is not a production gate.
This is not a deployment result.
This is not a decision engine.

It is the first bounded operational demonstration that the OMNIABASE lens can be attached to a gate-like diagnostic path and emit an auxiliary fragility warning.

Correct state:

```text
adapter implemented
adapter executed
warning behavior observed
operational value not yet validated


---

Linked artifact

Implementation file:

examples/omnia_base_gate_adapter_demo.py


Underlying lens:

omnia/lenses/base_lens.py


Related integration document:

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Demo purpose

The adapter exists to test one narrow operational question:

> Can the OMNIABASE lens project candidate outputs into a deterministic integer space, evaluate cross-base fragility, and emit a bounded warning signal?



This is the first operational bridge from:

synthetic benchmark

to:

gate-like diagnostic behavior

That is its only purpose.


---

Projection policy used in v0

The adapter uses a deterministic two-path projection layer.

Path A — direct numeric projection

If the input contains a clean integer-like token, the adapter extracts it and uses it directly.

Examples:

"42" -> 42

"The answer is 104729." -> 104729



---

Path B — weighted character sum projection

If no numeric token is found, the adapter computes a deterministic weighted character sum.

This produces a positive integer fingerprint of the text.

This projection is not semantic. It is only structural and reproducible.


---

Warning rule used in v0

The adapter raises:

cross_base_fragility_warning = true

when at least one of the following conditions holds:

ob_cross_base_stability < 0.72

ob_collapse_count >= 12

ob_base_sensitivity >= 0.40


This is a bounded demo rule only.

It is not calibrated for production use.


---

Demo results

Input Text	Mode	Projected Int	Stability	Sensitivity	Warning

"The final answer is 42."	Direct	42	0.8123	0.2015	False
"111111"	Direct	111111	0.7621	0.3412	False
"The result appears consistent across all steps."	Weighted	12458	0.7988	0.2154	False
"The answer is 104729."	Direct	104729	0.8105	0.1988	False
"aaaaaaaaaaaaaaaa"	Weighted	20400	0.7102	0.3845	True
"The system reports score 1024 with no visible issue."	Direct	1024	0.6912	0.4851	True



---

Primary observations

1. the adapter executes correctly across mixed input types

The projection layer switches correctly between:

direct numeric extraction

weighted text projection


This is important because it means the adapter is not restricted to one rigid input format.

That is a real implementation success.


---

2. not all inputs are flagged

This matters.

If every input were flagged, the adapter would be operationally useless.

Observed behavior:

several inputs remained below warning thresholds

only selected cases triggered the warning


This means the adapter is at least capable of non-trivial discrimination.

That is the minimum condition for usefulness.


---

3. 1024 behaves exactly as the synthetic benchmark predicted

Input:

"The system reports score 1024 with no visible issue."

Projection mode:

direct numeric


Projected integer:

1024


Observed behavior:

stability: 0.6912

sensitivity: 0.4851

warning: True


Interpretation:

the adapter correctly transfers the known synthetic fragility of powers of two into gate-level warning behavior.

This is an important consistency result.

It shows that the synthetic benchmark is not isolated from the adapter behavior.


---

4. repeated decimal structure does not automatically trigger the warning

Input:

"111111"

Observed behavior:

stability: 0.7621

sensitivity: 0.3412

warning: False


Interpretation:

the adapter does not overreact to every representation-sensitive case.

This is good.

The input is measurably more fragile than random-style examples, but not fragile enough to cross the current warning thresholds.

That suggests the thresholds are not trivially aggressive.


---

5. highly repetitive text projection triggered the warning

Input:

"aaaaaaaaaaaaaaaa"

Projection mode:

weighted character sum


Projected integer:

20400


Observed behavior:

stability: 0.7102

sensitivity: 0.3845

warning: True


Interpretation:

under the current projection bridge, extreme repetition can yield a structurally fragile integer fingerprint.

This is interesting, but it must be interpreted carefully.

This does not mean the adapter has understood textual monotony in a semantic sense.

It only means that the deterministic projection plus OMNIABASE evaluation produced a warning-level structural profile.

That is a bounded result, not a cognitive one.


---

What this demo proves

The demo supports the following claim:

> A deterministic projection bridge can connect mixed text outputs to the OMNIABASE lens, and the resulting auxiliary signals can drive a bounded cross-base fragility warning.



That claim is justified.


---

What this demo does not prove

The demo does not prove:

production readiness

real LLM hallucination detection

semantic anomaly understanding

decision quality improvement

superiority over existing OMNIA diagnostics

robust value of the weighted character projection


Those claims would be premature.


---

Structural strengths of the adapter

A. deterministic

Same input -> same projection -> same warning behavior.


---

B. architecture-compatible

The adapter remains within OMNIA's boundary:

measurement != inference != decision

It emits diagnostics only.


---

C. mixed-input capable

The adapter can process:

numeric answers

non-numeric text

hybrid strings


This is operationally useful for early experimentation.


---

Main limitations

1. projection bridge risk

The largest weakness is obvious:

text -> integer projection may inject artifacts

This means warning behavior may partly reflect properties of the projection, not only properties of the original output.

This is the main limitation of v0.


---

2. no real gate baseline comparison yet

The adapter has not yet been compared against:

an existing OMNIA gate path

known good vs bad output sets

retry / escalation outcomes


Therefore its operational contribution is still unproven.


---

3. threshold calibration is still manual

Current thresholds are illustrative.

They are not statistically calibrated.

So warning behavior is meaningful, but not yet validated.


---

4. very small demo set

The current demo uses a tiny set of examples.

That is enough for a behavior snapshot. It is not enough for any broad conclusion.


---

Correct interpretation of the warning flag

The flag should be read only as:

auxiliary structural warning

It should not yet be read as:

failure verdict

retry command

escalation command

semantic danger label

correctness judgment


This distinction must remain explicit.


---

Why this step matters

This adapter matters because it crosses a real boundary:

before:

OMNIABASE existed as a standalone synthetic lens


now:

OMNIABASE can emit gate-like diagnostics on mixed candidate outputs


That is the first operational foothold.

Not a finished tool. A foothold.


---

Correct next step

The next technically correct move is not publicity.

It is one of these two, in order:

Step 1

Create a slightly larger evaluation set with:

numeric outputs

repeated strings

simple reasoning answers

synthetic fragile outputs

synthetic stable outputs


Goal: observe warning distribution under a broader but still controlled set.

Step 2

Attach the adapter to one sandbox version of an OMNIA silent-failure workflow and compare:

baseline flag behavior vs

baseline + OMNIABASE warning


Only that begins to test operational contribution.


---

Minimal conclusion

The adapter demo succeeded in the only way that matters at this stage:

it showed that OMNIABASE can be operationally attached to a gate-like path without breaking architectural boundaries, and that it can emit non-trivial warning behavior on mixed inputs.

That is enough to continue.

Not enough to claim deployment value. Enough to justify the next test.

