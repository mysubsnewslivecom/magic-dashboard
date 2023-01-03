from rest_framework_simplejwt.tokens import RefreshToken

from main.authuser.models import User


class GenerateJWT:
    def __init__(self, user: User) -> None:
        self.user = user
        assert self.user, "User not provided"

    def get_tokens_for_user(self):

        refresh = RefreshToken.for_user(self.user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
