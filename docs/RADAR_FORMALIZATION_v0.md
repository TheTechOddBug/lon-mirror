# OMNIA-RADAR — Formalization v0

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  
**Status:** Offline / synthetic / non-semantic

---

## Purpose

This document defines the first formal offline version of **OMNIA-RADAR**.

OMNIA-RADAR does not measure collapse.
It does not measure truth.
It does not decide action.

Its role is narrower:

- detect whether useful structural space still remains
- estimate whether a case is still recoverable
- suppress false opportunity in already-degraded states

OMNIA-RADAR is therefore an **opportunity detector**, not a fragility detector.

---

## Position in the ecosystem

```text
Dual-Echo -> OMNIAMIND -> OMNIA -> OMNIA-RADAR -> OMNIA-LIMIT -> Decision Layer

Within this chain:

OMNIAMIND measures pre-output instability

OMNIA measures post-hoc structural stability

OMNIA-RADAR estimates residual structural opportunity

OMNIA-LIMIT defines structural stop / saturation conditions

Decision Layer remains external


OMNIA-RADAR does not replace OMNIA or OMNIAMIND. It complements them.


---

Core intuition

A case may be:

not yet clean

not yet collapsed

not yet saturated

still structurally worth continuing


OMNIA-RADAR exists to detect that middle region.

It should answer only this question:

Is there still usable structural opportunity here?

Nothing more.


---

Boundary conditions

OMNIA-RADAR must remain strictly non-semantic.

It must not measure:

meaning

usefulness in a human sense

correctness

truth

preference

narrative quality


It measures only whether structural conditions still support continued useful exploration or recovery.


---

What OMNIA-RADAR is not

OMNIA-RADAR is not:

a retry policy

a confidence score

a semantic relevance score

a truth estimator

a replacement for OMNIA-LIMIT


It is not the same as fragility.

A fragile case may still have opportunity. A stable case may have little opportunity left. A saturated case may have none.


---

Minimal input assumptions

The offline v0 version assumes access to three synthetic signal families:

1. Opportunity

A structural estimate of how much unexplored or still-usable space remains.

2. Recoverability

A structural estimate of whether the case is still recoverable rather than already lost.

3. Stability gate

A suppressor term preventing the radar from assigning false opportunity to states that are too degraded or too chaotic.

These are abstract structural inputs in v0. They are not yet tied to a real backend.


---

Core variables

Let:

O in [0, 1] = opportunity
R in [0, 1] = recoverability
G in [0, 1] = stability_gate

Interpretation:

O = 0 -> no useful structural opportunity remains

O = 1 -> strong residual structural opportunity

R = 0 -> effectively non-recoverable

R = 1 -> highly recoverable

G = 0 -> gate closed; state too degraded for opportunity to count

G = 1 -> gate fully open



---

Radar score v0

Version v0 defines:

radar_score = O * R * G

This is intentionally simple.

Why multiplicative form

The multiplicative form enforces a hard structural discipline:

if opportunity is absent, score collapses

if recoverability is absent, score collapses

if the gate is closed, score collapses


This prevents inflated scores from one strong term masking failure in another critical term.


---

Interpretation of radar_score

High radar score

A high score means:

some useful structural space remains

the case is still recoverable

the state is not so degraded that opportunity becomes misleading


This is the target region of OMNIA-RADAR.

Low radar score

A low score means at least one of the following:

little useful opportunity remains

the case is not recoverable enough

structural degradation is too high for the opportunity signal to be trusted



---

Minimal decision interpretation

OMNIA-RADAR does not decide action directly.

But its score can be interpreted structurally:

high radar_score -> residual opportunity exists
mid radar_score  -> ambiguous / borderline opportunity
low radar_score  -> little or no justified opportunity

The actual action remains external.


---

Why the gate term is necessary

Without G, OMNIA-RADAR would over-score noisy or degraded cases.

Example:

a highly chaotic state might appear to have many possible continuations

but those continuations may be structurally useless


The gate exists to suppress false opportunity from unstable or already broken states.

This is why:

opportunity alone is insufficient


---

Synthetic regime examples

Case A — Growth zone

O = 0.85
R = 0.80
G = 0.90

Then:

radar_score = 0.85 * 0.80 * 0.90 = 0.612

Interpretation: strong residual structural opportunity.


---

Case B — Recoverable but narrow

O = 0.45
R = 0.70
G = 0.85

Then:

radar_score = 0.45 * 0.70 * 0.85 = 0.26775

Interpretation: some opportunity remains, but not strongly.


---

Case C — False opportunity suppressed

O = 0.90
R = 0.40
G = 0.20

Then:

radar_score = 0.90 * 0.40 * 0.20 = 0.072

Interpretation: apparent possibility exists, but structural gate closes most of it.


---

Case D — Saturated dead zone

O = 0.10
R = 0.10
G = 0.10

Then:

radar_score = 0.001

Interpretation: no meaningful residual opportunity.


---

Regime categories

A simple v0 regime reading may be:

Growth zone

radar_score >= 0.50

Borderline zone

0.20 <= radar_score < 0.50

Dead zone

radar_score < 0.20

These are not final thresholds. They are only synthetic regime markers for the offline branch.


---

Relation to OMNIA-LIMIT

OMNIA-RADAR and OMNIA-LIMIT are not opposites in the naive sense.

Correct relation:

OMNIA-RADAR estimates whether useful structural opportunity still exists

OMNIA-LIMIT certifies when structural continuation is no longer justified


So:

high RADAR does not imply no LIMIT
high LIMIT pressure suppresses RADAR usefulness

They are complementary.


---

Relation to OMNIAMIND

OMNIAMIND and OMNIA-RADAR also differ:

OMNIAMIND asks whether the structure is splitting, drifting, or destabilizing

OMNIA-RADAR asks whether useful recoverable space still remains


A case can have:

high instability and high opportunity

low instability and low opportunity

high instability and low opportunity


These are not the same variable.


---

Why offline v0 is useful

The offline version is useful because it allows the project to test:

whether the score behaves sensibly

whether opportunity detection stays distinct from fragility detection

whether false-positive opportunity is suppressed

whether regime categories remain structurally coherent


This is enough for an offline analytical branch.


---

Declared limits

1. Synthetic only

This formalization is not based on real runtime signals.

2. No semantic meaning

Opportunity is structural only.

3. No direct action policy

The score informs downstream systems but does not decide alone.

4. No empirical calibration yet

Thresholds are synthetic placeholders, not validated boundaries.

5. No guarantee of universality

This is a bounded analytical formalization.


---

Success condition for v0

OMNIA-RADAR v0 is successful if:

1. high-opportunity synthetic cases score high


2. degraded or saturated cases score low


3. false opportunity is reduced by the gate term


4. the score remains distinct from pure fragility


5. the branch is fully runnable offline



That is sufficient for v0.


---

Minimal conclusion

OMNIA-RADAR v0 is a non-semantic structural opportunity detector.

Its first score is:

radar_score = opportunity * recoverability * stability_gate

This score is not a truth estimate and not an action policy.

It is a bounded structural signal intended to detect whether useful residual structural space still exists before structural continuation becomes unjustified.