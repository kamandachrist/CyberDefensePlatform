from sqlalchemy import Enum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel
from app.models.enums import SeverityEnum


class Threat(BaseModel):
    __tablename__ = "threats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    severity: Mapped[SeverityEnum] = mapped_column(
        Enum(SeverityEnum),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(String(100), nullable=False)

    source: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str] = mapped_column(Text, nullable=False)

    ioc: Mapped[str] = mapped_column(Text, nullable=False)

    incidents = relationship(
        "Incident",
        back_populates="threat",
        cascade="all, delete-orphan",
    )

    alerts = relationship(
        "Alert",
        back_populates="threat",
   )
