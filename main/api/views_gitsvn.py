from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api import serializer
from main.utility.functions import ResourceLocator

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class GitsvnProjectViewset(ViewSet):
    serializer_class = serializer.GitProjectSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        gs = ResourceLocator().get_gitlab_service()
        projects = gs.get_gitlab_project_details()
        return Response(data=projects)


class GitlabIssuesViewset(ViewSet):
    serializer_class = serializer.GitlabIssueSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, pk: int, *args, **kwargs):
        gs = ResourceLocator().get_gitlab_issue()
        issue = gs.get_issue(pk)
        if isinstance(issue, str):
            issue = f"Issue id {pk}: {issue}"
            return Response(
                data=f"Unable to retrive {pk}. Error: {issue}",
                status=status.HTTP_404_NOT_FOUND,
            )

        issue = issue.asdict()
        issue_dict = dict()
        issue_dict["id"] = issue["id"]
        issue_dict["iid"] = issue["iid"]
        issue_dict["project_id"] = issue["project_id"]
        issue_dict["title"] = issue["title"]
        issue_dict["description"] = issue["description"]
        issue_dict["state"] = issue["state"]
        issue_dict["labels"] = issue["labels"]
        issue_dict["assignees"] = (
            issue["assignees"][0]["username"] if issue["assignees"] else "-"
        )
        issue_dict["issue_type"] = issue["issue_type"]
        issue_dict["web_url"] = issue["web_url"]

        return Response(data=issue_dict)
