class WeatherData:
    def __init__(self, weather):
        self.weather = weather

    def current_summary(self):
        current_temp = self.weather["current"]["temp_f"]
        current_feelslike = self.weather["current"]["feelslike_f"]
        current_humidity = self.weather["current"]["humidity"]
        current_conditions = self.weather["current"]["condition"]["text"]
        current_uv = round(self.weather["current"]["uv"])
        current_wind = self.weather["current"]["wind_mph"]

        return (f"Current:\n"
                f"\nTemperature: {current_temp} degrees"
                f"\nFeels like: {current_feelslike} degrees"
                f"\nHumidity: {current_humidity}%"
                f"\nConditions: {current_conditions}"
                f"\nUV Index: {current_uv}"
                f"\nWind Speed: {current_wind} mph\n")

    def forecast_summary(self):
        temp_high = self.weather["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
        temp_low = self.weather["forecast"]["forecastday"][0]["day"]["mintemp_f"]
        rain_amt = self.weather["forecast"]["forecastday"][0]["day"]["totalprecip_in"]
        snow_amt = self.weather["forecast"]["forecastday"][0]["day"]["totalsnow_cm"]
        avg_humidity = self.weather["forecast"]["forecastday"][0]["day"]["avghumidity"]
        rain_chance = self.weather["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
        snow_chance = self.weather["forecast"]["forecastday"][0]["day"]["daily_chance_of_snow"]
        conditions = self.weather["forecast"]["forecastday"][0]["day"]["condition"]["text"]

        return (f"Forecast for Today:\n"
                f"\nTemperature High: {temp_high} degrees"
                f"\nTemperature Low: {temp_low} degrees"
                f"\nChance of rain: {rain_chance}%"
                f"\nRain Amount: {rain_amt} in"
                f"\nHumidity: {avg_humidity}%"
                f"\nConditions: {conditions}"
                f"\nChance of snow: {snow_chance}%"
                f"\nSnow Amount: {snow_amt} cm")


