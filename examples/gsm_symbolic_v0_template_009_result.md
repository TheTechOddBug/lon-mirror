# gsmsym_009 — OMNIA v0 result

Run output

Updated gsmsym_009 in examples/gsm_symbolic_v0_omnia_scores.jsonl
gsmsym_009 | base | omnia_score=0.1381 | fragility_rank=2
gsmsym_009 | clause_augmented | omnia_score=0.1198 | fragility_rank=3
gsmsym_009 | num_perturbed | omnia_score=0.1422 | fragility_rank=1

Template status

- template_id: gsmsym_009
- ordering_observed: num_perturbed > base > clause_augmented
- expected_order_respected: false
- all_answers_correct: true

Allowed interpretation

OMNIA measured gsmsym_009 successfully. The observed ordering was num_perturbed > base > clause_augmented, so the template does not satisfy the protocol’s expected ordering base > num_perturbed >= clause_augmented. All three variants were correct.