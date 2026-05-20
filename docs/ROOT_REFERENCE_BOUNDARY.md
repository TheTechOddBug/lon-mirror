# Root Reference Boundary

## Purpose

This document prevents lon-mirror from collapsing into the active software layers of the OMNIA backbone.

## Correct position

lon-mirror is the root reference layer.

It may expose a reference observer.

It may route a measurement through the existing backbone for reproducibility checks.

It may document the conceptual origin of the ecosystem.

It must not replace any of the active software layers.

## Active layers

OMNIA
  measurement artifact emission

omnia-limit
  BoundaryCertificate validation

OMNIA-VALIDATION
  ValidationEnvelope emission and regression control plane

OMNIAMIND
  orchestration

Satellite repositories
  producers, adapters, consumers, or observers

lon-mirror
  root reference observer

## Forbidden outputs

lon-mirror must not output:

final semantic truth
governance decision
replacement BoundaryCertificate
replacement ValidationEnvelope
parallel schema
parallel validation control plane
hidden policy engine

## Principle

The root reference can observe the backbone.

It must not swallow the backbone.
