# Importamos enum para definir valores limitados
# y controlados para el estado del proyecto.
import enum

# Importamos datetime para los campos de fecha y hora.
from datetime import datetime

# Importamos los tipos de columnas necesarios
# para construir la tabla projects.
from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, String, Text, func

# Sintaxis moderna de SQLAlchemy 2.x.
from sqlalchemy.orm import Mapped, mapped_column

# Base común para todos nuestros modelos.
from ..database import Base


# Definimos los estados permitidos para un proyecto.
class ProjectStatus(str, enum.Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


# Modelo que representa un proyecto tecnológico
# dentro de ServiceHub.
class Project(Base):

    # Nombre de la tabla que se creará en PostgreSQL.
    __tablename__ = "projects"

    # Identificador único del proyecto.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Nombre del proyecto.
    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    # Descripción detallada del proyecto.
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Usuario responsable o propietario del proyecto.
    #
    # Se relaciona con la tabla users.
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Estado actual del proyecto.
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus),
        default=ProjectStatus.PLANNING,
        nullable=False,
    )

    # Fecha planeada de inicio.
    start_date: Mapped[datetime | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Fecha objetivo de finalización.
    target_date: Mapped[datetime | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Fecha y hora en que se creó el registro.
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