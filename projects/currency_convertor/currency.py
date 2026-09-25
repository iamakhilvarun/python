import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
Base_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "INR"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    # given the base currencies telling the api to give the rest of currency value according to the base api
    url = f"{Base_url}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        # "data" is the key and data["data"] finds the key and whatever that keys has prints it
        return data["data"]
    except:  # if not its an error
        print("INVALID CURRENCY!")
        return None


while True:
    base = input("\nEnter the base currency (q for quit):").upper()
    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}:{value}")
