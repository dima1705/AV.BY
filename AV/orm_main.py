from sqlalchemy import insert, select

from db import session_factory
from models import Auto, Brand, Model, Generation, AutoPhoto


class ORM:

    # @staticmethod
    # def create_tables():
    #     Base.metadata.drop_all(async_engin)
    #     sync_engin.echo = True
    #     Base.metadata.create_all(async_engin)
    #     sync_engin.echo = True

    @staticmethod
    def insert_brand_model_gen(brand, model, generation):
        with session_factory() as session:

            query_brand = select(Brand.id, Brand.brand)
            res_brand = session.execute(query_brand)
            result_brand = dict(res_brand.all())
            if brand not in result_brand.values():
                auto_brand = [
                    {"brand": f'{brand}'}
                ]
                insert_brand = insert(Brand).values(auto_brand)
                session.execute(insert_brand)
                session.commit()

            query_brand = select(Brand.id, Brand.brand)
            res_brand = session.execute(query_brand)
            result_brand = dict(res_brand.all())

            query_model = (select(Model.model, Model.brand_id))
            res_model = session.execute(query_model)
            result_model = dict(res_model.all())

            brand_id = [key for key, value in result_brand.items() if value == brand][0]
            if model not in result_model.keys() or (
                    model in result_model.keys() and result_model[model] != brand_id
            ):
                models = [
                    {"model": f"{model}", "brand_id": f"{brand_id}"}
                ]
                insert_model = insert(Model).values(models)
                session.execute(insert_model)
                session.commit()

            query_model_id = (select(Model.id, Model.model))
            res_model_model_id = session.execute(query_model_id)
            result_model_id = dict(res_model_model_id.all())

            query_generation = (select(Generation.generation, Generation.model_id))
            res_generation = session.execute(query_generation)
            result_generation = dict(res_generation.all())

            model_id = [key for key, value in result_model_id.items() if value == model][0]
            if generation not in result_generation.keys() or (
                    generation in result_generation.keys() and result_generation[generation] != model_id
            ):
                generations = [
                    {"generation": f"{generation}", "model_id": f"{model_id}"}
                ]
                insert_generation = insert(Generation).values(generations)
                session.execute(insert_generation)
                session.commit()

    @staticmethod
    def insert_auto_parser(*auto_params):
        with session_factory() as session:
            auto = [
                {
                    "brand": f"{auto_params[0]}",
                    "model": f"{auto_params[1]}",
                    "generation_with_years": f"{auto_params[2]}",
                    "year": f"{auto_params[3]}",
                    "engine_capacity": f"{auto_params[4]}",
                    "engine_type": f"{auto_params[5]}",
                    "transmission_type": f"{auto_params[6]}",
                    "body_type": f"{auto_params[7]}",
                    "drive_type": f"{auto_params[8]}",
                    "color": f"{auto_params[9]}",
                    "mileage_km": f"{auto_params[10]}",
                    "power": f"{auto_params[11]}",
                    "fuel_consumption": f"{auto_params[12]}",
                    "price_amount_usd": f"{auto_params[13]}",
                    "price_amount_byn": f"{auto_params[14]}",
                    "description": f"{auto_params[15]}",
                    "main_photo": f"{auto_params[16]}",
                    "location": f"{auto_params[17]}",
                }
            ]
            insert_auto = insert(Auto).values(auto)
            session.execute(insert_auto)
            session.commit()
            print(auto)

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