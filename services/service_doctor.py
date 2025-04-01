from sqlalchemy.orm import Session
from app.models.service_doctor import ServiceDoctor
from app.schemas.service_doctor import ServiceDoctorCreate, ServiceDoctorUpdate

class ServiceDoctorService:
    def __init__(self, db: Session):
        self.db = db

    def create_service(self, data: ServiceDoctorCreate):
        new_service = ServiceDoctor(**data.model_dump())
        self.db.add(new_service)
        self.db.commit()
        self.db.refresh(new_service)
        return new_service

    def get_service(self, service_id: int):
        return self.db.query(ServiceDoctor).filter(ServiceDoctor.id == service_id).first()

    def update_service(self, service_id: int, data: ServiceDoctorUpdate):
        service_instance = self.db.query(ServiceDoctor).filter(ServiceDoctor.id == service_id).first()
        if service_instance:
            for field, value in data.dict(exclude_unset=True).items():
                setattr(service_instance, field, value)
            self.db.commit()
            self.db.refresh(service_instance)
        return service_instance

    def delete_service(self, service_id: int):
        service_instance = self.db.query(ServiceDoctor).filter(ServiceDoctor.id == service_id).first()
        if service_instance:
            self.db.delete(service_instance)
            self.db.commit()
        return service_instance
