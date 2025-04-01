from pydantic import BaseModel, constr
from datetime import datetime
from decimal import Decimal
from typing import Optional

class ServiceDoctorBase(BaseModel):
    doctor_id: int
    service_name: constr(max_length=100)
    description: Optional[str] = None
    price: Decimal
    duration: Optional[int] = None

class ServiceDoctorCreate(ServiceDoctorBase):
    pass

class ServiceDoctorUpdate(BaseModel):
    service_name: Optional[constr(max_length=100)] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    duration: Optional[int] = None

class ServiceDoctorResponse(ServiceDoctorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
