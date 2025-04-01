from sqlalchemy.orm import Session
from app.models.reviews import Review
from app.schemas.reviews import ReviewCreate, ReviewUpdate

class ReviewService:
    def __init__(self, db: Session):
        self.db = db

    def create_review(self, data: ReviewCreate):
        new_review = Review(**data.model_dump())
        self.db.add(new_review)
        self.db.commit()
        self.db.refresh(new_review)
        return new_review

    def get_review(self, review_id: int):
        return self.db.query(Review).filter(Review.id == review_id).first()

    def update_review(self, review_id: int, data: ReviewUpdate):
        review = self.db.query(Review).filter(Review.id == review_id).first()
        if review:
            for field, value in data.dict(exclude_unset=True).items():
                setattr(review, field, value)
            self.db.commit()
            self.db.refresh(review)
        return review

    def delete_review(self, review_id: int):
        review = self.db.query(Review).filter(Review.id == review_id).first()
        if review:
            self.db.delete(review)
            self.db.commit()
        return review
