from fastapi.encoders import jsonable_encoder
from sqlalchemy import insert, select
from models import Auto
from db import session_factory
from .photos_orm import PhotoORM


class AutoORM:

    @staticmethod
    def insert_auto_av(auto):
        with session_factory() as session:
            insert_auto = insert(Auto).values(dict(auto))
            session.execute(insert_auto)
            session.commit()
            PhotoORM.insert_photo(auto.main_photo)
            return f"Авто успешно добавлено"

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

    @staticmethod
    def select_filtered_car(auto):
        with session_factory() as session:
            query = (
                select(Auto)
                .filter(
                    Auto.brand == auto.brand,
                    Auto.model == auto.model,
                    Auto.generation_with_years == auto.generation

                )
            )
            res = session.execute(query)
            result = res.unique().scalars().all()
            result = jsonable_encoder(result)
            return result

    @staticmethod
    def select_engine_type():
        with session_factory() as session:
            query = (
                select(Auto.engine_type)
            )
            res = session.execute(query)
            result = res.all()
            return result