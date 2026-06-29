from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from ..database import Base


class FormPermission(Base):

    __tablename__ = "form_permissions"

    id = Column(
        Integer,
        primary_key=True
    )

    form_key = Column(
        String(100),
        nullable=False
    )

    company = Column(
        String(200),
        nullable=False
    )

    is_enabled = Column(
        Boolean,
        default=True,
        nullable=False
    )