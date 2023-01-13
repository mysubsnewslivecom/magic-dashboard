from django.db import models
from django.utils.translation import gettext_lazy as _

from main.utility.mixins import PrimaryIdMixin


class Media(PrimaryIdMixin):
    CATEGORY = [
        ("TV", "TV"),
        ("MOVIE", "Movie"),
        ("ANIME", "Anime"),
    ]
    SUB_CATEGORY = [
        ("FANTASY", "Fantasy"),
        ("ADVENTURE", "Adventure"),
        ("ACTION", "Action"),
        ("COMEDY", "Comedy"),
        ("CRIME", "Crime"),
        ("DRAMA", "Drama"),
        ("SCIENCE_FICTION", "Science Fiction"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
    ]
    name = models.CharField(help_text="Name", max_length=250, unique=True)
    category = models.CharField(choices=CATEGORY, max_length=250)
    sub_category = models.CharField(choices=SUB_CATEGORY, max_length=250)
    thumb_nail = models.ImageField(verbose_name="default", default="linux.jpg")

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Media"

    def __str__(self) -> str:
        return "".join(str(self.name))


class WatchingManager(models.Manager):
    pass


class Watching(PrimaryIdMixin):

    current_watch = models.ForeignKey(
        "mediamart.Media", verbose_name=_("watch"), on_delete=models.DO_NOTHING
    )
    completed = models.BooleanField(default=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Watching"

    def __str__(self) -> str:
        return "".join(str(self.current_watch.name))
