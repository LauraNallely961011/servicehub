# Importamos enum para definir valores controlados
# para el estado y la prioridad de una tarea.
import enum

# Importamos datetime para campos de fecha y hora.
from datetime import datetime

# Importamos los tipos de columnas necesarios
# para construir la tabla tasks.
from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, String, Text, func

# Sintaxis moderna de SQLAlchemy 2.x.
from sqlalchemy.orm import Mapped, mapped_column

# Base común para todos los modelos del proyecto.
from ..database import Base


# Estados permitidos para una tarea.
class TaskStatus(str, enum.Enum):
    TODO = "to_do"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    DONE = "done"


# Prioridades permitidas para una tarea.
class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# Modelo que representa una tarea dentro de un proyecto.
class Task(Base):

    # Nombre de la tabla en PostgreSQL.
    __tablename__ = "tasks"

    # Identificador único de la tarea.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Proyecto al que pertenece la tarea.
    # Se relaciona con projects.id.
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
        index=True,
    )

    # Usuario responsable de la tarea.
    # Puede ser NULL si la tarea aún no ha sido asignada.
    assigned_to_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    # Título corto de la tarea.
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    # Descripción detallada de la tarea.
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Estado actual de la tarea.
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus),
        default=TaskStatus.TODO,
        nullable=False,
    )

    # Prioridad de la tarea.
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority),
        default=TaskPriority.MEDIUM,
        nullable=False,
    )

    # Fecha límite de la tarea.
    due_date: Mapped[datetime | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Fecha y hora en que se creó la tarea.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Fecha y hora de la última actualización.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )