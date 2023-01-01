import requests
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.utility.functions import FifaEPLStandingScrapper

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class ISSLocation(ViewSet):
    def list(self, request, *args, **kwargs):

        resp = requests.request(method="GET", url=settings.ISS_LOCATION)
        return Response(resp.json())


class FifaEPLStanding(ViewSet):
    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):

        data = FifaEPLStandingScrapper().get_data()

        return Response(data)


class IPViewset(ViewSet):
    def list(self, request, *args, **kwargs):

        resp = requests.request(method="GET", url=settings.IPIFY_BASEURL)
        return Response(resp.json())
