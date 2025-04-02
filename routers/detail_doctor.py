from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.detail_doctor import DetailDoctorCreate, DetailDoctorResponse, DetailDoctorUpdate
from app.services.detail_doctor import DetailDoctorService
from app.database import get_db

router = APIRouter(prefix="/detail-doctor", tags=["DetailDoctor"])

@router.get("/", response_model=List[DetailDoctorResponse])
def read_all_detail_doctor(db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    details = service.get_all_detail_doctor()
    return details

@router.get("/{user_id}", response_model=DetailDoctorResponse)
def read_detail_doctor(user_id: int, db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    detail = service.get_detail_doctor(user_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail doctor not found")
    return detail

@router.get("/specialty/{specialty_id}", response_model=List[DetailDoctorResponse])
def read_doctors_by_specialty(specialty_id: int, db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    doctors = service.get_doctors_by_specialty_id(specialty_id)
    return doctors

@router.post("/", response_model=DetailDoctorResponse)
def create_detail_doctor(detail: DetailDoctorCreate, db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    if service.get_detail_doctor(detail.user_id):
        raise HTTPException(status_code=400, detail="Detail doctor already exists")
    new_detail = service.create_detail_doctor(detail)
    return new_detail

@router.put("/{user_id}", response_model=DetailDoctorResponse)
def update_detail_doctor(user_id: int, detail: DetailDoctorUpdate, db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    updated_detail = service.update_detail_doctor(user_id, detail)
    if not updated_detail:
        raise HTTPException(status_code=404, detail="Detail doctor not found")
    return updated_detail

@router.delete("/{user_id}", response_model=DetailDoctorResponse)
def delete_detail_doctor(user_id: int, db: Session = Depends(get_db)):
    service = DetailDoctorService(db)
    deleted_detail = service.delete_detail_doctor(user_id)
    if not deleted_detail:
        raise HTTPException(status_code=404, detail="Detail doctor not found")
    return deleted_detail