from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.patient_medical_records import PatientMedicalRecordCreate, PatientMedicalRecordResponse, PatientMedicalRecordUpdate
from app.services.patient_medical_records import PatientMedicalRecordService
from app.database import get_db

router = APIRouter(prefix="/patient_medical_records", tags=["Patient Medical Records"])

@router.post("/", response_model=PatientMedicalRecordResponse)
def create(data: PatientMedicalRecordCreate, db: Session = Depends(get_db)):
    service = PatientMedicalRecordService(db)
    return service.create_record(data)

@router.get("/{record_id}", response_model=PatientMedicalRecordResponse)
def read(record_id: int, db: Session = Depends(get_db)):
    service = PatientMedicalRecordService(db)
    record = service.get_record(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@router.put("/{record_id}", response_model=PatientMedicalRecordResponse)
def update(record_id: int, data: PatientMedicalRecordUpdate, db: Session = Depends(get_db)):
    service = PatientMedicalRecordService(db)
    record = service.update_record(record_id, data)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@router.delete("/{record_id}", response_model=PatientMedicalRecordResponse)
def delete(record_id: int, db: Session = Depends(get_db)):
    service = PatientMedicalRecordService(db)
    record = service.delete_record(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record
