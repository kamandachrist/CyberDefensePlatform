from sqlalchemy.orm import Session

from app.repositories.asset_repository import (
    create_asset,
    delete_asset,
    get_asset,
    get_assets,
    update_asset,
)
from app.schemas.asset import AssetCreate, AssetUpdate


def create_new_asset(
    db: Session,
    asset_data: AssetCreate,
):
    return create_asset(
        db,
        asset_data,
    )


def list_assets(
    db: Session,
):
    return get_assets(db)


def retrieve_asset(
    db: Session,
    asset_id: int,
):
    return get_asset(
        db,
        asset_id,
    )


def update_existing_asset(
    db: Session,
    asset_id: int,
    asset_data: AssetUpdate,
):
    asset = get_asset(
        db,
        asset_id,
    )

    if not asset:
        return None

    return update_asset(
        db,
        asset,
        asset_data,
    )


def remove_asset(
    db: Session,
    asset_id: int,
):
    asset = get_asset(
        db,
        asset_id,
    )

    if not asset:
        return None

    delete_asset(
        db,
        asset,
    )

    return asset
