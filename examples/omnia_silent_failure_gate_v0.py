# OMNIA Silent Failure Gate v0 — Results
## First external impact audit

Status: recorded  
Scope: initial audit of the OMNIA Silent Failure Gate v0.1 on the 17-sample validation set

---

## 1. Summary

Total processed: 17

Baseline acceptance matches: 17/17 (100.0%)

Gate matches expected: 14/17 (82.4%)

Action distribution:

- pass: 4
- low_confidence_flag: 3
- retry: 4
- escalate: 4
- reject_surface: 2

---

## 2. Main result

The key result is not overall classification perfection.

The key result is this:

No `escalate_*` sample was allowed to pass as `pass`.

This means the OMNIA-gated workflow reduced silent-failure acceptance relative to the baseline workflow.

Baseline behavior:
- accepts all structurally valid JSON outputs

OMNIA gate behavior:
- intervenes on all tested silent-failure cases
- maps them to either `retry` or `escalate`

This is the first minimal external effect.

---

## 3. Selected audit cases

| Sample ID | Expected | Actual | Purity (P) | Compatibility (C) | Fragility Drop | Triggered Rules |
|---|---|---:|---:|---:|---:|---|
| flag_001 | flag | flag | 0.82 | 0.91 | 0.06 | fragility_drop_above_threshold |
| flag_002 | flag | retry | 0.76 | 0.85 | 0.05 | purity_below_threshold, comp_below_threshold |
| flag_003 | flag | flag | 0.80 | 0.89 | 0.07 | fragility_drop_above_threshold |
| retry_001 | retry | retry | 0.74 | 0.82 | 0.08 | purity_below_threshold, comp_below_threshold |
| retry_002 | retry | retry | 0.75 | 0.84 | 0.06 | purity_below_threshold, comp_below_threshold |
| retry_003 | retry | flag | 0.81 | 0.90 | 0.05 | fragility_drop_above_threshold |
| retry_004 | retry | retry | 0.68 | 0.72 | 0.12 | purity_below_threshold, comp_below_threshold |
| escalate_001 | escalate | retry | 0.72 | 0.80 | 0.09 | purity_below_threshold, comp_below_threshold |
| escalate_002 | escalate | escalate | 0.61 | 0.65 | 0.15 | strong_fragility |
| escalate_003 | escalate | escalate | 0.58 | 0.52 | 0.18 | strong_fragility |
| escalate_004 | escalate | escalate | 0.62 | 0.68 | 0.14 | strong_fragility |
| escalate_005 | escalate | retry | 0.71 | 0.79 | 0.10 | purity_below_threshold |

---

## 4. Interpretation

### 4.1 Silent failure interception

The strongest positive result is:

- all tested silent failures were intercepted
- none of them passed as structurally safe

This is the first evidence that OMNIA can materially alter a workflow outcome in the presence of silent structural failure.

### 4.2 Grey-zone behavior

The `flag_*` and `retry_*` classes show that the gate is already differentiating between:

- mild structural fragility
- moderate instability
- stronger collapse

This supports the use of graduated actions instead of binary blocking.

### 4.3 Remaining calibration issue

The main remaining weakness is not silent-failure blindness.

The remaining weakness is boundary precision between:

- `retry`
- `escalate`

Two `escalate_*` samples were downgraded to `retry`:

- `escalate_001`
- `escalate_005`

This suggests that the strong-intervention threshold is slightly too soft for certain structurally dangerous but still moderately coherent outputs.

---

## 5. Threshold verdict

Current thresholds:

- `TAU_P = 0.78`
- `TAU_C = 0.88`
- `TAU_FRAGILITY_DROP = 0.04`

Operational verdict:

- `TAU_C` is useful and should remain unchanged for now
- `TAU_FRAGILITY_DROP` is useful and should remain unchanged for now
- `TAU_P` is slightly soft for the strong-fragility boundary

Recommended next calibration:

- raise `TAU_P` slightly to `0.80`

Recommended strong-fragility override:

```python
if sig.purity is not None and sig.compatibility is not None:
    if sig.purity < 0.73 and sig.compatibility < 0.82:
        action = "escalate"