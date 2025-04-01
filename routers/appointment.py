from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentUpdate
from app.services.appointment import AppointmentService
from app.database import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=AppointmentResponse)
def create(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.create_appointment(appointment)

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def read(appointment_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.get_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update(appointment_id: int, appointment_update: AppointmentUpdate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.update_appointment(appointment_id, appointment_update)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.delete("/{appointment_id}", response_model=AppointmentResponse)
def delete(appointment_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.delete_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
