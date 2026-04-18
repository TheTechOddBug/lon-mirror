# OMNIA - Proof Card

## One sentence

OMNIA measures when an output still looks acceptable on the surface but is already structurally fragile.

---

## What it is

OMNIA is a post-hoc structural measurement engine.

It does not interpret semantics.  
It does not replace reasoning.  
It does not make final decisions.

Its role is narrower:

**measure whether structure remains stable under controlled transformation**

Core principle:

```text
structural truth = invariance under transformation

Architectural boundary:

measurement != inference != decision


---

What the current evidence supports

The strongest technically honest claim is:

> OMNIABASE currently works as an auxiliary review sensor for suspicious-clean outputs.



That means outputs that:

still look readable

are not obviously broken

may still pass a shallow gate

but show rigidity, soft repetition, low diversity, or suspicious structural regularity


This is the current supported role.

Not more.


---

What this does in practice

The best current use is a layered policy:

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept

Interpretation:

strong handcrafted baselines handle obvious failures

OMNIABASE adds caution on subtler suspicious-clean cases

final decision remains external



---

Why this matters

Many outputs fail in a quiet way.

They are not visibly collapsed.
They are not obvious garbage.
They may still look acceptable.

But structurally they are already weak.

OMNIA is meant to detect that hidden weakness before it is mistaken for stability.


---

What OMNIA is not claiming

OMNIA and OMNIABASE are not currently claimed as:

a production-ready universal gate

a replacement for strong handcrafted baselines

a semantic truth engine

a correctness oracle

a final decision system


Those claims would exceed the evidence.


---

Shortest proof path

Read these in order:

1. docs/OMNIABASE_REVIEW_SENSOR_NOTE.md


2. docs/PHASE6_FREEZE.md


3. docs/OMNIA_END_TO_END_SANDBOX_v0_RESULTS.md


4. docs/OMNIA_SUSPICIOUS_CLEAN_EXPANSION_v0_RESULTS.md




---

Minimal examples

Example 1 - obvious failure

retry retry retry retry retry

A strong baseline should already catch this.

Example 2 - suspicious-clean output

The answer seems correct. The answer seems correct. The answer seems correct.

This may still pass shallow checks, but it is structurally suspicious enough to justify review.

Example 3 - near-threshold pattern

12121213

This can trigger caution even when a human might still accept it.

That is why OMNIABASE should currently remain a review sensor, not a rejection engine.


---

Current limitation

The current text-facing bridge still depends on:

text -> deterministic integer projection -> OMNIABASE lens

So the current role is useful, bounded, and credible, but not final.


---

Final compressed statement

OMNIA did not prove a universal gate.

It did something narrower and more honest:

it reduced a broad idea to a testable auxiliary review role with bounded evidence.

