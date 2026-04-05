# ZEH-2 Case Study — Logical Transitivity Early-Warning Support

## Status

- Type: empirical case study
- Scope: single model, second task
- Model: Llama-3-8B-Instruct (4-bit)
- Task: logical transitivity
- Validation status: empirical support obtained
- Generalization status: open

---

## Purpose

This case study evaluates whether OMNIA can detect structural degradation before the first observed logical failure on an abstract relational task.

Unlike parentheses balance, this benchmark does not test syntactic symmetry.  
It tests the stability of chained logical relations.

---

## Hypothesis

\[
\Delta_{struct}
\text{ degrades before the first observed model failure.}
\]

Operationally, the hypothesis is supported if:

1. \(\Delta_{struct}\) declines significantly while model accuracy remains at 100%
2. the decline precedes the first accuracy drop
3. the phenomenon is consistent with the bridge logic already observed in ZEH-1.1

---

## Test Protocol

### Task

Logical transitivity under increasing chain length.

### Dual-sequence setup

For each chain length \(n\):

- **Valid chain**
  - Example:
    `A = B, B = C, C = D, therefore A = D`
  - Ground truth: YES

- **Broken chain**
  - One internal relation is inverted or contradicted
  - Example:
    `A = B, B = C, C ≠ D, therefore A = D`
  - Ground truth: NO

### Prompt

`If [CHAIN], is it true that [QUERY]? Answer only YES or NO.`

### Metrics

- model accuracy
- \(\Delta_{struct}\)
- confidence interval for \(\Delta_{struct}\)

---

## Aggregated Results

| Chain Length | Mean \(\Delta_{struct}\) | 95% CI | Accuracy | Status |
|-------------:|--------------------------:|:------:|:--------:|:------:|
| 4  | 0.312 | [0.301 - 0.323] | 100% | Plateau |
| 6  | 0.298 | [0.285 - 0.311] | 100% | Plateau |
| 8  | 0.275 | [0.262 - 0.288] | 100% | Initial tension |
| 10 | 0.194 | [0.178 - 0.210] | 100% | Yield point |
| 12 | 0.125 | [0.105 - 0.145] | 92%  | ZEH entry |
| 14 | 0.082 | [0.065 - 0.099] | 74%  | Logical decay |
| 16 | 0.041 | [0.030 - 0.052] | 55%  | ZEH boundary |

---

## Main Observation

A significant drop in \(\Delta_{struct}\) appears at chain length 10, while model accuracy is still 100%.

This means:

- output correctness remains externally intact
- internal structural stability is already degraded
- OMNIA detects a pre-failure regime before visible collapse

---

## Interpretation

This result replicates the bridge behavior observed in ZEH-1.1:

- **ZEH** detects the first observed failure
- **OMNIA** detects the degradation phase that precedes failure

The important consequence is that the signal is no longer limited to syntactic topology.  
It also appears in a relational logical task.

---

## Scope of the Claim

This case study supports only the following claim:

> OMNIA provides empirical early-warning support across two structurally different tasks on a single model.

It does **not** establish:

- universal predictive validity
- multi-model generalization
- full task-independence

---

## Comparison with ZEH-1.1

| Case Study | Task Type | Signal Behavior |
|-----------|-----------|-----------------|
| ZEH-1.1 | Parentheses balance | Δ declines before first error |
| ZEH-2 | Logical transitivity | Δ declines before first error |

This strengthens the bridge hypothesis from a single-task result to a cross-task empirical trend.

---

## Limits

- single model only
- one implementation family
- no cross-architecture comparison yet
- no adversarial falsification yet

---

## Conclusion

ZEH-2 provides empirical support that OMNIA can act as an early-warning structural signal on a second task with different relational demands.

This does not close general validation.  
It upgrades the evidence from single-task support to multi-task support on a single model.

---

## Repository Artifacts

- Data: `data/transitivity_results.json`
- Related case study: `docs/ZEH_1_CASE_STUDY.md`
- Bridge hypothesis: `docs/OMNIA_BRIDGE_HYPOTHESIS.md`