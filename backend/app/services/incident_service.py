from sqlalchemy.orm import Session

from app.repositories.incident_repository import (
    create_incident,
    get_incident,
    get_incidents,
    delete_incident,
)

from app.schemas.incident import IncidentCreate


def create_new_incident(
    db: Session,
    incident_data: IncidentCreate,
):
    return create_incident(
        db,
        incident_data,
    )


def list_incidents(
    db: Session,
):
    return get_incidents(db)


def retrieve_incident(
    db: Session,
    incident_id: int,
):
    return get_incident(
        db,
        incident_id,
    )


def remove_incident(
    db: Session,
    incident_id: int,
):
    incident = get_incident(
        db,
        incident_id,
    )

    if incident:
        delete_incident(
            db,
            incident,
        )

    return incident
