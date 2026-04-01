# TΔ / IRI / Ω(t) — Minimal Operational Formalism

## Purpose

This note defines three operational quantities used in OMNIA-style structural diagnostics:

- Ω(t): local structural coherence
- TΔ: structural divergence time
- IRI: irreversibility index

These quantities do not measure truth, semantics, or chaos itself.

They measure when two initially nearby descriptions stop being structurally equivalent.

---

## 1. Divergence

Given two trajectories:

- x1(t)
- x2(t)

define pointwise divergence:

Δ(t) = d(x1(t), x2(t))

where d is an explicit distance.

---

## 2. Structural Divergence Time

TΔ is the first time at which divergence becomes structurally non-equivalent:

TΔ = min { t | S(Δ[t:t+w]) ∈ {UNSTABLE, COLLAPSE} }

where:

- w = observation window
- S = structural classifier on the divergence segment

Interpretation:

TΔ is the first time at which the difference can no longer be treated as structurally negligible.

---

## 3. Irreversibility Index

IRI measures persistence of divergence beyond a recovery threshold τ:

IRI = (1/T) Σ 1[Δ(t) > τ]

Interpretation:

- low IRI -> divergence is temporary or recoverable
- high IRI -> divergence is persistent and structurally non-recoverable

---

## 4. Local Structural Coherence

For each local window W_t:

Ω(t) = α C(t) + β K(t) + γ (1 - N(t))

where:

- C(t) = local compressibility
- K(t) = local coherence
- N(t) = local noise sensitivity
- α + β + γ = 1

Interpretation:

Ω(t) measures how much local structure survives in the current representation.

---

## 5. Operational Hierarchy

Ω(t) -> TΔ -> IRI -> LIMIT

Meaning:

- Ω(t): local structure
- TΔ: break of equivalence
- IRI: persistence of break
- LIMIT: no justified continuation

---

## 6. Important Clarification

This framework does not identify truth.

It identifies when equivalence can no longer be claimed.