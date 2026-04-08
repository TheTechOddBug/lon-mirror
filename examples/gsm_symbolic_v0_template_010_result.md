# gsmsym_010 — OMNIA v0 result

Run output

Updated gsmsym_010 in examples/gsm_symbolic_v0_omnia_scores.jsonl
gsmsym_010 | base | omnia_score=0.1314 | fragility_rank=2
gsmsym_010 | clause_augmented | omnia_score=0.1077 | fragility_rank=3
gsmsym_010 | num_perturbed | omnia_score=0.1401 | fragility_rank=1

Template status

- template_id: gsmsym_010
- ordering_observed: num_perturbed > base > clause_augmented
- expected_order_respected: false
- all_answers_correct: true

Allowed interpretation

OMNIA measured gsmsym_010 successfully. The observed ordering was num_perturbed > base > clause_augmented, so the template does not satisfy the protocol’s expected ordering base > num_perturbed >= clause_augmented. All three variants were correct.