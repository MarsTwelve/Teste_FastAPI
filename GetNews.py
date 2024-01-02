import requests
from bs4 import BeautifulSoup


def busca_noticias():
    site = requests.get("https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    jornal = BeautifulSoup(site.text, "html.parser")
    noticias = jornal.findAll("item")
    return noticias
