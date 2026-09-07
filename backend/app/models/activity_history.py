# datetime is used for typed timestamp fields.
from datetime import datetime

# SQLAlchemy column types, foreign keys, and database functions.
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base used by all ServiceHub models.
from ..database import Base


# Stores an audit trail of important incident activity.
class ActivityHistory(Base):

    # PostgreSQL table name.
    __tablename__ = "activity_history"

    # Unique identifier for each activity record.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Incident affected by the activity.
    incident_id: Mapped[int] = mapped_column(
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # User who triggered the activity.
    #
    # Nullable because some future events may be generated
    # automatically by the system.
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    # Machine-readable event type.
    #
    # Examples:
    # status_changed
    # technician_assigned
    # priority_changed
    # comment_added
    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # Database or business field affected by the change.
    field_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # Value before the change.
    old_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Value after the change.
    new_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Optional human-readable explanation of the activity.
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Timestamp automatically created when the event is recorded.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )