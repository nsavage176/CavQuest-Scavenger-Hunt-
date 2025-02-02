# Generated by Django 4.2 on 2023-11-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CavQuest_app", "0027_merge_20231112_0809"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="tasks_images/"),
        ),
        migrations.AlterField(
            model_name="place",
            name="image",
            field=models.ImageField(null=True, upload_to="location_pictures/"),
        ),
    ]
