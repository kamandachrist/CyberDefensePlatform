from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.models.incident import Incident
from app.models.vulnerability import Vulnerability


def get_asset_risk_data(
    db: Session,
    asset_id: int,
):
    asset = (
        db.query(Asset)
        .filter(Asset.id == asset_id)
        .first()
    )

    if not asset:
        return None

    vulnerabilities = (
        db.query(Vulnerability)
        .filter(Vulnerability.asset_id == asset_id)
        .all()
    )

    incidents = (
        db.query(Incident)
        .filter(Incident.asset_id == asset_id)
        .all()
    )

    return {
        "asset": asset,
        "vulnerabilities": vulnerabilities,
        "incidents": incidents,
    }
