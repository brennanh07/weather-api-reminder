from weather_api import WeatherAPI
from weather_data import WeatherData
from email_notifier import EmailNotifier
import schedule
import time

api_key = "5e33a117fe4f4e60be215515242106"
base_url = "https://api.weatherapi.com/v1"

email_username = "<EMAIL>"
email_password = "<PASSWORD>"

smtp_server = "smtp.gmail.com"
smtp_port = 587


def job():
    weather_api = WeatherAPI(api_key, base_url)
    current_weather = weather_api.get_current_weather()
    forecast = weather_api.get_forecast()
    email_notifier = EmailNotifier(smtp_server, smtp_port, email_username, email_password)

    current_summary = WeatherData(current_weather).current_summary()
    forecast_summary = WeatherData(forecast).forecast_summary()

    email_notifier.send_email("<EMAIL>", "Weather Today", current_summary + "\n" + forecast_summary)


schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


