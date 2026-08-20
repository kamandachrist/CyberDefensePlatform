from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.alert import AlertCreate, AlertResponse, AlertUpdate
from app.services.alert_service import (
    create_new_alert,
    delete_existing_alert,
    get_alert_by_id,
    get_all_alerts,
    update_existing_alert,
)


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.post(
    "/",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_alert_endpoint(
    alert: AlertCreate,
    db: Session = Depends(get_db),
):
    return create_new_alert(db, alert)


@router.get(
    "/",
    response_model=list[AlertResponse],
)
def get_alerts_endpoint(
    db: Session = Depends(get_db),
):
    return get_all_alerts(db)


@router.get(
    "/{alert_id}",
    response_model=AlertResponse,
)
def get_alert_endpoint(
    alert_id: int,
    db: Session = Depends(get_db),
):
    return get_alert_by_id(db, alert_id)


@router.put(
    "/{alert_id}",
    response_model=AlertResponse,
)
def update_alert_endpoint(
    alert_id: int,
    alert_update: AlertUpdate,
    db: Session = Depends(get_db),
):
    return update_existing_alert(
        db,
        alert_id,
        alert_update,
    )


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_alert_endpoint(
    alert_id: int,
    db: Session = Depends(get_db),
):
    delete_existing_alert(
        db,
        alert_id,
    )
