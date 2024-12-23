from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from app.cleaning_robot.settings import config

Base = declarative_base()

engine = create_engine(
    config.get("SQLALCHEMY_URL"),
    pool_size=5,
    max_overflow=10,
)
session_context = sessionmaker(bind=engine)


def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)

    from app.cleaning_robot.path_calculation.models import (  # noqa
        PathCalculationExecution,
    )

    Base.metadata.create_all(bind=engine)
