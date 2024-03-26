import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

sync_engin = create_engine(
    url=f'postgresql+psycopg://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}',
    echo=True,
    max_overflow=10
)

session_factory = sessionmaker(sync_engin)


def get_session():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()