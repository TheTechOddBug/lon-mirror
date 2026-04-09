# OMNIA — Transition Signal Schema v1

## Status

This document defines the minimal output schema emitted by OMNIA after evaluating a transition between two states.

This schema is the communication layer between:

- the measurement layer
- the operational protocol layer
- any external control or supervision layer

It does not redefine dO.
It does not redefine protocol actions.

It defines the standard transition signal format.

Architectural boundary remains unchanged:

measurement != cognition != decision

OMNIA emits structural transition signals.
External layers consume those signals.

---

## 1. Goal

Given a transition from a reference state S_ref to an observed state S_obs, produce a standard signal containing:

- the measured structural distance
- the current structural compatibility
- the assigned operational zone
- the protocol action label
- the continuity status
- the alert status

This signal is the minimal object that allows an external layer to react consistently.

---

## 2. Signal object

A transition signal is a structured record emitted for each evaluated transition.

Canonical name:

TransitionSignalV1

The signal must contain both:

- raw structural measurements
- protocol-ready interpretation fields

---

## 3. Required fields

### 3.1 Identity fields

- reference_state_id
- observed_state_id

Definition:

Identifiers for the source state and the target state of the evaluated transition.

Type:

string

Purpose:

Allows explicit tracking of transitions without relying on implicit ordering.

---

### 3.2 Measurement fields

- dO
- kappa

Definition:

- dO = Delta_Omega(S_ref, S_obs)
- kappa = 1 - dO

Type:

float

Range:

- dO in [0,1]
- kappa in [0,1]

Purpose:

Expose the primary structural measurements required by the operational protocol.

---

### 3.3 Regime fields

- assigned_zone
- protocol_label
- continuity_status

Type:

string

Allowed values:

assigned_zone:
- equivalence
- mild_variation
- structural_break

protocol_label:
- EQUIVALENT_CONTINUITY
- TRACKED_DRIFT
- REGIME_SHIFT_CANDIDATE

continuity_status:
- continuous
- continuous_with_drift
- continuity_suspended

Purpose:

Provide the interpreted structural regime of the transition.

---

### 3.4 Alert fields

- drift_tracking_flag
- regime_alert_flag

Type:

boolean

Purpose:

Expose the minimum binary control signals required for monitoring and escalation.

Default semantics:

- drift_tracking_flag = true only in mild_variation
- regime_alert_flag = true only in structural_break

---

## 4. Optional recommended fields

The following fields are not mandatory for schema validity, but are strongly recommended.

### 4.1 Signature support fields

- signature_distance
- best_transform
- transform_cost

Purpose:

Allow diagnostic inspection of how the final dO was obtained.

---

### 4.2 Temporal fields

- transition_index
- timestamp

Purpose:

Support trajectory reconstruction and cumulative drift tracking.

---

### 4.3 Reference support fields

- threshold_equivalence
- threshold_break

Purpose:

Expose the thresholds used to assign the zone for reproducibility.

---

### 4.4 Audit support fields

- notes
- metric_version
- protocol_version

Purpose:

Allow forensic traceability across revisions.

---

## 5. Canonical minimal schema

The minimal signal must contain at least:

- reference_state_id
- observed_state_id
- dO
- kappa
- assigned_zone
- protocol_label
- continuity_status
- drift_tracking_flag
- regime_alert_flag

This is the minimum valid TransitionSignalV1 object.

---

## 6. Zone-to-signal mapping

### 6.1 Equivalence

Condition:

dO <= 0.10

Required output:

- assigned_zone = equivalence
- protocol_label = EQUIVALENT_CONTINUITY
- continuity_status = continuous
- drift_tracking_flag = false
- regime_alert_flag = false

---

### 6.2 Mild variation

Condition:

0.10 < dO < 0.35

Required output:

- assigned_zone = mild_variation
- protocol_label = TRACKED_DRIFT
- continuity_status = continuous_with_drift
- drift_tracking_flag = true
- regime_alert_flag = false

---

### 6.3 Structural break

Condition:

dO >= 0.35

Required output:

- assigned_zone = structural_break
- protocol_label = REGIME_SHIFT_CANDIDATE
- continuity_status = continuity_suspended
- drift_tracking_flag = false
- regime_alert_flag = true

---

## 7. Canonical JSON example

```json
{
  "reference_state_id": "S_001",
  "observed_state_id": "S_002",
  "dO": 0.382,
  "kappa": 0.618,
  "assigned_zone": "structural_break",
  "protocol_label": "REGIME_SHIFT_CANDIDATE",
  "continuity_status": "continuity_suspended",
  "drift_tracking_flag": false,
  "regime_alert_flag": true,
  "signature_distance": 0.257,
  "best_transform": "identity",
  "transform_cost": 0.0,
  "threshold_equivalence": 0.10,
  "threshold_break": 0.35,
  "metric_version": "v0.2.1",
  "protocol_version": "v1"
}