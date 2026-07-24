from pydantic import BaseModel, ConfigDict


class AssetBase(BaseModel):
    hostname: str
    ip_address: str
    operating_system: str
    owner: str


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    hostname: str | None = None
    ip_address: str | None = None
    operating_system: str | None = None
    owner: str | None = None


class AssetResponse(AssetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
