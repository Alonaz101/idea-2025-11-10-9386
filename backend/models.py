# SCRUM-224: Data Models
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique user identifier")
    anonymous: bool = Field(default=True, description="Flag for anonymous user")

class Mood(BaseModel):
    id: int
    label: str
    description: Optional[str] = None

class Recipe(BaseModel):
    id: int
    name: str
    mood_tags: List[str]  # list of moods associated with the recipe
    ingredients: List[str]
    instructions: str

class Feedback(BaseModel):
    id: int
    user_id: Optional[int]
    recipe_id: int
    rating: Optional[int] = Field(default=None, description="User rating 1-5")
    comments: Optional[str] = Field(default=None)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
