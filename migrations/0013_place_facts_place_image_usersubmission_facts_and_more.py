# Generated by Django 4.2.7 on 2023-11-11 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CavQuest_app", "0012_huntdetails"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="facts",
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name="place",
            name="image",
            field=models.ImageField(null=True, upload_to="staticfiles/images"),
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="facts",
            field=models.CharField(max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="image",
            field=models.ImageField(null=True, upload_to="staticfiles/images"),
        ),
        migrations.DeleteModel(
            name="HuntDetails",
        ),
    ]
