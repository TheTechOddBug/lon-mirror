# OMNIA LLM SUPPORT SET V0 - Results

## Purpose

This file records a bounded proxy test on a small LLM-generated support-style set.

The goal is not to claim real-world deployment performance.

The goal is to test whether OMNIA can reduce false accepts under a layered policy on short support-like outputs.

---

## Setup

The set contains 15 LLM-generated support-style outputs labeled as:

- `accept`
- `review`
- `retry`

The comparison is:

- baseline only
- baseline + OMNIA

Where the combined policy is:

```python
if baseline warns:
    retry
elif OMNIA warns:
    review
else:
    accept


---

Summary

N_EXAMPLES: 15
BASELINE_FALSE_ACCEPTS: 8
COMBINED_FALSE_ACCEPTS: 1
FALSE_ACCEPT_REDUCTION: 7
EXTRA_REVIEWS_FROM_OMNIA: 7
BASELINE_CORRECT: 7
COMBINED_CORRECT: 11


---

Minimal interpretation

On this 15-example LLM support-style set:

the baseline alone produced 8 false accepts

the combined policy reduced false accepts to 1

this came at the cost of 7 additional review flags

the combined policy improved raw correctness from 7/15 to 11/15


This is a stronger bounded signal than a perfect toy result, because one review-worthy case still passes through the combined policy.


---

What the result shows

This result supports a narrow claim:

> On this 15-example LLM support-style set, OMNIA substantially reduced false accepts under a layered policy, at the cost of additional review flags.



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

One review-worthy case still passed through the combined policy.

That failure matters.

It shows that the current OMNIA signal is stronger on repetition and rigidity than on polite but vague low-action replies without overt structural repetition.

So the current result is useful, but not complete.


---

Current bounded takeaway

The main takeaway is:

OMNIA reduced false accepts from 8 to 1 on this small LLM support-style set, at the cost of 7 additional review flags.

That is a meaningful bounded result and a more credible external anchor than a perfect synthetic pass.