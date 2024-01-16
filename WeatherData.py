from datetime import datetime


class WeatherData:
    def __init__(self, forecast):
        self.forecast = forecast

    def weather(self):
        weather = self.forecast["weather"][0]
        weather_desc = weather["description"]
        weather_icon = weather["icon"]
        image_url = f"https://openweathermap.org/img/wn/{weather_icon}@2x.png"
        return weather_desc, image_url

    def temperature(self):
        temp = self.forecast["main"]["temp"]
        humidity = self.forecast["main"]["humidity"]
        return temp, humidity

    def wind(self):
        speed = self.forecast["wind"]["speed"]
        direction = self.forecast["wind"]["deg"]
        return speed, direction

    def sun_timing(self):
        sunrise_unix = self.forecast["sys"]["sunrise"]
        sunset_unix = self.forecast["sys"]["sunset"]
        sunrise_time = datetime.fromtimestamp(sunrise_unix)
        sunset_time = datetime.fromtimestamp(sunset_unix)
        sunrise = sunrise_time.strftime("%H:%M")
        sunset = sunset_time.strftime("%H:%M")
        return sunrise, sunset



