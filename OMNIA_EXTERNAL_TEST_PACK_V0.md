# OMNIA External Test Pack v0

## Scope

This file defines the first external test pack for OMNIA / LON-MIRROR.

The goal is simple:

allow an external reader to reproduce the current canonical evidence cases without reading the full repository.

This is not a benchmark claim.

This is not deployment validation.

This is a minimal reproducibility pack.

---

## Purpose

The external test pack exists to make the framework:

- easy to inspect
- easy to run
- easy to falsify
- easy to compare
- easy to cite

The core idea is:

surface validity does not always imply structural stability.

---

## What This Pack Should Reproduce

The pack should reproduce the current canonical evidence cases:

1. suspicious-clean review signal
2. correctness preserved while structural stability drops
3. reversible deformation vs irreversible loss
4. saturation vs oscillation
5. early vs delayed divergence
6. perfect vs partial vs failed recovery
7. residual invariant extraction

---

## Expected Outputs

A successful run should show:

Case 01:
baseline gives no warning
OMNIA triggers review

Case 02:
correctness remains true
Omega decreases
Score+ decreases

Case 03:
recoverable type drift gives low IRI
lossy deletion gives high IRI

Case 04:
saturated trajectory gives high SEI
unstable trajectory gives lower SEI

Case 05:
rapid divergence crosses threshold earlier than slow divergence

Case 06:
perfect recovery gives high R
failed recovery gives low R

Case 07:
Omega-hat returns surviving invariant components

---

## Current Canonical Sources

Canonical evidence document:

CANONICAL_EVIDENCE.md

Formal metric definitions:

FORMAL_METRICS.md

Metric validation results:

RESULTS_IRI_VALIDATION_V2.md
RESULTS_SEI_VALIDATION_V0.md
RESULTS_TDELTA_VALIDATION_V0.md
RESULTS_R_VALIDATION_V0.md
RESULTS_OMEGA_HAT_VALIDATION_V0.md

GSM formal metrics evidence:

RESULTS_GSM_FORMAL_METRICS_V0.md

Suspicious-clean review evidence:

docs/OMNIA_10_SECONDS_DEMO_RESULT.md

---

## Minimal Reproducibility Goal

The external user should be able to:

1. open the repository
2. read CANONICAL_EVIDENCE.md
3. run one external test cell or script
4. compare observed results with expected results
5. verify that the claims are bounded

---

## What This Pack Does Not Claim

This pack does not prove:

- universal AI safety
- semantic truth
- production readiness
- deployment-scale robustness
- general hallucination detection
- correctness validation

It only checks whether the current canonical structural evidence cases reproduce as expected.

---

## Architectural Boundary

The same boundary applies:

measurement != inference != decision

OMNIA measures structure.

It does not decide.

It does not infer truth.

It does not replace reasoning.

---

## External Reader Interpretation

If the pack runs correctly, the reader should conclude only this:

OMNIA currently contains a set of controlled structural measurements that separate multiple structural properties under bounded test conditions.

The reader should not conclude that OMNIA is a universal gate or final validator.

---

## Success Criterion

The external test pack succeeds if it reproduces the qualitative ordering of the canonical cases.

Examples:

IRI:
reorder approximately equals recoverable type drift
both are lower than nonrecoverable type drift
lossy deletion is highest

SEI:
saturated is higher than converging
converging is higher than unstable

TDelta:
rapid divergence crosses threshold before slow divergence
no divergence remains undefined

R:
perfect recovery is higher than partial recovery
partial recovery is higher than failed recovery

Omega-hat:
surviving invariant components are explicitly returned

---

## Failure Criterion

The pack fails if:

- expected orderings do not reproduce
- outputs are constant and non-informative
- structural signals do not separate cases
- claims require interpretation not supported by results

Failure is acceptable.

The framework must remain falsifiable.

---

## Recommended Next Artifact

The next practical artifact should be:

RUN_EXTERNAL_TEST_PACK_V0.md

or:

RUN_CANONICAL_EVIDENCE_NOW.ipynb

Its purpose should be to give external readers one simple way to rerun the canonical cases.

---

## Final Statement

The purpose of this pack is not to make OMNIA look complete.

The purpose is to make OMNIA testable by someone else.

A structural measurement framework should not be protected by narrative.

It should be exposed to reproducible transformation tests.