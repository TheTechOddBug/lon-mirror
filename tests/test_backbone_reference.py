from lon_mirror import (
    observe_backbone_envelope_as_root_reference,
    route_measurement_through_backbone_reference,
)


def test_route_measurement_through_backbone_reference_stop_flow():
    measurement = {
        "drift_score": 0.44,
        "perturbation_step": 4,
        "gate_status": "STOP",
        "omega": 0.82,
        "sei": 0.01,
        "iri": 0.99,
    }

    observation = route_measurement_through_backbone_reference(
        measurement,
        target_repository="lon-mirror",
        certificate_id="lon-mirror-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "lon-mirror"
    assert observation["role"] == "root_reference_observer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "lon-mirror-stop-cert"
    assert observation["target_repository"] == "lon-mirror"
    assert observation["saturation_detected"] is True
    assert observation["ast_deformation_index"] == 0.44
    assert observation["perturbation_step"] == 4
    assert observation["semantic_truth_claim"] is None
    assert observation["governance_decision"] is None
    assert observation["root_reference_preserved"] is True
    assert observation["backbone_contract_preserved"] is True


def test_route_measurement_through_backbone_reference_continue_flow():
    measurement = {
        "delta_omega": 0.12,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "omega": 0.91,
        "sei": 0.20,
        "iri": 0.40,
        "reason": "Measurement still productive",
    }

    observation = route_measurement_through_backbone_reference(
        measurement,
        target_repository="lon-mirror",
        certificate_id="lon-mirror-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "lon-mirror"
    assert observation["role"] == "root_reference_observer"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "lon-mirror-continue-cert"
    assert observation["target_repository"] == "lon-mirror"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.12
    assert observation["perturbation_step"] == 1
    assert observation["semantic_truth_claim"] is None
    assert observation["governance_decision"] is None
    assert observation["root_reference_preserved"] is True
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_as_root_reference():
    envelope = {
        "envelope_id": "lon-envelope",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-lon-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.03,
            "perturbation_step": 7,
        },
    }

    observation = observe_backbone_envelope_as_root_reference(envelope)

    assert observation["observer"] == "lon-mirror"
    assert observation["role"] == "root_reference_observer"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "existing-lon-cert"
    assert observation["target_repository"] == "OMNIA"
    assert observation["semantic_truth_claim"] is None
    assert observation["governance_decision"] is None
    assert observation["root_reference_preserved"] is True
    assert observation["backbone_contract_preserved"] is True
