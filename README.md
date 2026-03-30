## Canonical Index

- Ecosystem map: [ECOSYSTEM.md](ECOSYSTEM.md)
- Machine index: [repos.json](repos.json)

# OMNIA — Unified Structural Measurement Engine

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19318573.svg)](https://doi.org/10.5281/zenodo.19318573)

**DEMO**  
https://lon-reflect.emergent.host/

**MB-X.01**  
**Author:** Massimiliano Brighindi

---

## Overview

**OMNIA** is a **post-hoc structural measurement engine**.

It measures **invariance, instability, compatibility, and limit conditions** under **independent, non-semantic transformations**.

OMNIA is designed to detect:

- what remains invariant when representation changes
- where structure becomes unstable
- where continuation becomes structurally unjustified
- when systems become irreversibly degraded
- when representations become structurally indistinguishable

OMNIA does **not**:

- interpret meaning
- decide
- optimize
- learn
- explain

**The output is measurement, never narrative.**

---

## Core Principle

> **Structural truth is what survives the removal of representation.**

OMNIA treats truth as **measured invariance under transformation**, not as semantics, authority, or interpretation.

---

## Architectural Boundary

This repository exists to formalize a strict distinction:

**measurement ≠ cognition ≠ decision**

OMNIA occupies the **measurement layer only**.

It is not a model, not a reasoning agent, and not a policy layer.

---

## Quick Verification

Suggested entry points:

- [examples/omnia_validation_demo.py](examples/omnia_validation_demo.py)
- [examples/omnia_minimal_engine.py](examples/omnia_minimal_engine.py)
- [examples/omnia_sci_engine.py](examples/omnia_sci_engine.py)

Typical command:

```bash
python examples/omnia_validation_demo.py

Expected behavior:

stable structures retain higher Ω

unstable structures show faster Ω decay

cross-lens disagreement reduces SCI

exhausted regimes push SEI toward zero

irreversible degradation yields positive IRI


This is the key point:

OMNIA measures structural behavior under transformation rather than interpreting content.


---

Minimal Executable Systems

OMNIA includes compact executable systems that convert:

theory -> executable process -> measurable structure

Core examples:

examples/structural_dynamics_mod9.py

examples/structural_dynamics_modn.py

examples/structural_dynamics_modn_global.py

examples/structural_dynamics_strings.py

examples/omnia_sci_engine.py

examples/omnia_minimal_engine.py

examples/omnia_validation_demo.py


These examples show that OMNIA is not only conceptual.
It is executable and measurable.


---

Key Metrics

Ω — Structural Coherence

Measures persistence of structure under transformation.

SCI — Structural Compatibility Index

Measures agreement across independent structural lenses.

SEI — Saturation / Structural Exhaustion Index

Measures whether further transformation still yields structural gain.

IRI — Irreversibility Index

Measures non-recoverable structural loss after transformation cycles.

OMNIA-LIMIT

Defines when continuation is no longer structurally justified.


---

Structural Lenses

Canonical lenses include:

BASE — Omniabase

TIME — Omniatempo

CAUSA — Omniacausa

TOKEN

LCR


All lenses are:

deterministic

composable

non-semantic


Agreement across lenses is measured, not assumed.


---

OMNIA-LIMIT

OMNIA-LIMIT is the boundary condition of the framework.

Canonical stop conditions:

SEI -> 0

IRI > 0

Ω̂ stabilizes


At that point, continuation is treated as structural exhaustion, not as deeper insight.


---

Positioning

OMNIA differs from standard evaluation or interpretability layers because it:

operates post hoc

does not depend on semantics

does not require retraining

does not decide

does not optimize

measures structural persistence across transformations

can detect saturation and irreversibility conditions


This repository should be read as a structural measurement framework, not as a model claim.


---

Repository Structure

Main repository areas:

omnia/

examples/

tests/

docs/

experiments/


Canonical ecosystem map:

ECOSYSTEM.md


Machine-readable index:

repos.json



---

License

MIT License


---

Citation

Brighindi, M.
OMNIA — Unified Structural Measurement Engine (MB-X.01)
https://github.com/Tuttotorna/lon-mirror

