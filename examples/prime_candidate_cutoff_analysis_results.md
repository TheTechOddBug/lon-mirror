# OMNIA Prime Candidate Cutoff Analysis

Status: cutoff-based search-space reduction result  
Scope: 240 candidates across three disjoint intervals  
Method: global OMNIA ranking over merged candidate set  
Interpretation level: ranking-based filtering, not primality proof

---

## Input

Score files used:

- `examples/prime_candidates_1000_1200_scores.jsonl`
- `examples/prime_candidates_1200_1400_scores.jsonl`
- `examples/prime_candidates_2000_2200_scores.jsonl`

Runner:

- `examples/prime_candidate_cutoff_analysis.py`

---

## Terminal Output

```text
=== OMNIA PRIME CANDIDATE CUTOFF ANALYSIS ===
Total candidates: 240
Total primes: 86
Natural prime density: 0.358333

  cutoff |   kept | primes |     recall |    density |       lift
--------------------------------------------------------------------
      5% |     12 |      7 |    0.0814 |    0.5833 |    1.6280
     10% |     24 |     14 |    0.1628 |    0.5833 |    1.6280
     20% |     48 |     24 |    0.2791 |    0.5000 |    1.3953
     25% |     60 |     29 |    0.3372 |    0.4833 |    1.3488
     50% |    120 |     51 |    0.5930 |    0.4250 |    1.1860


---

Direct Reading

Natural prime density over the full candidate pool:

86 / 240 = 35.8333%


Observed after OMNIA ranking:

Top 5% subset density: 58.33%

Top 10% subset density: 58.33%

Top 20% subset density: 50.00%

Top 25% subset density: 48.33%

Top 50% subset density: 42.50%


This shows a consistent enrichment of primes in the upper part of the OMNIA ranking.


---

Interpretation

The top-ranked region is the most valuable region.

The signal decays smoothly as more candidates are retained:

Lift at 5%: 1.6280x

Lift at 10%: 1.6280x

Lift at 20%: 1.3953x

Lift at 25%: 1.3488x

Lift at 50%: 1.1860x


This is consistent with a real ranking signal rather than an unstable or random cluster.


---

Search-Space Reduction Reading

If only the top 10% of OMNIA-ranked candidates are retained:

candidates kept: 24

primes kept: 14

prime recall: 16.28%

prime density in subset: 58.33%


If only the top 20% are retained:

candidates kept: 48

primes kept: 24

prime recall: 27.91%

prime density in subset: 50.00%


If only the top 50% are retained:

candidates kept: 120

primes kept: 51

prime recall: 59.30%

prime density in subset: 42.50%


So OMNIA can be read as a ranking-based filter that increases prime density above baseline while retaining a controllable fraction of true primes.


---

Minimal Valid Claim

OMNIA supports non-trivial search-space reduction on this tested candidate pool.

More precisely:

keeping only the top-ranked portion of candidates increases the concentration of primes above natural density

the enrichment is strongest at small cutoffs

the signal decays gradually rather than collapsing immediately



---

Not Allowed Claims

This result does not show that:

OMNIA proves primality

OMNIA is a primality test

OMNIA solves an open number-theoretic problem

OMNIA provides universal prime prediction



---

Final Compression

OMNIA does not prove which numbers are prime.

But on the tested 240-candidate set, it produces a ranking that can be used as a practical filter: smaller top-cut subsets contain a meaningfully higher density of primes than the raw candidate pool.

