from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.models.threat import Threat
from app.models.vulnerability import Vulnerability
from app.models.incident import Incident
from app.models.enums import IncidentStatusEnum


def get_asset_count(db: Session):
    return db.query(Asset).count()


def get_online_asset_count(db: Session):
    return (
        db.query(Asset)
        .filter(func.lower(Asset.status) == "online")
        .count()
    )


def get_offline_asset_count(db: Session):
    return (
        db.query(Asset)
        .filter(func.lower(Asset.status) == "offline")
        .count()
    )


def get_threat_count(db: Session):
    return db.query(Threat).count()


def get_vulnerability_count(db: Session):
    return db.query(Vulnerability).count()


def get_critical_vulnerability_count(db: Session):
    return (
        db.query(Vulnerability)
        .filter(func.lower(Vulnerability.severity) == "critical")
        .count()
    )


def get_high_vulnerability_count(db: Session):
    return (
        db.query(Vulnerability)
        .filter(func.lower(Vulnerability.severity) == "high")
        .count()
    )


def get_incident_count(db: Session):
    return db.query(Incident).count()


def get_open_incident_count(db: Session):
    return (
        db.query(Incident)
        .filter(Incident.status == IncidentStatusEnum.OPEN)
        .count()
    )


def get_investigating_incident_count(db: Session):
    return (
        db.query(Incident)
        .filter(Incident.status == IncidentStatusEnum.INVESTIGATING)
        .count()
    )


def get_resolved_incident_count(db: Session):
    return (
        db.query(Incident)
        .filter(Incident.status == IncidentStatusEnum.RESOLVED)
        .count()
    )