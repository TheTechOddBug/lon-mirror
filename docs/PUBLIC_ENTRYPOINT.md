# Public Entry Point

## What this repository is

lon-mirror is the root reference observer for the MB-X.01 / L.O.N. ecosystem.

It is not the whole ecosystem.

It is not the control plane.

It is not the measurement engine.

It is not the validation contract.

It is not a decision engine.

It is the public root reference observer.

## Start here

For the full ecosystem orientation, start here:

    https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md

For the lon-mirror root reference role, start here:

    https://github.com/Tuttotorna/lon-mirror/blob/main/docs/MBX01_LON_ROOT_REFERENCE_LINK.md

This file exists as the short public doorway for readers who arrive directly at lon-mirror.

## Minimal definition

    MB-X.01 = ecosystem layer
    L.O.N.  = Logical Origin Node / root reference frame
    OMNIA   = measurement backbone component
    lon-mirror = root reference observer

## Canonical backbone

    OMNIA measurement
      -> BoundaryCertificate
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION ValidationEnvelope
      -> CI regression
      -> compliant producer / adapter / consumer / observer

## Role of lon-mirror

    role: root_reference_observer
    status: satellite_compliant

lon-mirror may observe validated backbone output.

lon-mirror may route measurements through the existing backbone for reference checks.

lon-mirror must preserve the already declared ecosystem boundary.

## What lon-mirror must not do

lon-mirror must not become:

    validator
    control plane
    governance engine
    decision engine
    semantic-truth engine
    measurement replacement
    BoundaryCertificate redefinition
    ValidationEnvelope redefinition

## Layer separation

The ecosystem remains valid only while these separations remain true:

    measurement != validation
    validation != orchestration
    orchestration != decision
    decision != measurement
    observation != decision
    domain adaptation != backbone redefinition

## Related public documents

    MB-X.01 / L.O.N. ecosystem entry point:
    https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md

    lon-mirror root reference link:
    https://github.com/Tuttotorna/lon-mirror/blob/main/docs/MBX01_LON_ROOT_REFERENCE_LINK.md

    OMNIA ecosystem map:
    https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md

    OMNIA ecosystem status:
    https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md

    Backbone compliance registry:
    https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md

    lon-mirror public entry point:
    https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md

## Minimal mental model

    OMNIA measures.
    omnia-limit validates the boundary certificate.
    OMNIA-VALIDATION validates the control-plane envelope.
    OMNIAMIND orchestrates.
    Satellites adapt, observe, or consume.
    lon-mirror acts as root reference observer.
    No satellite owns the backbone.
    No layer silently replaces another layer.

## Final boundary

This repository is valuable only if it remains a bounded observer.

The moment lon-mirror claims final truth, governance authority, or independent validation ownership, it exits the declared backbone boundary.
