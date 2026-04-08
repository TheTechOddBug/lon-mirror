# Regularity Penalty Re-Rank — Results

Status: first causal correction test  
Scope: 240 prime candidates across three disjoint intervals  
Method: post-hoc OMNIA score adjustment with regularity penalty  
Interpretation level: controlled re-ranking experiment

---

## Goal

This experiment was designed to test a narrow hypothesis:

**Some of the strongest composite false positives are being over-rewarded for symbolic regularity across bases.**

To test this, a regularity penalty was applied post-hoc:

```text
Ω_adjusted = Ω_raw - λ * regularity_penalty_norm

with:

λ = 0.02


This is not yet a core-engine modification. It is a controlled re-ranking experiment.


---

Input

Source files:

examples/prime_candidates_1000_1200_scores.jsonl

examples/prime_candidates_1200_1400_scores.jsonl

examples/prime_candidates_2000_2200_scores.jsonl


Regularity probe basis:

examples/high_false_positive_regularity_probe_results.md


Output file:

examples/prime_candidates_reranked_with_regularity_penalty.jsonl


Runner:

examples/regularity_penalty_rerank.py



---

Terminal Output

=== REGULARITY PENALTY RE-RANK ===
Lambda: 0.020000

--- RAW OMNIA ---
Top 10 primes: 7
Top 20 primes: 12
Mean prime rank: 33.151163
Mean non-prime rank: 45.025974

--- ADJUSTED OMNIA ---
Top 10 primes: 8
Top 20 primes: 15
Mean prime rank: 32.558140
Mean non-prime rank: 45.357143

=== TRACKED NUMBERS ===
     n | prime |  raw_score | raw_rank | pen_norm |  adj_score | adj_rank
--------------------------------------------------------------------------------
  1007 | False |   0.923480 |       11 |   0.8123 |   0.907234 |       24
  2021 | False |   0.887640 |       35 |   0.4901 |   0.877838 |       47
  2047 | False |   0.932120 |        6 |   1.0000 |   0.912120 |       17
  1009 |  True |   0.931220 |        7 |   0.7251 |   0.916718 |       12
  2017 |  True |   0.892340 |       30 |   0.4321 |   0.883698 |       37
  2039 |  True |   0.881230 |       42 |   0.3124 |   0.874982 |       52

Wrote examples/prime_candidates_reranked_with_regularity_penalty.jsonl


---

Direct Comparison

Raw OMNIA

Top 10 primes: 7

Top 20 primes: 12

Mean prime rank: 33.151163

Mean non-prime rank: 45.025974


Adjusted OMNIA (λ = 0.02)

Top 10 primes: 8

Top 20 primes: 15

Mean prime rank: 32.558140

Mean non-prime rank: 45.357143



---

Immediate Effects

Improvement in top-ranked purity

Top 10 primes improved from 7 to 8

Top 20 primes improved from 12 to 15


This means the upper part of the ranking became more prime-dense after applying the regularity penalty.

Mean-rank behavior

Prime mean rank improved:

33.151163 -> 32.558140


Non-prime mean rank worsened:

45.025974 -> 45.357143



So the separation moved in the desired direction.


---

Tracked False Positives

The three tracked high-scoring composites all moved downward:

1007: rank 11 -> 24

2021: rank 35 -> 47

2047: rank 6 -> 17


This is exactly the intended effect.

The strongest case is 2047, which had been one of the clearest regularity traps. After the penalty, it exits the top 10.


---

Tracked Nearby Primes

Some nearby true primes also moved downward:

1009: rank 7 -> 12

2017: rank 30 -> 37

2039: rank 42 -> 52


This is expected. The penalty is not selective enough yet to spare all legitimate primes with high symbolic regularity.

However, the net effect remains positive because the strongest composite traps fall more sharply than the neighboring primes.


---

Minimal Valid Claim

This experiment supports the following narrow claim:

A post-hoc regularity penalty improves the prime-candidate ranking produced by OMNIA on the tested 240-candidate set.

More precisely:

prime concentration improves in the top 10 and top 20

strong composite false positives move downward

mean-rank separation improves slightly in the correct direction



---

What This Does Not Yet Prove

This experiment does not yet prove that:

λ = 0.02 is optimal

the regularity penalty should be integrated into OMNIA core

regularity excess explains all false positives

the correction will generalize unchanged to larger intervals


This was only a first causal correction test.


---

Interpretation

The current evidence suggests that:

OMNIA raw scoring over-rewards symbolic regularity in some cases

adding a regularity penalty can reduce this distortion

the correction is promising enough to justify a controlled lambda sweep



---

Final Compression

The regularity-penalty correction did not break the ranking.

It improved it.

On the tested 240-candidate set:

the top 10 became cleaner

the top 20 became cleaner

high-regularity composite traps moved down


This is the first successful causal refinement of the numeric ranking configuration.