from sqlalchemy.orm import Session
from app.models.doctor_certificates import DoctorCertificate
from app.schemas.doctor_certificates import DoctorCertificateCreate, DoctorCertificateUpdate

class DoctorCertificateService:
    def __init__(self, db: Session):
        self.db = db

    def create_certificate(self, data: DoctorCertificateCreate):
        new_cert = DoctorCertificate(**data.model_dump())
        self.db.add(new_cert)
        self.db.commit()
        self.db.refresh(new_cert)
        return new_cert

    def get_certificate(self, cert_id: int):
        return self.db.query(DoctorCertificate).filter(DoctorCertificate.id == cert_id).first()

    def update_certificate(self, cert_id: int, data: DoctorCertificateUpdate):
        cert = self.db.query(DoctorCertificate).filter(DoctorCertificate.id == cert_id).first()
        if cert:
            for field, value in data.dict(exclude_unset=True).items():
                setattr(cert, field, value)
            self.db.commit()
            self.db.refresh(cert)
        return cert

    def delete_certificate(self, cert_id: int):
        cert = self.db.query(DoctorCertificate).filter(DoctorCertificate.id == cert_id).first()
        if cert:
            self.db.delete(cert)
            self.db.commit()
        return cert
