from types import SimpleNamespace

from app.services.risk_service import (
    calculate_asset_criticality_score,
    calculate_incident_score,
    calculate_vulnerability_score,
    determine_risk_level,
)


def test_calculate_vulnerability_score():
    vulnerabilities = [
        SimpleNamespace(
            cvss_score=8.5,
            status="open",
        ),
    ]

    score = calculate_vulnerability_score(
        vulnerabilities
    )

    assert score == 85.0


def test_calculate_vulnerability_score_multiple():
    vulnerabilities = [
        SimpleNamespace(
            cvss_score=8.0,
            status="open",
        ),
        SimpleNamespace(
            cvss_score=6.0,
            status="open",
        ),
    ]

    score = calculate_vulnerability_score(
        vulnerabilities
    )

    assert score == 70.0


def test_calculate_vulnerability_score_empty():
    score = calculate_vulnerability_score([])

    assert score == 0.0


def test_calculate_incident_score():
    incident = SimpleNamespace(
        severity=SimpleNamespace(value="High"),
        status=SimpleNamespace(value="Open"),
    )

    score = calculate_incident_score(
        [incident]
    )

    assert score == 75.0


def test_calculate_incident_score_empty():
    score = calculate_incident_score([])

    assert score == 0.0


def test_calculate_asset_criticality_score():
    asset = SimpleNamespace(
        criticality="high"
    )

    score = calculate_asset_criticality_score(
        asset
    )

    assert score == 75.0


def test_calculate_asset_criticality_score_critical():
    asset = SimpleNamespace(
        criticality="critical"
    )

    score = calculate_asset_criticality_score(
        asset
    )

    assert score == 100.0


def test_determine_risk_level():
    assert determine_risk_level(10) == "Low"
    assert determine_risk_level(25) == "Medium"
    assert determine_risk_level(50) == "High"
    assert determine_risk_level(75) == "Critical"
    assert determine_risk_level(100) == "Critical"


def test_open_vulnerability_keeps_full_cvss_risk():
    vulnerability = SimpleNamespace(
        cvss_score=8.5,
        status="open",
    )

    score = calculate_vulnerability_score(
        [vulnerability]
    )

    assert score == 85.0


def test_patched_vulnerability_has_lower_risk():
    vulnerability = SimpleNamespace(
        cvss_score=8.5,
        status="patched",
    )

    score = calculate_vulnerability_score(
        [vulnerability]
    )

    assert score < 85.0


def test_resolved_incident_has_lower_risk():
    incident = SimpleNamespace(
        severity=SimpleNamespace(value="High"),
        status=SimpleNamespace(value="Resolved"),
    )

    score = calculate_incident_score(
        [incident]
    )

    assert score < 75.0


def test_open_incident_keeps_full_severity_risk():
    incident = SimpleNamespace(
        severity=SimpleNamespace(value="High"),
        status=SimpleNamespace(value="Open"),
    )

    score = calculate_incident_score(
        [incident]
    )

    assert score == 75.0
