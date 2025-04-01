from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class DetailCustomer(Base):
    __tablename__ = "detail_customer"
    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    gender = Column(Enum(GenderEnum), default=GenderEnum.other)
    dob = Column(Date)
    phone = Column(String(15))
    address = Column(String(255))
    
