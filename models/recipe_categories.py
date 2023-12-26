from datetime import datetime, date
from typing import List

from sqlalchemy import Integer, DateTime, func, ForeignKey, Date, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class RecipeCategory(Base):
    __tablename__ = "recipe_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)

    recipes: Mapped[List["Recipe"]] = relationship(back_populates="category")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
