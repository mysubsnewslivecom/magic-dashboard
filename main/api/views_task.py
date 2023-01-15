from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets
from rest_framework.response import Response

from main.api import serializer
from main.task.models import Todo
from main.utility.functions import LoggingService

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class TodoViewset(viewsets.ModelViewSet):
    serializer_class = serializer.TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request, *args, **kwargs):
        data = Todo.objects.filter(is_active=True)
        return Response(list(data.values()))
