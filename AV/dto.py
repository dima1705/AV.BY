from pydantic import BaseModel


class CarDto(BaseModel):
    name: str
    price_for_bel_rub: str
    price_for_usd: str
    year: str
    kpp: str
    volume: str
    type_engine: str
    probeg: str
    kyzov: str
    privod: str
    color: str
    power: str
    comment: str


# class MainCategoryDto(BaseModel):
#     category: str
#
#
# class AddCategoryDto(BaseModel):
#     category: str