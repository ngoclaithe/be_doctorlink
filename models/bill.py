from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

class BillStatus(enum.Enum):
    unpaid = "unpaid"
    paid = "paid"
    cancelled = "cancelled"

class Bill(Base):
    __tablename__ = "bill"
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(BillStatus), default=BillStatus.unpaid)
    paid_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    
