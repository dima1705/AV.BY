from pydantic import BaseModel


class AutoDTO(BaseModel):
    brand: str
    model: str
    generation_with_years: str
    year: int
    engine_capacity: float
    engine_type: str
    transmission_type: str
    body_type: str
    drive_type: str
    color: str
    mileage_km: int
    power: int | None = None
    fuel_consumption: float | None = None
    price_amount_usd: int
    price_amount_byn: int
    description: str
    main_photo: str
    location: str
    user_id: int | None = None


class UserDTO(BaseModel):
    username: str
    email: str
    password: str
    phone: int | None = None


