from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class DetailDoctorBase(BaseModel):
    full_name: str
    gender: GenderEnum
    dob: date
    phone: str
    address: str
    specialty_id: int
    experience_years: int
    bio: str
    avg_rating: float
    image_url: str

class DetailDoctorCreate(DetailDoctorBase):
    user_id: int

class DetailDoctorUpdate(BaseModel):
    full_name: Optional[str] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    specialty_id: Optional[int] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None
    avg_rating: Optional[float] = None
    image_url: str

class DetailDoctorResponse(DetailDoctorBase):
    user_id: int

    class Config:
        orm_mode = True
