from fastapi import FastAPI
from busca_noticias import empacotador


app = FastAPI()
@app.get("/")
async def root():
    return ("Welcome to the news stuff")



@app.get("/News")
def mostra_noticias():
    noticias = empacotador()
    return noticias
