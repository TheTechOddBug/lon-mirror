# Regularity Penalty Lambda Sweep — Results

Status: controlled stability scan for the regularity correction  
Scope: 240 candidates across three disjoint intervals  
Method: post-hoc OMNIA re-ranking under multiple values of λ  
Interpretation level: parameter stability analysis

---

## Goal

This sweep was designed to answer one narrow question:

**Is the regularity-penalty correction stable across a range of λ values, or does it improve ranking only at a single fragile point?**

The tested adjustment was:

```text
Ω_adjusted = Ω_raw - λ * regularity_penalty_norm

The goal was not to change OMNIA core yet. The goal was to identify whether a usable correction zone exists.


---

Tested Values

The following λ values were tested:

0.00

0.01

0.02

0.03

0.05

0.08



---

Terminal Output

=== REGULARITY PENALTY LAMBDA SWEEP ===

  lambda | top10 | top20 |  mean_prime |  mean_nonprime |       gap
------------------------------------------------------------------------
    0.00 |     7 |    12 |   33.151163 |      45.025974 | 11.874811
    0.01 |     8 |    13 |   32.848837 |      45.194805 | 12.345968
    0.02 |     8 |    15 |   32.558140 |      45.357143 | 12.799003
    0.03 |     8 |    16 |   32.220930 |      45.545455 | 13.324524
    0.05 |     8 |    17 |   32.255814 |      45.525974 | 13.270160
    0.08 |     8 |    17 |   32.616279 |      45.324675 | 12.708396

=== TRACKED NUMBERS BY LAMBDA ===

--- n = 1007 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |       11 |   0.923480 |   0.8123
    0.01 |       16 |   0.915357 |   0.8123
    0.02 |       24 |   0.907234 |   0.8123
    0.03 |       31 |   0.899111 |   0.8123
    0.05 |       44 |   0.882865 |   0.8123
    0.08 |       57 |   0.858496 |   0.8123

--- n = 2021 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |       35 |   0.887640 |   0.4901
    0.01 |       40 |   0.882739 |   0.4901
    0.02 |       47 |   0.877838 |   0.4901
    0.03 |       54 |   0.872937 |   0.4901
    0.05 |       67 |   0.863135 |   0.4901
    0.08 |       81 |   0.848432 |   0.4901

--- n = 2047 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |        6 |   0.932120 |   1.0000
    0.01 |       10 |   0.922120 |   1.0000
    0.02 |       17 |   0.912120 |   1.0000
    0.03 |       24 |   0.902120 |   1.0000
    0.05 |       34 |   0.882120 |   1.0000
    0.08 |       51 |   0.852120 |   1.0000

--- n = 1009 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |        7 |   0.931220 |   0.7251
    0.01 |       11 |   0.923969 |   0.7251
    0.02 |       12 |   0.916718 |   0.7251
    0.03 |       14 |   0.909467 |   0.7251
    0.05 |       17 |   0.894965 |   0.7251
    0.08 |       23 |   0.873212 |   0.7251

--- n = 2017 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |       30 |   0.892340 |   0.4321
    0.01 |       34 |   0.888019 |   0.4321
    0.02 |       37 |   0.883698 |   0.4321
    0.03 |       41 |   0.879377 |   0.4321
    0.05 |       45 |   0.870735 |   0.4321
    0.08 |       54 |   0.857772 |   0.4321

--- n = 2039 ---
  lambda | adj_rank |  adj_score | pen_norm
--------------------------------------------
    0.00 |       42 |   0.881230 |   0.3124
    0.01 |       48 |   0.878106 |   0.3124
    0.02 |       52 |   0.874982 |   0.3124
    0.03 |       58 |   0.871858 |   0.3124
    0.05 |       62 |   0.865610 |   0.3124
    0.08 |       72 |   0.856238 |   0.3124


---

Direct Reading

The correction is not fragile.

As λ increases from 0.00 to 0.05:

Top 10 primes improves from 7 to 8

Top 20 primes improves from 12 to 17

mean prime rank improves from 33.151163 to a best region around 32.22–32.26

mean non-prime rank worsens in the desired direction

the separation gap increases from 11.874811 to a peak of 13.324524


This means the correction operates over a stable interval, not at a single accidental point.


---

Best Regions

Best gap

The largest prime vs non-prime separation appears at:

λ = 0.03

gap = 13.324524


This is the strongest balanced setting.

Best Top 20 purity

The strongest Top 20 result appears at:

λ = 0.05

Top 20 primes = 17 / 20


This is the most aggressive setting among the tested values.

Saturation sign

At:

λ = 0.08


the gap decreases again:

12.708396


This indicates over-penalization is starting. The correction is no longer improving cleanly.


---

Tracked False Positives

The known composite traps are progressively pushed downward as λ increases.

2047

rank 6 -> 24 -> 34 -> 51 across the sweep

strongest example of a regularity-driven false positive being neutralized


1007

rank 11 -> 31 -> 44 -> 57


2021

rank 35 -> 54 -> 67 -> 81


This confirms that the penalty is acting in the intended direction.


---

Tracked Nearby Primes

Nearby legitimate primes also move downward, but less effectively in the key region than the strongest composite traps.

This is why λ cannot be increased without limit.

Examples:

1009: rank 7 -> 14 -> 17 -> 23

2017: rank 30 -> 41 -> 45 -> 54

2039: rank 42 -> 58 -> 62 -> 72


So the correction is useful, but not free. Past a certain point it starts to over-penalize structurally elegant primes as well.


---

Minimal Valid Claim

The regularity-penalty correction is stable across a non-trivial λ interval.

More precisely:

there is a clear improvement zone between λ = 0.01 and λ = 0.05

the correction consistently improves top-ranked prime concentration

the correction consistently suppresses the strongest regularity-driven composite traps

the correction eventually saturates and begins to over-penalize at higher λ



---

Practical Recommendation

Based on the tested values:

λ = 0.03 is the best balanced candidate

λ = 0.05 is the best aggressive candidate


Interpretation:

use 0.03 if the goal is overall ranking quality

use 0.05 if the goal is maximum top-20 purity

do not treat 0.08 as a good default



---

Not Yet Supported

This sweep does not yet prove that:

the correction should be integrated into OMNIA core immediately

the same λ will generalize unchanged to larger numeric ranges

regularity penalty alone explains every false positive


It only establishes that the correction is real, useful, and tunable.


---

Final Compression

The first causal correction did not just help at one point.

It opened a stable operating window.

Current best reading:

λ = 0.03 is the strongest balanced setting

λ = 0.05 is the strongest aggressive setting

the correction works

but it must still be treated as a tested refinement, not yet as a frozen law


