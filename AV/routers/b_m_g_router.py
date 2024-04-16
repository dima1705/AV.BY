from fastapi import APIRouter
from orm.bmg_orm import BmgORM

router = APIRouter(prefix='/bmg', tags=['Бренды/Модели/Поколения'])


@router.get('/get_bmg')
async def get_brands():
    return BmgORM.get_brand_model_gen()
