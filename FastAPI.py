from fastapi import FastAPI
from busca_noticias import empacotador_news
from weatherAPI_requests import empacotador_tempo

app = FastAPI()


@app.get("/")
async def root():
    return "<h1>Welcome to WeazelNews website</h1>"


@app.get("/News")
def show_news():
    news = empacotador_news()
    return news


@app.get("/Weather")
def show_weather():
    weather = empacotador_tempo()
    return weather
