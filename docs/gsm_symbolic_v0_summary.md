# OMNIA x GSM-style mini-set v0 — summary

## Final status

- templates_total: 10
- conforming_templates: 5
- non_conforming_templates: 5
- all_variants_correct_templates: 9
- templates_with_incorrect_variants: 1
- total_records: 30
- correct_records: 27
- incorrect_records: 3
- clause_rank_3_consistency: 10/10

## Final technical statement

The mini-set v0 is complete. The expected ordering base > num_perturbed >= clause_augmented was respected in 5 out of 10 templates. The ordering failed in the other 5 templates because num_perturbed scored above base. However, clause_augmented was the least stable variant in all 10 templates. Only gsmsym_003 contained incorrect answers; all other templates were fully correct.

## Template-level results

| Template | Base Omega | Num Omega | Clause Omega | Status | Correctness |
|---|---:|---:|---:|---|---|
| 001 | 0.1428 | 0.1256 | 0.1084 | Conforming | 3/3 |
| 002 | 0.1384 | 0.1501 | 0.1092 | Non-conforming | 3/3 |
| 003 | 0.0754 | 0.0821 | 0.0612 | Non-conforming | 0/3 |
| 004 | 0.1412 | 0.1304 | 0.1156 | Conforming | 3/3 |
| 005 | 0.1325 | 0.1458 | 0.1211 | Non-conforming | 3/3 |
| 006 | 0.1342 | 0.1297 | 0.1189 | Conforming | 3/3 |
| 007 | 0.1482 | 0.1244 | 0.1102 | Conforming | 3/3 |
| 008 | 0.1395 | 0.1281 | 0.1123 | Conforming | 3/3 |
| 009 | 0.1381 | 0.1422 | 0.1198 | Non-conforming | 3/3 |
| 010 | 0.1314 | 0.1401 | 0.1077 | Non-conforming | 3/3 |

## Strongest result supported by v0

- clause_augmented is the least stable variant in 10 out of 10 templates

## Results not supported as universal laws

- base is not always more stable than num_perturbed
- the ordering base > num_perturbed is only observed in 5 out of 10 templates

## Minimal interpretation boundary

Allowed:
- OMNIA detected a consistent structural fragility signal for clause-augmented variants in this 10-template GSM-style mini-set.
- OMNIA separated clause-augmented variants from base and number-perturbed variants across all templates in this v0 slice.

Not allowed:
- OMNIA solves mathematical reasoning
- OMNIA proves truth
- OMNIA universally ranks base above num_perturbed
- OMNIA measures hallucination risk as a validated general law