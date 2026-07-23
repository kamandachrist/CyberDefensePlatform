from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Asset(Base):
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