import requests
from datetime import datetime
from Localization import Localization


class WeatherData:
    def __init__(self, latitude, longitude, forecast):
        self.latitude = latitude
        self.longitude = longitude
        self.forecast = forecast

    def get_forecast(self):
        weather_key = "0663035a8316bd463c63093370b24744"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={weather_key}&units=metric"
        response = requests.get(url)
        previsao = response.json()
        return previsao

    def weather(self):
        forecast = self.forecast
        weather = forecast["weather"][0]
        weather_desc = weather["description"]
        weather_icon = weather["icon"]
        return weather_desc, weather_icon

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
        return sunrise, sunset


# Exemplos, lembrar de deletar depoix
automatic_latlng = Localization.automatic_localization()

Class1 = WeatherData(automatic_latlng[0], automatic_latlng[1], None)
Func1 = WeatherData.get_forecast(Class1)
Class2 = WeatherData(automatic_latlng[0], automatic_latlng[1], Func1)
print(WeatherData.weather(Class2))
print(WeatherData.temperature(Class2))
print(WeatherData.wind(Class2))
print(WeatherData.sun_timing(Class2))

local = "Sao Jose Do Rio Preto, BR"
ClassM1 = Localization(local, None)
manual_latlng = Localization.manual_localization(ClassM1)

Class1 = WeatherData(manual_latlng[0], manual_latlng[1], None)
Func1 = WeatherData.get_forecast(Class1)
Class2 = WeatherData(manual_latlng[0], manual_latlng[1], Func1)

address_obj = Localization(None, manual_latlng)
address = Localization.get_address(address_obj)
print(address)
print(WeatherData.weather(Class2))
temp_data = WeatherData.temperature(Class2)
print(f'{temp_data[0]}ºC, {temp_data[1]}')
print(WeatherData.wind(Class2))
print(WeatherData.sun_timing(Class2))
# Exemplos, lembrar de deletar depoix