# Generated by Django 4.2.5 on 2023-11-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CavQuest_app", "0021_usertask"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="image",
            field=models.ImageField(null=True, upload_to="location_images/"),
        ),
    ]
