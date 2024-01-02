import re
from GetNews import busca_noticias


class NewsFormat:

    def __init__(self, obj_news):
        self.news = obj_news

    def extrai_titulo(self):
        mensagem = self.news.title.text
        return mensagem

    def extrai_data(self):
        data_raw = self.news.pubdate.text
        data = data_raw[5:16]
        hora = data_raw[17:22]
        completo = f"{data} as {hora}"
        return completo

    def extrai_link(self):
        source = self.news.description.text
        comeco = re.search("https", source)
        fim = re.search("oc=5", source)
        link = source[comeco.start():fim.end()]
        return link
