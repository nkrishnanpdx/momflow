from openai_agentic import tool

@tool
def get_kid_schedule():
    return {
        "Aanya": {"event": "Piano", "time": "4PM", "location": "Studio 21"},
        "Maya": {"event": "Soccer", "time": "4:30PM", "location": "Lincoln Park"}
    }

@tool
def determine_logistics():
    return {
        "dropoffs": ["Maya - Mom", "Aanya - Dad"],
        "pickups": ["Maya - carpool with Sara", "Aanya - Mom"]
    }
