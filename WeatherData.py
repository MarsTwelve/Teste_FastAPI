import geocoder
import requests
from datetime import datetime


class Localization:
    def __init__(self, location=None):
        self.location = location
        self.bing_key = "ApLbhMovO66Qk048JY2Iqhx9vTuxAqh-P2mjk13xWt7G2TLuAzBMj_fKlBnWVimI"

    def latitude_longitude(self):
        if self.location is not None:
            # Localização Manual, a partir do nome da cidade
            geo_location = geocoder.bing(location=self.location, key=self.bing_key)
            location = geo_location.latlang
            longitude = location[0]
            latitude = location[1]
            return latitude, longitude
        # Localização automática, a partir do IP do usuário
        geo_location = geocoder.ip("me")
        location = geo_location.latlng
        latitude = location[0]
        longitude = location[1]
        return latitude, longitude

    def get_address(self):
        latitude, longitude = self.latitude_longitude()
        geo_address = geocoder.bing([latitude, longitude], method="reverse", key=self.bing_key)
        address_json = geo_address.json
        address = address_json["address"]
        return address


class WeatherData(Localization):

    def get_forecast(self):
        weather_key = "0663035a8316bd463c63093370b24744"
        lat, lon = self.latitude_longitude()
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=metric"
        response = requests.get(url)
        previsao = response.json()
        return previsao

    def weather(self):
        weather = self.get_forecast()["weather"][0]
        weather_desc = weather["description"]
        weather_icon = weather["icon"]
        return weather_desc, weather_icon

    def temperature(self):
        temp = self.get_forecast()["main"]["temp"]
        humidity = self.get_forecast()["main"]["humidity"]
        return temp, humidity

    def wind(self):
        speed = self.get_forecast()["wind"]["speed"]
        direction = self.get_forecast()["wind"]["deg"]
        return speed, direction

    def rain(self):
        try:
            rain_1h = self.get_forecast()["rain"]["1h"]
            return rain_1h
        except KeyError:
            return "Sem dados"

    def sun_timing(self):
        sunrise_unix = self.get_forecast()["sys"]["sunrise"]
        sunset_unix = self.get_forecast()["sys"]["sunset"]
        sunrise_time = datetime.fromtimestamp(sunrise_unix)
        sunset_time = datetime.fromtimestamp(sunset_unix)
        sunrise = sunrise_time.strftime("%H:%M")
        sunset = sunset_time.strftime("%H:%M")
        return sunrise, sunset


# def empacotador_tempo():
#     lat, lng = achar_lat_lng()
#     json = pegar_previsao_tempo(lat, lng)
#     desc, icon = clima(json)
#     temp, humidity = temperatura(json)
#     velocidade, direcao = vento(json)
#     vol_chuva = chuva(json)
#     sunrise, sunset = horario_sol(json)
#     clima_info = {"tempo": desc, "icon_id": icon}
#     temp_info = {"temperatura": temp, "humidade": humidity}
#     wind_info = {"velocidade(m/s)": velocidade, "direção": direcao}
#     sun_info = {"Nascer do Sol": sunrise, "Por do Sol": sunset}
#     rain_info = {"Volume de chuva": vol_chuva}
#     weather = [clima_info, temp_info, wind_info, sun_info, rain_info]
#     return weather

