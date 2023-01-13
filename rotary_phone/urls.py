from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.home.urls")),
    path("accounts/", include("main.authuser.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # authentication
    path("api/", include("main.api.urls")),
    path("misc/", include("main.misc.urls")),
    path("git/", include("main.gitsvn.urls")),
    path("mediamart/", include("main.mediamart.urls")),
]
