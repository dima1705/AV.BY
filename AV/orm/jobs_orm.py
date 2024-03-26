from models import Jobs
from sqlalchemy import insert, select
from db import session_factory


class JobORM:

    @staticmethod
    def job():
        with session_factory() as session:
            query = (select(Jobs))
            res = session.execute(query)
            result = res.scalars().all()
            print(result)

