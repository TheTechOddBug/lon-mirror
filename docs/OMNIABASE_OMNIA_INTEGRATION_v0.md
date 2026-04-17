# OMNIABASE -> OMNIA Integration v0

## Status

This document defines the first integration path of the OMNIABASE lens inside OMNIA.

This is not a full production integration.
This is not a deployment claim.

It is the first bounded operational bridge from:

```text
standalone synthetic lens

to:

OMNIA diagnostic component

Correct state:

synthetic lens available
integration path defined
operational value not yet demonstrated


---

Integration principle

OMNIA remains the measurement engine.

Architectural boundary remains unchanged:

measurement != inference != decision

The OMNIABASE lens must therefore enter OMNIA only as:

a diagnostic sub-signal

a bounded structural probe

a non-semantic measurement component


It must not become:

a decision layer

a reasoning layer

a semantic interpreter

a truth oracle



---

Why integration is now justified

The synthetic benchmark already established three things:

1. the lens is implemented


2. the corrected base_sensitivity is usable


3. some controlled classes are structurally separable



This does not prove external usefulness.

But it is enough to justify a first bounded integration test.

Without this step, the lens remains isolated. With this step, the lens begins to test whether it adds value inside OMNIA.


---

Best first integration target

Recommended target

Silent Failure Gate

Reason:

already post-hoc

already diagnostic

already aligned with OMNIA boundaries

easiest place to test whether cross-base fragility adds useful signal


This is the lowest-risk and highest-coherence entry point.


---

Operational goal

The first integration does not try to prove broad superiority.

It tries to answer one narrow question:

> Can cross-base fragility add a useful warning signal when an output looks superficially acceptable but may still be structurally weak?



This is the correct first question.


---

Minimal integration model

Input

A candidate output already under OMNIA inspection.

Additional OMNIABASE step

Extract one or more integer-like structural projections from the candidate.

Then run the OMNIABASE lens on those projections.

Output

Emit auxiliary signals such as:

ob_cross_base_stability

ob_representation_drift

ob_base_sensitivity

ob_collapse_count


These remain auxiliary measurements only.


---

Important constraint

The current OMNIABASE lens accepts positive integers only.

Therefore the first integration must use a bounded projection layer.

This means:

the real output is not directly fed into the lens as arbitrary text. Instead, one or more simple deterministic integer projections must be derived first.

This is a temporary bridge, not a final architecture.


---

Candidate integer projections for v0

The projection layer must remain deterministic, transparent, and non-semantic.

Recommended first candidates:

1. digit-only numeric extraction

If the inspected output already contains a numeric answer, use that number directly.

Use case:

arithmetic outputs

GSM-style answer outputs

structured numeric fields


This is the cleanest first case.


---

2. character-code sum projection

Map the output string to an integer via bounded deterministic aggregation, for example:

sum of character codes

weighted sum by position

rolling modular accumulation


This does not preserve semantics. It only creates a reproducible structural fingerprint.

Use case:

generic text outputs

fallback when no direct numeric answer exists



---

3. token-length projection

Map the output to an integer based on length or weighted token lengths.

This is weaker, but still deterministic.

Use case:

backup structural projection

comparative fragility probe



---

Recommended v0 projection policy

Use a minimal two-path policy:

Path A - direct numeric projection

If a clean numeric answer is present, use it directly.

Path B - fallback structural integer projection

If not, use a deterministic text-to-integer projection.

This is enough for the first integration experiment.


---

Minimal integration outputs

The OMNIABASE lens should emit the following names inside OMNIA:

ob_cross_base_stability

ob_representation_drift

ob_base_sensitivity

ob_collapse_count


Prefixing with ob_ is recommended to avoid ambiguity with existing OMNIA metrics.


---

How OMNIABASE should influence the gate

At v0, the lens must not make final decisions.

Correct behavior:

emit additional measurements

optionally raise a weak structural warning

contribute to flagging logic only as a bounded auxiliary signal


Incorrect behavior:

direct retry trigger by itself

direct escalation by itself

final override of existing OMNIA signals


That would be too strong for v0.


---

Minimal decision policy for v0

The safest first policy is:

Rule 1

If OMNIABASE metrics are normal, do nothing.

Rule 2

If OMNIABASE metrics are strongly fragile, attach an auxiliary warning flag such as:

cross_base_fragility_warning = true

Rule 3

Only combine this warning with existing OMNIA signals.

That preserves architectural discipline.


---

Example bounded rule

Illustrative only:

if
    ob_cross_base_stability < 0.72
    or ob_collapse_count >= 12
    or ob_base_sensitivity >= 0.40
then
    cross_base_fragility_warning = true
else
    cross_base_fragility_warning = false

This is not yet calibrated. It is only an initial bounded rule for integration testing.


---

What success looks like

The first integration counts as successful only if at least one of these happens:

A. auxiliary detection gain

OMNIABASE flags cases that looked acceptable under surface form but later appear structurally weak.

B. coherent agreement

OMNIABASE agrees with existing OMNIA fragility signals on clearly weak cases.

C. bounded disagreement with diagnostic value

OMNIABASE disagrees in a way that exposes a previously unseen representation-sensitive fragility.

This is especially interesting if it happens on superficially clean outputs.


---

What failure looks like

The integration counts as weak or failed if:

1. uniform irrelevance

OMNIABASE adds no usable variation inside the gate.

2. arbitrary noise

OMNIABASE fires warnings inconsistently without relation to observed fragility.

3. projection contamination

The text-to-integer bridge dominates behavior in arbitrary ways.

This is a serious risk and must be monitored.


---

Main limitation of v0 integration

The biggest limitation is obvious:

integer-only lens + projection bridge

This means that v0 integration is only a first test of representational sensitivity. It is not yet a full native OMNIA text lens.

That limitation must be stated clearly.


---

Why this step still matters

Even with the projection bridge, the integration matters because it tests something precise:

whether cross-base instability can contribute additional bounded signal inside a real diagnostic path.

If the answer is yes, the OMNIABASE lens earns its place inside OMNIA.

If the answer is no, the lens remains an interesting synthetic probe but not yet an operational component.

That is a clean test.


---

Recommended next implementation artifact

After this document, the next correct artifact is a minimal adapter file.

Suggested path:

examples/omnia_base_gate_adapter_demo.py

Purpose:

take simple candidate outputs

project them to integers

run OMNIABASE lens

emit prefixed OMNIA-style auxiliary signals

show warning/no-warning behavior


This should be done before touching any core gate files.

That keeps the first integration reversible and auditable.


---

Minimal conclusion

The synthetic benchmark was enough to justify one thing only:

not celebration, not large claims, but the first bounded integration test.

That is the correct next move.

