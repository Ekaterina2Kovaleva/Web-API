from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

import crud.models.reviews as crud
from api.sockets import notify_clients
from database import get_db
from schemas.reviews import ReviewSchema, ReviewSchemaCreate, ReviewSchemaUpdate

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/", response_model=ReviewSchema)
async def create_review(review_schema: ReviewSchemaCreate, db: Session = Depends(get_db)):
    review = crud.create_review(db=db, schema=review_schema)
    await notify_clients(f"Создан Отзыв '(ID: {review.id})' для рецепта '(ID: {review.recipe_id})'")
    return review


@router.get("/", response_model=List[ReviewSchema])
async def read_reviews(db: Session = Depends(get_db)):
    review = crud.read_reviews(db=db)
    return review


@router.get("/", response_model=ReviewSchema)
async def read_review(review_id: int, db: Session = Depends(get_db)):
    try:
        review = crud.read_review(db=db, review_id=review_id)
        return review
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Review not found")


@router.patch("/", response_model=ReviewSchema)
async def update_review(review_id: int, review_schema: ReviewSchemaUpdate, db: Session = Depends(get_db)):
    try:
        review = crud.update_review(db=db, review_id=review_id, schema=review_schema)
        await notify_clients(f"Обновлён Отзыв '(ID: {review.id})' для рецепта '(ID: {review.recipe_id}'")
        return review
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Review not found")


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    try:
        review = crud.delete_review(db=db, review_id=review_id)
        await notify_clients(f"Удалён Отзыв '(ID: {review_id})'")
        return review
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Review not found")
