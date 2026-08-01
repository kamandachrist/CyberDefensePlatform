from sqlalchemy.orm import Session

from app.repositories.threat_repository import (
    create_threat,
    get_threat,
    get_threats,
    update_threat,
    delete_threat,
)

from app.schemas.threat import (
    ThreatCreate,
    ThreatUpdate,
)


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


def update_existing_threat(
    db: Session,
    threat_id: int,
    threat_data: ThreatUpdate,
):
    threat = get_threat(
        db,
        threat_id,
    )

    if not threat:
        return None

    updates = threat_data.model_dump(
        exclude_unset=True
    )

    return update_threat(
        db,
        threat,
        updates,
    )


def remove_threat(
    db: Session,
    threat_id: int,
):
    threat = get_threat(
        db,
        threat_id,
    )

    if threat:
        delete_threat(
            db,
            threat,
        )

    return threat
