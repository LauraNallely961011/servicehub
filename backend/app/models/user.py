# Enum is used to define a controlled set of user roles.
import enum

# SQLAlchemy column types and database functions.
from sqlalchemy import Boolean, DateTime, Enum, Integer, String, func

# SQLAlchemy 2.x typed ORM mapping utilities.
from sqlalchemy.orm import Mapped, mapped_column

# Shared declarative base used by all ServiceHub database models.
from ..database import Base


# Roles supported by ServiceHub.
#
# Using an enum prevents arbitrary role values from being stored.
class UserRole(str, enum.Enum):
    ADMIN = "admin"
    IT_MANAGER = "it_manager"
    TECHNICIAN = "technician"
    USER = "user"


# Represents a ServiceHub user stored in the "users" table.
class User(Base):

    # PostgreSQL table name.
    __tablename__ = "users"

    # Unique numeric identifier for each user.
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # User's display or full name.
    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    # User's email address.
    #
    # unique=True prevents two users from sharing the same email.
    # index=True improves lookup performance.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    # Stores only a secure password hash.
    #
    # Plain-text passwords must never be stored in the database.
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Defines the user's authorization role.
    #
    # New users receive the USER role by default.
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.USER,
        nullable=False,
    )

    # Controls whether the account is allowed to use the system.
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # Timestamp automatically generated when the user is created.
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Timestamp representing the latest update to the record.
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )