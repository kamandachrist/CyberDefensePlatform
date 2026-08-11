from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.risk import AssetRiskResponse
from app.services.risk_service import calculate_asset_risk


router = APIRouter(
    prefix="/risk",
    tags=["Risk"],
)


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
