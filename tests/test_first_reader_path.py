from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOC = ROOT / "docs" / "FIRST_READER_PATH.md"
CI = ROOT / ".github" / "workflows" / "ci.yml"

OV_COMMIT = "2e7e63c"
LON_COMMIT = "f74b799"

def test_first_reader_path_doc_exists():
    assert DOC.exists()

def test_first_reader_path_contains_short_public_model():
    text = DOC.read_text(encoding="utf-8")
    required = [
        "First Reader Path",
        "Thirty-second version",
        "MB-X.01",
        "Logical Origin Node",
        "root reference observer",
        "OMNIA measures",
        "omnia-limit validates",
        "OMNIA-VALIDATION validates",
        "OMNIA measurement",
        "BoundaryCertificate",
        "omnia-limit validate_certificate()",
        "OMNIA-VALIDATION ValidationEnvelope",
        "CI regression",
    ]
    missing = [fragment for fragment in required if fragment not in text]
    assert not missing

def test_first_reader_path_preserves_lon_mirror_boundary():
    text = DOC.read_text(encoding="utf-8")
    required = [
        "role: root_reference_observer",
        "status: satellite_compliant",
        "measurement != validation",
        "validation != orchestration",
        "orchestration != decision",
        "decision != measurement",
        "observation != decision",
        "domain adaptation != backbone redefinition",
        "validator",
        "control plane",
        "governance engine",
        "decision engine",
        "semantic-truth engine",
        "measurement replacement",
        "BoundaryCertificate redefinition",
        "ValidationEnvelope redefinition",
    ]
    missing = [fragment for fragment in required if fragment not in text]
    assert not missing

def test_first_reader_path_links_to_public_docs():
    text = DOC.read_text(encoding="utf-8")
    required = [
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/MBX01_LON_ROOT_REFERENCE_LINK.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/FIRST_READER_PATH.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_MAP.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_STATUS.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/ECOSYSTEM_BACKBONE_COMPLIANCE_REGISTRY.md",
    ]
    missing = [fragment for fragment in required if fragment not in text]
    assert not missing


def test_first_reader_path_records_patch_anchors():
    text = DOC.read_text(encoding="utf-8")
    assert OV_COMMIT in text
    assert LON_COMMIT in text

def test_readme_contains_first_reader_path_section():
    assert README.exists()
    text = README.read_text(encoding="utf-8")
    required = [
        "<!-- FIRST READER PATH:START -->",
        "<!-- FIRST READER PATH:END -->",
        "docs/FIRST_READER_PATH.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/FIRST_READER_PATH.md",
        "https://github.com/Tuttotorna/lon-mirror/blob/main/docs/PUBLIC_ENTRYPOINT.md",
        "https://github.com/Tuttotorna/OMNIA-VALIDATION/blob/main/docs/MBX01_LON_ECOSYSTEM_ENTRYPOINT.md",
        "measurement != validation != orchestration != decision",
    ]
    missing = [fragment for fragment in required if fragment not in text]
    assert not missing

def test_ci_runs_first_reader_path_test():
    assert CI.exists()
    text = CI.read_text(encoding="utf-8")
    assert "python -m pytest -q tests/test_first_reader_path.py" in text
