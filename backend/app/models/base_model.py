from app.database.base import Base
from app.models.mixins.timestamp import TimestampMixin


class BaseModel(Base, TimestampMixin):
    __abstract__ = True
