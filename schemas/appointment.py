from pydantic import BaseModel
from datetime import date, datetime
from enum import Enum

class AppointmentStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class AppointmentBase(BaseModel):
    customer_id: int
    doctor_id: int
    appointment_date: date
    session_id: int
    status: AppointmentStatus = AppointmentStatus.pending

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    status: AppointmentStatus

class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True