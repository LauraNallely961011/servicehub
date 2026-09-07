# Enum is used to define controlled project status values.
import enum

# date is used for calendar dates.
# datetime is used for timestamp fields.
from datetime import date, datetime

# SQLAlchemy column types, foreign keys, and database functions.
from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, String, Text, func

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base used by all ServiceHub models.
from ..database import Base


# Lifecycle states supported by a ServiceHub project.
class ProjectStatus(str, enum.Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


# Represents a technology project managed within ServiceHub.
class Project(Base):

    # PostgreSQL table name.
    __tablename__ = "projects"

    # Unique identifier for the project.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Project name.
    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    # Optional detailed project description.
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # User responsible for the project.
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Current project lifecycle state.
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus),
        default=ProjectStatus.PLANNING,
        nullable=False,
    )

    # Planned project start date.
    start_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Expected project completion date.
    target_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Timestamp automatically generated when the project is created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Timestamp representing the latest project update.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )