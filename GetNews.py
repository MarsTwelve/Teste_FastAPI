import requests
from bs4 import BeautifulSoup


def get_news():
    site = requests.get("https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419")
    journal = BeautifulSoup(site.text, "html.parser")
    news = journal.findAll("item")
    return news
