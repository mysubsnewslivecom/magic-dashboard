from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HealthView(LoginRequiredMixin, TemplateView):
    template_name = "health.html"
