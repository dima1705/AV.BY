from datetime import datetime
import time

from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData, TIMESTAMP, JSON, Boolean
from db import Base
from sqlalchemy.orm import relationship

metadata = MetaData()


class MainCategory(Base):
    __tablename__ = "MainCategory"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)

    # cat_parent = relationship('AddCategory', backref='MainCategory')


class AddCategory(Base):
    __tablename__ = "AddCategory"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    maincategory_id = Column(Integer, ForeignKey("MainCategory.id"))

    cat_child = relationship('MainCategory', backref='AddCategory')


class UsedAuto(Base):
    __tablename__ = "Used_auto"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price_for_bel_rub = Column(String)
    price_for_usd = Column(String)
    year = Column(String)
    kpp = Column(String)
    volume = Column(String)
    type_engine = Column(String)
    probeg = Column(String)
    kyzov = Column(String)
    privod = Column(String)
    color = Column(String)
    power = Column(String)
    comment = Column(String)
    addcat_id = Column(Integer, ForeignKey('AddCategory.id'))
    # user_id = Column(Integer, ForeignKey('User.id'))

    category = relationship('AddCategory', backref='Used_auto')
    # user = relationship('Users', backref='Used_auto')


class AutoPhoto(Base):
    __tablename__ = "auto_photo"

    id = Column(Integer, primary_key=True, index=True)
    s_photo = Column(String)
    m_photo = Column(String)
    b_photo = Column(String)
    auto_id = Column(Integer, ForeignKey("Used_auto.id"))

    photo_child = relationship('UsedAuto', backref='auto_photo')


class AutoBrand(Base):
    __tablename__ = "auto_brand"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)


class AutoModel(Base):
    __tablename__ = "auto_model"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    brand_id = Column(Integer, ForeignKey("auto_brand.id"))

    model_child = relationship('AutoBrand', backref='auto_model')


class AutoGen(Base):
    __tablename__ = "auto_gen"

    id = Column(Integer, primary_key=True, index=True)
    generation = Column(String)
    model_id = Column(Integer, ForeignKey("auto_model.id"))

    gen_child = relationship('AutoModel', backref='auto_gen')


class Roles(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    emai = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.now)

    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    role_id = Column(Integer, ForeignKey("role.id"))

    users = relationship('Roles', backref='users')



