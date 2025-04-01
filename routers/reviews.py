from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reviews import ReviewCreate, ReviewResponse, ReviewUpdate
from app.services.reviews import ReviewService
from app.database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=ReviewResponse)
def create(data: ReviewCreate, db: Session = Depends(get_db)):
    service = ReviewService(db)
    return service.create_review(data)

@router.get("/{review_id}", response_model=ReviewResponse)
def read(review_id: int, db: Session = Depends(get_db)):
    service = ReviewService(db)
    review = service.get_review(review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/{review_id}", response_model=ReviewResponse)
def update(review_id: int, data: ReviewUpdate, db: Session = Depends(get_db)):
    service = ReviewService(db)
    review = service.update_review(review_id, data)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.delete("/{review_id}", response_model=ReviewResponse)
def delete(review_id: int, db: Session = Depends(get_db)):
    service = ReviewService(db)
    review = service.delete_review(review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
