from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate


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
    db.commit()
    db.refresh(asset)

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


def delete_asset(
    db: Session,
    asset: Asset,
) -> None:
    db.delete(asset)
    db.commit()
