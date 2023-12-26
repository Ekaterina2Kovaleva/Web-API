from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, index=True, nullable=True)
    instruction: Mapped[str] = mapped_column(String, index=True, nullable=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipe_categories.id", ondelete="CASCADE"))

    # Relationships
    category: Mapped[List["RecipeCategory"]] = relationship(back_populates="recipes", lazy="selectin")
    ingredients: Mapped[List["Ingredient"]] = relationship(back_populates="recipe", lazy="selectin")
    reviews: Mapped[List["Review"]] = relationship(back_populates="recipe", lazy="selectin")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())