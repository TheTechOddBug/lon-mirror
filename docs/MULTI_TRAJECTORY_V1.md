# OMNIA — Multi-Trajectory Handling v1

## Status

This document defines how OMNIA handles multiple independent trajectories in the same process.

It extends Trajectory Memory v1 from single-stream state tracking to parallel stream tracking.

Architectural boundary remains unchanged:

measurement != protocol != memory != decision

OMNIA tracks multiple trajectories independently.
It does not merge them unless an external layer explicitly requests cross-trajectory comparison.

---

## 1. Goal

The goal of Multi-Trajectory Handling v1 is to allow OMNIA to process multiple ordered streams in parallel without mixing:

- transition history
- drift accumulation
- break counters
- active regimes
- alerts

Each stream must preserve its own memory state.

---

## 2. Core principle

Each trajectory is keyed by:

stream_id

All memory operations are local to that stream_id.

No state from stream A may affect:

- cumulative_drift of stream B
- regime_status of stream B
- alert flags of stream B
- regime identifiers of stream B

This isolation rule is mandatory.

---

## 3. Required input extension

To support multiple trajectories, each input record must include:

- stream_id
- t
- v

Minimal example:

```json
{"stream_id":"asset_A","t":"2026-01-01","v":100.0}
{"stream_id":"asset_A","t":"2026-01-02","v":100.4}
{"stream_id":"asset_B","t":"2026-01-01","v":42.0}
{"stream_id":"asset_B","t":"2026-01-02","v":41.8}

Records may be interleaved in the file. OMNIA must reconstruct trajectory continuity separately for each stream_id.


---

4. Stream-local ordering rule

Within each stream_id, records must be processed in ascending temporal order.

If the input file is already ordered by stream and time, processing may proceed directly.

If records are interleaved, OMNIA must first group by stream_id and then sort by t inside each group.

No cross-stream ordering is meaningful for trajectory memory.


---

5. Core objects

5.1 MultiTrajectoryManager

A MultiTrajectoryManager is the stateful container that holds one TrajectoryTracker per stream_id.

Responsibilities:

create a new TrajectoryTracker when a new stream_id appears

route each transition to the correct tracker

preserve isolation across trackers

emit output records with both stream-local signal and stream-local memory state



---

5.2 Tracker registry

The manager maintains:

trackers: Dict[str, TrajectoryTracker]

where:

key = stream_id

value = tracker instance for that stream


If a stream_id is unseen, a new tracker is initialized.


---

6. Initialization rule

When a new stream_id appears for the first time:

create a new TrajectoryTracker

assign trajectory_id derived from stream_id

initialize:

active_regime_id = REG_ALPHA

last_stable_regime_id = REG_ALPHA

regime_status = STABLE

cumulative_drift = 0

consecutive_mild_count = 0

consecutive_break_count = 0



This initialization is local to that stream only.


---

7. Output requirements

Each emitted output record must include:

stream_id

transition_signal

trajectory_status


Both signal and memory state must refer to the same stream.

Minimal output shape:

{
  "stream_id": "asset_A",
  "transition_signal": { ... },
  "trajectory_status": { ... }
}


---

8. Isolation invariants

The following invariants must always hold:

1. cumulative_drift is computed only from transitions of the same stream_id


2. consecutive_mild_count is local to one stream_id


3. consecutive_break_count is local to one stream_id


4. active_regime_id is local to one stream_id


5. trajectory_alert_flag is local to one stream_id


6. resetting one trajectory must not reset any other trajectory



If any of these invariants fail, the multi-trajectory engine is invalid.


---

9. Recommended trajectory_id rule

Recommended mapping:

trajectory_id = "T_" + stream_id

Examples:

stream_id = asset_A -> trajectory_id = T_asset_A

stream_id = server_01 -> trajectory_id = T_server_01


This keeps trajectory identity stable and auditable.


---

10. Minimal claim

Multi-Trajectory Handling v1 allows OMNIA to scale from one temporal stream to many parallel streams while preserving strict memory isolation.

This is the minimum required step before testing OMNIA on realistic monitoring environments.

