from django.db import models
from django.utils.translation import gettext_lazy as _

from main.utility.mixins import ActiveStatusMixin, PrimaryIdMixin, TimestampMixin


class Todo(PrimaryIdMixin, TimestampMixin, ActiveStatusMixin):
    name = models.CharField(_("Task Name"), max_length=50)
    status = models.BooleanField(_("Status"), default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Todo"

    def __str__(self) -> str:
        return "".join(str(self.name))
