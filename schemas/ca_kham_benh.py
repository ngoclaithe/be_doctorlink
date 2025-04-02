from pydantic import BaseModel, conint
from datetime import date, time
from enum import Enum
from typing import List, Optional

class ServiceType(str, Enum):
    kham_tai_nha = "kham_tai_nha"
    tu_van_online = "tu_van_online"

class SessionStatus(str, Enum):
    available = "available"
    booked = "booked"
    cancelled = "cancelled"

# Schemas cho Ca Kham Benh
class CaKhamBenhBase(BaseModel):
    doctor_id: int
    session_date: date
    start_time: time
    end_time: time
    service_type: ServiceType
    status: SessionStatus = SessionStatus.available

class CaKhamBenhCreate(CaKhamBenhBase):
    ca_lam_viec_id: int

class CaKhamBenhUpdate(BaseModel):
    status: Optional[SessionStatus] = None

class CaKhamBenhResponse(CaKhamBenhBase):
    id: int
    ca_lam_viec_id: int
    
    class Config:
        from_attributes = True

# Schemas cho Ca Lam Viec
class CaLamViecBase(BaseModel):
    doctor_id: int
    session_date: date
    start_time: time
    end_time: time
    service_type: ServiceType

class CaLamViecCreate(CaLamViecBase):
    pass

class CaLamViecUpdate(BaseModel):
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    service_type: Optional[ServiceType] = None

class CaKhamBenhInCaLamViec(CaKhamBenhResponse):
    pass

class CaLamViecResponse(CaLamViecBase):
    id: int
    ca_kham_benh: List[CaKhamBenhInCaLamViec] = []
    
    class Config:
        from_attributes = True
