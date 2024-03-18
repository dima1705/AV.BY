from fastapi import APIRouter
from orm.bmg_orm import BmgORM

router = APIRouter(prefix='/bmg', tags=['Бренды/Модели/Поколения'])


@router.get('/get_bmg')
async def get_brands():
    return BmgORM.get_brand_model_gen()


# @router.get('/model/{id}')
# async def get_model_id(brand_id: int):
#     return ORM.select_model_auto_by_brand_id(brand_id)
#
#
# @router.get('/generation/{id}')
# async def get_generations(model_id: int):
#     return ORM.select_generations_auto_by_model_id(model_id)