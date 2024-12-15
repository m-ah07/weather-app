# Weather App

A simple Python CLI Weather App to fetch current weather information using the OpenWeatherMap API.

## Features
- Fetch current weather data for any city.
- Display temperature, humidity, and weather description.
- Easy-to-use and extendable.

## Directory Structure

weather-app/
├── src/
│   └── weather.py        # Core logic for fetching weather data
├── examples/
│   └── example.py        # Demonstration of the Weather App usage
├── .gitignore            # Git ignore file
└── README.md             # Documentation file


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/marwan-ahmed-23/weather-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-app
    ```

3. Install dependencies:

    ```bash
    pip install requests
    ```

## Usage

1. Replace `your_api_key_here` in `example.py` with your OpenWeatherMap API key.
2. Run the example script:

    ```bash
    python examples/example.py
    ```

## Example

Here’s an example of how the app works:

```bash
    Enter city name: London

    Weather in London:
    Temperature: 15°C
    Description: Clear sky
    Humidity: 68%
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

