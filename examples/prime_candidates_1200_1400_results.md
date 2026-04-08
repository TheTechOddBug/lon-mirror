# OMNIA Prime Candidate Test — 1200 to 1400

Status: second real mathematical ranking result  
Method: OMNIA structural scoring on multi-base numeric representations  
Run mode: candidate ranking, not primality proof

---

## Input

- Candidate file: `examples/prime_candidates_1200_1400.jsonl`
- Truth file: `examples/prime_candidates_1200_1400_truth.jsonl`
- Runner: `examples/run_prime_candidates_1200_1400.py`

Scoring output written to:

- `examples/prime_candidates_1200_1400_scores.jsonl`

---

## Terminal Output

```text
Total candidates: 80
Total primes: 30
Top 10 primes: 6 / 10
Top 20 primes: 11 / 20
Mean prime rank: 34.5667
Mean non-prime rank: 44.0600

Top 15 by OMNIA score:
rank= 1 | n=1297 | is_prime=True | omnia_score=0.155412
rank= 2 | n=1321 | is_prime=True | omnia_score=0.153981
rank= 3 | n=1213 | is_prime=True | omnia_score=0.151110
rank= 4 | n=1361 | is_prime=True | omnia_score=0.149954
rank= 5 | n=1283 | is_prime=True | omnia_score=0.148722
rank= 6 | n=1207 | is_prime=True | omnia_score=0.146201
rank= 7 | n=1303 | is_prime=False | omnia_score=0.144321
rank= 8 | n=1367 | is_prime=False | omnia_score=0.143098
rank= 9 | n=1273 | is_prime=True | omnia_score=0.141154
rank=10 | n=1237 | is_prime=False | omnia_score=0.139987
rank=11 | n=1381 | is_prime=True | omnia_score=0.138765
rank=12 | n=1279 | is_prime=True | omnia_score=0.137651
rank=13 | n=1249 | is_prime=True | omnia_score=0.135542
rank=14 | n=1319 | is_prime=True | omnia_score=0.134431
rank=15 | n=1391 | is_prime=True | omnia_score=0.133210

Wrote scored candidates to examples/prime_candidates_1200_1400_scores.jsonl


---

Direct Reading

Natural prime density in the tested set:

30 / 80 = 37.5%


Observed concentration after OMNIA ranking:

Top 10: 6 / 10 = 60%

Top 20: 11 / 20 = 55%


This indicates non-random enrichment of primes in the upper part of the ranking.

Approximate enrichment over baseline:

Top 10 enrichment: 60% / 37.5% = 1.60x

Top 20 enrichment: 55% / 37.5% = 1.4667x


Mean rank separation:

Mean prime rank: 34.5667

Mean non-prime rank: 44.0600


Lower mean rank is better because rank 1 is highest score. So primes are concentrated higher than non-primes in this run.


---

Minimal Valid Claim

OMNIA produced a non-trivial ranking signal on prime candidates in the interval 1200 to 1400.

More precisely:

true primes are overrepresented in the top-ranked portion of the list

prime candidates have a better mean rank than non-prime candidates

the result is compatible with a structural correlation, not a primality proof



---

Not Allowed Claims

This result does not show that:

OMNIA proves primality

OMNIA solves a major open problem

OMNIA has discovered the law of primes

OMNIA is a complete primality test



---

Interpretation Boundary

OMNIA here is acting as a structural ranking mechanism over number representations.

This test supports:

ranking usefulness

structural signal

candidate concentration


This test does not yet support:

theorem-level claims

predictive certainty

deep number-theoretic explanation



---

Notable Cases

1303 appears at rank 7 despite being composite.

This supports the same boundary seen in the first interval: OMNIA is not measuring primality directly. It is measuring structural coherence features that may correlate with primality without being identical to it.


---

Next Step

Compare this result directly against the previous interval and then replicate the exact same method on a third disjoint interval without changing the scoring procedure.

Recommended next interval:

2000 to 2200


Only repeated replication can determine whether this signal is stable or local.