from sqlalchemy.orm import Session

from app.repositories.risk_repository import get_asset_risk_data
from app.schemas.risk import AssetRiskResponse, RiskFactor


def calculate_vulnerability_score(vulnerabilities) -> float:
    if not vulnerabilities:
        return 0.0

    total_score = 0.0

    for vulnerability in vulnerabilities:
        cvss = float(vulnerability.cvss_score)

        if cvss < 0:
            cvss = 0.0
        elif cvss > 10:
            cvss = 10.0

        total_score += cvss

    maximum_score = len(vulnerabilities) * 10

    return round(
        (total_score / maximum_score) * 100,
        2,
    )


def calculate_incident_score(incidents) -> float:
    if not incidents:
        return 0.0

    severity_scores = {
        "Critical": 100.0,
        "High": 75.0,
        "Medium": 50.0,
        "Low": 25.0,
        "Informational": 10.0,
    }

    total_score = 0.0

    for incident in incidents:
        severity = incident.severity.value

        total_score += severity_scores.get(
            severity,
            0.0,
        )

    return round(
        total_score / len(incidents),
        2,
    )


def calculate_asset_criticality_score(asset) -> float:
    criticality_scores = {
        "critical": 100.0,
        "high": 75.0,
        "medium": 50.0,
        "low": 25.0,
    }

    criticality = asset.criticality.lower()

    return criticality_scores.get(
        criticality,
        0.0,
    )


def determine_risk_level(risk_score: float) -> str:
    if risk_score >= 75:
        return "Critical"

    if risk_score >= 50:
        return "High"

    if risk_score >= 25:
        return "Medium"

    return "Low"


def calculate_asset_risk(
    db: Session,
    asset_id: int,
) -> AssetRiskResponse | None:

    risk_data = get_asset_risk_data(
        db,
        asset_id,
    )

    if not risk_data:
        return None

    asset = risk_data["asset"]
    vulnerabilities = risk_data["vulnerabilities"]
    incidents = risk_data["incidents"]

    vulnerability_score = calculate_vulnerability_score(
        vulnerabilities
    )

    incident_score = calculate_incident_score(
        incidents
    )

    asset_criticality_score = calculate_asset_criticality_score(
        asset
    )

    vulnerability_weight = 0.50
    incident_weight = 0.30
    criticality_weight = 0.20

    vulnerability_contribution = (
        vulnerability_score * vulnerability_weight
    )

    incident_contribution = (
        incident_score * incident_weight
    )

    criticality_contribution = (
        asset_criticality_score * criticality_weight
    )

    risk_score = round(
        vulnerability_contribution
        + incident_contribution
        + criticality_contribution,
        2,
    )

    risk_level = determine_risk_level(
        risk_score
    )

    risk_factors = [
        RiskFactor(
            name="Vulnerabilities",
            score=vulnerability_score,
            weight=vulnerability_weight,
            contribution=round(
                vulnerability_contribution,
                2,
            ),
        ),
        RiskFactor(
            name="Incidents",
            score=incident_score,
            weight=incident_weight,
            contribution=round(
                incident_contribution,
                2,
            ),
        ),
        RiskFactor(
            name="Asset Criticality",
            score=asset_criticality_score,
            weight=criticality_weight,
            contribution=round(
                criticality_contribution,
                2,
            ),
        ),
    ]

    return AssetRiskResponse(
        asset_id=asset.id,
        hostname=asset.hostname,
        risk_score=risk_score,
        risk_level=risk_level,
        vulnerability_score=vulnerability_score,
        incident_score=incident_score,
        asset_criticality_score=asset_criticality_score,
        risk_factors=risk_factors,
    )
