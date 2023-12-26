from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

import crud.models.ingredients as crud
from api.sockets import notify_clients
from database import get_db
from schemas.ingredients import IngredientSchema, IngredientSchemaCreate, IngredientSchemaUpdate

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.post("/", response_model=IngredientSchema)
async def create_ingredient(ingredient_schema: IngredientSchemaCreate, db: Session = Depends(get_db)):
    ingredient = crud.create_ingredient(db=db, schema=ingredient_schema)
    await notify_clients(f"Создан Ингредиент '{ingredient.name} | Кол-во: {ingredient.quantity}"
                         f" для рецепта '{ingredient.recipe.title} (ID: {ingredient.recipe.id})'")
    return ingredient


@router.get("/", response_model=List[IngredientSchema])
async def read_ingredients(db: Session = Depends(get_db)):
    ingredient = crud.read_ingredients(db=db)
    return ingredient


@router.get("/", response_model=IngredientSchema)
async def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    try:
        ingredient = crud.read_ingredient(db=db, ingredient_id=ingredient_id)
        return ingredient
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ingredient not found")


@router.patch("/", response_model=IngredientSchema)
async def update_ingredient(ingredient_id: int, ingredient_schema: IngredientSchemaUpdate, db: Session = Depends(get_db)):
    try:
        ingredient = crud.update_ingredient(db=db, ingredient_id=ingredient_id, schema=ingredient_schema)
        await notify_clients(f"Обновлён Ингредиент '{ingredient.name} | Кол-во: {ingredient.quantity}"
                             f" для рецепта '{ingredient.recipe.title} (ID: {ingredient.recipe.id})'")
        return ingredient
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ingredient not found")


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
   try:
       ingredient = crud.delete_ingredient(db=db, ingredient_id=ingredient_id)
       await notify_clients(f"Удалён Ингредиент '(ID: {ingredient_id})'")
       return ingredient
   except NoResultFound:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail="Ingredient not found")
