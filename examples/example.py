from src.weather import WeatherApp

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"

def main():
    app = WeatherApp(API_KEY)
    city = input("Enter city name: ")
    weather = app.fetch_weather(city)
    if isinstance(weather, dict):
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
    else:
        print(weather)

if __name__ == "__main__":
    main()
