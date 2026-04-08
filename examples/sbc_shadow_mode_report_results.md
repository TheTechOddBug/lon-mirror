# SBC Shadow Mode Report — Results

Status: passive monitoring validation  
Scope: million-range batch (`1,000,000–1,002,000`)  
Purpose: quantify the trade-off between composite declassification gains and prime ranking losses under SBC shadow mode

---

## Goal

This report measures whether Structural Bias Correction is only "useful" or also "economically justified" in ranking terms.

The key question is:

**How many dangerous composite traps are removed for each real prime that is materially harmed?**

This is measured through the **Sacrifice Ratio**.

---

## Source

Input file:

- `examples/prime_candidates_1m_1m002_raw_vs_adjusted_scores.jsonl`

Runner:

- `examples/monitor_sbc_shadow_mode.py`

Generated report:

- `examples/sbc_shadow_mode_report.md`

---

## Monitoring Thresholds

### Positive Gain

A composite is counted as a successful declassification if:

- `raw_omnia_score > 0.90`
- `adjusted_score < 0.85`

### Negative Impact

A prime is counted as harmed if:

- it loses more than `5` ranking positions after correction

---

## Terminal Output

```text
=== SBC SHADOW MODE MONITOR ===
Source: examples/prime_candidates_1m_1m002_raw_vs_adjusted_scores.jsonl
Total records: 800
Positive Gain count: 18
Negative Impact count: 2
Sacrifice Ratio: 9.000000
Spread widening: 37.521258
Wrote examples/sbc_shadow_mode_report.md


---

Direct Reading

Positive Gain count

18


Meaning:

18 high-confidence composite traps were pushed below the configured safety threshold.

This confirms that SBC is not only adjusting rank mildly. It is actively removing structurally deceptive composite candidates from the danger zone.

Negative Impact count

2


Meaning:

Only 2 real primes crossed the configured harm threshold.

This indicates that the correction is selective rather than indiscriminate.

Sacrifice Ratio

9.000000


Meaning:

For every one real prime materially harmed by the correction, SBC successfully removes 9 dangerous composite traps.

This is a strongly favorable trade-off.

Spread Widening

37.521258


Meaning:

The average separation between primes and composites widens by more than 37 ranking positions under the correction.

This is not a cosmetic improvement. It is a population-level structural separation effect.


---

Minimal Valid Claim

This shadow-mode run supports the following narrow claim:

SBC-Regularity v1 produces a highly favorable gain-to-cost trade-off on the million-range batch.

More precisely:

many dangerous composites are successfully declassified

very few real primes are materially harmed

the average prime/composite separation widens strongly

the correction behaves like a useful filtering layer, not like blind score suppression



---

Operational Interpretation

Under the current thresholds, SBC is already behaving like a production-grade correction candidate.

It is still in shadow mode, but the monitoring signal is clearly positive:

high removal rate of composite traps

very low collateral damage

strong global spread improvement


This is the first batch where the correction is not only validated by ranking quality, but also by explicit cost accounting.


---

What This Does Not Yet Prove

This report does not yet prove that:

SBC should immediately replace legacy scoring globally

the same Sacrifice Ratio will remain stable across all future numeric ranges

the current thresholds are final


It proves only that the correction is now monitorable, economically interpretable, and favorable on the tested batch.


---

Final Compression

The shadow-mode monitor confirms that SBC is not merely accurate.

It is efficient.

On the million-range batch:

18 composite traps were cleanly declassified

only 2 primes crossed the configured harm threshold

Sacrifice Ratio = 9.0

spread widened by 37.521258


This is the strongest operational justification so far for keeping SBC active in shadow mode and continuing toward eventual promotion.

