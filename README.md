# OMNIA / MB-X.01 — Logical Origin Node (L.O.N.)

**OMNIA** is a deterministic measurement engine for **structural coherence, instability, saturation, and irreversibility**
across numbers, time, causality, and token sequences.

It does not interpret meaning.  
It does not make decisions.  
It **measures invariants, limits, and path-dependent loss**.

This repository (`Tuttotorna/lon-mirror`) is the **canonical public mirror**
of the **MB-X.01 / OMNIA** research line.

---

## What OMNIA Is

OMNIA is a **pure diagnostic layer**.

### Input
- Numeric signals  
- Temporal series  
- Causal structures  
- Token sequences (e.g. model outputs)

### Output
- Structure-only, machine-readable metrics

### Constraints
- No semantic assumptions  
- No policy, intent, or alignment layer  
- Deterministic, bounded, reproducible  
- **Post-hoc only** (never in-loop)

### Core Principle
> **Truth is what remains invariant under transformation.**

OMNIA operates **after signals exist**, without influencing their generation,
selection, or interpretation.

---

## What OMNIA Is Not

OMNIA is **not**:
- a language model  
- a classifier  
- an optimizer  
- an agent  
- a decision system  
- a safety or alignment layer  

OMNIA never chooses.  
It **only measures structure**.

---

## Universal Superposition Operator (Core Concept)

OMNIA is not a collection of ad-hoc metrics.

OMNIA is a **universal superposition operator**.

> **Anything that can be represented in more than one way  
> can be measured by OMNIA.**

### Definitions

**Object**  
Any artifact: number, sequence, text, model output, time series, causal trace, code.

**Representation (View)**  
A deterministic encoding of the same object under a specific transformation
(e.g. numeric base, tokenization, order, compression, temporal granularity).

**Lens**  
A deterministic generator of one or more representations.  
A lens does **not** score, decide, or interpret.

**Superposition**  
Given multiple representations of the same object, OMNIA measures:
- pairwise structural distances  
- global invariance  
- structural fractures (where invariance collapses)

### Structural Truth (Operational)
A property is **structural** only if it remains **invariant**
under superposition across **independent representations**.

If invariance collapses, the property is representation-dependent, not structural.

---

## Core Lenses (Implemented)

OMNIA lenses generate **views only**.  
All scoring happens in the metric core.

### Foundational Lenses
- **BASE** — multi-base numeric representations  
- **TIME** — multi-granularity temporal views  
- **CAUSA** — causal consistency views  
- **TOKEN** — tokenization-dependent views  
- **LCR** — local consistency / rigidity views  

### Superposition-Based Extension Lenses
(Proof of universality)

- **COMPRESSION** — survivability under lossy / lossless reduction  
- **PERMUTATION** — order-dependence and rhetorical fragility  
- **CONSTRAINTS** — robustness under restriction (length, budget, form)

Demos:
- `examples/superposition_minimal_demo.py`
- `examples/compression_superposition_demo.py`
- `examples/multi_lens_superposition_demo.py`

---

## Core Metrics (Stable API)

All metrics are deterministic, bounded, and numerically stable.

| Metric | Description |
|------|-------------|
| `truth_omega` | Structural incoherence measure (0 = perfect coherence) |
| `co_plus` | Inverse coherence score |
| `score_plus` | Composite score (coherence + information bias) |
| `delta_coherence` | Dispersion / instability proxy |
| `kappa_alignment` | Relative similarity between two signals |
| `epsilon_drift` | Relative temporal change |

**Implementation**

omnia/metrics.py

The API is explicit, import-stable, deterministic, and globals-free.

---

## Layer-1: Saturation / Exhaustion Index (SEI)

SEI measures **marginal structural yield** under increasing computational cost.

SEI does **not** decide and does **not** stop execution.  
It quantifies diminishing returns.

### Question Answered
> Is further computation still producing measurable structural benefit?

### Conceptual Definition

SEI = (Δquality + Δuncertainty_reduction) ---------------------------------- (tokens + latency + iterations + energy_proxy)

### Properties
- Rolling window (trend-based)
- No fixed thresholds
- Fully diagnostic

### Artifacts

omnia/sei.py examples/sei_demo.py examples/sei_gsm8k_from_jsonl.py examples/sei_gsm8k_uncertainty_from_jsonl.py

SEI prepares, but does not trigger, higher-order boundary reasoning.

---

## Visual Diagnostic — SEI Trend

Minimal visual artifact:

assets/diagnostics/sei_trend.png

Shows:
- marginal structural yield
- flattening or decline under increasing computation

No thresholds.  
No stop conditions.  
Evidence, not instruction.

---

## Layer-2: Irreversibility / Hysteresis (IRI)

