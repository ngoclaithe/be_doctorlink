from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

