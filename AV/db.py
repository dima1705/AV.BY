from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    API_TOKEN: str

    @property
    def DB_URL_psycopg(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def DB_URL_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file=f".env")


settings = Settings()


sync_engin = create_engine(
    url=settings.DB_URL_psycopg,
    echo=True,
    max_overflow=10
)

async_engin = create_async_engine(
    url=settings.DB_URL_asyncpg,
    echo=True
)

session_factory = sessionmaker(sync_engin)
async_session_factory = async_sessionmaker(async_engin,  expire_on_commit=False)


def get_session():
    db = async_session_factory()
    try:
        yield db
    finally:
        db.close()