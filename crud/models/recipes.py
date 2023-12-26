import crud.base as crud
from sqlalchemy.orm import Session
from models import Recipe
from schemas.recipes import RecipeSchemaCreate, RecipeSchemaUpdate


def create_recipe(db: Session, schema: RecipeSchemaCreate):
    return crud.create_object(db=db, model=Recipe, schema=schema)


def read_recipe(db: Session, **kwargs):
    return crud.get_object(db=db, model=Recipe, **kwargs)


def read_recipe_by_id(db: Session, recipe_id: int):
    return crud.get_object_by_id(db=db, model=Recipe, obj_id=recipe_id)


def read_recipes(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=Recipe, offset=offset, limit=limit, **kwargs)


def update_recipe(db: Session, recipe_id: int, schema: RecipeSchemaUpdate):
    return crud.update_object(db=db, obj_id=recipe_id, model=Recipe, schema=schema)


def delete_recipe(db: Session, recipe_id: int):
    return crud.delete_object(db=db, obj_id=recipe_id, model=Recipe)


def delete_all_recipes(db: Session):
    return crud.delete_all_objects(db=db, model=Recipe)
