from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = "567a1e126c0a4beeb6484313251603"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = {}
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"  # Use "imperial" for Fahrenheit
            }
            response = requests.get(WEATHER_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Ensure the port is correct