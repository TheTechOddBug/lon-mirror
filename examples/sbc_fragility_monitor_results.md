# SBC Fragility Monitor Results

Status: display-branch benchmark  
Scope: 1 reasoning triplet with 3 near-equivalent variants  
Purpose: show that surface correctness can remain constant while structural stability changes

---

## Input

Source file:

- `examples/fragility_display_triplets_v1.jsonl`

Runner:

- `examples/benchmark_fragility_display.py`

Generated score file:

- `examples/fragility_display_triplets_v1_scores.jsonl`

---

## Terminal Output

```text
=== FRAGILITY DISPLAY BENCHMARK ===
rank=1 | variant=A_base | omega_total=0.924150 | is_correct=True
rank=2 | variant=B_symbolic_pressure | omega_total=0.881230 | is_correct=True
rank=3 | variant=C_distractor_added | omega_total=0.741200 | is_correct=True

Wrote examples/fragility_display_triplets_v1_scores.jsonl
Wrote examples/sbc_fragility_monitor_results.md


---

Core result

All three variants are correct on the surface.

OMNIA still separates them by structural stability.


---

Fragility table

Variant	is_correct	omega_total	Structural Stability	Collapse Risk

A_base	true	0.924150	HIGH	Low
B_symbolic_pressure	true	0.881230	MEDIUM	Moderate
C_distractor_added	true	0.741200	LOW	High



---

Ranked reading

Rank 1 — A_base

omega_total: 0.924150

is_correct: true

final_extracted_answer: 10

expected_answer: 10


Interpretation:

This is the most stable variant. The reasoning path is short, direct, and structurally coherent.


---

Rank 2 — B_symbolic_pressure

omega_total: 0.881230

is_correct: true

final_extracted_answer: 20

expected_answer: 20


Interpretation:

The answer remains correct, but symbolic pressure is higher. OMNIA detects a measurable drop in structural stability even without visible failure.


---

Rank 3 — C_distractor_added

omega_total: 0.741200

is_correct: true

final_extracted_answer: 20

expected_answer: 20


Interpretation:

This is the most fragile variant. The answer is still correct on the surface, but the reasoning path shows strong structural fatigue.


---

Compression

A standard evaluator sees three correct answers.

OMNIA sees three different stability levels.

That is the point of the display.

The system is not only evaluating whether an answer is correct. It is evaluating how close the reasoning structure is to collapse.


---

Minimal valid claim

This benchmark supports the following narrow claim:

OMNIA detects structural fragility across near-equivalent math reasoning variants, even when final correctness remains unchanged.


---

Public meaning

This is the practical message:

correct does not automatically mean reliable

a model can still be right while already becoming structurally fragile

OMNIA exposes that hidden pre-error state



---

Final compression

This is the display-level result of OMNIA:

A is correct and structurally solid

B is correct but already stressed

C is correct on the surface but structurally fragile


So the visible answer does not tell the whole story.

OMNIA is designed to measure the part that standard evaluation misses.