from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from main.home.forms import CustomUserAuthenticationForm


class UserLoginView(LoginView):
    form_class = CustomUserAuthenticationForm
    authentication_form = CustomUserAuthenticationForm

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)


class UserLogout(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

