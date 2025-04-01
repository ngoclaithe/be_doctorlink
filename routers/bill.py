from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.bill import BillCreate, BillResponse, BillUpdate
from app.services.bill import BillService
from app.database import get_db

router = APIRouter(prefix="/bills", tags=["Bills"])

@router.post("/", response_model=BillResponse)
def create(bill: BillCreate, db: Session = Depends(get_db)):
    service = BillService(db)
    return service.create_bill(bill)

@router.get("/{bill_id}", response_model=BillResponse)
def read(bill_id: int, db: Session = Depends(get_db)):
    service = BillService(db)
    bill = service.get_bill(bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill

@router.put("/{bill_id}", response_model=BillResponse)
def update(bill_id: int, bill_update: BillUpdate, db: Session = Depends(get_db)):
    service = BillService(db)
    bill = service.update_bill(bill_id, bill_update)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill

@router.delete("/{bill_id}", response_model=BillResponse)
def delete(bill_id: int, db: Session = Depends(get_db)):
    service = BillService(db)
    bill = service.delete_bill(bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill
