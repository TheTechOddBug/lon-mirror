# OMNIA SUPPORT FALSE ACCEPT MINISET V1 - Results

## Purpose

This file records the second bounded proxy test connecting OMNIA to a realistic operational damage pattern:

```text
false accept

The goal is not to claim real-world deployment performance.

The goal is to test whether OMNIA can reduce false accepts on suspicious-clean outputs in a larger and slightly more credible support-style set.


---

Setup

The miniset contains 20 short support-style outputs divided into three groups:

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

N_EXAMPLES: 20
BASELINE_FALSE_ACCEPTS: 6
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 6
EXTRA_REVIEWS_FROM_OMNIA: 6
BASELINE_CORRECT: 14
COMBINED_CORRECT: 20


---

Minimal interpretation

On this 20-example support-style set:

the baseline alone produced 6 false accepts

the combined policy reduced false accepts to 0

this came at the cost of 6 additional review flags

the combined policy matched the target label on all 20 examples in this bounded test


This is a stronger bounded proxy than v0 because the set is larger and the acceptable examples are more varied.


---

What the result shows

This result supports a narrow claim:

> On this 20-example support-style miniset, OMNIA reduced false accepts on suspicious-clean outputs, at the cost of additional review flags.



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

One obvious-failure case behaved like this:

BASELINE_ACTION: retry
OMNIA: accept
COMBINED_ACTION: retry

This is not a contradiction.

It confirms the intended hierarchy:

obvious failures are still handled by the baseline

OMNIA is not required to replace that layer

the combined policy remains coherent



---

Comparison with v0

Compared with v0:

the set is larger

the acceptable group is more varied

the same structural pattern remains visible

false accepts still drop from a positive baseline count to zero under the combined policy


This makes the damage-proxy signal more credible than the initial version.


---

Current bounded takeaway

The main takeaway is:

OMNIA can be evaluated against a realistic damage proxy:
false accept reduction under a layered policy.

The v1 result strengthens that statement without expanding it into a universal claim.