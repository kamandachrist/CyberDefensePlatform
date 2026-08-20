from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.alert_repository import (
    create_alert,
    delete_alert,
    get_alert,
    get_alerts,
    update_alert,
)
from app.schemas.alert import AlertCreate, AlertUpdate


def create_new_alert(
    db: Session,
    alert: AlertCreate,
):
    return create_alert(db, alert)


def get_all_alerts(
    db: Session,
):
    return get_alerts(db)


def get_alert_by_id(
    db: Session,
    alert_id: int,
):
    alert = get_alert(db, alert_id)

    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return alert


def update_existing_alert(
    db: Session,
    alert_id: int,
    alert_update: AlertUpdate,
):
    alert = get_alert_by_id(db, alert_id)

    return update_alert(
        db,
        alert,
        alert_update,
    )


def delete_existing_alert(
    db: Session,
    alert_id: int,
):
    alert = get_alert_by_id(db, alert_id)

    delete_alert(db, alert)
