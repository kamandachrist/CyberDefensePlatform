from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.risk import (
    AlertPriorityResponse,
    AssetRiskListResponse,
    AssetRiskResponse,
)
from app.services.risk_service import (
    calculate_alert_priority,
    calculate_all_asset_risks,
    calculate_asset_risk,
)


router = APIRouter(
    prefix="/risk",
    tags=["Risk"],
)


@router.get(
    "/assets",
    response_model=AssetRiskListResponse,
)
def get_all_asset_risks(
    db: Session = Depends(get_db),
):
    return calculate_all_asset_risks(db)


@router.get(
    "/assets/{asset_id}",
    response_model=AssetRiskResponse,
)
def get_asset_risk(
    asset_id: int,
    db: Session = Depends(get_db),
):
    risk = calculate_asset_risk(
        db,
        asset_id,
    )

    if risk is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return risk


@router.get(
    "/alerts/{alert_id}/priority",
    response_model=AlertPriorityResponse,
)
def get_alert_priority(
    alert_id: int,
    db: Session = Depends(get_db),
):
    priority = calculate_alert_priority(
        db,
        alert_id,
    )

    if priority is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    return priority
