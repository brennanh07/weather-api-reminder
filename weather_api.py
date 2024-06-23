import requests

MY_LAT = "<LAT>"
MY_LONG = "<LON>"


class WeatherAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather(self):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={MY_LAT},{MY_LONG}"
        response = requests.get(url)
        return response.json()

    def get_forecast(self):
        url = f"{self.base_url}/forecast.json?key={self.api_key}&q={MY_LAT},{MY_LONG}"
        response = requests.get(url)
        return response.json()
