from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
import requests

from main.utility.functions import WebScrapping

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class ISSLocation(ViewSet):
    def list(self, request, *args, **kwargs):

        resp = requests.request(method="GET", url="http://api.open-notify.org/iss-now.json")
        print(resp)
        return Response(resp.json())



class FifaEPLStanding(ViewSet):

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        url = "https://onefootball.com/en/competition/premier-league-9/table"
        feature = "lxml"
        soup = WebScrapping(url=url, features=feature).get_soup_text()

        data = soup.find_all("a", class_="standings__row-grid")
        
        table_arr = list()
        for row in data:
            temp_dict = dict()
            temp = row.text.split()
            temp_dict["position"] = temp[0]

            if len(temp) == 8:
                temp_dict["team"] = temp[1]
            elif len(temp) == 9:
                temp_dict["team"] = " ".join([temp[1], temp[2]])

            temp_dict["played"] = temp[-6]
            temp_dict["wins"] = temp[-5]
            temp_dict["draw"] = temp[-4]
            temp_dict["loss"] = temp[-3]
            temp_dict["goal_diff"] = temp[-2]
            temp_dict["points"] = temp[-1]

            table_arr.append(temp_dict)

        return Response(table_arr)



