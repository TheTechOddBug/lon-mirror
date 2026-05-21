# First Reader Path

## Purpose

This is the shortest public path for a reader who lands directly on lon-mirror.

lon-mirror is not the whole MB-X.01 / L.O.N. ecosystem.

lon-mirror is the root reference observer.

## Thirty-second version

MB-X.01 is the ecosystem layer.

L.O.N. means Logical Origin Node.

OMNIA measures structural behavior.

omnia-limit validates the boundary certificate.

OMNIA-VALIDATION validates the control-plane envelope and protects the public registry.

lon-mirror acts as root reference observer.

lon-mirror may observe validated backbone output.

lon-mirror must not become the validator, the control plane, the governance engine, or the decision engine.

## Start here

1. lon-mirror public entry point:
   https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md

2. lon-mirror root reference link:
   https://github.com/Tuttotorna/lon-mirror/blob/main/docs/MBX01_LON_ROOT_REFERENCE_LINK.md

3. Full MB-X.01 / L.O.N. ecosystem entry point:
   https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md

4. OMNIA-VALIDATION first reader path:
   https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/FIRST_READER_PATH.md

5. Ecosystem map:
   https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md

6. Ecosystem status:
   https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md

7. Backbone compliance registry:
   https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md

## One-line backbone

OMNIA measurement -> BoundaryCertificate -> omnia-limit validate_certificate() -> OMNIA-VALIDATION ValidationEnvelope -> CI regression -> compliant producer / adapter / consumer / observer

## lon-mirror role

role: root_reference_observer
status: satellite_compliant

## Boundary rule

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement
observation != decision
domain adaptation != backbone redefinition

## What lon-mirror must not become

validator
control plane
governance engine
decision engine
semantic-truth engine
measurement replacement
BoundaryCertificate redefinition
ValidationEnvelope redefinition

## Current public anchors

OMNIA-VALIDATION commit at patch time:
2e7e63c

lon-mirror commit at patch time:
f74b799

## Minimal mental model

lon-mirror observes the declared ecosystem boundary.

It does not own the backbone.

It does not validate independently.

It does not decide.

It points the reader back to the public MB-X.01 / L.O.N. entry point and remains a bounded root reference observer.
