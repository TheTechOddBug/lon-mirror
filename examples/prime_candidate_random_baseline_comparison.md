# OMNIA Prime Candidate Ranking vs Random Baseline

Status: cleaned global comparison across three intervals  
Scope: 240 candidates total  
Method: OMNIA structural ranking vs random ranking baseline  
Interpretation level: correlation and enrichment only, not primality proof

---

## Input

OMNIA score files:

- `examples/prime_candidates_1000_1200_scores.jsonl`
- `examples/prime_candidates_1200_1400_scores.jsonl`
- `examples/prime_candidates_2000_2200_scores.jsonl`

Baseline script:

- `examples/baseline_random_prime_ranking.py`

Run mode:

- global ranking over all 240 candidates
- random baseline simulated over 10000 shuffled rankings

---

## Terminal Output

```text
DEBUG: Actual top10 length: 10
DEBUG: Actual top20 length: 20
=== OMNIA vs RANDOM BASELINE ===
Total candidates: 240
Total primes: 86
Natural prime density: 0.358333

--- OMNIA observed ---
Top 10 primes: 7
Top 20 primes: 12
Mean prime rank: 33.151163
Mean non-prime rank: 45.025974

--- Random baseline expected ---
Top 10 primes mean: 3.586600
Top 20 primes mean: 7.168700
Mean prime rank mean: 120.504210
Mean non-prime rank mean: 120.493821

--- Lift over random ---
Top 10 lift: 1.951709
Top 20 lift: 1.673944
Prime rank improvement: 87.353047
Non-prime rank separation: 11.874811


---

Direct Reading

Natural prime density over the full set:

86 / 240 = 35.8333%


OMNIA global ranking:

Top 10 primes: 7 / 10 = 70%

Top 20 primes: 12 / 20 = 60%


Random baseline expectation:

Top 10 primes mean: 3.5866 / 10

Top 20 primes mean: 7.1687 / 20


Observed lift over random:

Top 10 lift: 1.951709x

Top 20 lift: 1.673944x


Mean rank comparison:

OMNIA mean prime rank: 33.151163

Random mean prime rank: 120.504210


Prime rank improvement over random:

87.353047 positions



---

Minimal Valid Claim

Across 240 candidates taken from three disjoint intervals, OMNIA produces a global ranking that enriches prime numbers above random baseline.

More precisely:

the top-ranked region contains substantially more primes than expected under random ranking

prime candidates receive much better mean rank than under random ordering

the effect remains visible after correcting earlier aggregation and counting errors



---

Not Allowed Claims

This comparison does not show that:

OMNIA proves primality

OMNIA is a primality test

OMNIA solves an open problem about primes

OMNIA identifies all primes and only primes



---

Interpretation Boundary

What this result supports:

non-random global enrichment

ranking usefulness

correlation between OMNIA score and primality


What this result does not yet support:

theorem-level conclusions

causal explanation in number theory

generalization beyond the tested intervals without further replication



---

Final Compression

OMNIA does not prove primality.

But on the tested 240-candidate set, it ranks numbers in a way that nearly doubles the concentration of primes in the global top 10 relative to random baseline.

