# 🚀 Multi-Agent AI System – SpaceX Launch Delay Predictor

## 🎯 Goal
"Find the next SpaceX launch, check the weather at that location, and summarize if it may be delayed."

## 🔄 System Flow
1. Planner Agent: Goal ko samajhta hai.
2. Launch Agent: Next SpaceX launch ka data lata hai.
3. Weather Agent: Launch location ka weather check karta hai.
4. Summary Agent: Sab data combine karke delay risk batata hai.

## 🔐 .env File Format
OPENWEATHER_API_KEY=your_api_key_here

## ⚙️ Setup & Run
pip install -r requirements.txt  
python driver.py

## ✅ Sample Output
🚀 Next Launch: USSF-44  
📍 Location: Cape Canaveral  
🌦 Weather: Clear  
🌡 Temperature: 27.1°C  
💨 Wind Speed: 2.57 m/s  
⚠️ Delay Risk: No

👨‍💻 Made by: Khizzer ul Islam
