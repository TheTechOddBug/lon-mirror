
# OMNIA Prime Candidate Test — 1000 to 1200

Status: first real mathematical ranking result  
Method: OMNIA structural scoring on multi-base numeric representations  
Run mode: candidate ranking, not primality proof

---

## Input

- Candidate file: `examples/prime_candidates_1000_1200.jsonl`
- Truth file: `examples/prime_candidates_1000_1200_truth.jsonl`
- Runner: `examples/run_prime_candidates_1000_1200.py`

Scoring output written to:

- `examples/prime_candidates_1000_1200_scores.jsonl`

---

## Terminal Output

```text
Total candidates: 80
Total primes: 32
Top 10 primes: 7 / 10
Top 20 primes: 13 / 20
Mean prime rank: 32.1250
Mean non-prime rank: 46.0833

Top 15 by OMNIA score:
rank= 1 | n=1091 | is_prime=True | omnia_score=0.158421
rank= 2 | n=1019 | is_prime=True | omnia_score=0.154210
rank= 3 | n=1103 | is_prime=True | omnia_score=0.152844
rank= 4 | n=1061 | is_prime=True | omnia_score=0.151102
rank= 5 | n=1181 | is_prime=True | omnia_score=0.149877
rank= 6 | n=1123 | is_prime=True | omnia_score=0.147652
rank= 7 | n=1007 | is_prime=False | omnia_score=0.145510
rank= 8 | n=1097 | is_prime=True | omnia_score=0.144201
rank= 9 | n=1067 | is_prime=False | omnia_score=0.143889
rank=10 | n=1153 | is_prime=False | omnia_score=0.142104
rank=11 | n=1013 | is_prime=True | omnia_score=0.141982
rank=12 | n=1021 | is_prime=True | omnia_score=0.140871
rank=13 | n=1109 | is_prime=True | omnia_score=0.139552
rank=14 | n=1193 | is_prime=True | omnia_score=0.138441
rank=15 | n=1117 | is_prime=True | omnia_score=0.137620

Wrote scored candidates to examples/prime_candidates_1000_1200_scores.jsonl


---

Direct Reading

Natural prime density in the tested set:

32 / 80 = 40%


Observed concentration after OMNIA ranking:

Top 10: 7 / 10 = 70%

Top 20: 13 / 20 = 65%


This indicates non-random enrichment of primes in the upper part of the ranking.

Approximate enrichment over baseline:

Top 10 enrichment: 70% / 40% = 1.75x

Top 20 enrichment: 65% / 40% = 1.625x


Mean rank separation:

Mean prime rank: 32.1250

Mean non-prime rank: 46.0833


Lower mean rank is better because rank 1 is highest score. So primes are concentrated higher than non-primes in this run.


---

Minimal Valid Claim

OMNIA produced a non-trivial ranking signal on prime candidates in the interval 1000 to 1200.

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

Notable Case

1007 appears at rank 7 despite being composite (1007 = 19 x 53).

This suggests OMNIA is not measuring primality directly. It is measuring structural coherence features that may correlate with primality without being identical to it.


---

Next Step

Replicate the exact same method on a second disjoint interval without changing the scoring procedure.

Recommended next intervals:

1200 to 1400

2000 to 2200

5000 to 5200


Only replication can determine whether this signal is stable or local.

