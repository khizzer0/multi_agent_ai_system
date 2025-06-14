import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(lat, lon, fallback_city=None):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print("📡 STEP 1: API KEY:", api_key)

    if not api_key:
        return {"error": "API key missing in .env"}

    print("📍 STEP 2: Coordinates:", lat, lon)
    print("🏙️ STEP 3: City:", fallback_city)

    # First try with lat/lon
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    print("🌐 STEP 4: URL Used:", url)
    response = requests.get(url)

    print("🔄 STEP 5: Response Code:", response.status_code)

    if response.status_code != 200 and fallback_city:
        print("⚠️ STEP 6: Lat/Lon failed, trying with city fallback")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={fallback_city}&appid={api_key}&units=metric"
        print("🌐 STEP 7: Fallback URL:", url)
        response = requests.get(url)

    print("🔚 STEP 8: Final Response Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("✅ STEP 9: Weather Data:", data)
        return {
            "weather": data["weather"][0]["main"],
            "temperature": data["main"]["temp"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        print("❌ STEP 10: Weather fetch failed:", response.status_code, response.text)
        return {"error": f"Weather fetch failed: {response.status_code}"}
