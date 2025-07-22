from openai_agentic import tool

@tool
def create_grocery_list(meals: list[str]):
    return ["Paneer", "Tortilla", "Spinach", "Curry Powder"]

@tool
def order_for_pickup(store="Fred Meyer"):
    return f"Order sent to {store} for curbside pickup."
