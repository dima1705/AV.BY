from fastapi import APIRouter
from dto import AutoDTO
from orm.auto_orm import AutoORM

router = APIRouter(prefix='/auto', tags=['Авто'])


@router.get('/all')
async def get_all():
    return AutoORM.select_auto()


@router.get('/{id}')
async def get_car_by_id(id: int):
    return AutoORM.select_car_by_id(id)


@router.post('/create_auto')
async def advert_car(auto: AutoDTO):
    return AutoORM.insert_auto_av(auto)