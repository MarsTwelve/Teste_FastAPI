from fastapi import FastAPI
from busca_noticias import empacotador_news
from Localization import Localization
from WeatherData import WeatherData

app = FastAPI(title="FastAPI_Teste", description="<h1>descrição</h1>", summary="sumário",
              version="0.0.2", terms_of_service="https://twitter.com/en/tos",
              contact={"nome": "Roberto Antonio Borges Quadrilha",
                       "url": "https://github.com/MarsTwelve/Teste_FastAPI",
                       "email": "matheusfer33@hotmail.com"})


@app.get("/")
async def root():
    return "Welcome to WeazelNews website"


@app.get("/News")
def show_news():
    news = empacotador_news()
    return news


@app.get("/Weather")
def show_weather():
    latlng = Localization.automatic_localization()
    address_latlng_obj = Localization(None, latlng)
    address = Localization.get_address(address_latlng_obj)

    weather_latlng_obj = WeatherData(latlng[0], latlng[1], None)
    forecast = WeatherData.get_forecast(weather_latlng_obj)
    forecast_obj = WeatherData(None, None, forecast)
    weather = WeatherData.weather(forecast_obj)
    temp = WeatherData.temperature(forecast_obj)
    wind = WeatherData.wind(forecast_obj)
    suntime = WeatherData.sun_timing(forecast_obj)
    wheatherdata = {"Address": address,
                    "Description": weather[0],
                    "Icon_id": weather[1],
                    "temp": temp[0],
                    "humidity": temp[1],
                    "wind_speed": wind[0],
                    "wind_direction": wind[1],
                    "sunrise_time": suntime[0],
                    "sunset_time": suntime[1]}
    return wheatherdata


@app.get("/Weather/{custom}")
def show_custom_weather(manual):
    obj_localization = Localization(manual, None)
    latlng = Localization.manual_localization(obj_localization)
    obj_latlng_address = Localization(None, latlng)
    address = Localization.get_address(obj_latlng_address)
    weather_latlng_obj = WeatherData(latlng[0], latlng[1], None)
    forecast = WeatherData.get_forecast(weather_latlng_obj)
    forecast_obj = WeatherData(None, None, forecast)
    weather = WeatherData.weather(forecast_obj)
    temp = WeatherData.temperature(forecast_obj)
    wind = WeatherData.wind(forecast_obj)
    suntime = WeatherData.sun_timing(forecast_obj)
    wheatherdata = {"Address": address,
                    "Description": weather[0],
                    "Icon_id": weather[1],
                    "temp": temp[0],
                    "humidity": temp[1],
                    "wind_speed": wind[0],
                    "wind_direction": wind[1],
                    "sunrise_time": suntime[0],
                    "sunset_time": suntime[1]}
    return wheatherdata
