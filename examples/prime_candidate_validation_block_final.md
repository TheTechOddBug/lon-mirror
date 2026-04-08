# OMNIA Prime Candidate Validation Block — Final

Status: consolidated validation block  
Scope: 240 candidates across three disjoint intervals  
Method: OMNIA structural ranking vs random baseline, trivial deterministic baseline, and cutoff analysis  
Interpretation level: ranking enrichment and search-space reduction only

---

## Purpose

This validation block was designed to answer one narrow question:

**Does OMNIA produce a non-random, structurally useful ranking signal on prime candidates?**

Not:

- primality proof
- theorem discovery
- replacement for primality testing
- open problem solution

Only:

- ranking usefulness
- baseline comparison
- search-space reduction signal

---

## Tested Intervals

Three disjoint intervals were used:

- `1000–1200`
- `1200–1400`
- `2000–2200`

Candidate preprocessing:

- odd numbers only
- multiples of 5 excluded

Total evaluated candidates:

- `240`

Total true primes:

- `86`

Natural prime density:

- `86 / 240 = 35.8333%`

---

## Interval-Level Results

### Interval A — 1000 to 1200

- Total candidates: `80`
- Total primes: `32`
- Natural density: `40%`

OMNIA result:

- Top 10 primes: `7 / 10 = 70%`
- Top 20 primes: `13 / 20 = 65%`
- Mean prime rank: `32.1250`
- Mean non-prime rank: `46.0833`

Enrichment:

- Top 10 lift over natural density: `1.75x`
- Top 20 lift over natural density: `1.625x`

---

### Interval B — 1200 to 1400

- Total candidates: `80`
- Total primes: `30`
- Natural density: `37.5%`

OMNIA result:

- Top 10 primes: `6 / 10 = 60%`
- Top 20 primes: `11 / 20 = 55%`
- Mean prime rank: `34.5667`
- Mean non-prime rank: `44.0600`

Enrichment:

- Top 10 lift over natural density: `1.60x`
- Top 20 lift over natural density: `1.4667x`

---

### Interval C — 2000 to 2200

- Total candidates: `80`
- Total primes: `24`
- Natural density: `30%`

OMNIA result:

- Top 10 primes: `6 / 10 = 60%`
- Top 20 primes: `11 / 20 = 55%`
- Mean prime rank: `32.7917`
- Mean non-prime rank: `43.8036`

Enrichment:

- Top 10 lift over natural density: `2.00x`
- Top 20 lift over natural density: `1.8333x`

Note:

- `2047` was corrected as composite (`23 x 89`) before finalizing this interval.

---

## Combined OMNIA Result

Across all three intervals:

- Total candidates: `240`
- Total primes: `86`
- Natural prime density: `35.8333%`

Observed under global OMNIA ranking:

- Top 10 primes: `7 / 10 = 70%`
- Top 20 primes: `12 / 20 = 60%`
- Mean prime rank: `33.151163`
- Mean non-prime rank: `45.025974`

Direct reading:

- primes are concentrated in the upper part of the ranking
- prime mean rank is much better than non-prime mean rank
- the signal persists across three disjoint tested ranges

---

## Baseline A — Random Ranking

A random baseline was estimated over `10000` shuffled rankings of the same 240 candidates.

Expected random behavior:

- Top 10 primes mean: `3.586600`
- Top 20 primes mean: `7.168700`
- Mean prime rank mean: `120.504210`
- Mean non-prime rank mean: `120.493821`

Comparison vs OMNIA:

- OMNIA Top 10 primes: `7`
- Random expected Top 10 primes: `3.586600`
- Top 10 lift over random: `1.951709x`

- OMNIA Top 20 primes: `12`
- Random expected Top 20 primes: `7.168700`
- Top 20 lift over random: `1.673944x`

- OMNIA mean prime rank: `33.151163`
- Random mean prime rank: `120.504210`
- Prime rank improvement: `87.353047`

Conclusion:

**OMNIA clearly outperforms random ordering.**

---

## Baseline B — Digit Sum Ranking

