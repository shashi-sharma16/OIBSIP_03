import requests
from datetime import datetime

print("-" * 40)
print("           WEATHER CHECKER")
print("-" * 40)

API_key = "82f4019b0e394747c6b9c97dfd91109d"

City = input("Enter City Name: ").strip()
Date = datetime.now().strftime("%Y-%m-%d")

url = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_key}&units=metric"

try:
    resp = requests.get(url)
    data = resp.json()

    if resp.status_code != 200:
        print("API ERROR")

    elif data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["description"]

        print("\nWeather Information")
        print("-" * 40)
        print(f"Date: {Date}")
        print(f"City : {City.title()}")
        print(f"Temperature : {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition.title()}")

        if temp > 30:
            print("ADVICE : It's quite hot today!")
        elif temp < 15:
            print("ADVICE : It's a cold day!")
        else:
            print("ADVICE : Weather is pleasant today!")
    else:
        print("City not found. Please try again.")
except:
    print("Unable to get weather data. Please try again later.")

    