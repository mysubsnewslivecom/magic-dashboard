from django.urls import path

from main.gitsvn.views import IssueList, ProjectList

app_name = "git"

urlpatterns = [
    path(route="projects", view=ProjectList.as_view(), name="git-projects"),
    path(route="issue/list", view=IssueList.as_view(), name="git-issue-list"),
]
