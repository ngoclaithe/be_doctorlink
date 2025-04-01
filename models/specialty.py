from sqlalchemy import Column, String, Float, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Specialty(Base):
    __tablename__ = "specialty"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    image_url = Column(Text)
    
