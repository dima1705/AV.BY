from fastapi.encoders import jsonable_encoder
from models import Brand, Model, Generation
from sqlalchemy import insert, select
from db import session_factory
from sqlalchemy.orm import selectinload


class BmgORM:

    # @staticmethod
    # def select_brand_auto():
    #     with session_factory() as session:
    #         select_brand_auto = (
    #             select(Brand.brand)
    #             .order_by(Brand.brand)
    #         )
    #         res = session.execute(select_brand_auto)
    #         result_select_brand_auto = res.scalars().all()
    #         return result_select_brand_auto
    #
    # @staticmethod
    # def select_model_auto_by_brand_id(brand_id):
    #     with session_factory() as session:
    #         select_model_auto = (
    #             select(Model.model)
    #             .filter(
    #                 Model.brand_id == brand_id
    #             )
    #         )
    #         res = session.execute(select_model_auto)
    #         result_select_model_auto_by_brand_id = res.unique().scalars().all()
    #         print(result_select_model_auto_by_brand_id)
    #         return result_select_model_auto_by_brand_id
    #
    # @staticmethod
    # def select_generations_auto_by_model_id(model_id):
    #     with session_factory() as session:
    #         select_generation_auto = (
    #             select(Generation.generation)
    #             .filter(
    #                 Generation.model_id == model_id
    #             )
    #         )
    #         res = session.execute(select_generation_auto)
    #         result_select_generation_auto_by_brand_id = res.unique().scalars().all()
    #         return result_select_generation_auto_by_brand_id

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
