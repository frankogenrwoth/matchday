# Generated by Django 4.2 on 2023-04-23 10:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("matchday360", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="match",
            old_name="competiton",
            new_name="competition",
        ),
    ]
