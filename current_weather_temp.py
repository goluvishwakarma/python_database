import requests

"""
    requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, 
    form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response
     data of Python in the same way."""
"""
    requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of 
    making requests behind a beautiful, simple API so that you can focus on interacting with services and 
    consuming data in your application."""

""" a module is a collection of code or functions that uses the . py extension. A Python library is a set of related
    modules or packages bundled together."""


def get_curr_weather_details():
    api = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=7b249235cf6be2334a7582c5d8906c25"
    api_data = requests.get(api).json()
    print(api_data)

    print("Temperature: ", round((api_data['main']['temp'] - 273.15), 4), "°C")
    print("Pressure: ", api_data['main']['pressure'], "hPa")
    print("Humidity: ", api_data['main']['humidity'], "%")
    print("Wind Speed: ", api_data['wind']['speed'], "m/s")
    print("Weather Description: ", api_data['weather'][0]['description'])


get_curr_weather_details()

"""
    JSON is an open standard file format and data interchange format that uses human-readable text to store 
    and transmit data objects consisting of attribute–value pairs and arrays. 
    
    JSON stands for JavaScript Object Notation

    JSON is a lightweight format for storing and transporting data

    JSON is often used when data is sent from a server to a web page

    JSON is "self-describing" and easy to understand.         
      
    hpa = Hectopascal is a 100x multiple of the Pascal which is the SI unit for pressure.  """