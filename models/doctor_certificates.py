from sqlalchemy import Column, String, Float, Integer, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class DoctorCertificate(Base):
    __tablename__ = "doctor_certificates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    certificate_name = Column(String(100), nullable=False)
    issuing_organization = Column(String(100))
    date_issued = Column(Date)
    valid_until = Column(Date)
    certificate_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
