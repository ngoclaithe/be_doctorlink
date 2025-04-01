from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.doctor_certificates import DoctorCertificateCreate, DoctorCertificateResponse, DoctorCertificateUpdate
from app.services.doctor_certificates import DoctorCertificateService
from app.database import get_db

router = APIRouter(prefix="/doctor_certificates", tags=["Doctor Certificates"])

@router.post("/", response_model=DoctorCertificateResponse)
def create(data: DoctorCertificateCreate, db: Session = Depends(get_db)):
    service = DoctorCertificateService(db)
    return service.create_certificate(data)

@router.get("/{cert_id}", response_model=DoctorCertificateResponse)
def read(cert_id: int, db: Session = Depends(get_db)):
    service = DoctorCertificateService(db)
    cert = service.get_certificate(cert_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert

@router.put("/{cert_id}", response_model=DoctorCertificateResponse)
def update(cert_id: int, data: DoctorCertificateUpdate, db: Session = Depends(get_db)):
    service = DoctorCertificateService(db)
    cert = service.update_certificate(cert_id, data)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert

@router.delete("/{cert_id}", response_model=DoctorCertificateResponse)
def delete(cert_id: int, db: Session = Depends(get_db)):
    service = DoctorCertificateService(db)
    cert = service.delete_certificate(cert_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert
