from sqlalchemy import Column, String, Integer, DateTime, Enum
from app.database import Base
from datetime import datetime
import enum

class UserRole(enum.Enum):
    customer = "customer"
    doctor = "doctor"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
