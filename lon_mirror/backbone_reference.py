from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Any

from omnia_limit import validate_certificate
from omnia_validation.enveloper import process_boundary_step


def _load_omnia_boundary_builder():
    """Load OMNIA's builder without being shadowed by lon-mirror/omnia.

    The lon-mirror repository may contain a local directory named `omnia`.
    When tests run from the repository root, that local directory can shadow
    the installed OMNIA package. For that reason this loader first honors the
    explicit OMNIA_SOURCE_DIR environment variable used by the reproducible
    workspace and then falls back to the normal installed import.

    Important implementation detail:
    dataclasses require the dynamically loaded module to be present in
    sys.modules before exec_module(...), otherwise dataclass processing can
    fail while resolving cls.__module__.
    """

    source_dir = os.environ.get("OMNIA_SOURCE_DIR")
    if source_dir:
        candidate = Path(source_dir) / "omnia" / "boundary_certificate.py"
        if candidate.exists():
            module_name = "_omnia_external_boundary_certificate"
            spec = importlib.util.spec_from_file_location(module_name, candidate)
            if spec is None or spec.loader is None:
                raise ImportError(f"Cannot load OMNIA boundary module from {candidate}")

            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module.build_boundary_certificate_from_measurement

    try:
        from omnia import build_boundary_certificate_from_measurement

        return build_boundary_certificate_from_measurement
    except ImportError as exc:
        raise ImportError(
            "Could not import OMNIA build_boundary_certificate_from_measurement. "
            "Set OMNIA_SOURCE_DIR to the cloned OMNIA repository root when running "
            "inside a repository that contains a local omnia/ directory."
        ) from exc


def observe_backbone_envelope_as_root_reference(envelope: dict[str, Any]) -> dict[str, Any]:
    """Observe a validated OMNIA backbone envelope from the lon-mirror layer.

    lon-mirror is treated as the root reference / conceptual anchor.

    It does not define BoundaryCertificate.
    It does not define ValidationEnvelope.
    It does not validate contracts.
    It does not emit governance decisions.
    It does not claim semantic truth.
    It observes the existing backbone output while preserving layer separation.
    """

    details = envelope.get("details", {})

    return {
        "observer": "lon-mirror",
        "role": "root_reference_observer",
        "observed_status": envelope.get("validation_status"),
        "target_repository": details.get("target_repository"),
        "certificate_id": details.get("certificate_id"),
        "saturation_detected": details.get("saturation_detected"),
        "ast_deformation_index": details.get("ast_deformation_index"),
        "perturbation_step": details.get("perturbation_step"),
        "semantic_truth_claim": None,
        "governance_decision": None,
        "root_reference_preserved": True,
        "backbone_contract_preserved": True,
    }


def route_measurement_through_backbone_reference(
    measurement: dict[str, Any],
    *,
    target_repository: str = "lon-mirror",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Route a measurement through the canonical backbone for reference observation.

    Flow:

    measurement
      -> OMNIA build_boundary_certificate_from_measurement()
      -> BoundaryCertificate-compatible artifact
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION process_boundary_step()
      -> ValidationEnvelope
      -> lon-mirror root-reference observation

    lon-mirror does not own the measurement contract.

    lon-mirror remains a reference observer over the validated backbone.
    """

    build_boundary_certificate_from_measurement = _load_omnia_boundary_builder()

    raw_certificate = build_boundary_certificate_from_measurement(
        measurement,
        target_repository=target_repository,
        certificate_id=certificate_id,
        timestamp=timestamp,
    )

    validate_certificate(raw_certificate)
    envelope = process_boundary_step(raw_certificate)

    return observe_backbone_envelope_as_root_reference(envelope)
