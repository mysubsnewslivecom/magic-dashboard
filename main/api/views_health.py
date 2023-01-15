from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.vary import vary_on_cookie
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from main.api import serializer
from main.health.models import DailyTracker, Rule
from main.utility.functions import LoggingService
from main.utility.mixins import EnablePartialUpdateMixin

log = LoggingService()


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class RuleAPIViewset(viewsets.ModelViewSet):
    serializer_class = serializer.RulesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Rule.objects.all()


class DailyActivityViewset(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = DailyTracker.objects.all()
    serializer_class = serializer.DailyTrackerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "date"
    http_method_names = ["get", "patch"]

    # @action(detail=False, methods=['get'], url_path='gdt', name='Get daily status')
    @action(detail=False, url_path="gdt", methods=["get"], name="Get daily status")
    @method_decorator(never_cache)
    @method_decorator(vary_on_cookie)
    def get_daily_status(self, request, *args, **kwargs):
        data = DailyTracker.objects.get_daily_status()
        return Response(data=data)

    @method_decorator(never_cache)
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        date = kwargs["date"]
        # data = Rule.objects.filter(date=date).values()
        data = list(DailyTracker.objects.filter(date=date).select_related("rule_id"))
        data_arr = list()
        for d in data:
            # data_dict = dict()
            data_dict = {
                "name": d.rule_id.name,
                "id": d.id,
                "status": d.status,
                "date": d.date,
            }
            data_arr.append(data_dict)
        return Response(data_arr)

    def update(self, request, pk=None, *args, **kwargs):

        data = request.data
        id = data["id"]
        data_status = data["status"]
        result = DailyTracker.objects.filter(id=id).update(status=data_status)
        message = {"message": f"{result} record updated."}

        return Response(data=message, status=status.HTTP_202_ACCEPTED)
