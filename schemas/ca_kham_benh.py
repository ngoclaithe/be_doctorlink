from pydantic import BaseModel, conint
from datetime import date, time
from enum import Enum

class SessionStatus(str, Enum):
    available = "available"
    booked = "booked"
    cancelled = "cancelled"

class CaKhamBenhBase(BaseModel):
    doctor_id: int
    session_date: date
    start_time: time
    end_time: time
    status: SessionStatus = SessionStatus.available

class CaKhamBenhCreate(CaKhamBenhBase):
    pass

class CaKhamBenhUpdate(BaseModel):
    status: SessionStatus

class CaKhamBenhResponse(CaKhamBenhBase):
    id: int
    class Config:
        from_attributes = True