# OMNIA SUPPORT FALSE ACCEPT REALISH V0 - Results

## Purpose

This file records the first more realistic bounded proxy test connecting OMNIA to an operational damage pattern:

```text
false accept

The goal is not to claim real-world deployment performance.

The goal is to test whether OMNIA can reduce false accepts on suspicious-clean support-style outputs that are less synthetic than the earlier minisets.


---

Setup

The set contains 15 short support-style outputs divided into three groups:

obvious_failure

suspicious_clean

acceptable


Each example has a target label:

retry

review

accept


The comparison is:

baseline only

baseline + OMNIA


Where the combined policy is:

if baseline warns:
    retry
elif OMNIA warns:
    review
else:
    accept


---

Summary

N_EXAMPLES: 15
BASELINE_FALSE_ACCEPTS: 5
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 5
EXTRA_REVIEWS_FROM_OMNIA: 5
BASELINE_CORRECT: 10
COMBINED_CORRECT: 15


---

Minimal interpretation

On this 15-example realish support-style set:

the baseline alone produced 5 false accepts

the combined policy reduced false accepts to 0

this came at the cost of 5 additional review flags

the combined policy matched the target label on all 15 examples in this bounded test


This is a stronger proxy than the earlier synthetic-style minisets because the acceptable cases are written more like plausible support replies.


---

What the result shows

This result supports a narrow claim:

> On this 15-example realish support-style set, OMNIA reduced false accepts on suspicious-clean outputs, at the cost of additional review flags.



This remains consistent with the current OMNIA role:

baseline handles obvious failures

OMNIA adds bounded review signal on suspicious-clean outputs

final decision policy remains layered



---

What the result does not show

This result does not show that OMNIA is:

a universal gate

deployment-validated at scale

stronger than all baselines in general

a semantic truth engine

a correctness oracle


It is a bounded proxy test only.


---

Important detail

The obvious-failure cases still preserve the intended hierarchy.

One case behaved like this:

BASELINE_ACTION: retry
OMNIA: accept
COMBINED_ACTION: retry

This is not a contradiction.

It confirms the architecture:

obvious failures are still handled by the baseline

OMNIA is not required to replace that layer

the combined policy remains coherent



---

Comparison with earlier proxy sets

Compared with the earlier v0 and v1 support-style minisets:

the examples are less synthetic

the acceptable replies are more operationally plausible

the same structural pattern remains visible

false accepts still drop from a positive baseline count to zero under the combined policy


This makes the damage-proxy signal harder to dismiss as a purely toy formatting effect.


---

Current bounded takeaway

The main takeaway is:

OMNIA can be evaluated against a realistic damage proxy:
false accept reduction under a layered policy.

The realish-v0 result strengthens that statement without expanding it into a universal claim.