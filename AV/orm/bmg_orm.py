from fastapi.encoders import jsonable_encoder
from models import Brand, Model, Generation
from sqlalchemy import insert, select
from db import session_factory
from sqlalchemy.orm import selectinload


class BmgORM:

    @staticmethod
    def get_brand_model_gen():
        with session_factory() as session:
            query = (
                select(Brand, Model)
                .options(selectinload(Brand.auto_model))
                .options(selectinload(Model.auto_generation))
            )
            res = session.execute(query)
            result = res.unique().scalars().all()
            result = jsonable_encoder(result)
            return result
