from django.urls import path

from main.gitsvn.views import IssueCreate, IssueEdit, IssueList, ProjectList

app_name = "git"

urlpatterns = [
    path(route="projects", view=ProjectList.as_view(), name="git-projects"),
    path(route="issue/list", view=IssueList.as_view(), name="git-issue-list"),
    path(route="issue/create", view=IssueCreate.as_view(), name="git-issue-create"),
    path(route="issue/edit/<int:iid>", view=IssueEdit.as_view(), name="git-issue-edit"),
]
