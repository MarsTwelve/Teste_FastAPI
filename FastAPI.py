from fastapi import FastAPI
from busca_noticias import empacotador_news
from WeatherData import WeatherData

app = FastAPI(title="FastAPI_Teste", description="<h1>descrição</h1>", summary="sumário",
              version="0.0.2", terms_of_service="https://twitter.com/en/tos", contact={"nome": "Roberto Antonio Borges Quadrilha",
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
    WeatherData.localizacao_automatica()

    return

@app.get("/Weather/{Manual}")
def Localizacao_manual(Manual):
    return {"localização": Manual}

