# OMNIA Canonical Files
## What is canonical vs historical

Status: active
Purpose: reduce ambiguity in the repo

---

## 1. Canonical

These files define the current public and technical identity of OMNIA.

### Core identity
- `README.md`
- `ARCHITECTURE_BOUNDARY.md`
- `INFERENCE_FREEZE.md`
- `INTERFACE.md`
- `OMNIA_MINIMAL_INTERFACE.md`

### Core package
- `omnia/`

### Primary evidence
- `benchmarks/`
- `tests/`
- selected files in `case_studies/`

### Primary adoption path
- `integrations/`
- `adapters/` if still active and aligned with the minimal interface

---

## 2. Historical / legacy

These files may still contain useful provenance, but they do not define the current project identity.

Typical examples:
- old root-level `OMNIA_TOTALE_*` scripts
- old reports superseded by newer benchmark structure
- one-off experiment files
- earlier standalone prototypes later absorbed into `omnia/`

Rule:
historical files are preserved for traceability, not for primary onboarding.

---

## 3. Archive-only material

Anything that is no longer part of active Core, Evidence, or Adoption should live conceptually in:

- `archive/`
- `experiments/`

These materials may be useful internally, but should not define public positioning.

---

## 4. Canonical rule

If two files overlap, the canonical file wins.

If a historical file conflicts with a canonical file, the historical file is considered outdated unless explicitly restored.

---

## 5. Public reading order

A new external reader should follow this order:

1. `README.md`
2. `ARCHITECTURE_BOUNDARY.md`
3. `INTERFACE.md`
4. `OMNIA_MINIMAL_INTERFACE.md`
5. `docs/ROADMAP_CORE_EVIDENCE_ADOPTION.md`
6. selected benchmark and integration materials

---

## 6. Maintenance rule

When a new important file is added, it must be classified immediately as one of:

- canonical
- historical
- archive/experiment

Unclassified files increase repo noise and reduce external clarity.