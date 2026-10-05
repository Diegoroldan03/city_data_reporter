# City Data Reporter

This Python program asks for a city name and gets current weather data from OpenWeatherMap. It displays the city, country code, temperature in Celsius, humidity, and weather description.

The program saves each successful result to city_data.csv. It then reads the file, displays the number of saved records, and lists their cities and temperatures. Repeated searches for the same city create separate records.

## Requirements

You need Python 3, an internet connection, and an OpenWeatherMap API key.

Install the requests library:
```powershell
python -m pip install requests
```

The other modules used in this project, json, csv, and os, are included with Python.

## API Key Setup

Create a free account on the OpenWeatherMap website. After signing in, open the API keys section of your account and copy your key.

In the VS Code PowerShell terminal, set the environment variable:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your own key. This variable is available for the current terminal session, so you need to set it again if you open a new terminal.

The program reads the key from this environment variable. Your personal API key should not be added to the code or uploaded to GitHub.

## How to Run

Open the project folder in VS Code and run this command in the same terminal where you set the API key:

```powershell
python reporter.py
```

Enter a city name when prompted. You can also include a country code, such as Caracas,VE.

Empty input is rejected, and the program asks again. If the city cannot be found or the API request fails, it displays an error message.

After a successful search, the program prints the weather report, adds the data to city_data.csv, and displays a summary of the saved records.

## Project Files

`reporter.py` contains the program.

`city_data.csv` stores the weather results and is created automatically after a successful search.

`README.md` explains the project and how to run it.

## Video Demonstration

Watch the video demonstratio here: https://youtu.be/D-Q5JVeRCrE
