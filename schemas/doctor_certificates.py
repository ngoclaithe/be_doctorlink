from pydantic import BaseModel, constr
from datetime import date, datetime
from typing import Optional

class DoctorCertificateBase(BaseModel):
    doctor_id: int
    certificate_name: constr(max_length=100)
    issuing_organization: Optional[constr(max_length=100)] = None
    date_issued: Optional[date] = None
    valid_until: Optional[date] = None
    certificate_url: Optional[constr(max_length=255)] = None

class DoctorCertificateCreate(DoctorCertificateBase):
    pass

class DoctorCertificateUpdate(BaseModel):
    certificate_name: Optional[constr(max_length=100)] = None
    issuing_organization: Optional[constr(max_length=100)] = None
    date_issued: Optional[date] = None
    valid_until: Optional[date] = None
    certificate_url: Optional[constr(max_length=255)] = None

class DoctorCertificateResponse(DoctorCertificateBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
