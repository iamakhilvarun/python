if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url="https://api.open-meteo.com/v1/forecast"
    weather_params={
        "longitude":lon,
        "latitude":lat,
    }