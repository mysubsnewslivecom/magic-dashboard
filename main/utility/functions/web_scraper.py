import requests
from bs4 import BeautifulSoup as BS
from typing import Optional


class WebScrapping:
    def __init__(
        self, url: Optional[str] = None, features: Optional[str] = "html.parser"
    ) -> None:
        self.url = url
        self.features = features

    def get_soup_content(self):
        content = requests.get(self.url).content
        soup = BS(content, features=self.features)
        return soup

    def get_soup_text(self):
        content = requests.get(self.url).text
        soup = BS(content, features=self.features)
        return soup
