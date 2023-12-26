from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ReviewSchemaBase(BaseModel):
    rating: int = Field(..., ge=0, le=10)
    comment: Optional[str] = None
    recipe_id: int


class ReviewSchemaCreate(ReviewSchemaBase):
    pass


class ReviewSchemaUpdate(ReviewSchemaBase):
    rating: int = Field(None, ge=0, le=10)
    comment: Optional[str] = None
    recipe_id: Optional[int] = None


class ReviewSchema(ReviewSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
