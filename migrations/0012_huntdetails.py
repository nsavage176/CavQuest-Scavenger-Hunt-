# Generated by Django 4.2.7 on 2023-11-11 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("CavQuest_app", "0011_rename_place_text_difficulty_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HuntDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="staticfiles/images")),
                ("description", models.TextField()),
                (
                    "task",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CavQuest_app.task",
                    ),
                ),
            ],
        ),
    ]
