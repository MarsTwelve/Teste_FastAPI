import re


class NewsFormat:

    def __init__(self, news):
        self.news = news

    def extract_title(self):
        title = self.news.title.text
        return title

    def extract_date(self):
        raw_date = self.news.pubdate.text
        date = raw_date[5:16]
        hour = raw_date[17:22]
        date_hour = f"{date} as {hour}"
        return date_hour

    def extract_link(self):
        source = self.news.description.text
        start = re.search("https", source)
        stop = re.search("oc=5", source)
        link = source[start.start():stop.end()]
        return link
