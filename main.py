from dotenv import load_dotenv
from agents import meal_planner, grocery_agent, event_planner, wellness_agent

load_dotenv()

# Simulate running each agent
context = meal_planner.ask_meal_context()
meals = meal_planner.suggest_meals(**context)
print("Meal suggestions:", meals)

items = grocery_agent.create_grocery_list(meals)
print("Grocery List:", items)
print(grocery_agent.order_for_pickup())

schedule = event_planner.get_kid_schedule()
logistics = event_planner.determine_logistics()
print("Afterschool Schedule:", schedule)
print("Logistics Plan:", logistics)

print(wellness_agent.send_affirmation())
print(wellness_agent.suggest_recharge_activity())
