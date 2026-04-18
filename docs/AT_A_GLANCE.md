# OMNIA - At a Glance

## What it is

OMNIA is a post-hoc structural measurement engine.

It measures whether an output remains structurally stable under controlled transformation.

Core principle:

```text
structural truth = invariance under transformation

Architectural boundary:

measurement != inference != decision


---

What it is not

OMNIA is not:

a semantic truth engine

a correctness oracle

a production-ready universal gate

a replacement for strong handcrafted baselines

a final decision system



---

Strongest current claim

The strongest technically honest claim is:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.



Anything stronger is premature.


---

One example

Readable is not the same as structurally safe.

Example:

The answer seems correct. The answer seems correct. The answer seems correct.

This is readable and superficially acceptable.

But it is also structurally suspicious enough to justify review.

That is the regime where OMNIABASE currently adds value.


---

One policy

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept

Interpretation:

baseline handles obvious failures

OMNIABASE adds caution on suspicious-clean cases

decision remains external



---

Current limit

The current system is useful, bounded, and technically honest.

But it is still limited by:

sandbox-heavy evidence

limited independent human validation

no real deployment evidence yet

open threshold calibration

current text bridge via deterministic integer projection


So the current role is real, but narrow.


---

Best entry path

For the shortest correct reading path:

1. docs/AT_A_GLANCE.md


2. docs/PROOF_CARD.md


3. docs/ONE_EXAMPLE.md


4. docs/EXTERNAL_STATUS.md




---

One-line summary

OMNIA currently supports a bounded auxiliary review role for suspicious-clean outputs, not a universal gate claim.