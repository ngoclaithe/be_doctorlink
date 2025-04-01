from sqlalchemy.orm import Session
from app.models.bill import Bill, BillStatus
from app.schemas.bill import BillCreate, BillUpdate

class BillService:
    def __init__(self, db: Session):
        self.db = db

    def create_bill(self, bill_data: BillCreate):
        new_bill = Bill(**bill_data.model_dump())
        self.db.add(new_bill)
        self.db.commit()
        self.db.refresh(new_bill)
        return new_bill

    def get_bill(self, bill_id: int):
        return self.db.query(Bill).filter(Bill.id == bill_id).first()

    def update_bill(self, bill_id: int, bill_update: BillUpdate):
        bill = self.db.query(Bill).filter(Bill.id == bill_id).first()
        if bill:
            bill.status = bill_update.status
            bill.paid_date = bill_update.paid_date
            self.db.commit()
            self.db.refresh(bill)
        return bill

    def delete_bill(self, bill_id: int):
        bill = self.db.query(Bill).filter(Bill.id == bill_id).first()
        if bill:
            self.db.delete(bill)
            self.db.commit()
        return bill