from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RecipeCategorySchemaBase(BaseModel):
    name: str


class RecipeCategorySchemaCreate(RecipeCategorySchemaBase):
    pass


class RecipeCategorySchemaUpdate(RecipeCategorySchemaBase):
    name: Optional[str] = None


class RecipeCategorySchema(RecipeCategorySchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
