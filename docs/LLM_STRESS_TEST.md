# OMNIA — LLM Stress Test (v1)

## Objective

Test Δ_struct against:
- logical reasoning
- fluent hallucination
- degenerated loops

## Results

logic_strong = 0.1654  
hallucination_fluent = 0.0821  
degenerated_loop = 0.0114  

## Invariant

logic > hallucination > loop

## Result

PASS

## Interpretation

- Fluency ≠ structure
- Hallucination loses relational stability
- Loops collapse structural diversity

## Limits

- manual dataset
- small sample
- not real LLM outputs

## Status

pre-validation