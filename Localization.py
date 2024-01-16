import geocoder
import requests


class Localization:

    def __init__(self, location=None):
        self.location = location
        self.bing_key = "ApLbhMovO66Qk048JY2Iqhx9vTuxAqh-P2mjk13xWt7G2TLuAzBMj_fKlBnWVimI"

    def get_localization(self):
        if self.location is not None:
            geo_location = geocoder.bing(self.location, key=self.bing_key)
            lat_lng = geo_location.latlng
            latitude = lat_lng[0]
            longitude = lat_lng[1]
            return latitude, longitude
        geocoder_location = geocoder.ip("me")
        lat_lng = geocoder_location.latlng
        latitude = lat_lng[0]
        longitude = lat_lng[1]
        return latitude, longitude

    def get_address(self):
        latitude, longitude = Localization.get_localization(self)
        geo_address = geocoder.bing([latitude, longitude], method="reverse", key=self.bing_key)
        address_json = geo_address.json
        address = address_json["address"]
        return address

    def get_forecast(self):
        latitude, longitude = Localization.get_localization(self)
        weather_key = "0663035a8316bd463c63093370b24744"
        url = (f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}"
               f"&appid={weather_key}&units=metric")
        response = requests.get(url)
        forecast = response.json()
        return forecast
