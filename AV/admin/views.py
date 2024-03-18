from sqladmin import ModelView

from models import User, Auto, TGUser, Brand, Model, Generation


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email]
    column_details_exclude_list = [User.hashed_password]
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

