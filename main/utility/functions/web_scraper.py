from typing import Optional

import requests
import urllib3
from bs4 import BeautifulSoup as BS
from django.conf import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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


class FifaEPLStandingScrapper:
    def __init__(self, url: Optional[str] = settings.FIFA_EPL_STANDING) -> None:
        self.url = url
        self.feature = "lxml"

    def get_data(self):
        soup = WebScrapping(url=self.url, features=self.feature).get_soup_text()

        data = soup.find_all("a", class_="standings__row-grid")

        table_arr = list()
        for row in data:
            temp_dict = dict()
            temp = row.text.split()
            temp_dict["position"] = int(temp[0])

            if len(temp) == 8:
                temp_dict["team"] = temp[1]
            elif len(temp) == 9:
                temp_dict["team"] = " ".join([temp[1], temp[2]])

            temp_dict["played"] = int(temp[-6])
            temp_dict["wins"] = int(temp[-5])
            temp_dict["draw"] = int(temp[-4])
            temp_dict["loss"] = int(temp[-3])
            temp_dict["goal_diff"] = int(temp[-2])
            temp_dict["points"] = int(temp[-1])

            table_arr.append(temp_dict)
        return table_arr
