import requests
import datetime

API_KEY = "YOUR_API_KEY"  # Get from https://openweathermap.org/api
BASE_URL = "https://api.openweathermap.org/data/2.5/"

HISTORY_FILE = "weather_history.txt"

def save_to_history(city, data):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{datetime.datetime.now()} - {city} - {data}\n")

def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15, 2)

def kelvin_to_fahrenheit(temp_k):
    return round((temp_k - 273.15) * 9/5 + 32, 2)

def get_weather(city, unit="C"):
    try:
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print(" City not found. Please try again.")
            return

        temp_k = data["main"]["temp"]
        if unit.upper() == "C":
            temp = f"{kelvin_to_celsius(temp_k)}°C"
        else:
            temp = f"{kelvin_to_fahrenheit(temp_k)}°F"

        weather_condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        result = (f"Temperature: {temp}\n"
                  f"Condition: {weather_condition}\n"
                  f"Wind Speed: {wind_speed} m/s\n"
                  f"Sunrise: {sunrise.strftime('%I:%M %p')}\n"
                  f"Sunset: {sunset.strftime('%I:%M %p')}")

        print(f"\n Weather in {city.title()}:\n{result}")
        save_to_history(city, result)

    except Exception as e:
        print(" Error fetching weather data:", e)

def get_forecast(city, unit="C"):
    try:
        url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "200":
            print(" City not found for forecast.")
            return

        print(f"\n 5-Day Forecast for {city.title()}:\n")
        for entry in data["list"]:
            date_time = datetime.datetime.fromtimestamp(entry["dt"])
            temp_k = entry["main"]["temp"]
            if unit.upper() == "C":
                temp = f"{kelvin_to_celsius(temp_k)}°C"
            else:
                temp = f"{kelvin_to_fahrenheit(temp_k)}°F"
            description = entry["weather"][0]["description"].title()
            print(f"{date_time.strftime('%Y-%m-%d %H:%M')} | {temp} | {description}")

    except Exception as e:
        print(" Error fetching forecast data:", e)

def main():
    while True:
        print("\n--- WeatherCLI Menu ---")
        print("1. Current Weather")
        print("2. 5-Day Forecast")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice in ["1", "2"]:
            city = input("Enter city name: ")
            unit = input("Choose temperature unit (C/F): ").upper()

            if choice == "1":
                get_weather(city, unit)
            elif choice == "2":
                get_forecast(city, unit)

        elif choice == "3":
            print(" Exiting WeatherCLI. Stay updated!")
            break
        else:
            print(" Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
