from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


def create_asset(
    db: Session,
    asset_data: AssetCreate,
) -> Asset:
    asset = Asset(
        hostname=asset_data.hostname,
        ip_address=asset_data.ip_address,
        operating_system=asset_data.operating_system,
        owner=asset_data.owner,
    )

    db.add(asset)

    try:
        db.commit()
        db.refresh(asset)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Asset with hostname '{asset_data.hostname}' already exists"
        )

    return asset


def get_asset(
    db: Session,
    asset_id: int,
) -> Asset | None:
    return (
        db.query(Asset)
        .filter(Asset.id == asset_id)
        .first()
    )


def get_assets(
    db: Session,
) -> list[Asset]:
    return db.query(Asset).all()


def update_asset(
    db: Session,
    asset: Asset,
    asset_data: AssetUpdate,
) -> Asset:
    update_data = asset_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(asset, key, value)

    db.commit()
    db.refresh(asset)

    return asset


def delete_asset(
    db: Session,
    asset: Asset,
) -> None:
    db.delete(asset)
    db.commit()
