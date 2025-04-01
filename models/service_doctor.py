from sqlalchemy import Column, String, Float, Integer, DateTime, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class ServiceDoctor(Base):
    __tablename__ = "service_doctor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    service_name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    duration = Column(Integer)  
    created_at = Column(DateTime, default=datetime.utcnow)
    
