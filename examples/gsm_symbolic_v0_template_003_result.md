# gsmsym_003 — OMNIA v0 result

Run output

Updated gsmsym_003 in examples/gsm_symbolic_v0_omnia_scores.jsonl
gsmsym_003 | base | omnia_score=0.0754 | fragility_rank=2
gsmsym_003 | clause_augmented | omnia_score=0.0612 | fragility_rank=3
gsmsym_003 | num_perturbed | omnia_score=0.0821 | fragility_rank=1

Template status

- template_id: gsmsym_003
- ordering_observed: num_perturbed > base > clause_augmented
- expected_order_respected: false
- all_answers_correct: false

Allowed interpretation

OMNIA measured gsmsym_003 successfully. The observed ordering was num_perturbed > base > clause_augmented, so the template does not satisfy the protocol’s expected ordering base > num_perturbed >= clause_augmented. All three variants were incorrect, and the overall Omega levels were lower than in gsmsym_001 and gsmsym_002.