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