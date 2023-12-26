import crud.base as crud
from sqlalchemy.orm import Session
from models import Ingredient
from schemas.ingredients import IngredientSchemaCreate, IngredientSchemaUpdate


def create_ingredient(db: Session, schema: IngredientSchemaCreate):
    return crud.create_object(db=db, model=Ingredient, schema=schema)


def read_ingredient(db: Session, **kwargs):
    return crud.get_object(db=db, model=Ingredient, **kwargs)


def read_ingredient_by_id(db: Session, ingredient_id: int):
    return crud.get_object_by_id(db=db, model=Ingredient, obj_id=ingredient_id)


def read_ingredients(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Ingredient, offset=offset, limit=limit, **kwargs)


def update_ingredient(db: Session, ingredient_id: int, schema: IngredientSchemaUpdate):
    return crud.update_object(db=db, obj_id=ingredient_id, model=Ingredient, schema=schema)


def delete_ingredient(db: Session, ingredient_id: int):
    return crud.delete_object(db=db, obj_id=ingredient_id, model=Ingredient)


def delete_all_ingredients(db: Session):
    return crud.delete_all_objects(db=db, model=Ingredient)
