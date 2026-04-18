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

Two minimal executable cases

Case 1 - suspicious-clean output

INPUT: The answer seems correct. The answer seems correct. The answer seems correct.
BASELINE: no warning
OMNIA: review
ACTION: review

Case 2 - obvious failure

INPUT: retry retry retry retry retry
BASELINE: warning
OMNIA: review
ACTION: retry

These two cases expose the current bounded policy split:

suspicious-clean case -> review

obvious failure case -> retry



---

Damage-proxy results

V0

N_EXAMPLES: 12
BASELINE_FALSE_ACCEPTS: 4
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 4
EXTRA_REVIEWS_FROM_OMNIA: 4

V1

N_EXAMPLES: 20
BASELINE_FALSE_ACCEPTS: 6
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 6
EXTRA_REVIEWS_FROM_OMNIA: 6

REALISH V0

N_EXAMPLES: 15
BASELINE_FALSE_ACCEPTS: 5
COMBINED_FALSE_ACCEPTS: 0
FALSE_ACCEPT_REDUCTION: 5
EXTRA_REVIEWS_FROM_OMNIA: 5

This is the first bounded proxy linking OMNIA to a realistic operational cost pattern:

false accept reduction under a layered policy


---

One policy

if baseline warns:
    retry
elif OMNIA warns:
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


2. docs/RUN_OMNIA_NOW_RESULT.md


3. docs/RUN_OMNIA_NOW_SECOND_RESULT.md


4. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v0_RESULTS.md


5. docs/OMNIA_SUPPORT_FALSE_ACCEPT_MINISET_v1_RESULTS.md


6. docs/OMNIA_SUPPORT_FALSE_ACCEPT_REALISH_v0_RESULTS.md


7. docs/PROOF_CARD.md


8. docs/EXTERNAL_STATUS.md




---

One-line summary

OMNIA currently supports a bounded auxiliary review role for suspicious-clean outputs, not a universal gate claim.
