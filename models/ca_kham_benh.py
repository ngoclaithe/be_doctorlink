from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Time, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timedelta
import enum

class ServiceType(enum.Enum):
    kham_tai_nha = "kham_tai_nha"
    tu_van_online = "tu_van_online"

class SessionStatus(enum.Enum):
    available = "available"
    booked = "booked"
    cancelled = "cancelled"

class CaLamViec(Base):
    __tablename__ = "ca_lam_viec"
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    session_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    service_type = Column(Enum(ServiceType), nullable=False)
    ca_kham_benh = relationship("CaKhamBenh", back_populates="ca_lam_viec", cascade="all, delete-orphan")
    
    def create_appointment_slots(self):
        slots = []
        start = datetime.combine(self.session_date, self.start_time)
        end = datetime.combine(self.session_date, self.end_time)
        
        current = start
        while current + timedelta(minutes=30) <= end:
            slot = CaKhamBenh(
                ca_lam_viec_id=self.id,
                doctor_id=self.doctor_id,
                session_date=self.session_date,
                start_time=current.time(),
                end_time=(current + timedelta(minutes=30)).time(),
                service_type=self.service_type,
                status=SessionStatus.available
            )
            slots.append(slot)
            current += timedelta(minutes=30)
            
        return slots

class CaKhamBenh(Base):
    __tablename__ = "ca_kham_benh"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ca_lam_viec_id = Column(Integer, ForeignKey("ca_lam_viec.id"), nullable=False)
    doctor_id = Column(Integer, nullable=False)
    session_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    service_type = Column(Enum(ServiceType), nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.available)
    ca_lam_viec = relationship("CaLamViec", back_populates="ca_kham_benh")