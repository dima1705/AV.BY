# from datetime import datetime
# from typing import AsyncGenerator
#
# from fastapi import Depends
# from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
# from sqlalchemy import String, Column, Boolean, Integer, TIMESTAMP, ForeignKey
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
# from sqlalchemy.orm import sessionmaker
#
# # DATABASE_URL = "postgresql://postgres:postgres@localhost/auto_s_probegom"
# Base: DeclarativeMeta = declarative_base()
#
#
# class User(SQLAlchemyBaseUserTable[int], Base):
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     registered_at = Column(TIMESTAMP, default=datetime.now)
#
#     role_id = Column(Integer, ForeignKey("roles.id"))
#
#     email: str = Column(String(length=320), unique=True, index=True, nullable=False)
#     hashed_password: str = Column(String(length=1024), nullable=False)
#     is_active: bool = Column(Boolean, default=True, nullable=False)
#     is_superuser: bool = Column(Boolean, default=False, nullable=False)
#     is_verified: bool = Column(Boolean, default=False, nullable=False)
#
#
#
#
#
# # async def create_db_and_tables():
# #     async with engine.begin() as conn:
# #         await conn.run_sync(Base.metadata.create_all)
# #
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
#
#
# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)