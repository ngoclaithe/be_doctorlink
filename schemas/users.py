from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any

class UserRole(str, Enum):
    customer = "customer"
    doctor = "doctor"
    admin = "admin"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: constr(min_length=6)

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginStatus(BaseModel):
    message: str
    loggedIn: bool
    user: Optional[Dict[str, Any]] = None