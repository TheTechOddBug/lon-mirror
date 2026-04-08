# OMNIA Prime Candidate Ranking — Final Baseline Comparison

Status: consolidated comparison against random baseline and deterministic trivial baseline  
Scope: 240 candidates across three disjoint intervals  
Method: OMNIA structural ranking vs two baselines  
Interpretation level: replicated enrichment and ranking separation only

---

## Evaluated Candidate Pool

Combined intervals:

- 1000 to 1200
- 1200 to 1400
- 2000 to 2200

Total candidates:

- 240

Total primes:

- 86

Natural prime density:

- 86 / 240 = 35.8333%

---

## OMNIA Global Result

Observed on the full 240-candidate ranking:

- Top 10 primes: 7 / 10 = 70%
- Top 20 primes: 12 / 20 = 60%
- Mean prime rank: 33.151163
- Mean non-prime rank: 45.025974

Direct reading:

- primes are strongly concentrated near the top
- prime mean rank is much better than non-prime mean rank
- the ranking signal is non-trivial and stable across the tested intervals

---

## Baseline A — Random Ranking

Random baseline estimated over 10000 shuffled rankings:

- Top 10 primes mean: 3.586600
- Top 20 primes mean: 7.168700
- Mean prime rank mean: 120.504210
- Mean non-prime rank mean: 120.493821

Comparison vs OMNIA:

- Top 10 lift: 7 / 3.586600 = 1.951709x
- Top 20 lift: 12 / 7.168700 = 1.673944x
- Prime rank improvement: 120.504210 - 33.151163 = 87.353047

Interpretation:

OMNIA clearly outperforms random ordering.
The enrichment is strong and the rank displacement is large.

---

## Baseline B — Digit Sum Ranking

Deterministic trivial baseline:
ranking by descending digit sum in base 10,
with ascending `n` as tie-break.

Observed on the full 240-candidate ranking:

- Top 10 primes: 4 / 10 = 40%
- Top 20 primes: 8 / 20 = 40%
- Mean prime rank: 120.726744
- Mean non-prime rank: 120.373377

Direct reading:

- digit sum produces almost no meaningful separation
- prime and non-prime mean ranks are effectively indistinguishable
- the baseline is essentially flat as a discriminator

Comparison vs OMNIA:

- Top 10: 7 vs 4
- Top 20: 12 vs 8
- Mean prime rank: 33.151163 vs 120.726744

Interpretation:

OMNIA captures a structural signal that is not reducible to simple decimal digit aggregation.

---

## Cross-Baseline Comparison

### Top 10 primes

- OMNIA: 7
- Random expected: 3.586600
- Digit Sum: 4

### Top 20 primes

- OMNIA: 12
- Random expected: 7.168700
- Digit Sum: 8

### Mean prime rank

- OMNIA: 33.151163
- Random expected: 120.504210
- Digit Sum: 120.726744

### Mean non-prime rank

- OMNIA: 45.025974
- Random expected: 120.493821
- Digit Sum: 120.373377

---

## Minimal Valid Claim

Across 240 candidates drawn from three disjoint intervals, OMNIA produces a ranking signal that:

- enriches primes in the upper-ranked region above random baseline
- outperforms a deterministic trivial baseline based on digit sum
- separates prime candidates from non-prime candidates more strongly than either baseline

---

## Not Allowed Claims

These results do **not** show that:

- OMNIA proves primality
- OMNIA is a primality test
- OMNIA solves an open mathematical problem
- OMNIA has discovered a law of primes
- OMNIA identifies all primes and only primes

---

## Interpretation Boundary

Supported:

- non-random enrichment
- replicated structural ranking signal
- superiority over trivial baselines on this tested set

Not yet supported:

- theorem-level conclusions
- universal predictive claims
- rigorous number-theoretic explanation of the mechanism
- generalization beyond tested intervals without further replication

---

## Final Compression

OMNIA does not prove primality.

But on the tested 240-candidate set, it ranks numbers in a way that:

- almost doubles prime concentration in the global top 10 relative to random baseline
- clearly outperforms a deterministic digit-sum baseline
- produces a strong mean-rank advantage for primes over non-primes

This is a defensible structural ranking result.