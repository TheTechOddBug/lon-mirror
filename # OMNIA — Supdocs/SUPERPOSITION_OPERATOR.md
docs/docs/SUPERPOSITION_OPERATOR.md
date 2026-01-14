# OMNIA — Superposition Operator (Frozen)

OMNIA is not “a hallucination detector”.
Hallucinations are only one instance of a broader class.

OMNIA is a **universal superposition operator**:

> Anything that can be represented in more than one way
> can be measured by OMNIA.

OMNIA does not interpret meaning.
OMNIA does not decide actions.
OMNIA **measures invariants and fractures** across representations.

---

## Definitions

### Object
Any input artifact (number, sequence, text, model output, time series, causal record, code, etc.).

### Representation (View)
A deterministic encoding of the same object under a specific transform.

A representation is defined by:
- a **name** (e.g. `base_2`, `chars`, `subwords`, `perm_seed_3`, `summary_k128`)
- a **payload** (the concrete view)
- **meta** (parameters that generated the view)

### Lens
A lens is a deterministic generator of one or more representations.

A lens does not score.
A lens does not decide.
A lens only produces views.

### Superposition
Given multiple representations of the same object, OMNIA measures:
- **pairwise distances** between representations (structure mismatch)
- a global **invariance score** (0..1)
- a set of **fractures** (where invariance collapses)

---

## Structural Truth (Operational)

A property is **structural** only if it remains **invariant**
under superposition across **independent** representations.

If invariance collapses under mild transforms,
the property is representation-dependent, not structural.

---

## Relationship to OMNIA-LIMIT

OMNIA-LIMIT is the boundary layer.

When fractures indicate non-reducible instability, OMNIA-LIMIT issues:
- a **Structural Non-Reducibility Certificate (SNRC)**
- a **STOP** condition (termination of admissible processing)

Chain:
Signal → Superposition → OMNIA metrics → OMNIA-LIMIT → STOP

---

## Minimal Practical Examples (Lens Families)

Already implemented or present in ecosystem:
- BASE (multi-base views)
- TIME (multi-granularity temporal views)
- CAUSA (cause/constraint consistency views)
- TOKEN (tokenization views)
- LCR (structural consistency views)

New lens families enabled by the same operator:
- COMPRESSION (lossy/lossless summaries, hashes)
- PERMUTATION (order variations, stable seeds)
- CONSTRAINT (budget, length, rules)
- LANGUAGE (natural text vs math vs code forms)
- SCALE (micro/meso/macro views)
- OBSERVER (observer-dependent pipelines, still measured structurally)

OMNIA remains model-agnostic and post-inference.