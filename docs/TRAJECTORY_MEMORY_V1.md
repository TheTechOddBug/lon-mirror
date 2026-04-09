# OMNIA — Trajectory Memory v1

## Status

This document defines the stateful memory layer of OMNIA.

While dO measures structural distance and TransitionSignalV1 labels a single transition, TrajectoryMemoryV1 organizes transitions into a coherent structural history.

Architectural boundary remains unchanged:

measurement != protocol != memory != decision

OMNIA memory tracks trajectories.
It does not decide the truth, value, or desirability of destination states.

---

## 1. Goal

The goal of Trajectory Memory v1 is to transform isolated transition signals into a persistent structural history that can detect:

- cumulative drift
- regime persistence
- regime rupture
- recovery to a known regime
- migration toward a new regime

The memory layer exists to distinguish:

- noise
- evolution
- rupture

across time, not just in isolated comparisons.

---

## 2. Core objects

### 2.1 Trajectory

A Trajectory is a directed sequence of states connected by transition signals.

Required fields:

- trajectory_id
- active_regime_id
- last_stable_regime_id
- regime_status
- start_timestamp

Definitions:

- trajectory_id: unique identifier for the trajectory
- active_regime_id: identifier of the currently active regime
- last_stable_regime_id: identifier of the last confirmed stable regime
- regime_status: current memory-level regime condition
- start_timestamp: creation time of the trajectory

Allowed regime_status values:

- STABLE
- DRIFTING
- SUSPENDED
- MIGRATING

---

### 2.2 Memory state

The Memory State is the current state of trajectory tracking updated at each transition.

Required fields:

- transition_index
- previous_signal_id
- cumulative_drift
- consecutive_mild_count
- consecutive_break_count
- trajectory_alert_flag

Definitions:

- transition_index: index of the current transition in the trajectory
- previous_signal_id: identifier of the previous processed signal
- cumulative_drift: accumulated dO across consecutive mild transitions
- consecutive_mild_count: number of consecutive mild signals
- consecutive_break_count: number of consecutive break signals
- trajectory_alert_flag: boolean flag raised when memory-level heuristics trigger

---

## 3. Memory logic

### 3.1 Equivalence rule

Condition:

assigned_zone == equivalence

Operational effect:

- cumulative_drift remains unchanged
- consecutive_mild_count = 0
- consecutive_break_count = 0
- trajectory_alert_flag = false
- regime_status remains unchanged unless recovery logic applies

Interpretation:

The transition does not justify regime change.

---

### 3.2 Mild variation rule

Condition:

assigned_zone == mild_variation

Operational effect:

- cumulative_drift = cumulative_drift + dO
- consecutive_mild_count = consecutive_mild_count + 1
- consecutive_break_count = 0
- regime_status = DRIFTING
- if consecutive_mild_count > 5, trajectory_alert_flag = true

Interpretation:

Variation is compatible with the active regime, but structural drift is accumulating.

Recommended heuristic label:

SLOW_SHIFT_ALERT

---

### 3.3 Structural break rule

Condition:

assigned_zone == structural_break

Operational effect:

- consecutive_break_count = consecutive_break_count + 1
- consecutive_mild_count = 0
- regime_status = SUSPENDED
- trajectory_alert_flag = true

Interpretation:

Continuity with the currently active regime is no longer justified.

Recommended heuristic labels:

- if consecutive_break_count == 1 -> ISOLATED_BREAK_WARNING
- if consecutive_break_count >= 3 -> NEW_REGIME_CANDIDATE

---

## 4. Recovery and migration rules

### 4.1 Recovery rule

Condition:

- current regime_status == SUSPENDED
- a new equivalence signal is observed
- the equivalence is compatible with last_stable_regime_id

Operational effect:

- active_regime_id = last_stable_regime_id
- regime_status = STABLE
- cumulative_drift = 0
- consecutive_mild_count = 0
- consecutive_break_count = 0
- trajectory_alert_flag = false

Interpretation:

The system has returned to a previously known stable regime.

---

### 4.2 Migration rule

Condition:

- current regime_status == SUSPENDED
- consecutive_break_count >= 3
- break pattern remains structurally consistent across transitions

Operational effect:

- regime_status = MIGRATING
- trajectory_alert_flag = true

Interpretation:

The trajectory may be stabilizing into a new regime, but the new regime is not yet confirmed.

---

### 4.3 New regime confirmation rule

Condition:

- current regime_status == MIGRATING
- subsequent transitions show internal equivalence or low drift around the new pattern

Operational effect:

- active_regime_id = new confirmed regime id
- last_stable_regime_id = active_regime_id
- regime_status = STABLE
- cumulative_drift = 0
- consecutive_mild_count = 0
- consecutive_break_count = 0
- trajectory_alert_flag = false

Interpretation:

A new regime is confirmed.

---

## 5. Trajectory state transition table

| Current status | Input signal zone | New status | Logic |
|---|---|---|---|
| STABLE | equivalence | STABLE | continuity preserved |
| STABLE | mild_variation | DRIFTING | drift tracking begins |
| STABLE | structural_break | SUSPENDED | continuity interrupted |
| DRIFTING | equivalence | DRIFTING or STABLE | depends on drift reset policy |
| DRIFTING | mild_variation | DRIFTING | cumulative drift continues |
| DRIFTING | structural_break | SUSPENDED | rupture interrupts drift |
| SUSPENDED | equivalence to old regime | STABLE | recovery |
| SUSPENDED | structural_break | SUSPENDED or MIGRATING | depends on break persistence |
| MIGRATING | equivalence around new regime | STABLE | new regime confirmed |

---

## 6. Output object

For each processed transition, the memory layer emits a trajectory status update.

Canonical name:

TrajectoryStatusV1

Required fields:

- trajectory_id
- transition_index
- active_regime_id
- last_stable_regime_id
- regime_status
- cumulative_drift
- consecutive_mild_count
- consecutive_break_count
- trajectory_alert_flag
- last_signal_id
- protocol_version
- memory_version

Canonical JSON example:

```json
{
  "trajectory_id": "T_001",
  "transition_index": 12,
  "active_regime_id": "REG_ALPHA",
  "last_stable_regime_id": "REG_ALPHA",
  "regime_status": "DRIFTING",
  "cumulative_drift": 0.425,
  "consecutive_mild_count": 3,
  "consecutive_break_count": 0,
  "trajectory_alert_flag": false,
  "last_signal_id": "SIG_123",
  "protocol_version": "v1",
  "memory_version": "v1"
}


---

7. Scope

Trajectory Memory v1 is designed for:

ordered state sequences

transition streams

continuity monitoring

drift surveillance

early regime-shift detection


It is not designed to decide:

semantic correctness

truth value

policy actions

business logic


Those remain external.


---

8. Minimal claim

Trajectory Memory v1 provides the minimum stateful layer required to turn OMNIA from transition detection into trajectory surveillance.

It allows the system to distinguish between:

isolated noise

cumulative evolution

structural rupture

regime recovery

regime migration


without violating the architectural boundary.

