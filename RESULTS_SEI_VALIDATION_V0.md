# SEI Validation v0 — Saturation Index

## Scope

This document reports a controlled validation test for:

```text
SEI — Saturation Index

SEI measures stabilization of structural behavior across transformation trajectories.

It does not measure correctness, truth, or quality.

It measures whether structural variation continues or saturates over time.


---

Formal Definition

Given a trajectory of invariance measurements:

Ω_tau(x)

Define normalized variance:

Var_norm({Ω_tau(x)})

Then:

SEI(x) = 1 - Var_norm({Ω_tau(x)})

Where:

SEI(x) in [0,1]


---

Interpretation

SEI → 1

indicates:

structural stabilization

saturation

low ongoing variation



---

SEI → 0

indicates:

persistent instability

continued oscillation

ongoing structural variation



---

Important Constraint

SEI does not measure whether a trajectory is:

correct

good

optimal

true


It measures only:

stabilization of structural behavior

A bad but stable trajectory can still produce high SEI.


---

Validation Design

Three synthetic Ω-trajectories were tested.


---

1. Saturated Trajectory

Description

Ω rapidly stabilizes around a fixed value.

Trajectory:

[0.92, 0.91, 0.91, 0.90, 0.91, 0.91]

Expected behavior:

very high SEI


---

2. Unstable Trajectory

Description

Ω continues oscillating strongly across steps.

Trajectory:

[0.95, 0.40, 0.88, 0.35, 0.90, 0.30]

Expected behavior:

low SEI


---

3. Converging Trajectory

Description

Ω initially varies, then progressively stabilizes.

Trajectory:

[0.55, 0.68, 0.76, 0.82, 0.84, 0.85]

Expected behavior:

medium-high SEI


---

Results

Saturated

mean_omega:           0.910000
normalized_variance:  0.000160
SEI:                  0.999840


---

Unstable

mean_omega:           0.630000
normalized_variance:  0.382400
SEI:                  0.617600


---

Converging

mean_omega:           0.750000
normalized_variance:  0.054400
SEI:                  0.945600


---

Observed Ordering

SEI(saturated) > SEI(converging) > SEI(unstable)

Observed:

0.999840 > 0.945600 > 0.617600

This matches the expected behavior.


---

Interpretation

SEI successfully separates:

stable trajectories

from:

persistently unstable trajectories

Key observations:

1. Saturated trajectories produce near-maximal SEI.


2. Converging trajectories produce high but not maximal SEI.


3. Oscillatory trajectories produce lower SEI.




---

Relation to Ω

Ω measures instantaneous structural invariance.

SEI measures stabilization of Ω across trajectories.

Therefore:

Ω   = instantaneous structural behavior
SEI = stability of structural behavior over time


---

Relation to IRI

IRI measures irreversible structural loss after recovery.

SEI measures whether structural dynamics continue changing.

Therefore:

IRI = residual damage
SEI = saturation of dynamics


---

Limits

This validation is minimal and synthetic.

Limitations:

handcrafted trajectories

no real-world datasets

fixed bounded variance assumption

no adaptive thresholds

no stochastic trajectory modeling



---

Status

SEI v0: operationally coherent in controlled trajectory tests

Not externally validated.

Requires future testing on:

iterative LLM trajectories

optimization dynamics

recurrent perturbation systems

temporal structural measurements

adaptive convergence systems



---

Final Statement

SEI does not measure correctness.

SEI measures whether structural behavior stabilizes.

A trajectory can be stable or unstable independently of whether it is correct.

