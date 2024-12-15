import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city_name):
        """Fetch weather data for a given city."""
        params = {"q": city_name, "appid": self.api_key, "units": "metric"}
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
            }
        except requests.exceptions.RequestException as e:
            return f"Error: Unable to fetch weather data. {e}"
