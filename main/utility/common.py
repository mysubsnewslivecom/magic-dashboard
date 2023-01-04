from enum import Enum

from django.utils.translation import gettext_lazy as _


class Status(Enum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    IN_PROGRESS = "IN-PROGRESS"
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    SKIPPED = "SKIPPED"
    INFO = "INFO"
    DEBUG = "DEBUG"


STATUS = [
    (Status.ERROR.name, _(Status.ERROR.value)),
    (Status.SUCCESS.name, _(Status.SUCCESS.value)),
    (Status.IN_PROGRESS.name, _(Status.IN_PROGRESS.value)),
    (Status.CREATED.name, _(Status.CREATED.value)),
    (Status.COMPLETED.name, _(Status.COMPLETED.value)),
    (Status.SKIPPED.name, _(Status.SKIPPED.value)),
    (Status.INFO.name, _(Status.INFO.value)),
    (Status.DEBUG.name, _(Status.DEBUG.value)),
]
