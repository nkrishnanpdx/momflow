from openai_agentic import tool

@tool
def check_energy_level():
    return "low"

@tool
def send_affirmation():
    return "You’ve got this! Even small steps matter. ❤️"

@tool
def suggest_recharge_activity():
    return "How about a 10-min walk or a short breathing exercise?"
