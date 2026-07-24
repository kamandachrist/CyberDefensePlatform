from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import IncidentStatusEnum, SeverityEnum


class Incident(BaseModel):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    severity: Mapped[SeverityEnum] = mapped_column(
        Enum(SeverityEnum),
        nullable=False,
    )

    status: Mapped[IncidentStatusEnum] = mapped_column(
        Enum(IncidentStatusEnum),
        nullable=False,
        default=IncidentStatusEnum.OPEN,
    )

    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False,
    )

    threat_id: Mapped[int] = mapped_column(
        ForeignKey("threats.id"),
        nullable=False,
    )

    assigned_to: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    opened_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    asset = relationship(
        "Asset",
        back_populates="incidents",
    )

    threat = relationship(
        "Threat",
        back_populates="incidents",
    )
