from datetime import datetime
from typing import Annotated, Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, MetaData, Boolean, text
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped

metadata_obj = MetaData()
str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    metadata = metadata_obj


intpk = Annotated[int, mapped_column(primary_key=True)]

registered_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc',now())")
)]


class Auto(Base):

    __tablename__ = "auto"

    id: Mapped[intpk]
    brand: Mapped[str]
    model: Mapped[str]
    generation_with_years: Mapped[str]
    year: Mapped[int]
    engine_capacity: Mapped[float]
    engine_type: Mapped[str]
    transmission_type: Mapped[str]
    body_type: Mapped[str]
    drive_type: Mapped[str]
    color: Mapped[str]
    mileage_km: Mapped[int]
    power: Mapped[Optional[int]]
    fuel_consumption: Mapped[Optional[float]]
    price_amount_usd: Mapped[int]
    price_amount_byn: Mapped[int]
    description: Mapped[str]
    main_photo: Mapped[str]
    location: Mapped[str]
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(
        back_populates="auto"
    )

    auto_photo: Mapped[list["AutoPhoto"]] = relationship(
        back_populates="auto"
    )


class AutoPhoto(Base):

    __tablename__ = "auto_photo"

    id: Mapped[intpk]
    m_photo: Mapped[str]
    auto_id: Mapped[int] = mapped_column(ForeignKey("auto.id", ondelete="CASCADE"))

    auto: Mapped["Auto"] = relationship(
        back_populates="auto_photo"
    )

    def __str__(self):
        return self.m_photo


class Brand(Base):

    __tablename__ = "auto_brand"

    id: Mapped[intpk]
    brand: Mapped[str]

    auto_model: Mapped[list["Model"]] = relationship(
        back_populates="auto_brand"
    )

    def __str__(self):
        return self.brand


class Model(Base):
    __tablename__ = "auto_model"

    id: Mapped[intpk]
    model: Mapped[str]
    brand_id: Mapped[int] = mapped_column(ForeignKey("auto_brand.id", ondelete="CASCADE"))

    auto_brand: Mapped["Brand"] = relationship(
        back_populates="auto_model"
    )

    auto_generation: Mapped[list["Generation"]] = relationship(
        back_populates="auto_model"
    )

    def __str__(self):
        return self.model


class Generation(Base):

    __tablename__ = "auto_generation"

    id: Mapped[intpk]
    generation: Mapped[str]
    model_id: Mapped[int] = mapped_column(ForeignKey("auto_model.id", ondelete="CASCADE"))

    auto_model: Mapped["Model"] = relationship(
        back_populates="auto_generation"
    )

    def __str__(self):
        return self.generation


class User(SQLAlchemyBaseUserTable[int], Base):

    __tablename__ = 'user'

    id: Mapped[intpk]
    email: Mapped[str]
    username: Mapped[str]
    phone: Mapped[Optional[int]]
    hashed_password: Mapped[str]
    registered_at: Mapped[registered_at]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    auto: Mapped[list["Auto"]] = relationship(
        back_populates="user"
    )

    def __str__(self):
        return f"User {self.email}"


class TGUser(Base):

    __tablename__ = 'TGUser'

    id: Mapped[intpk]
    id_user: Mapped[int]
    username: Mapped[str]
    first_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
