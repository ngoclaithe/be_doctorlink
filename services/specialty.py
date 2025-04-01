from sqlalchemy.orm import Session
from app.models.specialty import Specialty
from app.schemas.specialty import SpecialtyCreate, SpecialtyUpdate

class SpecialtyService:
    def __init__(self, db: Session):
        self.db = db

    def get_specialty(self, specialty_id: int):
        return self.db.query(Specialty).filter(Specialty.id == specialty_id).first()

    def get_specialties(self):
        return self.db.query(Specialty).all()

    def create_specialty(self, specialty: SpecialtyCreate):
        new_specialty = Specialty(**specialty.dict())
        self.db.add(new_specialty)
        self.db.commit()
        self.db.refresh(new_specialty)
        return new_specialty

    def update_specialty(self, specialty_id: int, specialty: SpecialtyUpdate):
        db_specialty = self.get_specialty(specialty_id)
        if not db_specialty:
            return None
        for key, value in specialty.dict(exclude_unset=True).items():
            setattr(db_specialty, key, value)
        self.db.commit()
        self.db.refresh(db_specialty)
        return db_specialty

    def delete_specialty(self, specialty_id: int):
        db_specialty = self.get_specialty(specialty_id)
        if not db_specialty:
            return None
        self.db.delete(db_specialty)
        self.db.commit()
        return db_specialty
