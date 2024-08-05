import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
params = {"key": API_KEY, "q": "Paris"}


def get_weather() -> None:
    res = requests.get(BASE_URL, params=params)
    data = json.loads(res.text)
    print(f"{data["location"]["name"]}/{data["location"]["country"]}")
    print(f"{data["location"]["localtime"]}")
    print(f"Weather: {data["current"]["temp_c"]} Celsius, "
          f"{data["current"]["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
