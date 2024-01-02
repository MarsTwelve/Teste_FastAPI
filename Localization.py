import geocoder


class Localization:

    def __init__(self, location, lat_lng):
        self.lat_lng = lat_lng
        self.location = location
        self.bing_key = "ApLbhMovO66Qk048JY2Iqhx9vTuxAqh-P2mjk13xWt7G2TLuAzBMj_fKlBnWVimI"

    def manual_localization(self):
        geo_location = geocoder.bing(self.location, key=self.bing_key)
        lat_lng = geo_location.latlng
        return lat_lng

    @staticmethod
    def automatic_localization():
        geo_location = geocoder.ip("me")
        lat_lng = geo_location.latlng
        return lat_lng

    def get_address(self):
        latitude = self.lat_lng[0]
        longitude = self.lat_lng[1]
        geo_address = geocoder.bing([latitude, longitude], method="reverse", key=self.bing_key)
        address_json = geo_address.json
        address = address_json["address"]
        return address
