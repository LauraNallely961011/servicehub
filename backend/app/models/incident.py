# Enum is used to define controlled values for incident fields.
import enum

# datetime is used for typed timestamp columns.
from datetime import datetime

# SQLAlchemy column types, foreign keys, and database functions.
from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base for all ServiceHub models.
from ..database import Base


# Workflow states supported by an incident.
class IncidentStatus(str, enum.Enum):
    OPEN = "open"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    RESOLVED = "resolved"
    CLOSED = "closed"


# Priority levels used to determine incident urgency.
class IncidentPriority(str, enum.Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


# Categories used to classify IT incidents.
class IncidentCategory(str, enum.Enum):
    HARDWARE = "hardware"
    SOFTWARE = "software"
    NETWORK = "network"
    ACCESS_PERMISSIONS = "access_permissions"
    APPLICATION = "application"
    SECURITY = "security"
    OTHER = "other"


# Represents an IT incident stored in the "incidents" table.
class Incident(Base):

    # PostgreSQL table name.
    __tablename__ = "incidents"

    # Unique numeric identifier for the incident.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Short title describing the issue.
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    # Detailed explanation of the incident.
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Functional category assigned to the incident.
    category: Mapped[IncidentCategory] = mapped_column(
        Enum(IncidentCategory),
        nullable=False,
    )

    # Operational priority of the incident.
    priority: Mapped[IncidentPriority] = mapped_column(
        Enum(IncidentPriority),
        default=IncidentPriority.MEDIUM,
        nullable=False,
    )

    # Current workflow state.
    status: Mapped[IncidentStatus] = mapped_column(
        Enum(IncidentStatus),
        default=IncidentStatus.OPEN,
        nullable=False,
    )

    # User who originally created the incident.
    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Technician currently responsible for the incident.
    #
    # The value can be NULL while the incident is unassigned.
    assigned_to_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    # Timestamp automatically created by PostgreSQL.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Timestamp updated when the incident changes.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )