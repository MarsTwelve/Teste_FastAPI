import requests
from datetime import datetime


class WeatherData:
    def __init__(self, latitude, longitude, forecast):
        self.latitude = latitude
        self.longitude = longitude
        self.forecast = forecast

    def get_forecast(self):
        weather_key = "0663035a8316bd463c63093370b24744"
        url = (f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}"
               f"&appid={weather_key}&units=metric")
        response = requests.get(url)
        previsao = response.json()
        return previsao

    def weather(self):
        weather = self.forecast["weather"][0]
        weather_desc = weather["description"]
        weather_icon = weather["icon"]
        image_url = f"https://openweathermap.org/img/wn/{weather_icon}@2x.png"
        weather_list = [weather_desc, image_url]
        return weather_list

    def temperature(self):
        temp = self.forecast["main"]["temp"]
        humidity = self.forecast["main"]["humidity"]
        temp_list = [temp, humidity]
        return temp_list

    def wind(self):
        speed = self.forecast["wind"]["speed"]
        direction = self.forecast["wind"]["deg"]
        wind_list = [speed, direction]
        return wind_list

    def sun_timing(self):
        sunrise_unix = self.forecast["sys"]["sunrise"]
        sunset_unix = self.forecast["sys"]["sunset"]
        sunrise_time = datetime.fromtimestamp(sunrise_unix)
        sunset_time = datetime.fromtimestamp(sunset_unix)
        sunrise = sunrise_time.strftime("%H:%M")
        sunset = sunset_time.strftime("%H:%M")
        suntiming_list = [sunrise, sunset]
        return suntiming_list
