from fastapi import APIRouter
from orm.users_orm import UsersORM
from dto import UserDTO, UserAuthDTO


router = APIRouter(prefix='/users', tags=['Пользователи'])


@router.post('/user_register')
async def get_users(user: UserDTO):
    return UsersORM.create_users(user)


@router.post('/user_auth')
async def get_users_auth(user: UserAuthDTO):
    return UsersORM.get_auth(user)