# City Data Reporter.
# This program gets weather data and saves it to a CSV file.
import csv
import json
import os

import requests

# Get a non-empty city name from the user.
def get_city_name():
    """Ask the user for a city and prevent empy input"""
    while True:
        city = input("Enter a city name: ")

        if city:
            return city

        print("City name cannot be empty. Please try again")

# Get the weather data from the OpenWeatherMap API.
def get_weather_data(city, api_key):
    """Request and process current weather data for a city"""
    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=parameters, timeout=10)

        if response.status_code == 404:
            print("City not found. Please check the city name")
            return None

        if response.status_code == 401:
            print("he API key is invalid or not active yet.")
            return None

        response.raise_for_status()

        data = json.loads(response.text)

        weather_data = {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Temperature (C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Description": data["weather"][0]["description"]
        }
        return weather_data

    except requests.exceptions.Timeout:
        print("The request took to long. Please try again")
    except requests.exceptions.ConnectionError:
        print("Unable to connect. Please check your internet connection")
    except requests.exceptions.RequestException as error:
        print(f"API request error: {error}")
    except (json.JSONDecodeError, KeyError, IndexError):
        print ("The weather data could not be processed.")

    return None

# Display the weather information in the terminal.
def print_weather_report(weather_data):
    """Display a formatted weather report."""
    print("\nCity Weather Report")
    print(f"CIty: {weather_data['City']}")
    print(f"Country: {weather_data['Country']}")
    print(f"Temperature: {weather_data['Temperature (C)']:.1f} C")
    print(f"Humidity: {weather_data['Humidity (%)']}%")
    print(f"Description: {weather_data['Description']}")

# Save weather data and add headers if the CSV file is new.
def save_to_csv(weather_data):
    """Append weather data to a CSV file with column headers."""
    filename = "city_data.csv"
    
    headers = [
        "City",
        "Country",
        "Temperature (C)",
        "Humidity (%)",
        "Description"
    ]

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            #Add headers only when the file is empty
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(weather_data)

        print ("\nWeather data saved to city_data.csv.")
        return True

    except OSError:
        print ("Unable to save the CSV file.")
        return False

# Read the CSV file and display saved cities and temperatures.
def read_csv_report():
    """Read saved city data and display names and temperatures."""
    try:
        with open("city_data.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            cities = list(reader)

        print(f"\nCities saved in the file: {len(cities)}")

        for city in cities:
            print(f"{city['City']}: {city['Temperature (C)']} C")

    except FileNotFoundError:
        print("The CSV filr does not exist yet.")
    except OSError:
        print("Unable to read the CSV file.")

# Run the complete city weather reporter.
def main():
    """run the city weather reporter."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY enviroment variable")
        return
    
    city = get_city_name()
    weather_data = get_weather_data(city, api_key)
    
    if weather_data is None:
        return

    print_weather_report(weather_data)

    if save_to_csv(weather_data):
        read_csv_report()

# Start te program when its file is run directly.
if __name__ == "__main__":
    main()