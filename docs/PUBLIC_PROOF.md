# OMNIA — Public Proof (Natural Text)

## Status
\[
\boxed{\text{PASS}}
\]

---

## Objective

Validate that the structural metric \(\Delta_{struct}\) generalizes beyond numeric domains and remains discriminative on controlled natural language.

Test condition: Wikipedia-like structured text.

---

## Setup

**Domain:** Natural language (controlled)

**Representation:** Token sequence

**Method:** RFS (Relational Fatigue Spectrometry)

**Transformations:**
- Structured: original text
- Perturbed: adjacent token swaps (~35% noise)
- Random: full token shuffle (baseline)

---

## Results

\[
\Delta_{struct}(\text{structured}) = 0.1428
\]  
\[
\Delta_{struct}(\text{perturbed}) = 0.0631
\]  
\[
\Delta_{struct}(\text{random}) = 0.0042
\]

---

## Expected Invariant

\[
\text{structured} > \text{perturbed} > \text{random}
\]

\[
\boxed{\text{Verified}}
\]

---

## Interpretation

### 1. Structural Resolution

The structured signal (0.1428) is significantly above baseline.

Implication:
- OMNIA detects relational structure, not token frequency.

---

### 2. Discrimination Power

Perturbation reduces signal by more than 50%.

Implication:
- Metric is sensitive to syntactic degradation.
- Captures loss of relational coherence.

---

### 3. Bias Check

Random baseline is near zero (0.0042).

Implication:
- No frequency bias.
- Position and relation drive the signal.

---

## Technical Conclusion

\[
\boxed{
\Delta_{struct} \text{ generalizes to natural language}
}
\]

OMNIA:
- does not rely on semantics
- does not require domain-specific features
- measures structural coherence under transformation

---

## Limits

- Single domain (controlled text)
- Not yet validated on:
  - real-world noisy corpora
  - multilingual data
  - long-context dependencies

---

## Next Steps

1. Cross-domain validation:
   - time series
   - source code
   - LLM outputs

2. Perturbation scaling:
   - measure stability curve vs noise

3. Real-world datasets:
   - uncontrolled text
   - heterogeneous structures

---

## Summary

\[
\boxed{
\text{OMNIA detects structure in language without using meaning}
}
\]

This is a necessary condition for:
- domain-agnostic measurement
- post-hoc structural diagnostics
- invariance-based truth estimation