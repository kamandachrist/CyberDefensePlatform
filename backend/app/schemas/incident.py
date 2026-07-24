from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import IncidentStatusEnum, SeverityEnum


class IncidentBase(BaseModel):
    title: str
    description: str
    severity: SeverityEnum
    status: IncidentStatusEnum
    asset_id: int
    threat_id: int
    assigned_to: str | None = None
    opened_at: datetime
    closed_at: datetime | None = None


class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: SeverityEnum
    asset_id: int
    threat_id: int
    assigned_to: str | None = None


class IncidentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    severity: SeverityEnum | None = None
    status: IncidentStatusEnum | None = None
    assigned_to: str | None = None
    closed_at: datetime | None = None


class IncidentResponse(IncidentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
