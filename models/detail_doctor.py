from sqlalchemy import Column, String, Float, Integer, DateTime, Date, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class DetailDoctor(Base):
    __tablename__ = "detail_doctor"
    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    gender = Column(Enum(GenderEnum), default=GenderEnum.other)
    dob = Column(Date)
    phone = Column(String(15))
    address = Column(String(255))
    specialty_id = Column(Integer, nullable=False)
    experience_years = Column(Integer)
    bio = Column(Text)
    avg_rating = Column(Float, default=0)
    image_url = Column(Text)
    
