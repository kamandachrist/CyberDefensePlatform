from types import SimpleNamespace

from app.services.risk_service import (
    calculate_asset_criticality_score,
    calculate_incident_score,
    calculate_vulnerability_score,
    determine_risk_level,
)


def test_calculate_vulnerability_score():
    vulnerabilities = [
        SimpleNamespace(cvss_score=8.5),
    ]

    score = calculate_vulnerability_score(
        vulnerabilities
    )

    assert score == 85.0


def test_calculate_vulnerability_score_multiple():
    vulnerabilities = [
        SimpleNamespace(cvss_score=8.0),
        SimpleNamespace(cvss_score=6.0),
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
        severity=SimpleNamespace(value="High")
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
