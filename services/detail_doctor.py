from sqlalchemy.orm import Session
from app.models.detail_doctor import DetailDoctor
from app.schemas.detail_doctor import DetailDoctorCreate, DetailDoctorUpdate

class DetailDoctorService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_detail_doctor(self):
        return self.db.query(DetailDoctor).all()

    def get_detail_doctor(self, user_id: int):
        return self.db.query(DetailDoctor).filter(DetailDoctor.user_id == user_id).first()
        
    def get_doctors_by_specialty_id(self, specialty_id: int):
        return self.db.query(DetailDoctor).filter(DetailDoctor.specialty_id == specialty_id).all()

    def create_detail_doctor(self, detail: DetailDoctorCreate):
        new_detail = DetailDoctor(**detail.dict())
        self.db.add(new_detail)
        self.db.commit()
        self.db.refresh(new_detail)
        return new_detail

    def update_detail_doctor(self, user_id: int, detail: DetailDoctorUpdate):
        db_detail = self.get_detail_doctor(user_id)
        if not db_detail:
            return None
        for key, value in detail.dict(exclude_unset=True).items():
            setattr(db_detail, key, value)
        self.db.commit()
        self.db.refresh(db_detail)
        return db_detail

    def delete_detail_doctor(self, user_id: int):
        db_detail = self.get_detail_doctor(user_id)
        if not db_detail:
            return None
        self.db.delete(db_detail)
        self.db.commit()
        return db_detail