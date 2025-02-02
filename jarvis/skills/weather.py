import configparser
import os
from dotenv import load_dotenv
load_dotenv() 

API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"  # Use metric units (Celsius)
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"The weather in {location} is {description} with a temperature of {temperature}°C."
    except requests.exceptions.RequestException as e:
        return f"Error getting weather information: {e}"

