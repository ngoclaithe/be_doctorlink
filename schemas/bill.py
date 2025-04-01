from pydantic import BaseModel, condecimal
from datetime import date, datetime
from enum import Enum
from typing import Optional

class BillStatus(str, Enum):
    unpaid = "unpaid"
    paid = "paid"
    cancelled = "cancelled"

class BillBase(BaseModel):
    appointment_id: int
    amount: condecimal(max_digits=10, decimal_places=2)
    status: BillStatus = BillStatus.unpaid
    paid_date: Optional[date] = None

class BillCreate(BillBase):
    pass

class BillUpdate(BaseModel):
    status: BillStatus
    paid_date: Optional[date] = None

class BillResponse(BillBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
