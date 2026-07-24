from sqlalchemy.orm import Session

from app.models.threat import Threat
from app.schemas.threat import ThreatCreate


def create_threat(
    db: Session,
    threat_data: ThreatCreate,
) -> Threat:
    threat = Threat(
        name=threat_data.name,
        severity=threat_data.severity,
        category=threat_data.category,
        source=threat_data.source,
        description=threat_data.description,
        ioc=threat_data.ioc,
    )

    db.add(threat)
    db.commit()
    db.refresh(threat)

    return threat


def get_threat(
    db: Session,
    threat_id: int,
) -> Threat | None:
    return (
        db.query(Threat)
        .filter(Threat.id == threat_id)
        .first()
    )


def get_threats(
    db: Session,
) -> list[Threat]:
    return db.query(Threat).all()


def delete_threat(
    db: Session,
    threat: Threat,
) -> None:
    db.delete(threat)
    db.commit()
