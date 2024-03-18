from sqlalchemy import insert, select
from db import session_factory
from models import Auto, AutoPhoto


class PhotoORM:

    @staticmethod
    def insert_photo(photo):
        with session_factory() as session:
            query_auto = (
                select(Auto.id)
                .order_by(Auto.id.desc())
            )
            res_auto = session.execute(query_auto)
            auto_id = res_auto.scalar()
            photos = [
                {"m_photo": f"{photo}", "auto_id": f"{auto_id}"}
            ]
            insert_photo = insert(AutoPhoto).values(photos)
            session.execute(insert_photo)
            session.commit()

    @staticmethod
    def select_car_photos(id):
        with session_factory() as session:
            select_car_photos = (
                select(AutoPhoto.m_photo)
                .filter(
                    AutoPhoto.auto_id == id
                )
            )
            res = session.execute(select_car_photos)
            result_select_car_photos = res.unique().scalars().all()
            return result_select_car_photos