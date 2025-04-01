from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional

class ClinicBase(BaseModel):
    doctor_id: int
    clinic_name: constr(max_length=150)
    address: constr(max_length=255)
    phone: Optional[constr(max_length=15)] = None
    email: Optional[EmailStr] = None

class ClinicCreate(ClinicBase):
    pass

class ClinicUpdate(BaseModel):
    clinic_name: Optional[constr(max_length=150)] = None
    address: Optional[constr(max_length=255)] = None
    phone: Optional[constr(max_length=15)] = None
    email: Optional[EmailStr] = None

class ClinicResponse(ClinicBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
