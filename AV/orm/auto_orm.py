from sqlalchemy import insert, select
from models import Auto
from db import session_factory, sync_engin, async_engin


class AutoORM:

    @staticmethod
    def insert_auto_av(auto):
        with session_factory() as session:
            insert_auto = insert(Auto).values(dict(auto))
            session.execute(insert_auto)
            session.commit()
            print(auto)

    @staticmethod
    def select_auto():
        with session_factory() as session:
            select_auto = (
                select(Auto)
                .order_by(Auto.id.desc())
            )
            res = session.execute(select_auto)
            result_orm = res.scalars().all()
            return result_orm

    @staticmethod
    def select_car_by_id(id):
        with session_factory() as session:
            select_auto_by_id = (
                select(Auto)
                .filter(
                    Auto.id == id
                )
            )
            res = session.execute(select_auto_by_id)
            result_select_auto_by_id = res.scalars().all()
            return result_select_auto_by_id