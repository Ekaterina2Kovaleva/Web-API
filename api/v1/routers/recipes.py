from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

import crud.models.recipes as crud
from api.sockets import notify_clients
from database import get_db
from schemas.recipes import RecipeSchema, RecipeSchemaCreate, RecipeSchemaUpdate

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.post("/", response_model=RecipeSchema)
async def create_recipe(recipe_schema: RecipeSchemaCreate, db: Session = Depends(get_db)):
    if crud.read_recipe(db=db, title=recipe_schema.title):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Рецепт с таким названием уже существует.")
    recipe = crud.create_recipe(db=db, schema=recipe_schema)
    await notify_clients(f"Создан Рецепт '{recipe.title} (ID: {recipe.id})'")
    return recipe


@router.get("/", response_model=List[RecipeSchema])
async def read_recipes(db: Session = Depends(get_db)):
    recipe = crud.read_recipes(db=db)
    return recipe


@router.get("/", response_model=RecipeSchema)
async def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        recipe = crud.read_recipe(db=db, recipe_id=recipe_id)
        return recipe
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe not found")


@router.patch("/", response_model=RecipeSchema)
async def update_recipe(recipe_id: int, recipe_schema: RecipeSchemaUpdate, db: Session = Depends(get_db)):
    try:
        recipe = crud.update_recipe(db=db, recipe_id=recipe_id, schema=recipe_schema)
        await notify_clients(f"Обновлён Рецепт '{recipe.title} (ID: {recipe.id})'")
        return recipe
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe not found")


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        recipe = crud.delete_recipe(db=db, recipe_id=recipe_id)
        await notify_clients(f"Удалён Рецепт '(ID: {recipe_id})'")
        return recipe
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe not found")
