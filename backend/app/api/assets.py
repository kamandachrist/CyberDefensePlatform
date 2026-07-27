from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.asset import (
    AssetCreate,
    AssetUpdate,
    AssetResponse,
)

from app.services.asset_service import (
    create_new_asset,
    list_assets,
    retrieve_asset,
    update_existing_asset,
    remove_asset,
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=AssetResponse,
)
def create_asset_endpoint(
    asset: AssetCreate,
    db: Session = Depends(get_db),
):
    return create_new_asset(db, asset)


@router.get(
    "/",
    response_model=list[AssetResponse],
)
def get_assets_endpoint(
    db: Session = Depends(get_db),
):
    return list_assets(db)


@router.get(
    "/{asset_id}",
    response_model=AssetResponse,
)
def get_asset_endpoint(
    asset_id: int,
    db: Session = Depends(get_db),
):
    asset = retrieve_asset(db, asset_id)

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return asset


@router.put(
    "/{asset_id}",
    response_model=AssetResponse,
)
def update_asset_endpoint(
    asset_id: int,
    asset: AssetUpdate,
    db: Session = Depends(get_db),
):
    updated_asset = update_existing_asset(
        db,
        asset_id,
        asset,
    )

    if not updated_asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return updated_asset


@router.delete(
    "/{asset_id}",
)
def delete_asset_endpoint(
    asset_id: int,
    db: Session = Depends(get_db),
):
    asset = remove_asset(
        db,
        asset_id,
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return {
        "message": "Asset deleted successfully"
    }
