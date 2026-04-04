

# OMNIA — Validation Pipeline v1

## Status
- Step 1: closed
- Step 2: closed
- Step 3: closed
- Step 4: defined
- System: specified, falsifiable, not yet executed

---

## Step 1 — F (Transformations + Distances)

F = { (G1, d1), (G2, d2), (G3, d3) }

- Same transformation class
- Different intensities
- Reproducible

---

## Step 2 — Stability (kappa)

Local constraints:

Inv(x) <= k1  
Inv2(x) <= k2  

k1, k2:
- derived from baseline (structured)
- robust estimation preferred (median + MAD)
- bootstrap required

Important:
kappa is measured, not chosen

---

## Step 3 — Dataset B

B = B_structured ∪ B_perturbed ∪ B_random

Size:
- 100 structured
- 100 perturbed
- 100 random

Format (JSONL):

```json
{
  "id": "...",
  "class": "structured|perturbed|random",
  "text": "..."
}

Constraints:

same token length distribution

same charset

same format

perturbed derived from structured


Goal: structure != superficial differences


---

Step 4 — Separability Benchmark

For each x: Omega(x)

Distributions:

Omega_s

Omega_p

Omega_r


Constraint: E[Omega_s] > E[Omega_p] > E[Omega_r]


---

Metrics

1. Gaps

Delta_sp = E[Omega_s] - E[Omega_p]
Delta_pr = E[Omega_p] - E[Omega_r]


---

2. Effect size (mandatory)

d_sp = Delta_sp / sigma_pooled
d_pr = Delta_pr / sigma_pooled

Minimum:

d_sp > 0.5

d_pr > 0.5



---

3. Overlap

Low overlap required between:

Omega_s vs Omega_p

Omega_p vs Omega_r



---

4. Bootstrap

P(order preserved) >= tau


---

Failure Modes

System fails if:

1. Ordering violated


2. Positive gaps but low effect size


3. High overlap


4. High variance


5. Stability ok but no separability




---

Critical Insight

Step 2 != Step 4

Step 2: stability

Step 4: information


System can be stable but useless.


---

Final State

Theory: closed

Method: closed

Dataset: defined

Metrics: defined

System: specified, falsifiable, not yet executed



