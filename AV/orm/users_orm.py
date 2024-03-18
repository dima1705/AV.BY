from sqlalchemy import insert, select
from db import session_factory
from models import User


class UsersORM:

    @staticmethod
    def select_users():
        with session_factory() as session:
            select_users = (
                select(User.email)
            )
            res = session.execute(select_users)
            result_select_users = res.unique().scalars().all()
            return result_select_users

    @staticmethod
    def create_users():
        with session_factory() as session:
            pass