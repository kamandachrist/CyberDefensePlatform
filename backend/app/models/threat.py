from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class Threat(BaseModel):
    __tablename__ = "threats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    severity: Mapped[str] = mapped_column(String(50), nullable=False)

    category: Mapped[str] = mapped_column(String(100), nullable=False)

    source: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str] = mapped_column(Text, nullable=False)

    ioc: Mapped[str] = mapped_column(Text, nullable=False)
