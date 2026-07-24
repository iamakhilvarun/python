import requests
from plyer import notification

# Rich imports
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.status import Status

console = Console()

# ----------------------------------------------------
# coordinates of the city
# ----------------------------------------------------

console.print(
    Panel.fit(
        "[bold cyan]☁️ Weather Notification App[/bold cyan]",
        border_style="cyan",
    )
)

city = Prompt.ask("[bold green]Enter your city[/bold green]").lower()

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_parameter = {"name": city, "count": 1}

with console.status("[bold yellow]Searching city coordinates...[/bold yellow]"):
    geo_res = requests.get(geo_url, params=geo_parameter).json()

# ----------------------------------------------------
# fetching the current data
# ----------------------------------------------------

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "longitude": lon,
        "latitude": lat,
        "current_weather": True,
    }

    with console.status("[bold yellow]Fetching weather data...[/bold yellow]"):
        weather_res = requests.get(
            weather_url,
            params=weather_params
        ).json()

    if "current_weather" in weather_res:

        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]

        weather_info = (
            f"{city}: Temp: {temp} °C , windspeed: {wind} km/h"
        )

        # ----------------------------
        # Beautiful Output
        # ----------------------------

        table = Table(
            title="🌍 Current Weather",
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column("City", justify="center")
        table.add_column("Temperature", justify="center")
        table.add_column("Wind Speed", justify="center")

        table.add_row(
            city.title(),
            f"{temp} °C",
            f"{wind} km/h",
        )

        console.print()
        console.print(table)
        console.print()

        console.print(
            Panel.fit(
                f"[bold green]✅ Weather fetched successfully![/bold green]\n\n"
                f"[white]{weather_info}[/white]",
                title="Result",
                border_style="green",
            )
        )

        notification.notify(
            title="Weather App",
            message=weather_info,
            timeout=5,
        )

    else:
        console.print(
            Panel.fit(
                "[bold red]Weather data not found!![/bold red]",
                border_style="red",
            )
        )

else:
    console.print(
        Panel.fit(
            "[bold red]City not found!![/bold red]",
            border_style="red",
        )
    )
