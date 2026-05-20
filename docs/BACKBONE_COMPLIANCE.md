# lon-mirror Backbone Compliance

## Role

lon-mirror is the Root Reference Observer.

It is the conceptual / reference anchor of the ecosystem.

It must not become a competing measurement engine.

It must not become a competing boundary validator.

It must not become a competing validation control plane.

It must not become a decision engine.

## Canonical flow

lon-mirror may observe the canonical backbone:

measurement
  -> OMNIA
  -> BoundaryCertificate
  -> omnia-limit
  -> OMNIA-VALIDATION
  -> ValidationEnvelope
  -> lon-mirror reference observation

## Public API

lon-mirror exposes:

observe_backbone_envelope_as_root_reference(...)
route_measurement_through_backbone_reference(...)

## Contract rule

lon-mirror does not redefine BoundaryCertificate.

lon-mirror does not redefine ValidationEnvelope.

lon-mirror does not bypass omnia-limit.

lon-mirror does not bypass OMNIA-VALIDATION.

lon-mirror does not emit final semantic-truth claims.

lon-mirror does not emit governance decisions.

## Import boundary note

The lon-mirror repository may contain a local directory named `omnia`.

When running tests from the lon-mirror repository root, that local directory can shadow the installed OMNIA package.

For reproducible workspace tests, set:

OMNIA_SOURCE_DIR=/path/to/OMNIA

The reference observer then loads OMNIA's BoundaryCertificate builder directly from that source tree without redefining the contract locally.

## Dynamic module loading note

OMNIA's boundary module uses dataclasses.

When dynamically loading that module from source, the module must be inserted into sys.modules before exec_module(...).

Otherwise Python dataclass processing can fail while resolving cls.__module__.

## Boundary

reference != measurement
measurement != validation
validation != orchestration
orchestration != decision
decision != semantic truth
semantic truth != backbone artifact

lon-mirror remains a root reference observer over the validated backbone.