IRI measures **path-dependent structural loss**.

A system is structurally irreversible if returning to a prior state
does not restore the same structural conditions.

### Definition

State_t → Forward → State_t+1 State_t+1 → Inverse_Projection → State'_t State'_t ≠ State_t

### Irreversibility Index

IRI = hysteresis_residue / forward_distance

- IRI ≈ 0 → reversible  
- IRI ↑ → loss of reversibility  
- IRI → 1 → strong hysteresis  

### Artifacts

omnia/irreversibility.py examples/irreversibility_from_sei_report.py examples/irreversibility_plot.py

IRI does not stop systems.  
It documents **loss of options**.

---

## Prime Base Instability Index (PBII)

PBII is a zero-shot, non-ML structural metric derived from multi-base instability.

It separates primes from composites without:
- training
- embeddings
- heuristics
- learned parameters

### Verified Result
- Dataset: integers 2–5000  
- Method: deterministic, zero-shot  
- Metric: ROC-AUC (polarity-corrected)  
- Result: **AUC = 0.816**

Lower PBII → primes  
Higher PBII → composites  

Notebook:

PBII_benchmark_v0.3.ipynb

---

## Differential Diagnostics (Non-redundancy Evidence)

OMNIA detects instability even when outcome-based metrics remain stable.

Example (GSM8K):

| item_id | correct | acc_stable | self_consistent | omn_flag | truth_omega | pbii |
|--------|---------|------------|-----------------|----------|-------------|------|
| 137 | 1 | 1 | 1 | 1 | 1.92 | 0.81 |
| 284 | 1 | 1 | 1 | 1 | 2.31 | 0.88 |

Outcome-based metrics do not detect these cases.  
Structure-based diagnostics do.

---

## Architecture Overview

Signal (numbers / time / tokens / causality) ↓ +-------------------------------------------+ |              OMNIA LENSES                  | | BASE · TIME · CAUSA · TOKEN · LCR          | | COMPRESSION · PERMUTATION · CONSTRAINTS   | +-------------------------------------------+ ↓ +-------------------------------------------+ |              METRIC CORE                  | |   TruthΩ · Co⁺ · Δ · κ · ε                | +-------------------------------------------+ ↓ +-------------------------------------------+ |          SEI (Layer-1, trend only)         | |   Marginal Yield / Saturation Detection   | +-------------------------------------------+ ↓ +-------------------------------------------+ |          IRI (Layer-2, hysteresis)         | |   Path Irreversibility / Option Loss      | +-------------------------------------------+ ↓ +-------------------------------------------+ |              ICE ENVELOPE                 | |   Impossibility & Confidence Envelope     | +-------------------------------------------+

OMNIA outputs diagnostics, never judgments.

---

## Reproducibility

A fixed, reproducible execution path is provided.

**Real Benchmark Run**

colab/OMNIA_REAL_RUN.ipynb

Steps:
1. Clone repository  
2. Install fixed dependencies  
3. Lock random seeds  
4. Run benchmarks  
5. Produce machine-readable reports  

Goal: **verification**, not exploration.

---

## Recorded Benchmark Outputs (Closed Models)

results/closed_models/

Examples:
- `gpt4_metrics.jsonl`
- `gpt4_metrics_omnia.jsonl`

All files are deterministic, post-hoc, and machine-readable.

---

## Tests

tests/test_metrics.py

They verify:
- algebraic identities  
- monotonicity  
- edge cases  
- numerical stability  
- API contracts  

Run:

pytest

---

## Integration Philosophy

OMNIA is **composable by design**.

- OMNIA → measures structure  
- External systems → interpret, decide, optimize  

Validated boundary:
- OMNIA = geometry / invariants  
- Decision systems = policy / intent / judgment  

OMNIA is institution-agnostic and architecture-agnostic.

---

## Architecture Context (Downstream, Optional)

Aligned projects:
- **OMNIAMIND**  
  https://github.com/Tuttotorna/OMNIAMIND
- **OMNIA-LIMIT**  
  https://github.com/Tuttotorna/omnia-limit

These systems consume OMNIA signals.  
OMNIA itself remains independent.

---

## Repository Identity (Canonical)

Canonical repository:  
https://github.com/Tuttotorna/lon-mirror

Project name:  
**OMNIA / MB-X.01**

Author / Logical Origin Node:  
**Massimiliano Brighindi**

There is no secondary mirror.

---

## Status

- Metrics core: stable  
- SEI (Layer-1): active  
- IRI (Layer-2): active  
- Visual diagnostics: present  
- Tests: invariant-based  
- API: frozen  
- Research line: active  

This repository is intended to be read by **humans and machines**.

---

## License

MIT License