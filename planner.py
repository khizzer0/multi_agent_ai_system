from agents.launch_agent import get_next_launch
from agents.weather_agent import get_weather
from agents.summary_agent import generate_summary

def plan_and_execute(goal):
    launch = get_next_launch()
    weather = get_weather(launch["lat"], launch["lon"], launch["city"])
    return generate_summary(launch, weather)
