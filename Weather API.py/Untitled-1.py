import requests

# API key for accessing the OpenWeatherMap API
API_KEY = "d9653eaee22cc2b0e4fabcb43b6d3275"

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# User input for the city name
city = input("Enter a city name: ")

# Constructing the request URL with the API key and city name
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# Sending a GET request to the OpenWeatherMap API with the constructed URL
response = requests.get(request_url)

# Checking if the response status code is 200 (OK)
if response.status_code == 200:
    # Parsing the response JSON data
    data = response.json()
    
    # Retrieving weather description from the response
    weather = data['weather'][0]['description']
    
    # Calculating temperature in Celsius from Kelvin and rounding to two decimal places
    temperature = round(data["main"]["temp"] - 273.15, 2)
    
    # Printing weather information
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")

else:
    # Handling errors if the response status code is not 200
    print("An error occurred.")
