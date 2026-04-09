# OMNIA — Operational Protocol v1

## Status

This document defines the first operational protocol layer built on top of dO.

The metric layer remains unchanged.

This document does not redefine state distance.
It defines how OMNIA should react to measured structural distance once that distance has been computed.

Architectural boundary remains unchanged:

measurement != cognition != decision

OMNIA does not interpret meaning.
OMNIA does not decide policy by itself.
OMNIA emits regime-relevant structural signals that can be consumed by an external control layer.

---

## 1. Goal

Given a computed structural distance:

dO = Delta_Omega(S1, S2)

define a minimal operational response protocol based on the current validated regime zones.

The objective is not classification for its own sake.

The objective is to decide whether a new state:

- preserves continuity
- introduces manageable drift
- breaks the current regime

---

## 2. Regime zones

The current operational regime zones are:

- Equivalence zone: dO <= 0.10
- Mild variation zone: 0.10 < dO < 0.35
- Structural break zone: dO >= 0.35

These thresholds are operational thresholds for Protocol v1.

They are not final metaphysical boundaries.
They are current validated control thresholds for the present baseline.

---

## 3. Core protocol principle

The protocol must answer only one question:

What level of structural intervention is justified by the measured distance?

Not:

- what the state means
- whether the content is true
- whether the content is desirable
- whether the state is morally acceptable

Only:

what structural response is justified.

---

## 4. Zone actions

### 4.1 Equivalence zone

Condition:

dO <= 0.10

Interpretation:

The new state differs from the reference only at a representational or non-regime-changing level.

Operational action:

- treat S2 as structurally continuous with S1
- allow auto-merging
- do not trigger drift alert
- do not trigger regime alert
- preserve continuity index as stable

Protocol label:

EQUIVALENT_CONTINUITY

Minimal consequence:

No intervention required.

---

### 4.2 Mild variation zone

Condition:

0.10 < dO < 0.35

Interpretation:

The new state introduces structural variation, but the variation remains compatible with the active regime.

Operational action:

- accept S2 as same regime with variation
- log the transition
- accumulate drift history
- update local trajectory tracking
- do not trigger hard regime-shift response
- optionally increase observation density if repeated mild variation persists

Protocol label:

TRACKED_DRIFT

Minimal consequence:

Variation is real and must be monitored, but not treated as rupture.

---

### 4.3 Structural break zone

Condition:

dO >= 0.35

Interpretation:

The new state is no longer structurally continuous with the active regime.

Operational action:

- block automatic continuity assumption
- emit regime-shift alert
- require external review, recalibration, or supervised confirmation
- mark continuity as broken
- start a new regime candidate if confirmed by control layer

Protocol label:

REGIME_SHIFT_CANDIDATE

Minimal consequence:

Automatic merging is not justified.

---

## 5. Default response table

| dO zone | Structural interpretation | Protocol label | Default action |
|---|---|---|---|
| dO <= 0.10 | representational continuity | EQUIVALENT_CONTINUITY | auto-merge |
| 0.10 < dO < 0.35 | compatible drift | TRACKED_DRIFT | log and monitor |
| dO >= 0.35 | regime rupture candidate | REGIME_SHIFT_CANDIDATE | alert and require review |

---

## 6. State transition logic

For a transition from S_t to S_t+1:

1. compute dO(S_t, S_t+1)
2. assign the transition to a regime zone
3. apply the corresponding protocol action
4. store the transition in trajectory memory
5. if repeated drift accumulates, elevate observation priority
6. if structural break occurs, suspend continuity assumption

This protocol does not assume that every break is an error.

A break may be:

- anomaly
- adaptation
- attack
- shift of context
- legitimate new regime

OMNIA does not decide which one.
It only detects that continuity is no longer structurally justified.

---

## 7. Drift accumulation rule

A single mild transition does not imply instability.

However, repeated mild transitions may indicate cumulative regime movement.

Therefore Protocol v1 introduces the following rule:

If a sequence of consecutive transitions remains in the mild zone, the system must maintain a cumulative drift record.

This cumulative drift record may be used by an external layer to detect:

- slow regime migration
- progressive degradation
- transition toward break threshold

OMNIA itself only exposes the measurements required for this tracking.

---

## 8. Break handling rule

A structural break must not be silently absorbed into continuity.

Therefore, when dO >= 0.35:

- continuity status becomes suspended
- the previous state and new state must remain explicitly separated
- no auto-collapse into the same regime is allowed
- an external confirmation layer must decide whether:
  - the break is accepted as a new regime
  - the break is rejected as anomaly
  - the thresholding policy must be revised

This is the minimum protection rule against false continuity.

---

## 9. Protocol outputs

For each evaluated transition, Protocol v1 should emit at least:

- reference_state_id
- observed_state_id
- dO
- kappa
- assigned_zone
- protocol_label
- continuity_status
- drift_tracking_flag
- regime_alert_flag

Recommended continuity status values:

- continuous
- continuous_with_drift
- continuity_suspended

Recommended regime alert values:

- false
- true

---

## 10. What this protocol is for

Protocol v1 is suitable for:

- trajectory monitoring
- early warning
- structural continuity checks
- regime change detection
- anomaly gating before decision layers
- supervision support

It is especially useful when a system must distinguish:

- harmless reformulation
- manageable evolution
- actual structural rupture

---

## 11. What this protocol is not for

Protocol v1 is not:

- a semantic validator
- a truth engine
- a policy engine
- an optimizer
- a classifier of meaning
- an autonomous decision system

It is a structural control protocol built on measured distance.

---

## 12. Minimal claim

If dO is treated as the structural measurement primitive,
then Operational Protocol v1 defines the minimal justified actions associated with the three validated regime zones.

This allows OMNIA to move from pure measurement to structured signaling without violating the architectural boundary.