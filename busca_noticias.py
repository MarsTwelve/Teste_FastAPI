import requests
import re
from bs4 import BeautifulSoup


def busca_noticias():
    site = requests.get("https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    jornal = BeautifulSoup(site.text, "html.parser")
    noticias = jornal.findAll("item")
    return noticias


def extrai_titulo(news):
    mensagem = news.title.text
    return mensagem


def extrai_data(news):
    data_raw = news.pubdate.text
    data = data_raw[5:16]
    hora = data_raw[17:22]
    completo = f"{data} as {hora}"
    return completo


def extrai_link(news):
    source = news.description.text
    comeco = re.search("https", source)
    fim = re.search("oc=5", source)
    link = source[comeco.start():fim.end()]
    return link


def empacotador_news():
    list_news = []
    for news in busca_noticias():
        titulo = extrai_titulo(news)
        data = extrai_data(news)
        link = extrai_link(news)
        news_dict = {"titulo": titulo, "data": data, "link": link}
        list_news.append(news_dict)
    return list_news


print(empacotador_news())
