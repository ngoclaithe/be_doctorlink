from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.ca_kham_benh import CaKhamBenhCreate, CaKhamBenhResponse, CaKhamBenhUpdate
from app.services.ca_kham_benh import CaKhamBenhService
from app.database import get_db

router = APIRouter(prefix="/sessions", tags=["Sessions"])

@router.post("/", response_model=CaKhamBenhResponse)
def create(session: CaKhamBenhCreate, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    return service.create_session(session)

@router.get("/{session_id}", response_model=CaKhamBenhResponse)
def read(session_id: int, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    session = service.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.put("/{session_id}", response_model=CaKhamBenhResponse)
def update(session_id: int, session_update: CaKhamBenhUpdate, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    session = service.update_session(session_id, session_update)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.delete("/{session_id}", response_model=CaKhamBenhResponse)
def delete(session_id: int, db: Session = Depends(get_db)):
    service = CaKhamBenhService(db)
    session = service.delete_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
