# ZEH-1.1 Case Study — Empirical Early-Warning Support

## Status

- Type: empirical case study
- Scope: single model, single task
- Model: Llama-3-8B-Instruct (4-bit)
- Task: Parentheses Balance (dual-sequence protocol)
- Validation status: empirical support obtained
- Generalization status: open

---

## Purpose

This case study evaluates whether OMNIA can detect structural degradation **before** the first observed logical failure of a model.

The target comparison is:

- **ZEH** → detects the first failure boundary
- **OMNIA** → detects pre-failure structural degradation

---

## Hypothesis

\[
\Delta_{struct}
\text{ degrades before the first model error appears.}
\]

Operationally, the hypothesis is supported if:

1. a yield point \(d_y\) is detected before the first error depth
2. the drop in \(\Delta_{struct}\) is statistically distinguishable from the plateau
3. the phenomenon is repeatable across seeds

---

## Test Protocol

### Task

Parentheses balance under increasing depth.

### Dual-sequence setup

For each depth \(d\):

- **Balanced sample**  
  `"(" * d + ")" * d`

- **Unbalanced sample**  
  `"(" * d + ")" * (d - 1)`

### Prompt

`Is this parentheses sequence balanced? Answer only YES or NO.`

### Metrics

- model accuracy on balanced + unbalanced samples
- \(\Delta_{struct}\) computed with OMNIA v1.0 + v10.0
- plateau statistics
- bootstrap confidence intervals

---

## Yield Criterion

Plateau range:

\[
d \in [10,25]
\]

Measured plateau statistics:

- mean \(\Delta_{struct}\): 0.276
- std \(\sigma\): 0.012

Yield threshold:

\[
0.276 - 2 \cdot 0.012 = 0.252
\]

The yield point is defined as the first depth where mean \(\Delta_{struct}\) falls below this threshold.

---

## Aggregated Results

| Depth | Mean \(\Delta_{struct}\) | 95% CI | Accuracy | Status |
|------:|--------------------------:|:------:|:--------:|:------:|
| 25 | 0.272 | [0.264 - 0.280] | 100% | Plateau |
| 30 | 0.248 | [0.235 - 0.261] | 100% | Below 2σ threshold |
| 35 | 0.179 | [0.162 - 0.196] | 100% | Yielding |
| 40 | 0.108 | [0.089 - 0.127] | 50% | ZEH boundary |

---

## Main Observation

The system remains externally correct up to depth 35, while \(\Delta_{struct}\) has already undergone a statistically significant decline.

This indicates:

- the model is still producing correct answers
- the internal structural response is already degraded
- OMNIA detects the fatigue phase before visible failure

---

## Interpretation

This case study supports the following distinction:

- **ZEH** detects when failure becomes observable
- **OMNIA** detects when structural degradation becomes measurable

In this setting, OMNIA acts as an **early-warning structural signal**.

---

## Scope of the Claim

This result supports only the following claim:

> OMNIA provides empirical early-warning support on a single model and a single task.

It does **not** establish:

- universal predictive validity
- model-independent anticipation in all tasks
- a general law of pre-failure degradation

---

## Falsifiability

The bridge hypothesis would be weakened or falsified if future runs show one of the following:

- \(\Delta_{struct}\) remains stable until the first model error
- yield point varies randomly across seeds
- no significant gap exists between plateau and pre-failure region

---

## Repository Artifacts

- Data: `data/zeh_bridge_v1_1_full.json`
- Hypothesis protocol: `docs/OMNIA_BRIDGE_HYPOTHESIS.md`

---

## Conclusion

ZEH-1.1 provides the first empirical support that OMNIA can detect structural fatigue before explicit output failure.

This is a **proof-of-principle**, not a universal proof.

The next step is cross-task falsification, starting with a structurally different benchmark such as logical transitivity.