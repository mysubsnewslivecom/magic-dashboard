import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import OperationalError, connections

from main.utility.functions import LoggingService

log = LoggingService()


class Command(BaseCommand):
    def handle(self, *args, **options):
        log.debug("Waiting for database...")

        if settings.DB_SRC == "PG":
            while databases_check()["status"] == "ERROR":
                try:
                    log.error("Database unavailable, waiting 3 second...")
                    time.sleep(3)

                except Exception as ex:
                    log.error(ex.__str__)

            log.info(f"Database available! {databases_check()}")


def databases_check():
    return get_connection_info(connections["default"])


def get_connection_info(connection):
    return get_database_version(connection, connection.settings_dict.get("ENGINE"))


def get_database_version(connection, engine):
    engines = {
        "django.db.backends.postgresql": "SELECT version();",
    }
    return execute_sql(connection, engines[engine])


def execute_sql(connection, stmt):
    try:
        cursor = connection.cursor()
        cursor.execute(stmt)
        return {"status": "SUCCESS"}
    except OperationalError as e:
        return {"status": "ERROR", "error": str(e)}
