from django.urls import path

from main.gitsvn.views import ProjectList

app_name = "git"

urlpatterns = [path(route="projects", view=ProjectList.as_view(), name="git-projects")]
