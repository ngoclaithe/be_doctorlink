from sqlalchemy.orm import Session
from app.models.detail_customer import DetailCustomer
from app.schemas.detail_customer import DetailCustomerCreate, DetailCustomerUpdate

class DetailCustomerService:
    def __init__(self, db: Session):
        self.db = db

    def create_detail_customer(self, data: DetailCustomerCreate):
        new_detail = DetailCustomer(**data.model_dump())
        self.db.add(new_detail)
        self.db.commit()
        self.db.refresh(new_detail)
        return new_detail
    def get_all_customer(self):
        return self.db.query(DetailCustomer).all()
    def get_detail_customer(self, user_id: int):
        return self.db.query(DetailCustomer).filter(DetailCustomer.user_id == user_id).first()

    def update_detail_customer(self, user_id: int, update_data: DetailCustomerUpdate):
        detail = self.db.query(DetailCustomer).filter(DetailCustomer.user_id == user_id).first()
        if detail:
            for field, value in update_data.dict(exclude_unset=True).items():
                setattr(detail, field, value)
            self.db.commit()
            self.db.refresh(detail)
        return detail

    def delete_detail_customer(self, user_id: int):
        detail = self.db.query(DetailCustomer).filter(DetailCustomer.user_id == user_id).first()
        if detail:
            self.db.delete(detail)
            self.db.commit()
        return detail