import requests

API_KEY = "your_api_key_here"   # Get from https://openweathermap.org/

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res["cod"] == 200:
        temp = res["main"]["temp"]
        humidity = res["main"]["humidity"]
        condition = res["weather"][0]["description"]
        return f"🌤 Weather in {city}: {temp}°C, {humidity}% humidity, {condition}"
    else:
        return "❌ City not found!"

print("🤖 AI Chatbot with Weather Tracking (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello"]:
        print("Bot: Hello! 😊")
    elif "weather" in user:
        city = input("Bot: Enter city name: ")
        print("Bot:", get_weather(city))
    elif "bye" in user:
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: I can tell you the weather. Try: weather in Delhi")
