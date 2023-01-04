import datetime

import jwt
from django.conf import settings
from django.core.management.base import BaseCommand

from main.home.models import User
from main.utility.functions import LoggingService

log = LoggingService()


class GenerateJwt:
    def __init__(self) -> None:
        self.cmd = "openssl rand -hex 32"
        # self.SECRET_KEY = subprocess.getoutput(cmd=self.cmd)
        self.SECRET_KEY = settings.SECRET_KEY

    def generate_jwt(self, username: str):
        user = User.objects.get(username=username)
        payload = {
            "name": user.get_full_name(),
            "username": user.username,
            "email": user.email,
            "exp": round((datetime.datetime.now() + datetime.timedelta(1)).timestamp()),
            "iss": "Rotary Phone",
            "iat": round(datetime.datetime.now().timestamp()),
        }

        log.info(payload)
        token = jwt.encode(payload=payload, key=self.SECRET_KEY, algorithm="HS256")
        log.info(token)


# def generate_jwt(username: str):
#     user = User.objects.get(username=username)
#     payload = {
#         "name": user.get_full_name(),
#         "username": user.username,
#         "email": user.email,
#         "exp": round(datetime.datetime.now().timestamp() + 24 * 60 * 60),
#         "iss": "Rotary Phone",
#         "iat": round(datetime.datetime.now().timestamp()),
#     }
#     log.info(payload)


class Command(BaseCommand):
    def handle(self, *args, **options):
        GenerateJwt().generate_jwt(username="admin")
