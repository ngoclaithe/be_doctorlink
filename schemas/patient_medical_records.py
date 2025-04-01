from pydantic import BaseModel, constr
from datetime import date, datetime
from typing import Optional

class PatientMedicalRecordBase(BaseModel):
    customer_id: int
    record_title: constr(max_length=150)
    description: Optional[str] = None
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    record_date: Optional[date] = None
    file_url: Optional[constr(max_length=255)] = None

class PatientMedicalRecordCreate(PatientMedicalRecordBase):
    pass

class PatientMedicalRecordUpdate(BaseModel):
    record_title: Optional[constr(max_length=150)] = None
    description: Optional[str] = None
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    record_date: Optional[date] = None
    file_url: Optional[constr(max_length=255)] = None

class PatientMedicalRecordResponse(PatientMedicalRecordBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
