# gsmsym_005 — OMNIA v0 result

Run output

Updated gsmsym_005 in examples/gsm_symbolic_v0_omnia_scores.jsonl
gsmsym_005 | base | omnia_score=0.1325 | fragility_rank=2
gsmsym_005 | clause_augmented | omnia_score=0.1211 | fragility_rank=3
gsmsym_005 | num_perturbed | omnia_score=0.1458 | fragility_rank=1

Template status

- template_id: gsmsym_005
- ordering_observed: num_perturbed > base > clause_augmented
- expected_order_respected: false
- all_answers_correct: true

Allowed interpretation

OMNIA measured gsmsym_005 successfully. The observed ordering was num_perturbed > base > clause_augmented, so the template does not satisfy the protocol’s expected ordering base > num_perturbed >= clause_augmented. However, clause_augmented remained the least stable variant while all three answers were correct.