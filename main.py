from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


api_key = "e2b6001b34b0303c54f1e1dc1c4d0a50"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get city and country code from the form
        city = request.form["city"]
        country_code = request.form["country_code"]

        # Make a GET request to the OpenWeatherMap API
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}")

        if response.status_code == 200:
            # Extract the JSON data
            data = response.json()

            # Render the template with weather data
            return render_template("weather.html", data=data, round = round)
        else:
            error_message = "Failed to fetch weather data"
            return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)





