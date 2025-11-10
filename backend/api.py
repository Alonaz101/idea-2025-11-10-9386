# SCRUM-225: REST API specifications implementation using FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class MoodSubmission(BaseModel):
    user_id: Optional[int]
    mood_label: str

class FeedbackSubmission(BaseModel):
    user_id: Optional[int]
    recipe_id: int
    rating: Optional[int] = None
    comments: Optional[str] = None

# Dummy data store for recipes
recipes_db = {
    1: {"id": 1, "name": "Comfort Soup", "mood_tags": ["happy", "relaxed"], "ingredients": ["water", "vegetables"], "instructions": "Cook soup..."}
}

@app.post("/api/mood")
def submit_mood(mood: MoodSubmission):
    # For MVP, we just log and respond with a simple message
    return {"message": f"Mood '{mood.mood_label}' received for user {mood.user_id}"}

@app.get("/api/recipes/{id}")
def get_recipe(id: int):
    recipe = recipes_db.get(id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.post("/api/feedback")
def submit_feedback(feedback: FeedbackSubmission):
    # For MVP, we simply acknowledge feedback receipt
    return {"message": "Feedback received", "details": feedback.dict()}
