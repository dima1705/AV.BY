from fastapi import APIRouter
from orm.add_tg_users_orm import TgUsersORM
from dto import TgUserDTO


router = APIRouter(prefix='/tg_users', tags=['Телеграмм пользователи'])


@router.post('/add_user')
async def add_user(tg_user: TgUserDTO):
    return TgUsersORM.insert_tg_user(tg_user)


@router.get('/get_user')
async def add_user(id:int):
    return TgUsersORM.select_tg_user_id_by_id(id)