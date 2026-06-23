# Basic Weather App

## Overview

The Basic Weather App is a simple Python program that fetches real-time weather information for a specified city using the OpenWeatherMap API. It displays key weather details such as temperature, humidity, wind speed, and weather conditions, along with a basic weather advisory.

## Features

* Fetches real-time weather data for any city.
* Displays current temperature in Celsius.
* Shows humidity and wind speed.
* Provides a weather condition description.
* Gives simple weather-based advice.
* Handles invalid city names and API errors gracefully.
* Easy-to-use command-line interface.

## Technologies Used

* Python
* Requests Library
* OpenWeatherMap API
* Datetime Module

## How It Works

1. Enter the name of a city.
2. The program sends a request to the OpenWeatherMap API.
3. Weather data is retrieved and processed.
4. The program displays:

   * Date
   * City Name
   * Temperature
   * Humidity
   * Wind Speed
   * Weather Condition
5. A weather advisory is shown based on the current temperature.

## Weather Advisory Logic

* Temperature above 30°C → "It's quite hot today!"
* Temperature below 15°C → "It's a cold day!"
* Temperature between 15°C and 30°C → "Weather is pleasant today!"

=======

OIBSIP

Python projects completed during the Oasis Infobyte Internship Program.
