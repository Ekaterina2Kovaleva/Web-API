from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RecipeSchemaBase(BaseModel):
    title: str
    description: Optional[str] = None
    instruction: Optional[str] = None
    category_id: int


class RecipeSchemaCreate(RecipeSchemaBase):
    pass


class RecipeSchemaUpdate(RecipeSchemaBase):
    title: Optional[str] = None
    description: Optional[str] = None
    instruction: Optional[str] = None
    category_id: Optional[int] = None


class RecipeSchema(RecipeSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
