# START_HERE

If this is your first time here, do not start from the full architecture.

Start from one bounded claim:

> OMNIA includes a credible OMNIABASE-based auxiliary review sensor for suspicious-clean outputs, supported by sandbox and human-rated sandbox evidence.

This means outputs that:

- still look readable
- are not obviously broken
- may still pass shallow checks
- still show structural suspiciousness

That is the current supported role.

Not more.

---

## Fastest reading path

Read these in order:

1. `docs/AT_A_GLANCE.md`
2. `docs/PROOF_CARD.md`
3. `docs/ONE_EXAMPLE.md`
4. `docs/EXTERNAL_STATUS.md`
5. `docs/PHASE6_FREEZE.md`

This is the shortest path from first contact to the current bounded claim.

---

## What OMNIA is

OMNIA is a post-hoc structural measurement engine.

It does not replace reasoning.  
It does not interpret semantics.  
It does not make final decisions.

Its role is to measure whether structure remains stable under controlled transformation.

Core principle:

```text
structural truth = invariance under transformation

Architectural boundary:

measurement != inference != decision


---

What OMNIABASE currently does

OMNIABASE is currently best read as an auxiliary structural review sensor inside the broader OMNIA measurement architecture.

Its best-supported use is not direct rejection.

Its best-supported use is not replacement of strong handcrafted baselines.

Its current role is narrower:

baseline handles obvious failures

OMNIABASE adds caution on suspicious-clean outputs

final decision remains external


The correct policy sketch is:

if baseline warns:
    retry
elif OMNIABASE warns:
    review
else:
    accept


---

What has been shown

The repository currently shows:

bounded post-hoc structural measurement

executable sandbox experiments

a narrowed auxiliary review role

sandbox and human-rated sandbox support for that role



---

What has not been shown

The repository does not currently show that OMNIA or OMNIABASE is:

a production-ready universal gate

a replacement for strong handcrafted baselines

a semantic truth engine

a correctness oracle

a final decision system

deployment-proven at scale


Any such claim would exceed the current evidence.


---

One example

This output is readable:

The answer seems correct. The answer seems correct. The answer seems correct.

Readable does not automatically mean structurally safe.

That is the gap OMNIA is currently meant to measure.


---

If you only keep one line

OMNIA currently supports a bounded auxiliary review role for suspicious-clean outputs.