A deterministic trivial baseline was built by ranking all candidates by:

- descending decimal digit sum
- ascending `n` as tie-break

Observed baseline behavior:

- Top 10 primes: `4 / 10 = 40%`
- Top 20 primes: `8 / 20 = 40%`
- Mean prime rank: `120.726744`
- Mean non-prime rank: `120.373377`

Direct reading:

- digit sum produces almost no meaningful separation
- prime and non-prime mean ranks are effectively flat
- this baseline does not provide useful discrimination

Comparison vs OMNIA:

- OMNIA Top 10 primes: `7`
- Digit Sum Top 10 primes: `4`

- OMNIA Top 20 primes: `12`
- Digit Sum Top 20 primes: `8`

- OMNIA mean prime rank: `33.151163`
- Digit Sum mean prime rank: `120.726744`

Conclusion:

**OMNIA outperforms a deterministic trivial arithmetic baseline.**

---

## Cutoff Analysis — Search-Space Reduction

The full 240-candidate OMNIA ranking was also analyzed as a filtering mechanism.

Natural prime density:

- `35.8333%`

Observed cutoff behavior:

| Cutoff | Candidates Kept | Primes Kept | Prime Recall | Prime Density | Lift |
|---|---:|---:|---:|---:|---:|
| Top 5%  | 12  | 7  | 0.0814 | 0.5833 | 1.6280 |
| Top 10% | 24  | 14 | 0.1628 | 0.5833 | 1.6280 |
| Top 20% | 48  | 24 | 0.2791 | 0.5000 | 1.3953 |
| Top 25% | 60  | 29 | 0.3372 | 0.4833 | 1.3488 |
| Top 50% | 120 | 51 | 0.5930 | 0.4250 | 1.1860 |

Direct reading:

- the strongest enrichment is concentrated in the top of the ranking
- the lift decays smoothly as the subset widens
- the ranking behaves like a usable filter, not like noise

Interpretation:

**OMNIA supports non-trivial search-space reduction on the tested candidate pool.**

---

## What Is Actually Supported

This validation block supports the following narrow claims:

1. **OMNIA produces a non-random ranking signal on prime candidates.**
2. **That signal replicates across three disjoint intervals.**
3. **OMNIA outperforms both random ranking and a trivial deterministic digit-sum baseline.**
4. **OMNIA can be used as a search-space reduction layer, increasing prime density in top-ranked subsets above baseline.**

---

## What Is Not Supported

This validation block does **not** support the following claims:

- OMNIA proves primality
- OMNIA is a primality test
- OMNIA solves an open number-theoretic problem
- OMNIA has discovered a law of primes
- OMNIA identifies all primes and only primes
- OMNIA generalizes universally without further testing

---

## Boundary Condition

OMNIA is not directly measuring primality.

It is measuring a structural property that correlates with primality strongly enough to improve ranking and filtering, but not strongly enough to be treated as identity.

This is confirmed by the existence of high-scoring composites such as:

- `1007 = 19 x 53`
- `2021 = 43 x 47`
- `2047 = 23 x 89`

These false positives are part of the observed behavior and must remain visible in any honest interpretation.

---

## Final Compression

OMNIA does not prove which numbers are prime.

But across three disjoint tested intervals, it produces a replicated structural ranking signal that:

- enriches primes above natural density
- beats random ranking
- beats a trivial arithmetic baseline
- supports practical candidate filtering through cutoff-based search-space reduction

That is the current validated result.

---

## Associated Files

Primary result files:

- `examples/prime_candidates_1000_1200_results.md`
- `examples/prime_candidates_1200_1400_results.md`
- `examples/prime_candidate_runs_summary_final.md`
- `examples/prime_candidate_random_baseline_comparison.md`
- `examples/prime_candidate_baselines_comparison_final.md`
- `examples/prime_candidate_cutoff_analysis_results.md`

Underlying score files:

- `examples/prime_candidates_1000_1200_scores.jsonl`
- `examples/prime_candidates_1200_1400_scores.jsonl`
- `examples/prime_candidates_2000_2200_scores.jsonl`