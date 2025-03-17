from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# OpenWeatherMap API key
API_KEY = "567a1e126c0a4beeb6484313251603"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather")
def get_weather(city: str):
    """
    Fetch weather data for a given city.
    """
    if not city:
        raise HTTPException(status_code=400, detail="City name is required")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(WEATHER_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")

    weather_data = response.json()
    return {
        "city": weather_data["name"],
        "country": weather_data["sys"]["country"],
        "temperature": weather_data["main"]["temp"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
        "description": weather_data["weather"][0]["description"]
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather App! Use /weather?city=<city_name> to get weather data."}