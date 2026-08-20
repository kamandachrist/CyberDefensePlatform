from sqlalchemy.orm import Session

from app.repositories.risk_repository import (
    get_alert_risk_data,
    get_all_assets,
    get_asset_risk_data,
)
from app.schemas.risk import (
    AlertPriorityResponse,
    AssetRiskListResponse,
    AssetRiskResponse,
    RiskFactor,
)


def calculate_vulnerability_score(vulnerabilities) -> float:
    if not vulnerabilities:
        return 0.0

    status_multipliers = {
        "open": 1.0,
        "in_progress": 0.75,
        "patched": 0.10,
        "resolved": 0.10,
        "closed": 0.05,
    }

    total_score = 0.0

    for vulnerability in vulnerabilities:
        cvss = float(vulnerability.cvss_score)

        if cvss < 0:
            cvss = 0.0
        elif cvss > 10:
            cvss = 10.0

        status = vulnerability.status.lower()

        multiplier = status_multipliers.get(
            status,
            1.0,
        )

        total_score += (
            (cvss / 10) * 100 * multiplier
        )

    return round(
        total_score / len(vulnerabilities),
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

    status_multipliers = {
        "Open": 1.0,
        "Investigating": 0.90,
        "Contained": 0.50,
        "Resolved": 0.10,
        "Closed": 0.05,
    }

    total_score = 0.0

    for incident in incidents:
        severity = incident.severity.value
        status = incident.status.value

        severity_score = severity_scores.get(
            severity,
            0.0,
        )

        status_multiplier = status_multipliers.get(
            status,
            1.0,
        )

        total_score += (
            severity_score * status_multiplier
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


def calculate_all_asset_risks(
    db: Session,
) -> AssetRiskListResponse:

    assets = get_all_assets(db)

    risk_results = []

    for asset in assets:
        risk = calculate_asset_risk(
            db,
            asset.id,
        )

        if risk is not None:
            risk_results.append(risk)

    risk_results.sort(
        key=lambda item: item.risk_score,
        reverse=True,
    )

    return AssetRiskListResponse(
        total_assets=len(risk_results),
        assets=risk_results,
    )


def calculate_alert_severity_score(alert) -> float:
    severity_scores = {
        "Critical": 100.0,
        "High": 75.0,
        "Medium": 50.0,
        "Low": 25.0,
        "Informational": 10.0,
    }

    severity = alert.severity.value

    return severity_scores.get(
        severity,
        0.0,
    )


def determine_alert_priority(priority_score: float) -> str:
    if priority_score >= 80:
        return "Critical"

    if priority_score >= 60:
        return "High"

    if priority_score >= 30:
        return "Medium"

    return "Low"


def generate_alert_recommendation(priority: str) -> str:
    recommendations = {
        "Critical": (
            "Immediate investigation required. "
            "Escalate to the incident response team."
        ),
        "High": (
            "Investigate immediately and assign "
            "to a SOC analyst."
        ),
        "Medium": (
            "Investigate during normal SOC operations "
            "and monitor for escalation."
        ),
        "Low": (
            "Monitor the alert and investigate "
            "if additional suspicious activity occurs."
        ),
    }

    return recommendations.get(
        priority,
        "Monitor the alert.",
    )


def calculate_alert_priority(
    db: Session,
    alert_id: int,
) -> AlertPriorityResponse | None:

    alert = get_alert_risk_data(
        db,
        alert_id,
    )

    if not alert:
        return None

    asset_risk = calculate_asset_risk(
        db,
        alert.asset_id,
    )

    if asset_risk is None:
        return None

    alert_severity_score = calculate_alert_severity_score(
        alert
    )

    alert_severity_weight = 0.60
    asset_risk_weight = 0.40

    priority_score = round(
        (
            alert_severity_score
            * alert_severity_weight
        )
        + (
            asset_risk.risk_score
            * asset_risk_weight
        ),
        2,
    )

    priority = determine_alert_priority(
        priority_score
    )

    recommendation = generate_alert_recommendation(
        priority
    )

    return AlertPriorityResponse(
        alert_id=alert.id,
        asset_id=alert.asset_id,
        title=alert.title,
        alert_severity=alert.severity.value,
        alert_severity_score=alert_severity_score,
        asset_risk_score=asset_risk.risk_score,
        priority_score=priority_score,
        priority=priority,
        recommendation=recommendation,
    )
