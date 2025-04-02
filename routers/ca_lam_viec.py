from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.ca_kham_benh import (
    CaLamViecCreate, CaLamViecResponse, CaLamViecUpdate,
    CaKhamBenhResponse
)
from app.services.ca_kham_benh import CaLamViecService, CaKhamBenhService
from app.database import get_db
from typing import List
from datetime import date

router = APIRouter(prefix="/ca-lam-viec", tags=["Ca Làm Việc"])

@router.post("/", response_model=CaLamViecResponse)
def create_ca_lam_viec(data: CaLamViecCreate, db: Session = Depends(get_db)):
    service = CaLamViecService(db)
    return service.create_ca_lam_viec(data)

@router.get("/{ca_lam_viec_id}", response_model=CaLamViecResponse)
def read_ca_lam_viec(ca_lam_viec_id: int, db: Session = Depends(get_db)):
    service = CaLamViecService(db)
    ca_lam_viec = service.get_ca_lam_viec(ca_lam_viec_id)
    if not ca_lam_viec:
        raise HTTPException(status_code=404, detail="Ca làm việc không tìm thấy")
    return ca_lam_viec

@router.get("/bac-si/{doctor_id}", response_model=List[CaLamViecResponse])
def read_ca_lam_viec_by_doctor(
    doctor_id: int, 
    session_date: date = None, 
    db: Session = Depends(get_db)
):
    service = CaLamViecService(db)
    return service.get_ca_lam_viec_by_doctor(doctor_id, session_date)

@router.put("/{ca_lam_viec_id}", response_model=CaLamViecResponse)
def update_ca_lam_viec(
    ca_lam_viec_id: int, 
    update_data: CaLamViecUpdate, 
    db: Session = Depends(get_db)
):
    service = CaLamViecService(db)
    ca_lam_viec = service.update_ca_lam_viec(ca_lam_viec_id, update_data)
    if not ca_lam_viec:
        raise HTTPException(status_code=404, detail="Ca làm việc không tìm thấy")
    return ca_lam_viec

@router.delete("/{ca_lam_viec_id}", response_model=CaLamViecResponse)
def delete_ca_lam_viec(ca_lam_viec_id: int, db: Session = Depends(get_db)):
    service = CaLamViecService(db)
    ca_lam_viec = service.delete_ca_lam_viec(ca_lam_viec_id)
    if not ca_lam_viec:
        raise HTTPException(status_code=404, detail="Ca làm việc không tìm thấy")
    return ca_lam_viec

@router.get("/{ca_lam_viec_id}/ca-kham-benh", response_model=List[CaKhamBenhResponse])
def read_ca_kham_benh_by_ca_lam_viec(ca_lam_viec_id: int, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    return service.get_ca_kham_benh_by_ca_lam_viec(ca_lam_viec_id)