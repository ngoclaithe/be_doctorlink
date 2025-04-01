from pydantic import BaseModel, conint
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    appointment_id: int
    customer_id: int
    doctor_id: int
    rating: conint(ge=1, le=5) 
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    rating: Optional[conint(ge=1, le=5)] = None
    comment: Optional[str] = None

class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
