# OMNIA Fragility Display v1

Status: public-facing minimal demonstration  
Purpose: show that near-equivalent math problems can produce answers with very different structural stability

---

## Claim

OMNIA does not need to know whether an answer is correct in order to detect whether the reasoning structure is stable.

This demo shows a simple but public result:

**two answers can both look acceptable on the surface, while one is structurally fragile and one is structurally stable.**

---

## Why this matters

Most evaluation systems ask only one question:

- is the final answer correct?

OMNIA asks a different question:

- how stable is the reasoning path that produced the answer?

That difference matters because a model can still be correct while already operating on a fragile structure.

A fragile answer is not yet a visible failure.  
It is a hidden failure waiting for a slightly harder variant.

---

## The Display

We use three near-equivalent variants from the same math-word-problem family.

The point is not to prove that the model cannot solve them.

The point is to show that **surface correctness does not imply structural reliability**.

---

## A — Stable baseline

**Problem**  
Benny saw a 10-foot shark with 2 6-inch remoras attached to it. What percentage of the shark's body length is the combined length of the remoras?

**Model output**  
The shark is 10 feet long, which is 120 inches. The remoras together are 2 x 6 = 12 inches. 12/120 = 0.1, so the combined length of the remoras is 10% of the shark's body length. Final answer: 10%

**Final extracted answer**  
`10`

**Expected answer**  
`10`

**Observed interpretation**  
Surface result is correct.  
Reasoning chain is short, direct, and structurally coherent.

**OMNIA reading**  
`High structural stability`

**Verdict**  
`Stable`

---

## B — Same family, symbolic pressure increased

**Problem**  
Rania saw a 210-foot whale with 7 72-inch remoras attached to it. What percentage of the whale's body length is the combined length of the remoras?

**Model output**  
The whale is 210 feet long, which is 210 x 12 = 2520 inches. The remoras together are 7 x 72 = 504 inches. 504/2520 = 0.2, so the combined length of the remoras is 20% of the whale's body length. Final answer: 20%

**Final extracted answer**  
`20`

**Expected answer**  
`20`

**Observed interpretation**  
Surface result is correct.  
But the instance carries larger numbers and a heavier symbolic load.

**OMNIA reading**  
`Lower structural stability than A`

**Verdict**  
`Correct but more fragile`

---

## C — Same family, distractor added

**Problem**  
Sanjay saw a 60-foot dolphin with 16 12-inch remoras attached to it. But a quarter of the remoras go away. What percentage of the dolphin's body length is the combined length of the remaining remoras?

**Model output**  
A quarter of 16 remoras go away, so 16 x 1/4 = 4 go away and 16 - 4 = 12 remain. Each remaining remora is 12 inches long, so their combined length is 12 x 12 = 144 inches. The dolphin is 60 feet long, which is 60 x 12 = 720 inches. 144/720 = 0.2, so the remaining remoras are 20% of the dolphin's body length. Final answer: 20%

**Final extracted answer**  
`20`

**Expected answer**  
`20`

**Observed interpretation**  
Surface result is still correct.  
But the reasoning chain now includes an extra distractor operation.

**OMNIA reading**  
`Lowest structural stability in the triplet`

**Verdict**  
`Structurally fragile`

---

## Fragility Matrix

| Variant | Surface Correctness | OMNIA Structural Stability | Collapse Risk | Public Reading |
|---|---|---|---|---|
| **A — Base** | ✅ Correct | 🟦 **HIGH** | Low | The answer is correct and the reasoning path is structurally solid. |
| **B — Symbolic Pressure** | ✅ Correct | 🟨 **MEDIUM** | Moderate | The answer is still correct, but the structure is already under symbolic stress. |
| **C — Distractor Added** | ✅ Correct | 🟥 **LOW** | High | The answer is correct on the surface, but the reasoning structure is fragile and close to collapse. |

---

## Compression

All three answers are correct.

That is exactly why this display matters.

A normal evaluator sees:

- correct
- correct
- correct

OMNIA sees:

- stable
- less stable
- fragile

So the point of OMNIA is not only to score correctness.

The point is to detect **how close a reasoning path is to collapse**, even when the final answer still looks acceptable.

---

## Reading Rule

This matrix is not a truth table.

It is a structural warning system.

A normal evaluator asks:

- Is the answer correct?

OMNIA asks:

- How stable is the reasoning path that produced it?

That is the difference between surface success and structural reliability.

---

## Public meaning

This is the practical message:

**Correctness alone is not enough.  
Structural stability matters.**

A model can be right for the wrong structural reasons.  
OMNIA is designed to measure that hidden difference.

---

## Minimal conclusion

This demo does not claim that OMNIA solves math.

It claims something smaller and stronger:

**OMNIA detects structural fragility across near-equivalent math problems, even when surface correctness is unchanged.**

---

## Final Public Message

Three answers can all be correct.

But they are not equally trustworthy.

OMNIA is designed to show that hidden difference before the visible failure happens.