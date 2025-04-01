from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Time, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

class SessionStatus(enum.Enum):
    available = "available"
    booked = "booked"
    cancelled = "cancelled"

class CaKhamBenh(Base):
    __tablename__ = "ca_kham_benh"
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    session_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.available)
    
