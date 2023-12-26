import crud.base as crud
from sqlalchemy.orm import Session
from models import RecipeCategory
from schemas.recipe_categories import RecipeCategorySchemaCreate, RecipeCategorySchemaUpdate


def create_recipe_category(db: Session, schema: RecipeCategorySchemaCreate):
    return crud.create_object(db=db, model=RecipeCategory, schema=schema)


def read_recipe_category(db: Session, **kwargs):
    return crud.get_object(db=db, model=RecipeCategory, **kwargs)


def read_recipe_category_by_id(db: Session, recipe_category_id: int):
    return crud.get_object_by_id(db=db, model=RecipeCategory, obj_id=recipe_category_id)


def read_recipe_categories(db: Session, offset: int = 0, limit: int = None, **kwargs):
    return crud.get_all_objects(db=db, model=RecipeCategory, offset=offset, limit=limit, **kwargs)


def update_recipe_category(db: Session, recipe_category_id: int, schema: RecipeCategorySchemaUpdate):
    return crud.update_object(db=db, obj_id=recipe_category_id, model=RecipeCategory, schema=schema)


def delete_recipe_category(db: Session, recipe_category_id: int):
    return crud.delete_object(db=db, obj_id=recipe_category_id, model=RecipeCategory)


def delete_allrecipe_categories(db: Session):
    return crud.delete_all_objects(db=db, model=RecipeCategory)
