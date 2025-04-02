from sqlalchemy.orm import Session
from app.models.ca_kham_benh import CaLamViec, CaKhamBenh, SessionStatus, ServiceType
from app.schemas.ca_kham_benh import (
    CaLamViecCreate, CaLamViecUpdate, CaLamViecResponse,
    CaKhamBenhCreate, CaKhamBenhUpdate, CaKhamBenhResponse
)
from typing import List
from datetime import date


class CaLamViecService:
    def __init__(self, db: Session):
        self.db = db

    def create_ca_lam_viec(self, data: CaLamViecCreate):

        new_ca_lam_viec = CaLamViec(**data.model_dump())
        self.db.add(new_ca_lam_viec)
        self.db.commit()
        self.db.refresh(new_ca_lam_viec)
        
        slots = new_ca_lam_viec.create_appointment_slots()
        self.db.add_all(slots)
        self.db.commit()
        
        self.db.refresh(new_ca_lam_viec)
        return new_ca_lam_viec

    def get_ca_lam_viec(self, ca_lam_viec_id: int):
        return self.db.query(CaLamViec).filter(CaLamViec.id == ca_lam_viec_id).first()
    
    def get_ca_lam_viec_by_doctor(self, doctor_id: int, session_date: date = None):
        query = self.db.query(CaLamViec).filter(CaLamViec.doctor_id == doctor_id)
        if session_date:
            query = query.filter(CaLamViec.session_date == session_date)
        return query.all()

    def update_ca_lam_viec(self, ca_lam_viec_id: int, update_data: CaLamViecUpdate):
        ca_lam_viec = self.db.query(CaLamViec).filter(CaLamViec.id == ca_lam_viec_id).first()
        if not ca_lam_viec:
            return None
            
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(ca_lam_viec, key, value)
            
        self.db.commit()
        self.db.refresh(ca_lam_viec)
        return ca_lam_viec

    def delete_ca_lam_viec(self, ca_lam_viec_id: int):
        ca_lam_viec = self.db.query(CaLamViec).filter(CaLamViec.id == ca_lam_viec_id).first()
        if ca_lam_viec:
            self.db.delete(ca_lam_viec)
            self.db.commit()
        return ca_lam_viec


class CaKhamBenhService:
    def __init__(self, db: Session):
        self.db = db

    def get_ca_kham_benh(self, ca_kham_benh_id: int):
        return self.db.query(CaKhamBenh).filter(CaKhamBenh.id == ca_kham_benh_id).first()
    
    def get_ca_kham_benh_by_doctor(self, doctor_id: int, session_date: date = None, status: SessionStatus = None):
        query = self.db.query(CaKhamBenh).filter(CaKhamBenh.doctor_id == doctor_id)
        if session_date:
            query = query.filter(CaKhamBenh.session_date == session_date)
        if status:
            query = query.filter(CaKhamBenh.status == status)
        return query.all()
    
    def get_ca_kham_benh_by_ca_lam_viec(self, ca_lam_viec_id: int):
        return self.db.query(CaKhamBenh).filter(CaKhamBenh.ca_lam_viec_id == ca_lam_viec_id).all()

    def update_ca_kham_benh(self, ca_kham_benh_id: int, update_data: CaKhamBenhUpdate):
        ca_kham_benh = self.db.query(CaKhamBenh).filter(CaKhamBenh.id == ca_kham_benh_id).first()
        if not ca_kham_benh:
            return None
            
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(ca_kham_benh, key, value)
            
        self.db.commit()
        self.db.refresh(ca_kham_benh)
        return ca_kham_benh