from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.specialty import SpecialtyCreate, SpecialtyResponse, SpecialtyUpdate
from app.services.specialty import SpecialtyService
from app.database import get_db

router = APIRouter(prefix="/specialty", tags=["Specialty"])

@router.get("/", response_model=List[SpecialtyResponse])
def read_specialties(db: Session = Depends(get_db)):
    service = SpecialtyService(db)
    specialties = service.get_specialties()
    return specialties

@router.get("/{specialty_id}", response_model=SpecialtyResponse)
def read_specialty(specialty_id: int, db: Session = Depends(get_db)):
    service = SpecialtyService(db)
    specialty = service.get_specialty(specialty_id)
    if not specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return specialty

@router.post("/", response_model=SpecialtyResponse)
def create_specialty(specialty: SpecialtyCreate, db: Session = Depends(get_db)):
    service = SpecialtyService(db)
    new_specialty = service.create_specialty(specialty)
    return new_specialty

@router.put("/{specialty_id}", response_model=SpecialtyResponse)
def update_specialty(specialty_id: int, specialty: SpecialtyUpdate, db: Session = Depends(get_db)):
    service = SpecialtyService(db)
    updated_specialty = service.update_specialty(specialty_id, specialty)
    if not updated_specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return updated_specialty

@router.delete("/{specialty_id}", response_model=SpecialtyResponse)
def delete_specialty(specialty_id: int, db: Session = Depends(get_db)):
    service = SpecialtyService(db)
    deleted_specialty = service.delete_specialty(specialty_id)
    if not deleted_specialty:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return deleted_specialty
