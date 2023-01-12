from os import getenv

from django.conf import settings
from django.core.management.base import BaseCommand

from main.authuser.models import User
from main.utility.functions import LoggingService

log = LoggingService()


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.all()

        # user.delete()
        username = settings.DJANGO_SU_NAME
        log.debug(f"Creating superuser {username} account")

        # self.stdout.write(f"Creating superuser {username} account")
        if not user.exists():
            User.objects.create_superuser(
                email=settings.DJANGO_SU_EMAIL,
                # username=username,
                password=getenv("DJANGO_SU_PASSWORD"),
            )
            log.info(f"{settings.DJANGO_SU_NAME} user created")
        else:
            # self.stdout.write(self.style.NOTICE("Admin already exists"))
            log.warn(f"{settings.DJANGO_SU_NAME} already exists")
