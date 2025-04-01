from sqlalchemy.orm import Session
from app.models.patient_medical_records import PatientMedicalRecord
from app.schemas.patient_medical_records import PatientMedicalRecordCreate, PatientMedicalRecordUpdate

class PatientMedicalRecordService:
    def __init__(self, db: Session):
        self.db = db

    def create_record(self, data: PatientMedicalRecordCreate):
        new_record = PatientMedicalRecord(**data.model_dump())
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
        return new_record

    def get_record(self, record_id: int):
        return self.db.query(PatientMedicalRecord).filter(PatientMedicalRecord.id == record_id).first()

    def update_record(self, record_id: int, data: PatientMedicalRecordUpdate):
        record = self.db.query(PatientMedicalRecord).filter(PatientMedicalRecord.id == record_id).first()
        if record:
            for field, value in data.dict(exclude_unset=True).items():
                setattr(record, field, value)
            self.db.commit()
            self.db.refresh(record)
        return record

    def delete_record(self, record_id: int):
        record = self.db.query(PatientMedicalRecord).filter(PatientMedicalRecord.id == record_id).first()
        if record:
            self.db.delete(record)
            self.db.commit()
        return record
