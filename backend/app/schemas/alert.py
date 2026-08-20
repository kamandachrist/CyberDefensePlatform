from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import IncidentStatusEnum, SeverityEnum


class AlertBase(BaseModel):
    title: str
    description: str
    severity: SeverityEnum
    status: IncidentStatusEnum = IncidentStatusEnum.OPEN
    asset_id: int
    threat_id: int | None = None
    source: str
    assigned_to: str | None = None


class AlertCreate(AlertBase):
    pass


class AlertUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    severity: SeverityEnum | None = None
    status: IncidentStatusEnum | None = None
    asset_id: int | None = None
    threat_id: int | None = None
    source: str | None = None
    assigned_to: str | None = None


class AlertResponse(AlertBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
