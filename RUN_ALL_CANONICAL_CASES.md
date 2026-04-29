# RUN_ALL_CANONICAL_CASES

## Scope

This document defines the single-entry execution path for the current OMNIA canonical evidence layer.

The goal is to reduce external friction.

An external reader should be able to:

1. clone the repository
2. run the canonical cases
3. compare observed results with expected qualitative behavior
4. inspect the structural separations directly

---

# Goal

The purpose is not to prove universal structural truth.

The purpose is to expose the framework to executable external inspection.

---

# Canonical Cases Included

The canonical run includes:

1. suspicious-clean review signal
2. correctness preserved while structural stability drops
3. reversible vs irreversible structural loss
4. saturation vs instability
5. divergence timing
6. resilience
7. residual invariant extraction

---

# Expected Execution Flow

The canonical runner should execute:

Case 01:
llm_output_instability_v0.py

Case 02:
run_gsm_formal_metrics_v0.py

Case 03:
iri_validation_v2.py

Case 04:
sei_validation_v0.py

Case 05:
tdelta_validation_v0.py

Case 06:
r_validation_v0.py

Case 07:
omega_hat_validation_v0.py

---

# Expected Qualitative Outcomes

Case 01:
baseline gives no warning
OMNIA triggers review

Case 02:
correctness remains true
Omega decreases
Score+ decreases

Case 03:
recoverable transformations produce lower IRI
lossy deletion produces highest IRI

Case 04:
saturated trajectories produce higher SEI
unstable trajectories produce lower SEI

Case 05:
rapid divergence crosses threshold earlier than slow divergence

Case 06:
perfect recovery produces higher R
failed recovery produces lower R

Case 07:
surviving invariant components are explicitly returned

---

# Important Interpretation Constraint

The framework currently emphasizes:

qualitative separation
structural ordering
bounded reproducibility

not exact floating point identity.

---

# Recommended External Environment

Recommended:

Google Colab

The canonical run should also remain compatible with lightweight local Python environments when possible.

---

# What The Run Does Not Claim

The canonical run does not prove:

- semantic truth
- deployment readiness
- AGI safety
- universal hallucination detection
- correctness verification
- universal robustness

The framework remains experimental and bounded.

---

# Architectural Boundary

The boundary remains strict:

measurement != inference != decision

OMNIA measures structure.

It does not decide.

---

# Reader Outcome

If the canonical run behaves as expected, the external reader should conclude only this:

the framework currently separates multiple structural properties under controlled transformation tests.

No stronger conclusion is currently justified.

---

# Failure Is Allowed

If expected separations fail to reproduce:

- the framework should be revised
- thresholds may require recalibration
- metrics may require redesign

The framework must remain falsifiable.

---

# Related Documents

README.md

CANONICAL_EVIDENCE.md

FORMAL_METRICS.md

OMNIA_EXTERNAL_TEST_PACK_V0.md

RUN_EXTERNAL_TEST_PACK_V0.md

---

# Next Practical Step

The next practical artifact should be:

RUN_ALL_CANONICAL_CASES.py

or:

RUN_CANONICAL_EVIDENCE_NOW.ipynb

The purpose should be:

one entry point
minimal setup
minimal friction
bounded reproducibility

---

# Final Statement

The current value of the repository is not that it solved structural measurement completely.

The value is that it exposes structural behavior as executable, separable, inspectable phenomena instead of abstract narrative claims.