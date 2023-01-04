from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("wait_db")
        call_command("wait_redis")
        call_command("makemigrations")
        call_command("migrate")
        call_command("initiateadmin")
        if settings.DEBUG:
            call_command("runserver", f"0.0.0.0:{settings.DJANGO_PORT}")
