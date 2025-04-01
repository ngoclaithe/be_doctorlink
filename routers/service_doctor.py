from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.service_doctor import ServiceDoctorCreate, ServiceDoctorResponse, ServiceDoctorUpdate
from app.services.service_doctor import ServiceDoctorService
from app.database import get_db

router = APIRouter(prefix="/service_doctor", tags=["Service Doctor"])

@router.post("/", response_model=ServiceDoctorResponse)
def create(data: ServiceDoctorCreate, db: Session = Depends(get_db)):
    service = ServiceDoctorService(db)
    return service.create_service(data)

@router.get("/{service_id}", response_model=ServiceDoctorResponse)
def read(service_id: int, db: Session = Depends(get_db)):
    service = ServiceDoctorService(db)
    service_instance = service.get_service(service_id)
    if not service_instance:
        raise HTTPException(status_code=404, detail="Service not found")
    return service_instance

@router.put("/{service_id}", response_model=ServiceDoctorResponse)
def update(service_id: int, data: ServiceDoctorUpdate, db: Session = Depends(get_db)):
    service = ServiceDoctorService(db)
    service_instance = service.update_service(service_id, data)
    if not service_instance:
        raise HTTPException(status_code=404, detail="Service not found")
    return service_instance

@router.delete("/{service_id}", response_model=ServiceDoctorResponse)
def delete(service_id: int, db: Session = Depends(get_db)):
    service = ServiceDoctorService(db)
    service_instance = service.delete_service(service_id)
    if not service_instance:
        raise HTTPException(status_code=404, detail="Service not found")
    return service_instance
