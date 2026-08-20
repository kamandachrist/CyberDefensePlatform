from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.schemas.alert import AlertCreate, AlertUpdate


def create_alert(db: Session, alert: AlertCreate) -> Alert:
    db_alert = Alert(**alert.model_dump())

    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    return db_alert


def get_alert(db: Session, alert_id: int) -> Alert | None:
    return (
        db.query(Alert)
        .filter(Alert.id == alert_id)
        .first()
    )


def get_alerts(db: Session) -> list[Alert]:
    return (
        db.query(Alert)
        .order_by(Alert.created_at.desc())
        .all()
    )


def update_alert(
    db: Session,
    alert: Alert,
    alert_update: AlertUpdate,
) -> Alert:
    update_data = alert_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(alert, field, value)

    db.commit()
    db.refresh(alert)

    return alert


def delete_alert(
    db: Session,
    alert: Alert,
) -> None:
    db.delete(alert)
    db.commit()
