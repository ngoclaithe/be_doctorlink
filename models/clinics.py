from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    clinic_name = Column(String(150), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(15))
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    
