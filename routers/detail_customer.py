from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.detail_customer import DetailCustomerCreate, DetailCustomerResponse, DetailCustomerUpdate
from app.services.detail_customer import DetailCustomerService
from app.database import get_db

router = APIRouter(prefix="/detail_customer", tags=["Detail Customer"])

@router.post("/", response_model=DetailCustomerResponse)
def create(data: DetailCustomerCreate, db: Session = Depends(get_db)):
    service = DetailCustomerService(db)
    return service.create_detail_customer(data)

@router.get("/{user_id}", response_model=DetailCustomerResponse)
def read(user_id: int, db: Session = Depends(get_db)):
    service = DetailCustomerService(db)
    detail = service.get_detail_customer(user_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail Customer not found")
    return detail

@router.put("/{user_id}", response_model=DetailCustomerResponse)
def update(user_id: int, update_data: DetailCustomerUpdate, db: Session = Depends(get_db)):
    service = DetailCustomerService(db)
    detail = service.update_detail_customer(user_id, update_data)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail Customer not found")
    return detail

@router.delete("/{user_id}", response_model=DetailCustomerResponse)
def delete(user_id: int, db: Session = Depends(get_db)):
    service = DetailCustomerService(db)
    detail = service.delete_detail_customer(user_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail Customer not found")
    return detail
