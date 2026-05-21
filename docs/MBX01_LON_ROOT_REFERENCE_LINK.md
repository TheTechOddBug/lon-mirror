# lon-mirror Root Reference Link

## Status

`lon-mirror` is the root reference observer for the MB-X.01 / L.O.N. ecosystem.

This repository now links outward to the public ecosystem entry point maintained in `OMNIA-VALIDATION`.

The purpose of this document is not to redefine the ecosystem.

The purpose is to make the root reference path visible from `lon-mirror`.

## Public entry point

Start here:

~~~text
https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md
~~~

That document explains:

~~~text
MB-X.01 identity
L.O.N. identity
canonical backbone
core repositories
compliant satellites
role separation
forbidden overclaims
reader path
executable protection
~~~

## Root reference role

`lon-mirror` has this bounded role:

~~~text
root_reference_observer
~~~

It may observe validated backbone output.

It may route measurements through the existing backbone for reference checks.

It must not become a validator.

It must not become a control plane.

It must not become a governance engine.

It must not become a decision engine.

It must not become a semantic-truth engine.

## Canonical backbone

The ecosystem backbone remains:

~~~text
OMNIA measurement
  -> BoundaryCertificate
  -> omnia-limit validate_certificate()
  -> OMNIA-VALIDATION ValidationEnvelope
  -> CI regression
  -> compliant producer / adapter / consumer / observer
~~~

## Layer separation

The root reference remains valid only while these separations remain true:

~~~text
measurement != validation
validation != orchestration
orchestration != decision
decision != measurement
observation != decision
domain adaptation != backbone redefinition
~~~

## Related public documents

~~~text
MB-X.01 / L.O.N. entry point: https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md

Ecosystem map: https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md

Ecosystem status: https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md

Backbone compliance registry: https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md
~~~

## Boundary

This document does not create a new contract.

It points the root reference repository toward the already declared ecosystem entry point.

The backbone still belongs to the separated chain:

~~~text
OMNIA measures.
omnia-limit validates the boundary certificate.
OMNIA-VALIDATION validates the control-plane envelope.
OMNIAMIND orchestrates.
Satellites adapt, observe, or consume.
lon-mirror acts as root reference observer.
No satellite owns the backbone.
No layer silently replaces another layer.
~~~
