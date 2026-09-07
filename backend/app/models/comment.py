# Importamos datetime para indicar el tipo de dato
# de los campos de fecha y hora.
from datetime import datetime

# Importamos los tipos de columnas y funciones
# que vamos a utilizar desde SQLAlchemy.
from sqlalchemy import DateTime, ForeignKey, Integer, Text, func

# Mapped y mapped_column se utilizan para definir
# las columnas de nuestros modelos con SQLAlchemy 2.x.
from sqlalchemy.orm import Mapped, mapped_column

# Importamos Base, que es la clase base de todos
# nuestros modelos de base de datos.
from ..database import Base


# Definimos el modelo Comment.
# Cada instancia de esta clase representará
# un comentario almacenado en la tabla "comments".
class Comment(Base):

    # Nombre real que tendrá la tabla en PostgreSQL.
    __tablename__ = "comments"

    # Identificador único del comentario.
    # primary_key=True lo convierte en la llave primaria.
    # index=True crea un índice para búsquedas más rápidas.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ID del incidente al cual pertenece el comentario.
    # ForeignKey crea una relación con incidents.id.
    incident_id: Mapped[int] = mapped_column(
        ForeignKey("incidents.id"),
        nullable=False,
        index=True,
    )

    # ID del usuario que escribió el comentario.
    # Está relacionado con users.id.
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    # Texto del comentario.
    # Usamos Text porque puede contener contenido más largo
    # que un String tradicional.
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Fecha y hora en que se creó el comentario.
    # PostgreSQL asignará automáticamente la fecha actual
    # utilizando now().
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Fecha y hora de la última modificación.
    # Se crea inicialmente con now() y SQLAlchemy
    # actualizará el valor cuando el registro sea modificado.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )