from sqlalchemy.orm import Session
from app.models.clinics import Clinic
from app.schemas.clinics import ClinicCreate, ClinicUpdate

class ClinicService:
    def __init__(self, db: Session):
        self.db = db

    def create_clinic(self, clinic_data: ClinicCreate):
        new_clinic = Clinic(**clinic_data.model_dump())
        self.db.add(new_clinic)
        self.db.commit()
        self.db.refresh(new_clinic)
        return new_clinic

    def get_clinic(self, clinic_id: int):
        return self.db.query(Clinic).filter(Clinic.id == clinic_id).first()

    def update_clinic(self, clinic_id: int, clinic_update: ClinicUpdate):
        clinic = self.db.query(Clinic).filter(Clinic.id == clinic_id).first()
        if clinic:
            for field, value in clinic_update.dict(exclude_unset=True).items():
                setattr(clinic, field, value)
            self.db.commit()
            self.db.refresh(clinic)
        return clinic

    def delete_clinic(self, clinic_id: int):
        clinic = self.db.query(Clinic).filter(Clinic.id == clinic_id).first()
        if clinic:
            self.db.delete(clinic)
            self.db.commit()
        return clinic