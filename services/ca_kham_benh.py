from sqlalchemy.orm import Session
from app.models.ca_kham_benh import CaKhamBenh, SessionStatus
from app.schemas.ca_kham_benh import CaKhamBenhCreate, CaKhamBenhUpdate

class CaKhamBenhService:
    def __init__(self, db: Session):
        self.db = db

    def create_session(self, session_data: CaKhamBenhCreate):
        new_session = CaKhamBenh(**session_data.model_dump())
        self.db.add(new_session)
        self.db.commit()
        self.db.refresh(new_session)
        return new_session

    def get_session(self, session_id: int):
        return self.db.query(CaKhamBenh).filter(CaKhamBenh.id == session_id).first()

    def update_session(self, session_id: int, session_update: CaKhamBenhUpdate):
        session = self.db.query(CaKhamBenh).filter(CaKhamBenh.id == session_id).first()
        if session:
            session.status = session_update.status
            self.db.commit()
            self.db.refresh(session)
        return session

    def delete_session(self, session_id: int):
        session = self.db.query(CaKhamBenh).filter(CaKhamBenh.id == session_id).first()
        if session:
            self.db.delete(session)
            self.db.commit()
        return session