# OMNIA Prime Candidate Runs — Summary of First Two Intervals

Status: replicated structural ranking signal across two disjoint intervals  
Method: OMNIA structural scoring on multi-base numeric representations  
Scope: candidate ranking, not primality proof

---

## Interval A — 1000 to 1200

- Total candidates: 80
- Total primes: 32
- Natural prime density: 40%

Observed after OMNIA ranking:

- Top 10 primes: 7 / 10 = 70%
- Top 20 primes: 13 / 20 = 65%

Enrichment over baseline:

- Top 10 enrichment: 1.75x
- Top 20 enrichment: 1.625x

Mean ranks:

- Mean prime rank: 32.1250
- Mean non-prime rank: 46.0833

Rank gap:

- 13.9583

---

## Interval B — 1200 to 1400

- Total candidates: 80
- Total primes: 30
- Natural prime density: 37.5%

Observed after OMNIA ranking:

- Top 10 primes: 6 / 10 = 60%
- Top 20 primes: 11 / 20 = 55%

Enrichment over baseline:

- Top 10 enrichment: 1.60x
- Top 20 enrichment: 1.4667x

Mean ranks:

- Mean prime rank: 34.5667
- Mean non-prime rank: 44.0600

Rank gap:

- 9.4933

---

## Direct Comparison

Common pattern across both runs:

- OMNIA concentrates primes above baseline in the upper part of the ranking
- primes have better mean rank than non-primes
- the signal survives replication on a second disjoint interval

Differences across runs:

- the first interval is stronger
- the second interval is weaker but still clearly above baseline
- composite false positives still appear near the top, confirming that OMNIA is not directly measuring primality

---

## Minimal Valid Claim

Across two disjoint intervals, OMNIA shows a replicated non-trivial ranking signal on prime candidates.

More precisely:

- true primes are overrepresented in the top-ranked portion of the list
- prime candidates have systematically better mean rank than non-prime candidates
- the effect is replicated, but remains a ranking correlation rather than a primality proof

---

## Not Allowed Claims

These two runs do **not** show that:

- OMNIA proves primality
- OMNIA solves any major open problem
- OMNIA has discovered a law of primes
- OMNIA is a substitute for primality testing

---

## Interpretation Boundary

The current evidence supports:

- structural ranking usefulness
- repeated enrichment of primes near the top of the ranking
- non-random correlation between OMNIA score and primality

The current evidence does not yet support:

- theorem-level conclusions
- general predictive certainty
- explanation of why the correlation exists in number-theoretic terms

---

## Next Step

Run the exact same method on a third disjoint interval without changing the scoring procedure.

Recommended next interval:

- 2000 to 2200