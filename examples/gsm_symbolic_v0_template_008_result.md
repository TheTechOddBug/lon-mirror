# gsmsym_008 — OMNIA v0 result

Run output

Updated gsmsym_008 in examples/gsm_symbolic_v0_omnia_scores.jsonl
gsmsym_008 | base | omnia_score=0.1395 | fragility_rank=1
gsmsym_008 | clause_augmented | omnia_score=0.1123 | fragility_rank=3
gsmsym_008 | num_perturbed | omnia_score=0.1281 | fragility_rank=2

Template status

- template_id: gsmsym_008
- ordering_observed: base > num_perturbed > clause_augmented
- expected_order_respected: true
- all_answers_correct: true

Allowed interpretation

OMNIA measured gsmsym_008 successfully. The observed ordering was base > num_perturbed > clause_augmented, so the template satisfies the protocol’s expected ordering base > num_perturbed >= clause_augmented. All three variants were correct.