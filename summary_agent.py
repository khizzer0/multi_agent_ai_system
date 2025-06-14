def generate_summary(launch_data, weather_data):
    if "error" in launch_data:
        return "Launch data fetch failed."

    if "error" in weather_data:
        return "Weather data fetch failed."

    name = launch_data.get("name")
    date = launch_data.get("date")
    location = launch_data.get("location")

    weather = weather_data.get("weather")
    temp = weather_data.get("temperature")
    wind = weather_data.get("wind_speed")

    delay_risk = "No" if weather in ["Clear", "Clouds"] and wind < 10 else "Possible"

    return f"""
🚀 Next Launch: {name}
📅 Date (UTC): {date}
📍 Location: {location}

🌦 Weather: {weather}
🌡 Temperature: {temp}°C
💨 Wind Speed: {wind} m/s

⚠️ Delay Risk: {delay_risk}
"""
