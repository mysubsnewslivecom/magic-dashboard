from django.urls import path

from main.gitsvn.views import (
    IssueCreate,
    IssueFormView,
    IssueIdFormView,
    IssueList,
    ProjectList,
)

app_name = "git"

urlpatterns = [
    path(route="projects", view=ProjectList.as_view(), name="git-projects"),
    path(route="issue/list", view=IssueList.as_view(), name="git-issue-list"),
    path(route="issue/create", view=IssueCreate.as_view(), name="git-issue-create"),
    path(route="issue/edit", view=IssueFormView.as_view(), name="git-issue-edit"),
    path(
        route="issue/edit/<iid>",
        view=IssueIdFormView.as_view(),
        name="git-issue-id-edit",
    ),
]
