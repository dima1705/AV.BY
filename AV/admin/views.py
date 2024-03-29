from sqladmin import ModelView
from sqladmin import action
from models import User, Auto, TGUser, Brand, Model, Generation, Jobs
from starlette.requests import Request
from starlette.responses import RedirectResponse


class UserAdmin(ModelView, model=User):
    column_list = [c.name for c in User.__table__.c]
    can_delete = False
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = "fa-solid fa-user"


class AutoAdmin(ModelView, model=Auto):
    column_list = [c.name for c in Auto.__table__.c] + [Auto.auto_photo]
    name = 'Автомобиль'
    name_plural = 'Автомобили'


class TGUserAdmin(ModelView, model=TGUser):
    column_list = [c.name for c in TGUser.__table__.c]
    name = 'ТГ пользователь'
    name_plural = 'ТГ пользователи'
    icon = "fa-solid fa-user"

    @action(
        name="add_job",
        label="Добавить задание",
        confirmation_message="Вы уверены?",
        add_in_detail=True,
        add_in_list=True,
    )
    async def add_job(self, request: Request):
        pks = request.query_params.get("pks", "").split(",")
        if pks:
            for pk in pks:
                model: TGUser = await self.get_object_for_edit(pk)

            return RedirectResponse('/admin/jobs/create')


class BrandAdmin(ModelView, model=Brand):
    column_list = [c.name for c in Brand.__table__.c] + [Brand.auto_model]
    name = 'Бренд'
    name_plural = 'Бренды'


class ModelAdmin(ModelView, model=Model):
    column_list = [Model.brand_id] + [c.name for c in Model.__table__.c] + [Model.auto_generation]
    name = 'Модель'
    name_plural = 'Модели'


class GenerationAdmin(ModelView, model=Generation):
    column_list = [c.name for c in Generation.__table__.c] + [Generation.auto_model]
    name = 'Поколение'
    name_plural = 'Поколения'


class JobsAdmin(ModelView, model=Jobs):
    column_list = [c.name for c in Jobs.__table__.c]
    name = 'Задание'
    name_plural = 'Задания'
