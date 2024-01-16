from fastapi import FastAPI
from GetNews import get_news
from NewsData import NewsFormat
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
    news_html = get_news()
    news_dict = {}
    n = 1
    for news in news_html:
        news = NewsFormat(news)
        title = NewsFormat.extract_title(news)
        date = NewsFormat.extract_date(news)
        link = NewsFormat.extract_link(news)
        news_data = {"Titulo": title,
                     "Data de Publicaçao": date,
                     "Link da Noticia": link}
        news_dict.update({f"Noticia Nº{n}": news_data})
        n = n + 1
    return news_dict


@app.get("/Weather")
def show_weather():
    lat_lng = Localization()
    weather_data = WeatherData(lat_lng.get_forecast())
    description, image_url = weather_data.weather()
    temperature, humidity = weather_data.temperature()
    speed, direction = weather_data.wind()
    sunrise, sunset = weather_data.sun_timing()
    weather_data = {"Address": lat_lng.get_address(),
                    "Description": description,
                    "Image_url": image_url,
                    "temp": temperature,
                    "humidity": humidity,
                    "wind_speed": speed,
                    "wind_direction": direction,
                    "sunrise_time": sunrise,
                    "sunset_time": sunset}
    return weather_data


@app.get("/Weather/{custom}")
def show_custom_weather(manual):
    lat_lng = Localization(manual)
    weather_data = WeatherData(lat_lng.get_forecast())
    description, image_url = weather_data.weather()
    temperature, humidity = weather_data.temperature()
    speed, direction = weather_data.wind()
    sunrise, sunset = weather_data.sun_timing()
    weather_data = {"Address": lat_lng.get_address(),
                    "Description": description,
                    "Image_url": image_url,
                    "temp": temperature,
                    "humidity": humidity,
                    "wind_speed": speed,
                    "wind_direction": direction,
                    "sunrise_time": sunrise,
                    "sunset_time": sunset}
    return weather_data
