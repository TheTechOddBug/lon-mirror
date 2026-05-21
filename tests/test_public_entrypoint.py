from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOC = ROOT / "docs" / "PUBLIC_ENTRYPOINT.md"

def test_public_entrypoint_doc_exists():
    assert DOC.exists()

def test_public_entrypoint_contains_identity_and_role():
    text = DOC.read_text(encoding="utf-8")

    required_fragments = [
        "Public Entry Point",
        "lon-mirror",
        "MB-X.01",
        "L.O.N.",
        "Logical Origin Node",
        "root reference observer",
        "root_reference_observer",
        "satellite_compliant",
    ]

    missing = [fragment for fragment in required_fragments if fragment not in text]
    assert not missing

def test_public_entrypoint_contains_canonical_backbone():
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

def test_public_entrypoint_preserves_layer_separation():
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

def test_public_entrypoint_rejects_layer_collapse():
    text = DOC.read_text(encoding="utf-8")

    required_boundaries = [
        "validator",
        "control plane",
        "governance engine",
        "decision engine",
        "semantic-truth engine",
        "measurement replacement",
        "BoundaryCertificate redefinition",
        "ValidationEnvelope redefinition",
    ]

    missing = [boundary for boundary in required_boundaries if boundary not in text]
    assert not missing

def test_public_entrypoint_links_to_public_ecosystem_docs():
    text = DOC.read_text(encoding="utf-8")

    required_links = [
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/MBX01_LON_ROOT_REFERENCE_LINK.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md",
    ]

    missing = [link for link in required_links if link not in text]
    assert not missing

def test_readme_contains_public_entrypoint_section():
    assert README.exists()

    text = README.read_text(encoding="utf-8")

    required_fragments = [
        "<!-- LON-MIRROR PUBLIC ENTRYPOINT:START -->",
        "<!-- LON-MIRROR PUBLIC ENTRYPOINT:END -->",
        "docs/PUBLIC_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md",
        "root reference observer",
    ]

    missing = [fragment for fragment in required_fragments if fragment not in text]
    assert not missing
