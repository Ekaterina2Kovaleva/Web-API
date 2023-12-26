from typing import List
    
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

import crud.models.recipe_categories as crud
from api.sockets import notify_clients
from database import get_db
from schemas.recipe_categories import RecipeCategorySchema, RecipeCategorySchemaCreate, RecipeCategorySchemaUpdate

router = APIRouter(prefix="/recipe_categories", tags=["recipe_categories"])


@router.post("/", response_model=RecipeCategorySchema)
async def create_recipe_category(recipe_category_schema: RecipeCategorySchemaCreate, db: Session = Depends(get_db)):
    recipe_category = crud.create_recipe_category(db=db, schema=recipe_category_schema)
    await notify_clients(f"Создана Категория Рецептов (ID: {recipe_category.id})")
    return recipe_category


@router.get("/", response_model=List[RecipeCategorySchema])
async def read_recipe_categories(db: Session = Depends(get_db)):
    recipe_category = crud.read_recipe_categories(db=db)
    return recipe_category


@router.get("/", response_model=RecipeCategorySchema)
async def read_recipe_category(recipe_category_id: int, db: Session = Depends(get_db)):
    try:
        recipe_category = crud.read_recipe_category(db=db, recipe_category_id=recipe_category_id)
        return recipe_category
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe_Category not found")


@router.patch("/", response_model=RecipeCategorySchema)
async def update_recipe_category(recipe_category_id: int, recipe_category_schema: RecipeCategorySchemaUpdate, db: Session = Depends(get_db)):
    try:
        recipe_category = crud.update_recipe_category(db=db, recipe_category_id=recipe_category_id, schema=recipe_category_schema)
        await notify_clients(f"Обновлена Категория Рецептов (ID: {recipe_category.id})")
        return recipe_category
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe_Category not found")


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_recipe_category(recipe_category_id: int, db: Session = Depends(get_db)):
    try:
        recipe_category = crud.delete_recipe_category(db=db, recipe_category_id=recipe_category_id)
        await notify_clients(f"Удалёна Категория Рецептов '(ID: {recipe_category_id})'")
        return recipe_category
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Recipe_Category not found")

