from typing import AsyncGenerator
from fastapi import Depends
from db import async_session_factory
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)