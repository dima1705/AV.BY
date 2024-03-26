from fastapi.encoders import jsonable_encoder
from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload

from AV.models import TGUser, Jobs
from AV.AV_BOT.database import session_factory


class TgORM:
    @staticmethod
    def insert_tg_user(tg_user):
        with session_factory() as session:
            query_user = (select(TGUser.id_user))
            res_user = session.execute(query_user)
            result_user = res_user.unique().scalars().all()

            if tg_user.id_user not in result_user:
                insert_tg_user = insert(TGUser).values(dict(tg_user))
                session.execute(insert_tg_user)
                session.commit()

    @staticmethod
    def select_tg_user_id():
        with session_factory() as session:
            query = (
                select(TGUser.id_user)
            )
            res = session.execute(query)
            result_orm = res.unique().scalars().all()
            result = jsonable_encoder(result_orm)
            return result

    @staticmethod
    def select_tg_user_id_by_id(id_user):
        with session_factory() as session:
            query = (
                select(TGUser.id_user)
                .filter(TGUser.id == id_user)
            )
            res = session.execute(query)
            result_orm = res.unique().scalars().all()
            result = jsonable_encoder(result_orm)
            return result

    @staticmethod
    def job():
        with session_factory() as session:
            query = (
                select(Jobs)
            )
            res = session.execute(query)
            result_orm = res.unique().scalars().all()
            result = jsonable_encoder(result_orm)
            return result