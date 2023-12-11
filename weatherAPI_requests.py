import geocoder
import requests
from datetime import datetime


def achar_lat_lng():
    g = geocoder.ip("me")
    location = g.latlng
    lat = location[0]
    lng = location[1]
    return lat, lng


def achar_endereco(latitude, longitude):
    lat = latitude
    lng = longitude
    bing_key = "ApLbhMovO66Qk048JY2Iqhx9vTuxAqh-P2mjk13xWt7G2TLuAzBMj_fKlBnWVimI"
    loc_g = geocoder.bing([lat, lng], method="reverse", key=bing_key)
    loc_json = loc_g.json
    address = loc_json["address"]
    return address


def pegar_previsao_tempo(lat, lng):
    key = "0663035a8316bd463c63093370b24744"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={key}&units=metric"
    response = requests.get(url)
    prev_json = response.json()
    return prev_json


def clima(json):
    weather = json["weather"][0]
    weather_desc = weather["description"]
    weather_icon = weather["icon"]
    return weather_desc, weather_icon


def temperatura(json):
    temp = json["main"]["temp"]
    humidity = json["main"]["humidity"]
    return temp, humidity


def vento(json):
    speed = json["wind"]["speed"]
    direction = json["wind"]["deg"]
    return speed, direction


def chuva(json):
    try:
        rain_1h = json["rain"]["1h"]
        return rain_1h
    except KeyError:
        return "Sem dados"


def horario_sol(json):
    sunrise_unix = json["sys"]["sunrise"]
    sunset_unix = json["sys"]["sunset"]
    sunrise_time = datetime.fromtimestamp(sunrise_unix)
    sunset_time = datetime.fromtimestamp(sunset_unix)
    sunrise = sunrise_time.strftime("%H:%M")
    sunset = sunset_time.strftime("%H:%M")
    return sunrise, sunset


def empacotador_tempo():
    weather = []
    lat, lng = achar_lat_lng()
    json = pegar_previsao_tempo(lat, lng)
    desc, icon = clima(json)
    temp, humidity = temperatura(json)
    velocidade, direcao = vento(json)
    vol_chuva = chuva(json)
    sunrise, sunset = horario_sol(json)
    clima_info = {"tempo": desc, "icon_id": icon}
    temp_info = {"temperatura": temp, "humidade": humidity}
    wind_info = {"velocidade(m/s)": velocidade, "direção": direcao}
    sun_info = {"Nascer do Sol": sunrise, "Por do Sol": sunset}
    rain_info = {"Volume de chuva": vol_chuva}
    weather.append(clima_info)
    weather.append(temp_info)
    weather.append(wind_info)
    weather.append(sun_info)
    weather.append(rain_info)
    return weather


print(empacotador_tempo())
