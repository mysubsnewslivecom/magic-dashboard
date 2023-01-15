from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from django.conf.urls import url
from rest_framework import routers

from main.api import views_gitsvn, views_task, views, views_health


app_name = "api"

# newly registered ViewSet
router = routers.DefaultRouter()

router.register(r"iss", viewset=views.ISSLocation, basename="home-iss")
router.register(r"ip", viewset=views.IPViewset, basename="home-ip")
router.register(r"epl-standing", viewset=views.FifaEPLStanding, basename="home-epl-standing")
router.register(r"git/projects", viewset=views_gitsvn.GitsvnProjectViewset, basename="gitsvn-git-projects")
router.register(r"git/issues/gitab", viewset=views_gitsvn.GitlabIssuesViewset, basename="gitsvn-git-issues-gitlab")
router.register(r"git/issues", viewset=views_gitsvn.GitIssues, basename="gitsvn-git-issues")
router.register(r"task/todo", viewset=views_task.TodoViewset, basename="task-todo")
router.register(r"health/rule", viewset=views_health.RuleAPIViewset, basename="health-rule")
router.register(r"health/dt", viewset=views_health.DailyActivityViewset, basename="health-dt")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            # template_name="swagger-ui.html",
            url_name="api:schema"
        ),
        name="swagger-ui",
    ),
]
