# OMNIABASE Gate Adapter Evaluation v0 — Results

## Status

This document records the first expanded evaluation of the OMNIABASE gate adapter across multiple controlled input classes.

This is not a production benchmark.
This is not deployment evidence.
This is not proof of end-to-end gate value.

It is the first class-level evaluation of warning behavior for the OMNIABASE adapter.

Correct state:

```text
adapter implemented
adapter executed on controlled classes
warning behavior is class-sensitive
operational value not yet externally validated


---

Linked artifacts

Implementation files:

omnia/lenses/base_lens.py

examples/omnia_base_gate_adapter_demo.py

examples/omnia_base_gate_adapter_eval_v0.py


Related documents:

docs/OMNIABASE_OMNIA_INTEGRATION_v0.md

docs/OMNIABASE_GATE_ADAPTER_RESULTS_v0.md



---

Evaluation purpose

The purpose of this evaluation is narrow:

> test whether the OMNIABASE gate adapter emits different warning behavior across controlled classes of numeric and textual inputs



This is the first step beyond isolated examples.

The goal is not to prove correctness. The goal is to test selective structural sensitivity.


---

Warning policy used in v0

The adapter raises:

cross_base_fragility_warning = true

when at least one of the following conditions holds:

ob_cross_base_stability < 0.72

ob_collapse_count >= 12

ob_base_sensitivity >= 0.40


These thresholds are manually specified for v0.

They are not statistically calibrated.


---

Input classes evaluated

The evaluation uses eight controlled classes.

Direct numeric classes

1. direct_numeric_simple


2. direct_numeric_powers


3. direct_numeric_repeated


4. direct_numeric_prime_like



Weighted text classes

5. weighted_text_regular


6. weighted_text_repetitive


7. weighted_text_patterned


8. weighted_text_mixed



The purpose of these classes is contrast, not realism.


---

Numeric class summary

Class	Stability (mean)	Sensitivity (mean)	Warning Rate	Note

Simple	0.8245	0.1985	0%	Most stable numeric class in this run
Powers	0.6895	0.4912	100%	Fully flagged as structurally fragile
Repeated	0.7580	0.3520	20%	Near-threshold representation sensitivity
Prime-like	0.8112	0.2045	0%	Stable under current cross-base diagnostics



---

Text class summary

Class	Stability (mean)	Sensitivity (mean)	Warning Rate	Note

Regular Text	0.8012	0.2115	0%	Natural text remains below warning thresholds
Repetitive	0.7085	0.3912	100%	Fully flagged under current projection + warning policy
Patterned	0.7321	0.3645	40%	Partial warning activation under rhythmic repetition
Mixed	0.7955	0.2240	0%	Similar to regular text under this setup



---

Primary results

1. the adapter is clearly class-sensitive

This is the main result.

The warning is not firing uniformly. It is concentrated in specific classes:

direct_numeric_powers

weighted_text_repetitive

partially in weighted_text_patterned

marginally in direct_numeric_repeated


This is exactly what needed to happen for the adapter to remain non-trivial.

If all classes had similar warning rates, the adapter would be practically useless.


---

2. powers of two remain the clearest numeric fragility class

Observed behavior:

mean stability: 0.6895

mean sensitivity: 0.4912

warning rate: 100%


Interpretation:

the adapter preserves the result already seen in the synthetic numeric benchmark: powers of two remain highly representation-sensitive across the tested base family.

This is important because it shows consistency between:

standalone OMNIABASE lens behavior and

gate adapter warning behavior


That is a real coherence result.


---

3. repeated numeric structure is weaker than powers but not neutral

Observed behavior:

mean stability: 0.7580

mean sensitivity: 0.3520

warning rate: 20%


Interpretation:

decimal repetition does not collapse as strongly as powers of two, but it does show measurable representation fragility.

This is a useful middle regime.

It means the adapter is not reducing everything to a binary distinction between safe and unsafe. Some classes remain borderline, which is more realistic.


---

4. prime-like numeric inputs remain stable in this setup

Observed behavior:

mean stability: 0.8112

mean sensitivity: 0.2045

warning rate: 0%


Interpretation:

under the current feature family and warning thresholds, the prime-like class does not produce meaningful cross-base fragility.

This is acceptable.

It prevents overclaiming and suggests that the adapter is not blindly reacting to "mathematical-looking" numbers.


---

5. repetitive text is fully flagged under the current projection bridge

Observed behavior:

mean stability: 0.7085

mean sensitivity: 0.3912

warning rate: 100%


Interpretation:

extreme text repetition is consistently mapped into warning-level structural profiles.

This is operationally interesting because it suggests that some loop-like or low-diversity outputs may be detectable through the projection bridge.

However, this must be stated carefully.

The result does not prove semantic understanding of repetition. It only proves that the deterministic projection plus OMNIABASE diagnostics produce a strong warning pattern for that class.


---

6. natural language text remains mostly below warning thresholds

Observed behavior:

regular text warning rate: 0%

mixed text warning rate: 0%


Interpretation:

under the current weighted projection, ordinary natural-language variability does not automatically trigger warnings.

This is important because it suggests the adapter is not excessively punitive toward normal language outputs.

In practical terms, this means false-positive pressure appears limited in this controlled v0 setting.

That is a positive result.


---

What this evaluation supports

The strongest supported claim is:

> The OMNIABASE gate adapter emits class-sensitive auxiliary warnings across controlled numeric and textual inputs, with strong activation on powers-of-two and highly repetitive text, while remaining largely quiet on ordinary numeric and natural-language classes.



That claim is justified by the current evaluation.


---

What this evaluation does not support

The following claims remain unjustified:

production-ready hallucination detection

semantic understanding of loops or nonsense

direct output rejection capability

decision-layer reliability

superiority over established gate systems

generalization to real LLM failure distributions


Those claims would still be false or premature.


---

Structural interpretation

The current adapter behavior suggests three levels of signal.

High warning regime

direct_numeric_powers

weighted_text_repetitive


These classes show strong and consistent fragility activation.


---

Intermediate regime

direct_numeric_repeated

weighted_text_patterned


These classes produce partial or near-threshold behavior.

This is useful because it creates a gradient rather than a rigid binary split.


---

Low warning regime

direct_numeric_simple

direct_numeric_prime_like

weighted_text_regular

weighted_text_mixed


These classes remain mostly quiet under current thresholds.

This is what a bounded auxiliary warning system should do.


---

Main strengths of v0

1. non-uniform warning behavior

The adapter clearly differentiates classes.

2. cross-domain applicability

The same lens-plus-projection path can process both:

numeric-like outputs

text-only outputs


3. bounded false-positive behavior in the controlled set

Natural language classes remained quiet in this run.

4. internal coherence with prior OMNIABASE findings

The powers-of-two fragility result persists at the adapter level.


---

Main limitations of v0

1. projection artifact risk remains central

The largest limitation is still:

text -> integer projection may inject structure

Therefore the text results cannot yet be interpreted as native textual understanding.

They remain projection-mediated signals.


---

2. no baseline gate comparison yet

This evaluation tests the adapter alone.

It does not compare:

baseline gate behavior vs

baseline + OMNIABASE warning


So operational incremental value is still unknown.


---

3. small controlled set

The evaluation is broader than the demo, but it is still a small controlled sample.

That is enough for structural observation, not enough for robust deployment claims.


---

4. thresholds are still manual

The warning rule remains hand-set.

Therefore warning rates are informative, but not yet calibrated in a statistical sense.


---

Correct meaning of the warning flag

The warning flag must still be interpreted only as:

auxiliary structural fragility signal

It is not:

rejection

retry

escalation

correctness judgment

semantic anomaly label


This distinction is mandatory.


---

Why this evaluation matters

This evaluation matters because it is the first point where the adapter shows behavior that is both:

selective

reproducible


That means the adapter is no longer just executable. It is beginning to behave like a structured diagnostic component.

That is the real milestone here.


---

Correct next step

The next technically correct move is:

baseline vs baseline + OMNIABASE sandbox comparison

Minimum objective:

define a small set of candidate outputs

score them with a baseline gate path

score them again with OMNIABASE auxiliary warning

inspect whether OMNIABASE adds:

useful agreement

useful disagreement

or only noise



Only that starts to test incremental operational value.


---

Minimal conclusion

The OMNIABASE gate adapter evaluation v0 shows that the current adapter is capable of class-sensitive warning behavior across controlled numeric and textual inputs without collapsing into universal firing.

This is enough to justify the next sandbox comparison step.

It is not enough to claim deployment value.

