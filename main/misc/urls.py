from django.urls import path

from main.misc.views import FifaView

app_name = "misc"

urlpatterns = [path(route="fifa", view=FifaView.as_view(), name="misc-fifa")]
