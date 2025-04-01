from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.clinics import ClinicCreate, ClinicResponse, ClinicUpdate
from app.services.clinics import ClinicService
from app.database import get_db

router = APIRouter(prefix="/clinics", tags=["Clinics"])

@router.post("/", response_model=ClinicResponse)
def create(clinic: ClinicCreate, db: Session = Depends(get_db)):
    service = ClinicService(db)
    return service.create_clinic(clinic)

@router.get("/{clinic_id}", response_model=ClinicResponse)
def read(clinic_id: int, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.get_clinic(clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic

@router.put("/{clinic_id}", response_model=ClinicResponse)
def update(clinic_id: int, clinic_update: ClinicUpdate, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.update_clinic(clinic_id, clinic_update)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic

@router.delete("/{clinic_id}", response_model=ClinicResponse)
def delete(clinic_id: int, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.delete_clinic(clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic
