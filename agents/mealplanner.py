from openai_agentic import tool

@tool
def ask_meal_context():
    return {
        "cuisine": "Indian",  # Simulate user response
        "cook_time": "30 minutes",
        "cleanup": "Minimal",
    }

@tool
def suggest_meals(cuisine: str, cook_time: str, cleanup: str):
    return [
        f"{cuisine} Lentil Soup (20 min, 1 pot)",
        f"{cuisine} Paneer Wraps (30 min, quick cleanup)"
    ]
