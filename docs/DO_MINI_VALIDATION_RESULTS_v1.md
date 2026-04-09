# OMNIA — dO Mini Validation Results v1

## Status

This document records the v0.2 execution of the dO mini validation protocol on the expanded synthetic validation set.

This is not a proof of universality.
It is an intermediate falsifiable validation milestone.

Architectural boundary remains unchanged:

measurement != cognition != decision

---

## 1. Summary

Pairs tested: 36

- PASS: 31
- FAIL: 5

Family means:

- equivalent: mean_dO = 0.034120
- mild_variation: mean_dO = 0.178540
- structural_break: mean_dO = 0.452300

Observed ordering:

mean_dO(equivalent) < mean_dO(mild_variation) < mean_dO(structural_break)

This ordering held at the aggregate level in this run.

---

## 2. Interpretation

Compared to the previous broader run with the earlier metric configuration, v0.2 shows a strong recovery in regime separation.

Key improvements observed:

- recovery of local numeric variation sensitivity
- recovery of ordering-sensitive structural breaks
- reduction of over-cleaning through transformation cost

The current residual failures appear concentrated in pre-ingestion and canonicalization, not primarily in the structural core of the metric.

---

## 3. What this result supports

This run supports the following minimal claim:

dO v0.2 provides a significantly stronger operational separation between:

- representational equivalence
- mild structural variation
- structural break

on the 36-pair synthetic validation set.

---

## 4. What this result does not support

This run does not prove:

- universality across domains
- semantic correctness
- truth detection
- robustness on real-world data
- final threshold stability
- final optimality of weights or transform costs

No such claim should be made from this result alone.

---

## 5. Residual failure interpretation

The remaining failures are best interpreted as input-canonicalization failures.

Typical residual issues include:

- leading zeros in numeric forms
- currency or formatting symbols
- equivalent numeric formatting not normalized before signature extraction

This suggests that the next correction should target pre-ingestion, not the structural core.

---

## 6. Next step

The next correct step is a v0.2.1 patch introducing a pre-canonicalization layer before structural signature extraction.

That patch should normalize superficial numeric and symbolic formatting while preserving order and without introducing semantic reinterpretation.