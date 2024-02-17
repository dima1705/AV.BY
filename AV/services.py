from models import UsedAuto, MainCategory, AddCategory, AutoBrand, AutoModel, AutoGen, AutoPhoto
from sqlalchemy.orm import Session
from dto import CarDto


#################  АВТО
def create_car(car_dto: CarDto, db_session: Session):
    car = UsedAuto(
        brand=car_dto.brand,
        mark=car_dto.mark,
        year=car_dto.year,
    )
    try:
        db_session.add(car)
        db_session.commit()
        db_session.refresh(car)
    except Exception as e:
        print(e)
    return car


def get_car(id: int, db_session: Session):
    return db_session.query(UsedAuto).filter(UsedAuto.id == id).first()


def get_all_cars(db_session: Session):
    return db_session.query(UsedAuto).all()


def update_car(id: int, car_dto: CarDto, db_session: Session):
    car = db_session.query(UsedAuto).filter(UsedAuto.id == id).first()
    car.brand = car_dto.brand
    car.mark = car_dto.mark
    car.year = car_dto.year
    try:
        db_session.add(car)
        db_session.commit()
        db_session.refresh(car)
    except Exception as e:
        print(e)

    return car


def delete_car(id: int, db_session: Session):
    db_session.query(UsedAuto).filter(UsedAuto.id == id).delete()
    db_session.commit()
    return


def get_car_photo(id: int, db_session: Session):
    return db_session.query(AutoPhoto).filter(AutoPhoto.auto_id == id).all()



################ КАТЕГОРИИ

def get_main_categoryes(id:int, db_session: Session):
    return db_session.query(MainCategory).filter(MainCategory.id == id).first()


def get_all_main_categoryes(db_session: Session):
    return db_session.query(MainCategory).all()


def get_add_categoryes(id:int, db_session: Session):
    return db_session.query(AddCategory).filter(AddCategory.id == id).first()


def get_all_add_categoryes(db_session: Session):
    return db_session.query(AddCategory).all()


################### БРЕНД, МОДЕЛЬ, ПОКОЛЕНИЕ


def get_all_brands(db_session: Session):
    return db_session.query(AutoBrand).all()


def get_all_models_by_id_brand(id: int, db_session: Session):
    return db_session.query(AutoModel).filter(AutoModel.brand_id == id).all()


def get_all_models(db_session: Session):
    return db_session.query(AutoModel).all()


def get_all_generation_by_id_model(id: int, db_session: Session):
    return db_session.query(AutoGen).filter(AutoGen.model_id == id).all()