from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Asset(BaseModel):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(primary_key=True)

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )

    operating_system: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    owner: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    vulnerabilities = relationship(
        "Vulnerability",
        back_populates="asset",
        cascade="all, delete-orphan",
    )

    incidents = relationship(
        "Incident",
        back_populates="asset",
        cascade="all, delete-orphan",
    )

    asset_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    criticality: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    environment: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    last_seen: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
