# OMNIA — Bridge Hypothesis (OMNIA vs ZEH)

## Status
- Type: Experimental Hypothesis
- Validation: NOT YET EXECUTED
- Purpose: falsification protocol for predictive structural signal

---

## Hypothesis (H1)

Δ_struct degradation precedes model failure (ZEH) in pure topological tasks.

Formally:

∃ k :
    Δ_struct(k) shows significant decrease
    AND model accuracy(k) = 100%

---

## Falsification Condition

The hypothesis is FALSE if:

Δ_struct remains stable until the first model error occurs.

---

## Test Protocol

### Task
Parentheses balance (Regime C — pure structure)

### Dataset (Dual Sequence)

For each depth d:

- Sample S (Balanced):
  "(" * d + ")" * d

- Sample U (Unbalanced):
  "(" * d + ")" * (d - 1)

---

### Prompt (Fixed)

Is this parentheses sequence balanced?  
Answer only YES or NO.

---

### Metrics

- Model accuracy (binary correctness over S + U)
- Δ_struct (OMNIA structural separation metric)

---

### Procedure

For each depth d:

1. Compute Δ_struct
2. Query model on S and U
3. Record accuracy
4. Detect first failure point (ZEH boundary)

---

### Expected Behavior (Hypothesis)

- Phase 1 (Elastic):
  high Δ_struct, 100% accuracy

- Phase 2 (Yielding):
  Δ_struct decreases, accuracy still 100%

- Phase 3 (Failure):
  accuracy drops, Δ_struct near noise

---

## Interpretation

ZEH:
- detects failure point

OMNIA:
- detects pre-failure structural degradation

---

## Outcome

- If confirmed:
  OMNIA acts as a predictive reliability signal

- If falsified:
  OMNIA reduces to a descriptive structural metric

---

## Notes

- No claim of universality
- No semantic interpretation
- Measurement only