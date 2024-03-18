from fastapi import APIRouter
from orm.users_orm import UsersORM
from dto import UserDTO

router = APIRouter(prefix='/users', tags=['Пользователи'])


@router.get('/users')
async def get_users():
    return UsersORM.select_users()


@router.post('/user_create')
async def get_users(user: UserDTO):
    return UsersORM.create_users(user)