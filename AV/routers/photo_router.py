from fastapi import APIRouter
from orm.photos_orm import PhotoORM

router = APIRouter(prefix='/photos', tags=['Фото авто'])


@router.get('/{id}')
async def get_car_photo(id: int):
    return PhotoORM.select_car_photos(id)


@router.post('/add_photo')
async def get_car_photo(photo: str):
    pass