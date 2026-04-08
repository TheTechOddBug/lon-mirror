# OMNIA Prime Candidate Runs — Final Summary Across Three Intervals

Status: replicated structural ranking signal across three disjoint intervals  
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

## Interval C — 2000 to 2200

- Total candidates: 80
- Total primes: 24
- Natural prime density: 30%

Observed after OMNIA ranking:

- Top 10 primes: 6 / 10 = 60%
- Top 20 primes: 11 / 20 = 55%

Enrichment over baseline:

- Top 10 enrichment: 2.00x
- Top 20 enrichment: 1.8333x

Mean ranks:

- Mean prime rank: 32.7917
- Mean non-prime rank: 43.8036

Rank gap:

- 11.0119

Note:
- `2047` is composite (`23 x 89`) and was corrected in the truth file before finalizing this interval.
- High-scoring composites remain part of the observed behavior and must be treated as false positives, not ignored.

---

## Combined Totals Across All Three Runs

- Total candidates: 240
- Total primes: 86
- Natural prime density: 86 / 240 = 35.8333%

Observed after OMNIA ranking:

- Top 10 across 3 runs: 19 / 30 = 63.3333%
- Top 20 across 3 runs: 35 / 60 = 58.3333%

Combined enrichment over baseline:

- Top 10 enrichment: 63.3333% / 35.8333% = 1.7674x
- Top 20 enrichment: 58.3333% / 35.8333% = 1.6279x

Combined mean ranks:

- Mean prime rank:
  - ((32 x 32.1250) + (30 x 34.5667) + (24 x 32.7917)) / 86
  - = 33.1027

- Mean non-prime rank:
  - ((48 x 46.0833) + (50 x 44.0600) + (56 x 43.8036)) / 154
  - = 44.6110

Combined rank gap:

- 44.6110 - 33.1027 = 11.5083

---

## Direct Reading

Across three disjoint intervals, OMNIA repeatedly places true primes above baseline in the upper part of the ranking.

This pattern appears in three independent ways:

1. Prime density in the top-ranked region is consistently above the natural density of the tested set.
2. Mean prime rank is consistently better than mean non-prime rank.
3. The effect persists across all three intervals without changing the scoring procedure.

---

## Minimal Valid Claim

Across three disjoint intervals, OMNIA shows a replicated non-trivial ranking signal on prime candidates.

More precisely:

- true primes are overrepresented in the top-ranked portion of the list
- prime candidates have systematically better mean rank than non-prime candidates
- the effect replicates across all three tested intervals
- the result supports structural correlation, not primality proof

---

## Not Allowed Claims

These runs do **not** show that:

- OMNIA proves primality
- OMNIA solves a major open mathematical problem
- OMNIA has discovered the law of primes
- OMNIA is a replacement for primality testing
- OMNIA identifies all primes and only primes

---

## Interpretation Boundary

The current evidence supports:

- structural ranking usefulness
- repeated enrichment of primes near the top of the ranking
- non-random correlation between OMNIA score and primality

The current evidence does not yet support:

- theorem-level conclusions
- general predictive certainty
- explanation of the mechanism in rigorous number-theoretic terms

---

## Notable Boundary Condition

Composite numbers such as:

- `1007 = 19 x 53`
- `2021 = 43 x 47`
- `2047 = 23 x 89`

can still receive high OMNIA scores.

This confirms a central boundary:

OMNIA is not directly measuring primality.
It is measuring a structural property that correlates with primality but is not identical to it.

---

## Final Compression

Current result:

OMNIA produces a replicated ranking signal on prime candidates across three disjoint intervals, with enrichment well above baseline in the upper-ranked region.

Current limit:

This is a structural ranking result, not a proof of primality and not a resolution of a major open problem.

---

## Next Step

Freeze this result as baseline evidence.

Then move to one of the following:

1. Replicate on a fourth, more distant interval
2. Compare against a simple baseline ranking
3. Search for which structural features are driving the enrichment