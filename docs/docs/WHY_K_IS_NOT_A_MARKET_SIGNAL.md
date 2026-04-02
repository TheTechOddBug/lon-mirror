# Why k Is Not a Market Signal
**MB-X.01 — Negative Result Note**

---

## 1. Scope

This note closes a failed validation route.

The goal of the discarded route was:

> test whether a quantity labeled \(k\) could be extracted from market data and interpreted as a structurally meaningful physical threshold.

This route failed.

---

## 2. Original Intention

A dynamic signal \(k(t)\) was introduced as a candidate measure of structural distinguishability over time.

The working idea was:

- if \(k\) were fundamental, perhaps traces of it could emerge in noisy real-world series
- Bitcoin daily data was chosen as a stress test due to high volatility and regime variation

This was a methodological experiment, not a proof.

---

## 3. Data Used

A long BTC/USDT daily dataset was tested.

Properties:

- multi-year span
- daily close prices
- converted to log-returns for scale invariance

This removed the earlier issue of insufficient sample size.

---

## 4. Tested Metric

The tested operational definition was based on rolling distinguishability collapse.

In simplified form:

\[
k(t) = \min \{\Delta t \;|\; SCI(\Delta t) < \theta \}
\]

where:

- \(SCI\) was approximated through local structural similarity
- the test used rolling windows
- distinguishability was evaluated through shift-based decorrelation

This definition was only an exploratory proxy.

It was **not** equivalent to the later physical definition of k as minimum proper-time distinguishability.

---

## 5. Empirical Result

On the long BTC daily dataset, the result collapsed to a degenerate regime:

\[
k(t) = 1
\quad \text{for essentially all windows}
\]

Observed summary:

- mean \(k = 1\)
- min \(k = 1\)
- max \(k = 1\)
- std \(k = 0\)

This means the metric lost all discriminative power.

---

## 6. Interpretation of the Failure

The result does **not** show that k is false.

It shows something narrower and more precise:

> this market-based operationalization of k is structurally inadequate.

Why it failed:

### A. Returns decorrelate too quickly
Daily log-returns of BTC are already weakly autocorrelated at lag 1.

Thus the metric collapsed immediately.

### B. The metric was measuring short-lag decorrelation
Not a fundamental temporal threshold.

### C. Financial series are composite outputs
Market prices are aggregates of many overlapping causes and do not represent a clean substrate for probing fundamental temporal structure.

---

## 7. What This Failure Does Mean

This negative result is useful because it closes a false path.

It shows that:

- k cannot be validated as a physical principle through naive market decorrelation
- noisy financial series do not provide a credible route to derive a universal temporal threshold
- “first shift that breaks similarity” is too weak a definition

---

## 8. What This Failure Does NOT Mean

This result does **not** imply:

- that k is false
- that distinguishability thresholds are meaningless
- that dynamic structural analysis is useless
- that OMNIA fails as a framework

It only means:

> BTC daily series are not an appropriate validation layer for fundamental k.

---

## 9. Structural Lesson

The failed route exposed a category error.

The original confusion was:

- treating k as if it could emerge from generic real-world time series
- before establishing whether k was a physical or only system-dependent threshold

This note fixes that mistake.

---

## 10. Corrected Position

After this failure, the physically meaningful definition of k remains:

\[
\Delta \tau_{\min} = k
\]

where:

> k is the minimum physically distinguishable increment of proper time for timelike processes.

This is a physical hypothesis.

It is not reducible to a market signal.

---

## 11. Decision

This validation branch is closed.

Market-based signals may still be useful for:

- system instability
- structural degradation
- local distinguishability analysis

But not for:

- validating k as a fundamental physical principle

---

## 12. Final Statement

\[
\boxed{
\text{Market decorrelation does not validate } k.
}
\]

The BTC route was a useful negative result.

It eliminated noise, not truth.