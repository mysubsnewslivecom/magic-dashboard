import gzip
import os
import shutil
import tempfile
from datetime import date, datetime, time

from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.utils import timezone
from django.utils.timezone import make_aware

from main.utility.functions import LoggingService

log = LoggingService()
today = timezone.now()
today_start = make_aware(datetime.combine(today, time()))
today = date.today().strftime("%Y%m%d")
DJANGO_PROJECT = os.getenv("DJANGO_PROJECT")


class Command(BaseCommand):
    help = f"Backup of {DJANGO_PROJECT} database"

    def handle(self, *args, **options):
        output = f"{DJANGO_PROJECT}_{today}.json"
        try:

            with tempfile.TemporaryDirectory() as d:
                dump_path = os.path.join(d, output)
                log.info(f"Starting backup process. {dump_path}")

                call_command(
                    "dumpdata",
                    format="json",
                    indent=4,
                    natural_foreign=True,
                    output=dump_path,
                    exclude=[
                        "admin",
                        "auth",
                        "contenttypes",
                        "sessions",
                    ],
                )
                log.info("Data dumped.")
                tmp_backup_file = os.path.join(d, f"{output}.gz")

                backup_file = os.path.join(settings.BACKUP_DIR, f"{output}.gz")
                if not os.path.exists(settings.BACKUP_DIR):
                    os.mkdir(settings.BACKUP_DIR)
                log.info(f"Temp Backup file: {tmp_backup_file}")

                log.info(f"Backup file: {backup_file}")
                with open(dump_path, mode="rb") as f_input, gzip.open(
                    tmp_backup_file, mode="wb"
                ) as f_output:
                    shutil.copyfileobj(fsrc=f_input, fdst=f_output)
                log.info(f"Copying data file to {settings.BACKUP_DIR}")

                shutil.copyfile(tmp_backup_file, backup_file)

                # backup_path = os.path.join(settings.BACKUP_DIR, datetime.date.today().strftime("%Y-%m-%d.zip"))
                # with zipfile.ZipFile(backup_path, mode='w') as backup_zip:
                #     for root, dirs, files in os.walk(d):
                #         for file in files:
                #             filepath = os.path.join(root, file)
                #             log.info("Compressing {}...".format(filepath))
                #             backup_zip.write(filepath,
                #                             arcname=os.path.relpath(filepath, d))
                #     log.info("{} created.".format(backup_path))

                log.info(f"Backup of {DJANGO_PROJECT} database completed")
        except Exception as ex:
            log.error(str(ex))
