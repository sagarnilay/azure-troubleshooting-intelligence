from app.models.case import TroubleshootingCase
from app.services.diagnostics_engine import analyze_case


def test_windows_update_error():
    case = TroubleshootingCase(
        category="windows_update",
        error_code="0x800f081f",
        description="Update failed"
    )

    result = analyze_case(case)

    assert len(result["diagnoses"]) == 1
    assert result["diagnoses"][0]["confidence"] == 0.85