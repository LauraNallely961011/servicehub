# Importamos datetime para trabajar con fechas y horas.
from datetime import datetime

# Importamos los tipos de columnas y funciones
# que utilizaremos en este modelo.
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func

# Mapped y mapped_column forman parte de la sintaxis
# moderna de SQLAlchemy 2.x para declarar columnas.
from sqlalchemy.orm import Mapped, mapped_column

# Importamos la clase Base que comparten todos
# nuestros modelos de base de datos.
from ..database import Base


# Este modelo almacenará el historial de cambios
# realizados sobre cada incidente.
class ActivityHistory(Base):

    # Nombre real de la tabla en PostgreSQL.
    __tablename__ = "activity_history"

    # Identificador único del registro de actividad.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Incidente al que pertenece este cambio.
    # Se relaciona con la tabla incidents.
    incident_id: Mapped[int] = mapped_column(
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # Usuario responsable de realizar el cambio.
    #
    # Se permite NULL porque en el futuro algunos eventos
    # podrían ser generados automáticamente por el sistema.
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    # Tipo de acción realizada.
    #
    # Ejemplos:
    # "incident_created"
    # "status_changed"
    # "technician_assigned"
    # "priority_changed"
    # "comment_added"
    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # Nombre del campo que cambió.
    #
    # Por ejemplo:
    # "status"
    # "priority"
    # "assigned_to_id"
    #
    # Puede ser NULL porque algunos eventos no necesariamente
    # representan el cambio directo de un campo.
    field_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # Valor anterior antes del cambio.
    #
    # Lo almacenamos como texto porque puede representar
    # diferentes tipos de valores.
    old_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Nuevo valor después del cambio.
    new_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Descripción adicional del evento.
    #
    # Ejemplo:
    # "Incident assigned to technician John Doe"
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Fecha y hora en la que ocurrió el evento.
    # PostgreSQL la asignará automáticamente.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )