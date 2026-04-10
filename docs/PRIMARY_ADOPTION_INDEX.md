# OMNIA Primary Adoption Index
## Canonical adapter and canonical integration

Status: active
Purpose: define the exact adoption entry points that represent OMNIA publicly

---

## 1. Rule

This file identifies the exact adoption entry points that should represent OMNIA publicly.

These are not necessarily the only adoption-related materials in the repo.
They are the canonical path for external readers and early integrators.

---

## 2. Canonical adapter

### `adapters/llm_output_adapter.py`

Role:
translate LLM-style outputs into OMNIA-compatible structural inputs.

Why it is canonical:
it is the clearest bridge between OMNIA and a real post-hoc measurement use case.

Public function:
show how OMNIA can sit after generation and before final trust or escalation decisions.

Boundary rule:
the adapter must remain thin.
It translates format.
It does not add semantic reasoning or decision logic.

---

## 3. Canonical integration

### `integrations/caios/`

Role:
represent the main real integration path currently visible in the repo.

Why it is canonical:
it is the only explicit integration path presently exposed and therefore the natural adoption anchor.

Public function:
show that OMNIA can be inserted into an external workflow as a structural measurement layer.

Boundary rule:
the integration must preserve:
measurement != inference != decision

OMNIA may measure signals.
The host system may decide what to do with them.

---

## 4. Interface dependency

The canonical adoption path depends on these two interface documents:

- `OMNIA_MINIMAL_INTERFACE.md`
- `INTERFACE.md`

Reading order:

1. `OMNIA_MINIMAL_INTERFACE.md`
2. `INTERFACE.md`
3. `adapters/llm_output_adapter.py`
4. `integrations/caios/`

This is the shortest valid adoption path for an external reader.

---

## 5. Public adoption claim supported by this path

The strongest supported claim is:

OMNIA can be connected to external workflows as a post-hoc structural measurement layer through a minimal interface, a thin adapter, and a concrete integration path.

This path does NOT support claims such as:

- OMNIA replaces the model
- OMNIA performs semantic reasoning
- OMNIA is a decision engine
- OMNIA solves downstream tasks by itself

---

## 6. Replacement rule

If a stronger adapter or integration becomes more representative in the future, this file must be updated explicitly.

No adoption path should become canonical by accident.

---

## 7. Final rule

OMNIA adoption must remain narrow, explicit, and technically readable.

One clear adapter and one clear integration are stronger than many scattered possibilities.