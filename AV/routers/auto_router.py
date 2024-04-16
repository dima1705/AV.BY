from fastapi import APIRouter
from dto import AutoDTO, FilteredAutoDTO
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


# @router.post('/filtered_car')
# async def advert_car(auto: FilteredAutoDTO):
#     return AutoORM.select_filtered_car(auto)


@router.get('/engine_type')
async def get_auto_engine_type():
    return AutoORM.select_engine_type()