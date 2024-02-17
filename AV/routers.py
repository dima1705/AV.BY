from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_session
import services
from dto import CarDto


router = APIRouter()

####### API НА АВТО


@router.post('/')
async def create(car_dto: CarDto = None, db_session: Session = Depends(get_session)):
    return services.create_car(car_dto, db_session)


@router.get('/{id}')
async def get(car_id: int, db_session: Session = Depends(get_session)):
    return services.get_car(car_id, db_session)


@router.put('/{id}')
async def update(car_id: int, car_dto: CarDto = None, db_session: Session = Depends(get_session)):
    return services.update_car(car_id, car_dto, db_session)


@router.delete('/{id}')
async def delete(car_id: int, db_session: Session = Depends(get_session)):
    return services.delete_car(car_id, db_session)


@router.get('/all/')
async def get_all(db_session: Session = Depends(get_session)):
    return services.get_all_cars(db_session)

########## API НА ФОТО АВТО


@router.get('/photos/{id}')
async def get(car_id: int, db_session: Session = Depends(get_session)):
    return services.get_car_photo(car_id, db_session)




######## API НА КАТЕГОРИИ


@router.get('/main_category/{id}')
async def get(main_category: int, db_session: Session = Depends(get_session)):
    return services.get_main_categoryes(main_category, db_session)


@router.get('/main_category/all/')
async def get(db_session: Session = Depends(get_session)):
    return services.get_all_main_categoryes(db_session)


@router.get('/add_category/{id}')
async def get(main_category: int, db_session: Session = Depends(get_session)):
    return services.get_add_categoryes(main_category, db_session)


@router.get('/add_category/all/')
async def get(db_session: Session = Depends(get_session)):
    return services.get_all_add_categoryes(db_session)


##### API НА БРЕНД, МОДЕЛЬ, ПОКОЛЕНИЕ


@router.get('/brand/all/')
async def get(db_session: Session = Depends(get_session)):
    return services.get_all_brands(db_session)


@router.get('/model_by_brand_id/{id}')
async def get(brand_id: int, db_session: Session = Depends(get_session)):
    return services.get_all_models_by_id_brand(brand_id, db_session)


@router.get('/models/all/')
async def get(db_session: Session = Depends(get_session)):
    return services.get_all_models(db_session)


@router.get('/gen_by_model_id/{id}')
async def get(model_id: int, db_session: Session = Depends(get_session)):
    return services.get_all_generation_by_id_model(model_id, db_session)