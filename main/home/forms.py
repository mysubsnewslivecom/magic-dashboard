from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, CheckboxInput, TextInput


class CustomUserAuthenticationForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "floatingInput",
                "placeholder": "username",
                "name": "floatingInput",
            },
        ),
        label="",
    )
    password = CharField(
        widget=TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "id": "floatingInput",
                "placeholder": "password",
                "name": "floatingInput",
            },
        ),
        label="",
    )
    remember_me = BooleanField(
        required=False,
        label="remember me",
        widget=CheckboxInput(
            attrs={
                "type": "checkbox",
                "class": "form-check-input",
                "id": "floatingCheckBox",
                "name": "floatingCheckBox",
            },
        ),
    )

    class Meta:
        model = User
        fields = ["username", "content", "password1", "password2", "remember_me"]

    def __init__(self, request, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ""}
        self.helper.form_method = "post"  # get or post method
        self.helper.form_class = "row row-cols-lg-auto g-3 align-items-center"
