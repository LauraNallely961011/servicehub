# Standard library module used to read environment variables.
import os

# Loads variables from a local .env file when one is available.
from dotenv import load_dotenv

# SQLAlchemy function used to create the database engine.
from sqlalchemy import create_engine

# SQLAlchemy ORM utilities used to create database sessions
# and the common base class for all database models.
from sqlalchemy.orm import declarative_base, sessionmaker


# Load environment variables from a .env file.
# This allows local configuration without hardcoding production secrets.
load_dotenv()


# Read the database connection URL from the environment.
#
# The fallback value is intended only for the local development
# PostgreSQL container used by ServiceHub.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://servicehub:servicehub@localhost:5432/servicehub",
)


# Create the SQLAlchemy engine.
# The engine manages connections between the application and PostgreSQL.
engine = create_engine(DATABASE_URL)


# Create a reusable database session factory.
#
# autocommit=False:
# Transactions are committed explicitly.
#
# autoflush=False:
# SQLAlchemy will not automatically send pending changes
# to the database before every query.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Base class inherited by all SQLAlchemy ORM models.
# SQLAlchemy uses its metadata to discover database tables.
Base = declarative_base()


def get_db():
    """
    Provide a database session to application components.

    A new session is created for each request or operation
    and always closed when the operation finishes.
    """

    # Create a new database session.
    db = SessionLocal()

    try:
        # Yield the session so FastAPI dependencies can use it.
        yield db
    finally:
        # Always release the database connection.
        db.close()