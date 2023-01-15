import datetime

from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.management.base import BaseCommand

from main.health.models import DailyTracker, Rule
from main.utility.functions import LoggingService

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
REDIS_KEY_PREFIX = str(getattr(settings, "REDIS_KEY_PREFIX")).lower()


class Command(BaseCommand):
    help = "trigger daily tracker"

    def add_arguments(self, parser):
        # parser.add_argument('date', nargs='+', type=str, )
        parser.add_argument("-d", "--date", type=str)

    def handle(self, *args, **options):
        date_today = (
            options["date"]
            if options["date"]
            else datetime.date.today() - datetime.timedelta(days=0)
        )
        rules_id = Rule.objects.filter(is_active=True).order_by("-id")
        data_tracker_obj = [
            DailyTracker(date=date_today, rule_id=ri, status=False) for ri in rules_id
        ]
        DailyTracker.objects.filter(date=date_today, status=False).delete()
        result = DailyTracker.objects.bulk_create(
            data_tracker_obj, ignore_conflicts=True
        )
        log.debug("Setting DailyTracker data to cache")
        daily_tracker_today = DailyTracker.objects.get_daily_status()
        cache.set(
            f"{REDIS_KEY_PREFIX}_models__daily_tracker_today",
            daily_tracker_today,
            60 * 5,
        )

