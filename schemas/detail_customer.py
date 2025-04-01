from pydantic import BaseModel, constr
from datetime import date
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class DetailCustomerBase(BaseModel):
    full_name: constr(max_length=100)
    gender: GenderEnum = GenderEnum.other
    dob: Optional[date] = None
    phone: Optional[constr(max_length=15)] = None
    address: Optional[constr(max_length=255)] = None

class DetailCustomerCreate(DetailCustomerBase):
    user_id: int

class DetailCustomerUpdate(BaseModel):
    full_name: Optional[constr(max_length=100)] = None
    gender: Optional[GenderEnum] = None
    dob: Optional[date] = None
    phone: Optional[constr(max_length=15)] = None
    address: Optional[constr(max_length=255)] = None

class DetailCustomerResponse(DetailCustomerBase):
    user_id: int

    class Config:
        from_attributes = True
