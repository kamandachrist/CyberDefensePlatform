from sqlalchemy.orm import Session

from app.repositories import dashboard_repository


def get_dashboard_summary(db: Session):

    return {
        "assets": {
            "total": dashboard_repository.get_asset_count(db),
            "online": dashboard_repository.get_online_asset_count(db),
            "offline": dashboard_repository.get_offline_asset_count(db),
        },
        "threats": {
            "total": dashboard_repository.get_threat_count(db),
        },
        "vulnerabilities": {
            "total": dashboard_repository.get_vulnerability_count(db),
            "critical": dashboard_repository.get_critical_vulnerability_count(db),
            "high": dashboard_repository.get_high_vulnerability_count(db),
        },
        "incidents": {
            "total": dashboard_repository.get_incident_count(db),
            "open": dashboard_repository.get_open_incident_count(db),
            "investigating": dashboard_repository.get_investigating_incident_count(db),
            "resolved": dashboard_repository.get_resolved_incident_count(db),
        },
    }