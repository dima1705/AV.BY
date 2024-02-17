from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import psycopg2


# строка подключения

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/auto_s_probegom"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# создаем базовый класс для моделей
Base = declarative_base()

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_session():
    db = session()
    try:
        yield db
    finally:
        db.close()