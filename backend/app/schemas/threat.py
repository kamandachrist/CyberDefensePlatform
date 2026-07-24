from pydantic import BaseModel, ConfigDict

from app.models.enums import SeverityEnum


class ThreatBase(BaseModel):
    name: str
    severity: SeverityEnum
    category: str
    source: str
    description: str
    ioc: str


class ThreatCreate(ThreatBase):
    pass


class ThreatUpdate(BaseModel):
    name: str | None = None
    severity: SeverityEnum | None = None
    category: str | None = None
    source: str | None = None
    description: str | None = None
    ioc: str | None = None


class ThreatResponse(ThreatBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
