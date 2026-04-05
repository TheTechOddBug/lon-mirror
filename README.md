# OMNIA v1.0 — Relational Fatigue Spectrometry (RFS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19420935.svg)](https://doi.org/10.5281/zenodo.19420935)

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01  

---

## Overview

OMNIA is a **post-hoc structural measurement engine**.

It does not analyze meaning or content.  
It measures how a system **responds to controlled perturbations**.

Structure is treated as an observable property of **response stability**, not as a semantic feature.

---

## Core Principle

> Structure is not what is present.  
> Structure is what remains coherent under perturbation.

---

## Method: Relational Fatigue Spectrometry (RFS)

A sequence is modeled as a graph of local adjacencies:

\[
A(S) = \{(t_i, t_{i+1})\}
\]

OMNIA applies repeated local perturbations:

- adjacent swaps  
- multi-point stress per trial  
- multiple trials (response sampling)

For each perturbation:

\[
D = |A(S) \triangle A(S')|
\]

\[
I = \frac{D}{|A(S)|}
\]

---

## Signals Extracted

- **Impact (I)** → mean structural disruption  
- **Volatility (σ)** → variation across trials  

Volatility score:

\[
V = \frac{1}{1 + \alpha \cdot \sigma}
\]

---

## Omega Score

\[
\Omega = 0.7 \cdot V + 0.3 \cdot I
\]

Where:

- \(V\) → stability of response  
- \(I\) → magnitude of disruption  

---

## Interpretation

OMNIA treats information as a system under stress:

| System Type | Behavior |
|------------|---------|
| Structured | stable response |
| Perturbed  | partially unstable |
| Random     | highly volatile |

OMNIA does not read meaning.  
It measures **relational coherence**.

---

## Semantic Decoupling (v10.0)

Natural language introduces statistical coherence unrelated to structure.

To isolate structural signal, OMNIA introduces an internal baseline.

### Shuffle Baseline

\[
S_{shuffle}
\]

Preserves:
- token identity  
- distribution  

Destroys:
- sequential structure  

---

### Structural Differential

\[
\Delta_{struct} = \Omega_{raw} - \Omega_{shuffle}
\]

This yields:

```text
structural coherence − statistical coherence


---

Validation

OMNIA v1.0 + v10.0 has been validated across multiple regimes:

Dataset	Regime	Purpose	Result

B	Redundant	pattern sensitivity	✔
C	A-periodic	topology detection	✔
D	Semantic noise	robustness to language	✔



---

Key Result

Across all regimes:

\Delta_{structured} > \Delta_{perturbed} > \Delta_{random}

This ordering remains stable under stress.


---

Stress Scaling

Increasing perturbation intensity:

amplifies signal

compresses ratios

preserves ordering


Conclusion:

signal is scalable, not fragile


---

What OMNIA Measures

relational coherence

structural stability

consistency of response

resistance to perturbation



---

What OMNIA Does NOT Do

OMNIA:

does not interpret

does not predict

does not classify semantics

does not optimize

does not learn


\boxed{\text{Output = measurement only}}


---

Properties

non-semantic

token-agnostic

deterministic (given seed)

perturbation-based

differential (relative measurement)

model-independent



---

Use Cases

logical consistency analysis

code structure validation

pipeline integrity verification

detection of hidden inconsistencies



---

Limitations

OMNIA measures response behavior, not intrinsic structure.

Known limitations:

residual semantic influence

dependence on tokenization

reduced sensitivity in short sequences


OMNIA is:

operational

bounded

not universal



---

Empirical Case Studies

ZEH-1.1

Model: Llama-3-8B-Instruct (4-bit)

Task: Parentheses Balance

Result: structural degradation detected before first model error



---

ZEH-2 (Cross-Task Replication)

Model: same

Task: transitivity / relational consistency

Result: early structural degradation detected before failure



---

Empirical Status

multi-task single-model empirical support

Observed:

early-warning signal replicated across two structurally different tasks

consistent ordering and degradation pattern


Not established:

multi-model validation

domain generalization


See:

docs/ZEH_1_CASE_STUDY.md

docs/ZEH_2_CASE_STUDY.md



---

Repository Structure

omnia/        → core engine  
examples/     → demos  
tests/        → validation  
docs/         → formal definitions  
docs/paper/   → scientific draft  
experiments/  → research extensions  
data/         → empirical results


---

Minimal Execution

python examples/omnia_validation_demo.py

Expected:

structured → high Ω
perturbed → medium Ω
random → low Ω


---

Positioning

OMNIA is:

post-hoc

model-agnostic

non-semantic

structural

measurement-oriented


OMNIA is not a pattern detector.
It is a structural integrity sensor.


---

Statement

> OMNIA v1.0
Structure is not what you see.
It is what remains coherent under stress.




---

License

MIT License


---

Citation

Brighindi, M.
OMNIA v1.0 — Relational Fatigue Spectrometry Core
https://github.com/Tuttotorna/lon-mirror
