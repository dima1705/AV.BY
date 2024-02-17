from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


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

    category = relationship('AddCategory', backref='Used_auto')


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




