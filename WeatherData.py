import geocoder
import requests
from datetime import datetime

class WeatherData:
    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.bingkey = "ApLbhMovO66Qk048JY2Iqhx9vTuxAqh-P2mjk13xWt7G2TLuAzBMj_fKlBnWVimI"
        self.WeatherAPIkey = "0663035a8316bd463c63093370b24744"


    @staticmethod
    def localizacao_automatica():
        g = geocoder.ip("me")
        location = g.latlng
        a_lat = location[0]
        a_lng = location[1]
        return a_lat, a_lng
    a_lat, a_lng = localizacao_automatica()

    def localizacao_manual(self):
        g = geocoder.bing(location=self.localizacao, key=self.bingkey)
        location = g.latlang
        m_lat = location[0]
        m_lng = location[1]
        return m_lat, m_lng
    m_lat, m_lng = localizacao_manual()


    def achar_endereco(self, latitude, longitude):
        g_endereco = geocoder.bing([latitude, longitude], method="reverse", key=self.bingkey)
        endereco_json = g_endereco.json
        endereco = endereco_json["address"]
        return endereco

    def pegar_previsao_tempo(self, latitude, longitude):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.WeatherAPIkey}&units=metric"
        response = requests.get(url)
        previsao = response.json()
        return previsao


class PrevisaoTempo(WeatherData):
    previsao = WeatherData.achar_endereco()
    def clima(previsao):
        weather = previsao["weather"][0]
        weather_desc = weather["description"]
        weather_icon = weather["icon"]
        return weather_desc, weather_icon


    def temperatura(previsao):
        temp = previsao["main"]["temp"]
        humidity = previsao["main"]["humidity"]
        return temp, humidity


    def vento(previsao):
        speed = previsao["wind"]["speed"]
        direction = previsao["wind"]["deg"]
        return speed, direction


    def chuva(previsao):
        try:
            rain_1h = previsao["rain"]["1h"]
            return rain_1h
        except KeyError:
            return "Sem dados"


    def horario_sol(previsao):
        sunrise_unix = previsao["sys"]["sunrise"]
        sunset_unix = previsao["sys"]["sunset"]
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


print(empacotador_tempo())
