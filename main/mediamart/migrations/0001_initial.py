# Generated by Django 4.1.5 on 2023-01-12 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Media",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(help_text="Name", max_length=250, unique=True),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("TV", "TV"), ("MOVIE", "Movie"), ("ANIME", "Anime")],
                        max_length=250,
                    ),
                ),
                (
                    "sub_category",
                    models.CharField(
                        choices=[
                            ("FANTASY", "Fantasy"),
                            ("ADVENTURE", "Adventure"),
                            ("ACTION", "Action"),
                            ("COMEDY", "Comedy"),
                            ("CRIME", "Crime"),
                            ("DRAMA", "Drama"),
                            ("SCIENCE_FICTION", "Science Fiction"),
                            ("DRAMA", "Drama"),
                            ("HORROR", "Horror"),
                        ],
                        max_length=250,
                    ),
                ),
                (
                    "thumb_nail",
                    models.ImageField(
                        default="linux.jpg", upload_to="", verbose_name="default"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Media",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Watching",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("completed", models.BooleanField(default=True)),
                (
                    "current_watch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="mediamart.media",
                        verbose_name="watch",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Watching",
                "ordering": ["-id"],
            },
        ),
    ]
