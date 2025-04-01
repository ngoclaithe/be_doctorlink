from sqlalchemy.orm import Session
from app.models.appointment import Appointment, AppointmentStatus
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db

    def create_appointment(self, appointment_data: AppointmentCreate):
        new_appointment = Appointment(**appointment_data.model_dump())
        self.db.add(new_appointment)
        self.db.commit()
        self.db.refresh(new_appointment)
        return new_appointment

    def get_appointment(self, appointment_id: int):
        return self.db.query(Appointment).filter(Appointment.id == appointment_id).first()

    def update_appointment(self, appointment_id: int, appointment_update: AppointmentUpdate):
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            appointment.status = appointment_update.status
            self.db.commit()
            self.db.refresh(appointment)
        return appointment

    def delete_appointment(self, appointment_id: int):
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            self.db.delete(appointment)
            self.db.commit()
        return appointment