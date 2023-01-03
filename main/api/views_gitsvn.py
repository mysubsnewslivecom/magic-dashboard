from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.utility.functions import ResourceLocator

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class GitsvnProjectViewset(ViewSet):
    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        gs = ResourceLocator().get_gitlab_service()
        projects = gs.get_gitlab_project_details()
        return Response(data=projects)
