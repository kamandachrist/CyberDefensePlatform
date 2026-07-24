from sqlalchemy.orm import Session

from app.repositories.threat_repository import (
    create_threat,
    get_threat,
    get_threats,
)

from app.schemas.threat import ThreatCreate


def create_new_threat(
    db: Session,
    threat_data: ThreatCreate,
):
    return create_threat(
        db,
        threat_data,
    )


def list_threats(
    db: Session,
):
    return get_threats(db)


def retrieve_threat(
    db: Session,
    threat_id: int,
):
    return get_threat(
        db,
        threat_id,
    )
