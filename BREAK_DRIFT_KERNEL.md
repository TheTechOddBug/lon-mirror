

Break–Drift Kernel (BDK): Minimal Structural Decomposition of Change


---

1. Scope

This module defines a minimal, model-agnostic decomposition of dynamic change into two irreducible components:

Break: rapid loss of local dynamical equivalence

Drift: slow, persistent accumulation of deviation


The goal is not prediction, but structural diagnosis.


---

2. Input

Given two trajectories:

x(t),\; y(t)

derived from:

real signal vs perturbed signal
or

reference vs observed evolution



---

3. Distance Primitive

d(t) = \frac{|x(t) - y(t)|}{\max |x - y|}

Normalized absolute distance.


---

4. Break Kernel

Definition

k_{\text{break}}(t)
=
\alpha D_{\text{orbit}}(t)
+
\beta D_{\text{vel}}(t)
+
\gamma D_{\text{curv}}(t)

Where:

: windowed normalized trajectory difference

: difference of first derivatives

: difference of second derivatives


All components are z-score normalized locally.

Interpretation

Detects local structural rupture

Sensitive to:

chaos onset

discontinuities

rapid regime change




---

5. Drift Kernel

Definition

k_{\text{drift}}(t)
=
\max\big(0,\; M_L(d_t) - \lambda M_S(d_t)\big)

Where:

: long-window moving average

: short-window moving average

: compensation factor


Interpretation

Detects persistent directional deviation

Suppresses:

local noise

transient spikes




---

6. Kernel Pair

K(t) = \big(k_{\text{break}}(t),\; k_{\text{drift}}(t)\big)

This pair defines the minimal observable structure of change.


---

7. Regime Classification

Regime	Condition	Interpretation

Stable		No structural change
Drift		Slow deviation
Break		Sudden rupture
Mixed		Accelerated transition



---

8. Event Times

T_{\text{drift}} = \inf \{t : k_{\text{drift}}(t) > \varepsilon_d\}

T_{\text{break}} = \inf \{t : k_{\text{break}}(t) > \varepsilon_b\}


---

9. Structural Ordering

If :
gradual destabilization → rupture

If :
direct discontinuity



---

10. Properties

Model-agnostic

Post-hoc only

No semantic interpretation

Sensitive to structural invariance loss

Compatible with OMNIA measurement philosophy



---

11. Limitations

Requires paired trajectories

Threshold-dependent

Not predictive by construction

Drift–break separation is not absolute



---

12. Minimal Claim

> Dynamic systems do not change in a single mode.
Change decomposes into drift and break.
This pair is the minimal observable structure of transformation.




---

13. Position in OMNIA

Acts before OMNIA-LIMIT

Feeds structural instability signals

Can be combined with:

Ω (coherence)

SEI (saturation)

IRI (irreversibility)




---

14. Status

Validated on synthetic systems

Not yet validated on real-world data

