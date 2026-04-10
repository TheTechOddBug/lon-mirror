# OMNIA Primary Adoption Path
## What counts as real adoption and what does not

Status: active
Purpose: define the narrow external adoption path of OMNIA

---

## 1. Rule

OMNIA adoption does not mean broad conceptual recognition.

It means that OMNIA can be used by another system, pipeline, evaluator, or developer as a post-hoc structural measurement layer.

Adoption must stay narrow and concrete.

---

## 2. Primary adoption assets

The adoption layer of OMNIA should be centered on these assets:

- `INTERFACE.md`
- `OMNIA_MINIMAL_INTERFACE.md`
- `integrations/`
- `adapters/`

These define how OMNIA can be connected to external workflows.

---

## 3. Primary adoption path

The canonical adoption path should stay simple:

### A. Minimal interface
Define the smallest stable input/output contract required to use OMNIA.

Goal:
make OMNIA understandable as a tool, not only as a theory.

### B. Thin adapters
Adapters should translate host-system data into OMNIA inputs and return OMNIA outputs without adding host logic.

Goal:
keep the boundary clean.

### C. One or two real integrations
Only a very small number of integrations should be treated as central.

Goal:
show that OMNIA can be inserted into an actual workflow.

### D. One concrete case study
At least one adoption story should show that OMNIA changed or supported a real pipeline decision.

Goal:
move from architecture claim to practical relevance.

---

## 4. What does NOT count as adoption

The following do not count as real adoption by themselves:

- additional theories
- new naming layers
- side experiments without integration value
- historical scripts
- broad claims without interface usage
- results that cannot be connected to a workflow

Interesting internal work is not adoption.

---

## 5. Canonical adoption order

External users should be able to follow this path:

1. read `OMNIA_MINIMAL_INTERFACE.md`
2. read `INTERFACE.md`
3. inspect one adapter
4. inspect one integration
5. inspect one case study

If this path is not clear, adoption is still weak.

---

## 6. Integration rule

An integration is central only if it satisfies most of these:

- uses the minimal interface or a clear extension of it
- preserves the boundary:
  measurement != inference != decision
- has a clear input/output flow
- demonstrates a realistic use case
- can be understood without reading repo history

If not, it is secondary or exploratory.

---

## 7. Public adoption positioning

Public adoption claims must stay limited to this:

OMNIA can be integrated as an external structural measurement layer into selected workflows.

Avoid stronger claims such as:

- OMNIA replaces model reasoning
- OMNIA is a general intelligence layer
- OMNIA directly solves downstream tasks
- OMNIA makes final decisions

---

## 8. Immediate execution rule

From now on, adoption work should be classified as:

- primary adoption
- secondary integration
- exploratory integration
- archived

No integration should become central by accident.

---

## 9. Final rule

OMNIA adoption is successful only when another system can use it with minimal friction and without semantic confusion.

The goal is not expansion of concept.
The goal is external usability.