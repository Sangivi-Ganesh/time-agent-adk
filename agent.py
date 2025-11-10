from google.adk.agents.llm_agent import Agent
from datetime import datetime
import pytz

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    city_timezone_map = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "paris": "Europe/Paris",
        "tokyo": "Asia/Tokyo",
        "mumbai": "Asia/Kolkata",
        "delhi": "Asia/Kolkata",
        "sydney": "Australia/Sydney",
        "los angeles": "America/Los_Angeles"
    }

    timezone_name = city_timezone_map.get(city.lower())
    if not timezone_name:
        return {"status": "error", "message": f"Unknown city: {city}"}

    tz = pytz.timezone(timezone_name)
    current_time = datetime.now(tz).strftime("%I:%M %p")

    return {"status": "success", "city": city, "time": current_time}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='time_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)

print("✅ Time Agent created successfully!")
