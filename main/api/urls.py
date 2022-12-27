from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from main.api.views import ISSLocation
# from django.conf.urls import url
from rest_framework import routers


app_name = "api"

# newly registered ViewSet
router = routers.DefaultRouter()

router.register(r"iss", ISSLocation, basename="home-iss")


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