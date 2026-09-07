# Enum is used to define controlled task status and priority values.
import enum

# date is used for deadlines.
# datetime is used for timestamp fields.
from datetime import date, datetime

# SQLAlchemy column types, foreign keys, and database functions.
from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, String, Text, func

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base used by all ServiceHub models.
from ..database import Base


# Workflow states supported by project tasks.
class TaskStatus(str, enum.Enum):
    TODO = "to_do"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    DONE = "done"


# Priority levels available for project tasks.
class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# Represents a task that belongs to a ServiceHub project.
class Task(Base):

    # PostgreSQL table name.
    __tablename__ = "tasks"

    # Unique task identifier.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Project that contains the task.
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
        index=True,
    )

    # User currently responsible for the task.
    #
    # Nullable because tasks can exist before assignment.
    assigned_to_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    # Short task title.
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    # Optional detailed task description.
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Current task workflow state.
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus),
        default=TaskStatus.TODO,
        nullable=False,
    )

    # Business priority assigned to the task.
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority),
        default=TaskPriority.MEDIUM,
        nullable=False,
    )

    # Optional task deadline.
    due_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Timestamp automatically generated when the task is created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Timestamp representing the latest task update.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )