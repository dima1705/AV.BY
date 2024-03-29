from sqlalchemy import insert, select
from db import session_factory
from models import User
from fastapi import status


class UsersORM:

    @staticmethod
    def create_users(user):
        with session_factory() as session:
            insert_auto = insert(User).values(dict(user))
            session.execute(insert_auto)
            session.commit()
            print(user)

    @staticmethod
    def get_auth(user):
        with session_factory() as session:
            query = (select(User.email, User.password))
            res_query = session.execute(query)
            query_d = dict(res_query.all())

            try:
                if query_d[f'{user.email}'] == user.password:
                    query_user = (select(User.id, User.email))
                    res_query_user = session.execute(query_user)
                    res = dict(res_query_user.all())
                    for k, v in res.items():
                        if v == user.email:
                            return status.HTTP_200_OK, f"User_id: {k}", f"email: {v}"
                else:
                    return status.HTTP_422_UNPROCESSABLE_ENTITY
            except:
                return status.HTTP_422_UNPROCESSABLE_ENTITY
            # print(user.email)
