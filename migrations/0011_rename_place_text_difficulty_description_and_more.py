# Generated by Django 4.2.5 on 2023-11-05 15:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("CavQuest_app", "0010_task_completed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="difficulty",
            old_name="place_text",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="place",
            old_name="place_text",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="usersubmission",
            old_name="place_text",
            new_name="description",
        ),
    ]
