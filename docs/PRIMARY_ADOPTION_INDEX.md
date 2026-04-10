# Primary Adoption Index

This file defines the narrow external adoption index for OMNIA v1.0.

It exists to keep the integration entry path short, readable, and externally usable.

OMNIA should be adopted as a bounded post-hoc structural measurement layer.

It should not be read as a reasoning engine, semantic evaluator, or decision system.

---

## Primary adoption set

### 1. Minimal interface

`OMNIA_MINIMAL_INTERFACE.md`

Focus:
smallest readable integration surface.

Role:
first entry point for a new external integrator.

---

### 2. Full interface

`INTERFACE.md`

Focus:
explicit interaction boundary between OMNIA and a host system.

Role:
main interface reference after the minimal entry point.

---

### 3. Adapter path

`adapters/llm_output_adapter.py`

Focus:
practical bridge from structured LLM outputs to OMNIA-style measurement flow.

Role:
first concrete integration example.

---

### 4. Integration branch

`integrations/caios/`

Focus:
tested integration-oriented path where OMNIA signals are connected to a broader workflow.

Role:
strongest currently exposed adoption branch in the repository.

---

## Recommended adoption order

Read in this order:

1. `OMNIA_MINIMAL_INTERFACE.md`
2. `INTERFACE.md`
3. `adapters/llm_output_adapter.py`
4. `integrations/caios/`

This order moves from minimal interface, to boundary definition, to practical adapter path, to broader integration.

---

## How this index should be used

Use this index if the goal is to answer one of these questions quickly:

- Where should an external integrator start?
- What is the smallest usable OMNIA interface?
- Where is the first concrete adapter example?
- Where is the strongest currently exposed integration path?

This file is an index, not an integration report.

---

## Adoption boundary

This adoption path supports a bounded view of OMNIA as:

- a post-hoc structural measurement layer
- a runtime-compatible signal provider
- a bounded component for retry / escalation style workflows

It does not imply:

- semantic comprehension
- autonomous reasoning
- full deployment readiness in arbitrary environments
- replacement of host cognition
- replacement of a decision layer

The architectural boundary remains:

```text
measurement != inference != decision


---

Related files

README.md

docs/PRIMARY_BENCHMARKS.md

docs/PRIMARY_BENCHMARK_INDEX.md

docs/PRIMARY_ADOPTION_PATH.md


