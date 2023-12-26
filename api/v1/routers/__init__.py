from fastapi import APIRouter

from api.v1.routers.reviews import router as reviews_router
from api.v1.routers.recipes import router as recipes_router
from api.v1.routers.recipe_categories import router as recipe_categories_router
from api.v1.routers.ingredients import router as ingredients_router

router = APIRouter(prefix='/v1')

router.include_router(recipe_categories_router)
router.include_router(recipes_router)
router.include_router(ingredients_router)
router.include_router(reviews_router)
