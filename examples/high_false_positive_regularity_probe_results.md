# High False Positive Regularity Probe — Results

Status: causal inspection step  
Scope: comparison between high-scoring composites and nearby true primes  
Purpose: identify which structural regularities are likely causing false positives

---

## Goal

This probe was designed to move from correlation to mechanism.

Question:

**Why do some composites receive OMNIA scores close to, or competitive with, nearby primes?**

This is not a scoring benchmark.  
It is a structural feature inspection step.

---

## Tested Pairs

The following composite / prime pairs were inspected:

- `1007` (composite) vs `1009` (prime)
- `2021` (composite) vs `2017` (prime)
- `2047` (composite) vs `2039` (prime)

---

## Metrics Used

For each number, across bases `2` to `16`, the probe measured:

- average Shannon entropy
- average dominant-character ratio
- average maximum run-length ratio
- average palindrome mismatch ratio
- count of low-entropy bases
- count of high-dominance bases
- count of quasi-palindromic bases
- count of high-run bases

A synthetic regularity score was also tracked:

- `regularity_signature`

This is not an OMNIA score.
It is a regularity inspection metric.

---

## Summary Table

| label | type | avg_entropy | avg_dominance | avg_run_ratio | avg_pal_mismatch | low_entropy | high_dom | quasi_pal | high_run | reg_signature |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1007 composite | comp | 1.1557 | 0.4485 | 0.3541 | 0.0889 | 6 | 1 | 14 | 2 | 23 |
| 1009 prime | prime | 1.1539 | 0.4735 | 0.3396 | 0.1667 | 6 | 2 | 11 | 2 | 21 |
| 2021 composite | comp | 1.3413 | 0.4071 | 0.3019 | 0.2000 | 4 | 0 | 11 | 0 | 15 |
| 2017 prime | prime | 1.2599 | 0.4300 | 0.3114 | 0.1444 | 5 | 1 | 11 | 1 | 18 |
| 2047 composite | comp | 1.1566 | 0.4756 | 0.4034 | 0.0333 | 5 | 3 | 14 | 3 | 25 |
| 2039 prime | prime | 1.3283 | 0.4137 | 0.2974 | 0.1556 | 3 | 0 | 11 | 0 | 14 |

---

## Main Findings

### 1. High-scoring composites can be more regular than nearby primes

This is the main result.

In the two clearest cases:

- `1007` has `regularity_signature = 23`, while `1009` has `21`
- `2047` has `regularity_signature = 25`, while `2039` has `14`

So the false positives are not merely "close" to primes.
They can be **more symbolically regular** than the nearby primes.

---

### 2. The strongest false positive is 2047

`2047` is the clearest regularity trap.

Known factorization:

- `2047 = 23 x 89`

Observed structural behavior:

- base 2: `11111111111`
- base 4: `133333`
- base 8: `3777`
- base 16: `7ff`

This gives:

- very low entropy in several bases
- very high dominant-character ratio
- very high run-length ratio
- near-zero palindrome mismatch in many bases

Interpretation:

`2047` behaves like an extreme regularity object, especially in small bases.
A system that rewards symbolic stability too strongly will tend to overvalue it.

---

### 3. 1007 behaves like a quasi-palindromic trap

`1007 = 19 x 53`

Observed behavior:

- quasi-palindromic structure across many bases
- especially strong in base 4: `33233`
- strong palindrome closeness across bases
- elevated regularity signature compared to the nearby prime

Interpretation:

`1007` is not being rewarded for primality.
It is being rewarded for structural elegance.

---

### 4. 2021 is a different kind of false positive

`2021 = 43 x 47`

This case is important because it does **not** fit the same pattern as strongly.

Observed:

- `2021` regularity signature = `15`
- nearby prime `2017` regularity signature = `18`

So `2021` is not a clear “regularity excess” case in the same way as `1007` and `2047`.

Interpretation:

There are at least two classes of false positives:

1. **decorative regularity false positives**
   - like `1007`
   - like `2047`

2. **structural proximity false positives**
   - like `2021`
   - likely linked to deeper cross-base similarity not captured by simple regularity metrics alone

---

## Minimal Valid Claim

This probe supports the following narrow claim:

**Some of the highest-scoring composite false positives are being rewarded for excessive symbolic regularity across bases.**

More precisely:

- high-scoring composites can show lower entropy
- higher run concentration
- stronger palindrome closeness
- and higher aggregate regularity signatures than nearby primes

This identifies a concrete failure mode in the current ranking configuration.

---

## What This Does Not Yet Prove

This probe does **not** yet prove that:

- regularity excess explains all false positives
- a regularity penalty will necessarily improve global ranking
- the best correction is already known

It only isolates one real mechanism strongly enough to justify targeted re-ranking experiments.

---

## Design Consequence

The current OMNIA numeric setup appears to reward:

- symbolic compactness
- repeated-character dominance
- quasi-palindromic stability
- cross-base aesthetic regularity

too strongly in some cases.

This suggests a next-step correction of the form:

```text
Ω_adjusted = Ω_raw - λ * regularity_penalty

where the penalty is applied to numbers with unusually strong regularity signatures.


---

Final Compression

Current conclusion:

OMNIA is not merely confusing composites with primes at random.

At least some of its strongest numeric false positives are being pulled upward by an identifiable structural bias:

excessive symbolic regularity across bases.

This is the first causal defect isolated in the prime-ranking configuration.