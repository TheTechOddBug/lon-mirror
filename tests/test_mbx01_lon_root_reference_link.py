from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOC = ROOT / "docs" / "MBX01_LON_ROOT_REFERENCE_LINK.md"


def test_root_reference_link_doc_exists():
    assert DOC.exists()


def test_root_reference_link_doc_contains_entrypoint_url():
    text = DOC.read_text(encoding="utf-8")

    required_fragments = [
        "lon-mirror Root Reference Link",
        "root_reference_observer",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md",
    ]

    missing = [fragment for fragment in required_fragments if fragment not in text]
    assert not missing


def test_root_reference_link_doc_contains_canonical_backbone():
    text = DOC.read_text(encoding="utf-8")

    required_fragments = [
        "OMNIA measurement",
        "BoundaryCertificate",
        "omnia-limit validate_certificate()",
        "OMNIA-VALIDATION ValidationEnvelope",
        "CI regression",
        "compliant producer / adapter / consumer / observer",
    ]

    missing = [fragment for fragment in required_fragments if fragment not in text]
    assert not missing


def test_root_reference_link_doc_preserves_layer_separation():
    text = DOC.read_text(encoding="utf-8")

    required_rules = [
        "measurement != validation",
        "validation != orchestration",
        "orchestration != decision",
        "decision != measurement",
        "observation != decision",
        "domain adaptation != backbone redefinition",
    ]

    missing = [rule for rule in required_rules if rule not in text]
    assert not missing


def test_root_reference_link_doc_rejects_layer_collapse():
    text = DOC.read_text(encoding="utf-8")

    required_boundaries = [
        "must not become a validator",
        "must not become a control plane",
        "must not become a governance engine",
        "must not become a decision engine",
        "must not become a semantic-truth engine",
    ]

    missing = [boundary for boundary in required_boundaries if boundary not in text]
    assert not missing


def test_readme_contains_mbx01_lon_entrypoint_section():
    assert README.exists()

    text = README.read_text(encoding="utf-8")

    required_fragments = [
        "<!-- MB-X.01 LON ROOT REFERENCE LINK:START -->",
        "<!-- MB-X.01 LON ROOT REFERENCE LINK:END -->",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md",
        "docs/MBX01_LON_ROOT_REFERENCE_LINK.md",
        "root reference observer",
    ]

    missing = [fragment for fragment in required_fragments if fragment not in text]
    assert not missing
