# datetime is used for typed timestamp fields.
from datetime import datetime

# SQLAlchemy column types, foreign keys, and database functions.
from sqlalchemy import DateTime, ForeignKey, Integer, Text, func

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base used by all ServiceHub models.
from ..database import Base


# Represents a comment added to an incident.
class Comment(Base):

    # PostgreSQL table name.
    __tablename__ = "comments"

    # Unique identifier for the comment.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Incident associated with this comment.
    incident_id: Mapped[int] = mapped_column(
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # User who wrote the comment.
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Comment body.
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Timestamp automatically created when the comment is stored.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Timestamp updated if the comment changes.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )