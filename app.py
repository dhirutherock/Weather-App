from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your WeatherAPI key
API_KEY = "c6108ad077a04ac880061306250603"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=yes"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "Unable to fetch weather data."}
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)