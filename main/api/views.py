from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api import serializer
from main.utility.functions import FifaEPLStandingScrapper, GetRequests, LoggingService

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class ISSLocation(ViewSet):
    serializer_class = serializer.JsonSerializer

    def list(self, request, *args, **kwargs):

        resp = GetRequests(url=settings.ISS_LOCATION).get_request()

        return Response(data=resp)


class FifaEPLStanding(ViewSet):
    serializer_class = serializer.FifaEPLStandingSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):

        data = FifaEPLStandingScrapper().get_data()

        return Response(data)


class IPViewset(ViewSet):
    serializer_class = serializer.IPSerializer

    def list(self, request, *args, **kwargs):

        # hostname = socket.gethostname()
        # local_ip = socket.gethostbyname(hostname)

        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # print(s.getsockname()[0])
        # log.info(s.getsockname()[0])
        resp = GetRequests(url=settings.IPIFY_BASEURL).get_request()

        return Response(data=resp)
