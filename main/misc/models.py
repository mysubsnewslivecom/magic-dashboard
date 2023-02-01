from django.db import models

from main.utility.mixins import PrimaryIdMixin, TimestampMixin


class ISSLocation(PrimaryIdMixin, TimestampMixin):
    latitude = models.FloatField()
    longitude = models.FloatField()
    response = models.JSONField()

    class Meta:
        ordering = ["-id"]  # new
