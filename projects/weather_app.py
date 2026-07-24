import requests
from plyer import notification

# coordinates of the city
city = input("Enter your city: ")
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_parameter = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_parameter).json()

# fetching the current data
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url="https://api.open-meteo.com/v1/forecast"
    weather_params={
        "longitude":lon,
        "latitude":lat,
        "current_weather":True
    }
    weather_res=requests.get(weather_url,params=weather_params).json()
    print(weather_res)
    if "current_weather" in weather_res:
        temp=weather_res["current_weather"]["temperature"]
        wind=weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: Temp: {temp} °C ,windpeed: {wind} km/h"

        notification.notify(
            title="Weather app",
            message=weather_info,
            timeout=5
        )
    else:
        print("Weather data not found!!")

else:
    print("City not found!!")