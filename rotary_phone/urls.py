from django.conf import settings
from django.conf.urls.static import static
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
    path("health/", include("main.health.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
