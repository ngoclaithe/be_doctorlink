from sqlalchemy import Column, String, Float, Integer, DateTime, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class PatientMedicalRecord(Base):
    __tablename__ = "patient_medical_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    record_title = Column(String(150), nullable=False)
    description = Column(Text)
    diagnosis = Column(Text)
    treatment = Column(Text)
    record_date = Column(Date)
    file_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
