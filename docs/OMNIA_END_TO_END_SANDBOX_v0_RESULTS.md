# OMNIA End-to-End Sandbox v0 — Results

## Status

This document records the first end-to-end sandbox evaluation of a combined gate policy using:

- a stronger handcrafted baseline
- the OMNIABASE auxiliary warning adapter
- a three-state sandbox decision policy:
  - `accept`
  - `review`
  - `retry`

This is not a production benchmark.
This is not deployment evidence.
This is not proof of general superiority.

It is the first bounded end-to-end sandbox showing that OMNIABASE can improve policy behavior in a controlled setting without overriding baseline safety decisions.

Correct state:

```text
end-to-end sandbox executed
combined policy improved over baseline in this sandbox
no degradation observed in this sandbox
external validity still unproven


---

Linked artifacts

Implementation files:

examples/omnia_end_to_end_sandbox_v0.py

examples/omnia_real_output_sandbox_v0.py

examples/omnia_gate_stronger_baseline_vs_omniabase_v0.py

examples/omnia_base_gate_adapter_demo.py

omnia/lenses/base_lens.py


Related documents:

docs/OMNIA_REAL_OUTPUT_SANDBOX_v0_RESULTS.md

docs/OMNIA_GATE_STRONGER_BASELINE_VS_OMNIABASE_v0_RESULTS.md

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md



---

Sandbox purpose

The purpose of this sandbox is narrow:

> test whether OMNIABASE can improve a baseline gate policy by contributing an auxiliary review state on cases that the baseline would otherwise accept



This is the first step from:

warning comparison


to:

decision-policy comparison


That distinction matters.


---

Policy setup

Baseline policy

The baseline policy is intentionally simple:

if stronger baseline warns -> retry

else -> accept


So baseline has only two states:

accept / retry


---

Combined policy

The combined policy preserves baseline authority and adds one intermediate state:

if stronger baseline warns -> retry

else if OMNIABASE warns -> review

else -> accept


So the combined policy becomes:

accept / review / retry

This is the key design choice.

OMNIABASE does not override baseline retry decisions. It only adds caution where baseline remains silent.

That is architecturally correct.


---

Global metrics

Metric	Value	Note

Baseline Correct Rate	0.8125	Baseline misses some suspicious-clean cases
Combined Correct Rate	1.0000	Perfect match on the current sandbox labels
Combined Better Than Baseline	0.1875	Combined policy improves on baseline in part of the set
Combined Worse Than Baseline	0.0000	No degradation observed in the current sandbox



---

Primary result

The main result is this:

in the current sandbox, the combined policy outperforms the baseline policy

This is the first point where OMNIABASE stops being only a diagnostic curiosity and starts affecting downstream decisions in a useful way.

Important boundary:

this is true in the current sandbox. It is not yet a claim about real deployment performance.


---

Why the result improves

The gain does not come from replacing the baseline.

It comes from inserting a third state:

review

That state absorbs cases that are:

not bad enough for baseline retry

but suspicious enough for OMNIABASE warning


This is the right role for OMNIABASE at the current maturity level.

Not hard rejection. Not independent gate control. Auxiliary escalation to review.


---

Class-level interpretation

1. Clean Numeric

Behavior:

baseline: correct

combined: correct


Interpretation:

OMNIABASE does not interfere with ordinary clean numeric answers in this sandbox.

This is good. It preserves low-friction acceptance on normal cases.


---

2. Brittle Numeric

Behavior:

baseline: retry

combined: retry


Interpretation:

the baseline already catches these cases and the combined policy preserves that behavior.

This confirms that OMNIABASE is not weakening obvious safety behavior.


---

3. Clean Explanations

Behavior:

baseline: accept

combined: accept


Interpretation:

clean explanatory text remains untouched.

This is important because it suggests OMNIABASE is not adding unnecessary caution on healthy explanatory outputs in this sandbox.


---

4. Loop-like

Behavior:

baseline: retry

combined: retry


Interpretation:

obvious repetitive failure remains correctly handled by the baseline, and the combined system preserves that handling.

Again, OMNIABASE does not need to dominate this zone.


---

5. Pattern Heavy

Behavior:

baseline: typically stronger than OMNIABASE on these cases

combined: no advantage over baseline required


Interpretation:

explicit syntactic patterns remain a strong territory for handcrafted rules.

This is consistent with earlier sandbox findings.

OMNIABASE is not the best tool for obvious explicit pattern spam.


---

6. Suspicious Clean

This is the most important class.

Behavior:

baseline alone would accept some of these cases incorrectly

combined policy moves them to review


Interpretation:

this is exactly where OMNIABASE adds value in the current sandbox.

These outputs are not overtly broken. They are superficially acceptable, but structurally suspicious.

The combined policy improves because OMNIABASE contributes caution without forcing a full retry.

This is the first real operational niche identified for the system.


---

7. Natural Mixed

Behavior:

baseline: accept

combined: accept


Interpretation:

normal mixed natural-language outputs remain accepted under both policies.

This matters because the combined policy does not appear to degrade user experience on the controlled clean classes in this sandbox.

Important boundary: this is not proof of generally low false positives. It is only a positive sandbox result.


---

What the numbers actually mean

Baseline Correct Rate = 0.8125

This means the stronger baseline alone gets most sandbox labels right, but not all.

Its failure mode is concentrated in the suspicious-clean region.


---

Combined Correct Rate = 1.0000

This means the combined policy matches all expected labels in the current sandbox.

This is a strong sandbox result.

But it must be interpreted correctly:

small sample

hand-labeled sandbox

labels designed around the three-state policy


So this is best described as:

perfect fit on the current sandbox

not as general proof of perfect policy.


---

Combined Better Than Baseline = 0.1875

This means the combined policy improved over the baseline on 18.75% of the current examples.

That is a real gain.

It is also very interpretable: the gain comes from cases where review is a better action than premature accept.


---

Combined Worse Than Baseline = 0.0000

This means the combined policy did not make any baseline-correct example worse in the current sandbox.

This is highly encouraging.

But again, the correct wording is:

no degradation observed in this sandbox


not:

impossible to degrade or

guaranteed safe everywhere



---

What this sandbox supports

The strongest justified claim is:

> In the current end-to-end sandbox, adding OMNIABASE as an auxiliary review signal improves the baseline decision policy by catching some suspicious-clean cases that the baseline alone would accept, without degrading correct baseline decisions on the tested set.



That claim is supported.


---

What this sandbox does not support

The following claims remain unjustified:

OMNIABASE is production-ready

OMNIABASE guarantees safer real deployments

the combined policy is universally superior

OMNIABASE should directly reject outputs

the observed gain will generalize unchanged to real traffic

the current sandbox proves full gate superiority


Those would still be too strong.


---

Structural interpretation

This sandbox finally clarifies the practical role of OMNIABASE.

Not its role

OMNIABASE is not best positioned as:

explicit pattern detector

handcrafted rule replacement

dominant retry trigger


Plausible role

OMNIABASE is plausibly useful as:

auxiliary structural warning

subtle suspiciousness detector

review escalator between accept and retry


That is the cleanest interpretation of the current evidence.


---

Main strengths of the result

1. first decision-level gain

This is the most important milestone so far.

The gain is no longer just about warnings. It now affects policy outcome.

2. gain comes from a realistic architectural choice

Using review as the OMNIABASE action is much more coherent than forcing direct retries.

3. no degradation observed on the sandbox set

This is a strong bounded result.

4. role clarity improved

The experiments now show where OMNIABASE likely belongs in a system.

That is valuable even before large-scale validation.


---

Main limitations

1. small, hand-curated sandbox

The dataset is still tiny and manually designed. So the result is useful, but fragile.

2. expected labels are sandbox labels

The labels are not ground truth from production or human annotation at scale. They are policy-level targets for a controlled experiment.

3. projection bridge remains active

For text cases, OMNIABASE still depends on:

text -> deterministic integer projection -> OMNIABASE lens

That remains an unresolved structural limitation.

4. no downstream business metric yet

We still have not measured:

fewer bad outputs shown to users

better retry efficiency

better escalation triage

lower operational cost


Without that, this remains policy evidence, not deployment evidence.


---

Why this result matters

This result matters because it finally answers the most important question asked so far:

> can OMNIABASE improve a gate policy without needing to replace the baseline?



Current answer:

yes, in this sandbox, by acting as an auxiliary review signal on suspicious-clean outputs.

That is a much stronger and more useful answer than any earlier purely diagnostic result.


---

Correct next step

The next technically correct move is not broad celebration.

It is one of these:

1. enlarge the suspicious-clean class

This is the most important immediate test.

Need more examples of:

lightly repeated but paraphrased outputs

rigid answer templates

subtle self-repetition

suspicious numeric-language hybrids

low-diversity “looks fine” outputs


Goal: see whether the review gain persists.

2. small human-rated sandbox

Have a small external or manual labeling pass with the same three labels:

accept

review

retry


Then compare baseline vs combined again.

That would be much stronger than self-authored sandbox labels.

3. threshold calibration sweep

Test whether OMNIABASE thresholds can be adjusted to preserve the gain while avoiding over-warning.

This is necessary before any deeper integration.


---

Minimal conclusion

The end-to-end sandbox v0 shows that OMNIABASE can improve a stronger baseline policy in a controlled setting when used in the correct role:

not as a replacement gate, not as a rejection engine, but as an auxiliary review trigger for superficially clean yet structurally suspicious outputs.

That is the first genuinely operational result of the current phase.

It is enough to continue.

It is not enough to claim production readiness.

