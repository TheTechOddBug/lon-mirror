# Primary Adoption Path

This file defines the shortest external adoption path for OMNIA v1.0.

OMNIA should be adopted as a bounded post-hoc structural measurement layer.

It should not be read as a reasoning engine, semantic evaluator, or decision system.

---

## Minimal adoption sequence

For an external integrator, the shortest usable path is:

1. `OMNIA_MINIMAL_INTERFACE.md`
2. `INTERFACE.md`
3. `adapters/llm_output_adapter.py`
4. `integrations/caios/`

This is the narrowest practical entry path currently exposed in the repository.

---

## Step 1 - Minimal interface

`OMNIA_MINIMAL_INTERFACE.md`

Purpose:
understand the smallest usable interface of OMNIA without entering the full repository structure.

Read this first if the goal is fast integration understanding.

---

## Step 2 - Full interface

`INTERFACE.md`

Purpose:
inspect the exposed interface in more detail, including the expected interaction boundary between OMNIA and an external host system.

Read this after the minimal interface.

---

## Step 3 - Adapter example

`adapters/llm_output_adapter.py`

Purpose:
inspect a concrete adapter path showing how structured LLM outputs can be passed into OMNIA-style measurement flow.

This is the practical bridge between interface and runtime use.

---

## Step 4 - Integration example

`integrations/caios/`

Purpose:
inspect the tested integration-oriented branch where OMNIA signals are connected to a broader workflow.

This is the strongest currently exposed integration path in the repository.

---

## Adoption rule

OMNIA adoption means:

- external structural measurement
- bounded signal extraction
- downstream usability by host systems

OMNIA adoption does not mean:

- replacing the host model
- replacing reasoning
- replacing verification
- replacing a decision layer

The architectural boundary remains:

```text
measurement != inference != decision