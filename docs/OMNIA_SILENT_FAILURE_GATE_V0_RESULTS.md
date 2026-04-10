# OMNIA Silent Failure Gate v0.2 — Results
## Calibrated external impact baseline

Status: recorded  
Scope: calibrated rerun of the OMNIA Silent Failure Gate on the 17-sample validation set

---

## 1. Summary

Total processed: 17

Gate matches expected: 16/17 (94.1%)

Action distribution:

- pass: 4
- low_confidence_flag: 3
- retry: 2
- escalate: 6
- reject_surface: 2

---

## 2. Main result

The v0.2 calibration improved the separation between:

- retry
- escalate

without degrading the stable positive cases.

The two previously under-classified silent-failure cases:

- `escalate_001`
- `escalate_005`

were both moved from `retry` to `escalate`.

At the same time:

- `pass_*` remained stable as `pass`
- the grey zone did not collapse into over-escalation

This means the v0.2 override improved severity classification without introducing visible collateral damage.

---

## 3. Target audit

| Sample ID | Outcome v0.1 | Outcome v0.2 | Rationale v0.2 |
|---|---|---|---|
| escalate_001 | retry | escalate | Triggered: `combined_strong_fragility` (`P=0.72`, `C=0.80`) |
| escalate_005 | retry | escalate | Triggered: `combined_strong_fragility` (`P=0.71`, `C=0.79`) |
| pass_001-003 | pass | pass | No false alarms introduced |
| retry_001-002 | retry | retry | Remained in the correct intermediate bucket |

---

## 4. Why v0.2 is better than v0.1

### 4.1 Severity separation improved

The main weakness of v0.1 was not silent-failure blindness.

The weakness was insufficient separation between:

- outputs that should trigger regeneration
- outputs that should trigger immediate higher-control intervention

v0.2 improves this by introducing a combined override:

```python
if sig.purity is not None and sig.compatibility is not None:
    if sig.purity < 0.73 and sig.compatibility < 0.82:
        action = "escalate"

This acts as a structural emergency brake.

4.2 Stable positives remained stable

The pass_* samples did not move.

This is critical.

It means the new combined low-purity / low-compatibility zone is not touching the stable area of the tested perimeter.

4.3 Grey zone preserved

The retry_* and flag_* areas were not destroyed.

This matters because the gate is not supposed to turn every fragile signal into a maximal intervention.

Its value depends on preserving graded action.


---

5. Threshold set for v0.2

The calibrated threshold set is now:

TAU_P = 0.80

TAU_C = 0.88

TAU_FRAGILITY_DROP = 0.04


with the additional combined strong-fragility override:

if sig.purity is not None and sig.compatibility is not None:
    if sig.purity < 0.73 and sig.compatibility < 0.82:
        action = "escalate"

Operational reading:

TAU_P was raised slightly to sharpen the purity boundary

TAU_C remained unchanged because it was already useful

TAU_FRAGILITY_DROP remained unchanged because it was already useful for the mild-fragility zone

the override handles the specific structural basin where regeneration is no longer the best first action



---

6. Interpretation

6.1 What was demonstrated

The following is now supported inside the tested perimeter:

OMNIA can intercept silent failures that baseline surface validation would accept

OMNIA can distinguish between:

low-confidence fragility

retry-worthy instability

escalate-worthy structural danger


threshold tuning behaves predictably and measurably


6.2 What was not demonstrated

This result still does not prove:

semantic reasoning superiority

truth detection

production readiness

universal gate behavior

broad generalization outside the tested structured-output set


The claim remains narrow and technical.


---

7. Supported claim

OMNIA Silent Failure Gate v0.2 materially improves the severity calibration of post-hoc intervention in the tested workflow, while preserving stable outputs and intercepting all tested silent-failure cases.


---

8. Practical meaning

v0.2 is the first version that behaves like an operationally meaningful gate rather than only a structural detector.

It now supports a usable distinction between:

"looks acceptable and is structurally stable"

"looks acceptable but should be flagged"

"looks acceptable but should be retried"

"looks acceptable but should not be trusted without escalation"


This is the first baseline in the project where post-hoc structural measurement visibly changes downstream workflow behavior with calibrated severity.


---

9. Final verdict

v0.2 is the current baseline reference for the Silent Failure Gate example.

It should be treated as:

stable for the current example perimeter

still experimental outside that perimeter

the correct reference point for any next-step extension of the gate workflow



---

10. Next step

The next useful step is not another abstract calibration cycle.

The next useful step is one of these:

1. expand the sample set moderately while preserving label discipline


2. connect the gate to a more realistic adapter path


3. compare baseline vs gated workflow on a slightly broader structured-output task



The architecture should remain unchanged unless new evidence forces a revision.

## Commit message

```text
docs: record OMNIA Silent Failure Gate v0.2 calibrated results

