# C-Operator — Operational Definition

## Status: FORMAL OPERATOR (derived, not yet externally validated)

---

## Definition

\[
\boxed{
\mathcal C:\ (S,G,d)\ \mapsto\ (\Delta,\Omega,\hat\Omega,\mathrm{SEI},\mathrm{IRI})
}
\]

where:

- \(S\) = state space
- \(G\) = family of independent transformations
- \(d\) = distance / quasi-distance on representations

---

## 1. Residual per transformation

For \(g\in G\) and \(s\in S\):

\[
\boxed{
\Delta_g(s)=d\big(s,g(s)\big)
}
\]

For a trajectory \(T=(s_0,\dots,s_{k-1})\):

\[
\boxed{
\Delta_g(T)=\frac{1}{k}\sum_{i=0}^{k-1} d\big(s_i,g(s_i)\big)
}
\]

---

## 2. Aggregated invariance

Let \(\{g_j\}_{j=1}^m\subset G\) be an operational sample of transformations.

\[
\boxed{
\Omega(s)=1-\mathrm{Agg}\big(\{\Delta_{g_j}(s)\}_{j=1}^m\big)
}
\]

where \(\mathrm{Agg}\) is a robust aggregation operator, e.g.

\[
\mathrm{Agg}=\mathrm{median}
\qquad\text{or}\qquad
\mathrm{tmean}_\alpha
\]

Robust estimate:

\[
\boxed{
\hat\Omega(s)=\mathrm{RobustStat}\big(\{\Omega_{g_j}(s)\}\big)
}
\]

Interpretation:

- \(\Omega\): average invariance
- \(\hat\Omega\): robust invariance estimate

---

## 3. Structural time and divergence

Let \(\tau\) be a perturbation / complexity sweep parameter.

\[
\boxed{
\Omega(\tau)=\Omega\big(g_\tau(s)\big)
}
\]

Define divergence time:

\[
\boxed{
T\Delta=\inf\{\tau:\Omega(\tau)<\theta\}
}
\]

where \(\theta\) is an operational collapse threshold.

---

## 4. Saturation index

SEI measures remaining extractable structure.

Continuous form:

\[
\boxed{
\mathrm{SEI}(s)= -\frac{d}{d\tau}\Omega(\tau)\Big|_{\tau\to 0^+}
}
\]

Discrete approximation:

\[
\boxed{
\mathrm{SEI}\approx -\frac{\Omega(\tau_1)-\Omega(0)}{\tau_1}
}
\]

Interpretation:

- low SEI: near saturation
- high SEI: unstable / still structurally extractable

---

## 5. Irreversibility index

If an inverse exists:

\[
\boxed{
\mathrm{IRI}(s)=d\big(s,g^{-1}(g(s))\big)
}
\]

Cycle-based proxy (without explicit inverse):

\[
\boxed{
\mathrm{IRI}(s)=d\big(s,A'(s)\big)
}
\]

where \(A\to B\to A'\) is a structural loop.

Interpretation:

- \(\mathrm{IRI}=0\): locally reversible
- \(\mathrm{IRI}>0\): non-recoverable structural loss

---

## 6. Relaxed stability class

Define:

\[
\boxed{
s_1\sim_\varepsilon s_2
\iff
\sup_{g\in G} d\big(g(s_1),g(s_2)\big)\le \varepsilon
}
\]

This is a stability-under-transformation class, not exact equivalence.

---

## 7. Output of the operator

\[
\boxed{
\mathcal C(S,G,d)=\big(\Delta,\Omega,\hat\Omega,\mathrm{SEI},\mathrm{IRI}\big)
}
\]

with:

- \(\Delta\): residual vector over transformations
- \(\Omega\): invariance score
- \(\hat\Omega\): robust invariance estimate
- \(\mathrm{SEI}\): local saturation
- \(\mathrm{IRI}\): irreversible loss

---

## 8. Required properties

\[
\boxed{
\text{representation invariance}
}
\]

\[
\boxed{
\text{robustness to outliers in } G
}
\]

\[
\boxed{
\text{local monotonicity under increasing perturbation}
}
\]

\[
\boxed{
\text{separation between distinct stability classes}
}
\]

---

## 9. Minimal implementation constraints

- \(m = 8\text{–}16\) transformations
- \(d\) = composite distance:
  - edit / symbolic distance
  - numeric difference
  - structural difference
- \(\mathrm{Agg}=\mathrm{median}\) or trimmed mean (\(\alpha=0.2\))
- perturbation sweep: \(3\text{–}5\) levels
- threshold \(\theta\): operationally calibrated (e.g. \(0.7\text{–}0.8\))

---

## 10. Compression

\[
\boxed{
\mathcal C \text{ turns a structural framework into a computable operator}
}
\]

\[
\boxed{
(S,G,d)\ \longrightarrow\ (\Delta,\Omega,\hat\Omega,\mathrm{SEI},\mathrm{IRI})
}
\]

---

## Epistemic Note

This file defines the operator formally.

It does not establish:

- universal optimality
- external validation
- unique metric choice

It establishes only:

\[
\boxed{
\text{an executable structural operator derived from the framework}
}
\]