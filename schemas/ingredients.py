from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class IngredientSchemaBase(BaseModel):
    name: str
    quantity: Optional[str] = None
    recipe_id: int


class IngredientSchemaCreate(IngredientSchemaBase):
    pass


class IngredientSchemaUpdate(IngredientSchemaBase):
    name: Optional[str] = None
    quantity: Optional[str] = None
    recipe_id: Optional[int] = None


class IngredientSchema(IngredientSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
