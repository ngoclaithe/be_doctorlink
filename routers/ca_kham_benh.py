from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.ca_kham_benh import CaKhamBenhResponse, CaKhamBenhUpdate
from app.services.ca_kham_benh import CaKhamBenhService
from app.database import get_db
from typing import List, Optional
from datetime import date
from app.models.ca_kham_benh import SessionStatus

router = APIRouter(prefix="/ca-kham-benh", tags=["Ca Khám Bệnh"])

@router.get("/{ca_kham_benh_id}", response_model=CaKhamBenhResponse)
def read_ca_kham_benh(ca_kham_benh_id: int, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    ca_kham_benh = service.get_ca_kham_benh(ca_kham_benh_id)
    if not ca_kham_benh:
        raise HTTPException(status_code=404, detail="Ca khám bệnh không tìm thấy")
    return ca_kham_benh

@router.get("/bac-si/{doctor_id}", response_model=List[CaKhamBenhResponse])
def read_ca_kham_benh_by_doctor(
    doctor_id: int, 
    session_date: Optional[date] = None, 
    status: Optional[SessionStatus] = None,
    db: Session = Depends(get_db)
):
    service = CaKhamBenhService(db)
    return service.get_ca_kham_benh_by_doctor(doctor_id, session_date, status)

@router.put("/{ca_kham_benh_id}", response_model=CaKhamBenhResponse)
def update_ca_kham_benh(
    ca_kham_benh_id: int, 
    update_data: CaKhamBenhUpdate, 
    db: Session = Depends(get_db)
):
    service = CaKhamBenhService(db)
    ca_kham_benh = service.update_ca_kham_benh(ca_kham_benh_id, update_data)
    if not ca_kham_benh:
        raise HTTPException(status_code=404, detail="Ca khám bệnh không tìm thấy")
    return ca_kham_benh