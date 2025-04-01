from pydantic import BaseModel
from typing import Optional

class SpecialtyBase(BaseModel):
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
class SpecialtyCreate(SpecialtyBase):
    pass

class SpecialtyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
class SpecialtyResponse(SpecialtyBase):
    id: int

    class Config:
        orm_mode = True
