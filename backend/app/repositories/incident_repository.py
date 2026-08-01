from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.schemas.incident import IncidentCreate


def create_incident(
    db: Session,
    incident_data: IncidentCreate,
) -> Incident:

    incident = Incident(
        title=incident_data.title,
        description=incident_data.description,
        severity=incident_data.severity,
        asset_id=incident_data.asset_id,
        threat_id=incident_data.threat_id,
        assigned_to=incident_data.assigned_to,
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def get_incident(
    db: Session,
    incident_id: int,
) -> Incident | None:

    return (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )


def get_incidents(
    db: Session,
) -> list[Incident]:

    return db.query(Incident).all()


def update_incident(
    db: Session,
    incident: Incident,
    updates: dict,
) -> Incident:

    for field, value in updates.items():
        setattr(incident, field, value)

    db.commit()
    db.refresh(incident)

    return incident


def delete_incident(
    db: Session,
    incident: Incident,
) -> None:

    db.delete(incident)
    db.commit()
