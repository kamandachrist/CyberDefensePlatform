from sqlalchemy import Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import IncidentStatusEnum, SeverityEnum


class Alert(BaseModel):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

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

    threat_id: Mapped[int | None] = mapped_column(
        ForeignKey("threats.id"),
        nullable=True,
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    assigned_to: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    asset = relationship(
        "Asset",
        back_populates="alerts",
    )

    threat = relationship(
        "Threat",
        back_populates="alerts",
    )
