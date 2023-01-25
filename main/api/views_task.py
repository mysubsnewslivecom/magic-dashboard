from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import status, viewsets
from rest_framework.decorators import action
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
        return Response(list(data.values()), status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def pending(self, request):
        pending = Todo.objects.filter(is_active=True, status=False)
        return Response(list(pending.values()), status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def completed(self, request):
        completed = Todo.objects.filter(is_active=True, status=True)
        return Response(list(completed.values()), status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def count(self, request):
        # count = Todo.objects.filter(is_active=True, status=False).count()
        todo = Todo.objects.filter(is_active=True)
        pending_count = todo.filter(status=False).count()
        completed = todo.filter(status=True).count()

        data = {
            "pending": pending_count,
            "completed": completed,
        }
        return Response(data, status=status.HTTP_200_OK)
