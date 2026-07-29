from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import (
    AssetCriticality,
    AssetEnvironment,
    AssetStatus,
    AssetType,
)


class AssetBase(BaseModel):
    hostname: str
    ip_address: str
    operating_system: str
    owner: str
    asset_type: AssetType
    criticality: AssetCriticality
    environment: AssetEnvironment
    status: AssetStatus
    last_seen: datetime


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    hostname: str | None = None
    ip_address: str | None = None
    operating_system: str | None = None
    owner: str | None = None
    asset_type: AssetType | None = None
    criticality: AssetCriticality | None = None
    environment: AssetEnvironment | None = None
    status: AssetStatus | None = None
    last_seen: datetime | None = None


class AssetResponse(AssetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)