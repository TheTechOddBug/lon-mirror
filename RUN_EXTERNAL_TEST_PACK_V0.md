# RUN_EXTERNAL_TEST_PACK_V0

## Goal

This document provides the shortest external execution path for the current OMNIA canonical evidence pack.

The goal is not to prove universal structural truth.

The goal is to let an external reader reproduce the current bounded structural evidence cases.

---

# What This Run Should Demonstrate

The run should reproduce:

1. suspicious-clean review signal
2. correctness preserved while structural stability drops
3. reversible vs irreversible structural loss
4. saturation vs instability
5. divergence timing differences
6. resilience differences
7. residual invariant extraction

---

# Expected Runtime

Approximate runtime:

2 to 5 minutes

depending on environment.

---

# Environment

Recommended:

Google Colab

Minimal local Python environments should also work.

---

# Step 1 — Clone Repository

Clone:

https://github.com/Tuttotorna/lon-mirror

---

# Step 2 — Run Canonical Evidence Scripts

Run the following scripts in order.

---

## Case 01 — Suspicious-Clean Review

Script:

examples/llm_output_instability_v0.py

Expected qualitative result:

baseline gives no warning
OMNIA triggers review

---

## Case 02 — Correctness vs Structural Stability

Script:

examples/run_gsm_formal_metrics_v0.py

Expected qualitative result:

correctness remains true
Omega decreases
Score+ decreases

---

## Case 03 — Irreversibility

Script:

examples/iri_validation_v2.py

Expected qualitative ordering:

reorder approximately equals recoverable type drift

both are lower than nonrecoverable type drift

lossy deletion is highest

---

## Case 04 — Saturation

Script:

examples/sei_validation_v0.py

Expected qualitative ordering:

saturated > converging > unstable

---

## Case 05 — Divergence Timing

Script:

examples/tdelta_validation_v0.py

Expected qualitative ordering:

rapid divergence crosses threshold before slow divergence

no divergence remains undefined

---

## Case 06 — Resilience

Script:

examples/r_validation_v0.py

Expected qualitative ordering:

perfect recovery > partial recovery > failed recovery

---

## Case 07 — Residual Invariants

Script:

examples/omega_hat_validation_v0.py

Expected qualitative result:

surviving invariant components are explicitly returned

---

# What Should Be Compared

The important point is not exact floating point replication.

The important point is whether the structural separations remain visible.

The framework currently focuses on:

qualitative ordering
structural separation
bounded reproducibility

---

# Expected Reader Interpretation

If the runs behave as expected, the correct interpretation is:

OMNIA currently contains a bounded structural measurement layer capable of separating multiple structural properties under controlled transformations.

Not more.

---

# What This Run Does Not Prove

This run does not prove:

- semantic truth
- AGI safety
- universal hallucination detection
- deployment readiness
- production robustness
- correctness verification

The framework remains bounded and experimental.

---

# Architectural Boundary

The same boundary remains mandatory:

measurement != inference != decision

OMNIA measures structure.

It does not decide.

---

# Canonical Evidence Reference

For interpretation of the cases:

CANONICAL_EVIDENCE.md

---

# Formal Metric Definitions

For metric definitions:

FORMAL_METRICS.md

---

# Failure Is Allowed

The framework must remain falsifiable.

If expected separations fail to reproduce, the framework should be revised rather than protected by narrative.

---

# Final Statement

The purpose of this run is not to demonstrate perfection.

The purpose is to expose the framework to external reproducibility.