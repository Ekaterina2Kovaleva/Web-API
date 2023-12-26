import crud.base as crud
from sqlalchemy.orm import Session
from models import Review
from schemas.reviews import ReviewSchemaCreate, ReviewSchemaUpdate


def create_review(db: Session, schema: ReviewSchemaCreate):
    return crud.create_object(db=db, model=Review, schema=schema)


def read_review(db: Session, **kwargs):
    return crud.get_object(db=db, model=Review, **kwargs)


def read_review_by_id(db: Session, review_id: int):
    return crud.get_object_by_id(db=db, model=Review, obj_id=review_id)


def read_reviews(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Review, offset=offset, limit=limit, **kwargs)


def update_review(db: Session, review_id: int, schema: ReviewSchemaUpdate):
    return crud.update_object(db=db, obj_id=review_id, model=Review, schema=schema)


def delete_review(db: Session, review_id: int):
    return crud.delete_object(db=db, obj_id=review_id, model=Review)


def delete_all_reviews(db: Session):
    return crud.delete_all_objects(db=db, model=Review)
