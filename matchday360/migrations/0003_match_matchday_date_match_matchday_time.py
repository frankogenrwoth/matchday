# Generated by Django 4.2 on 2023-04-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("matchday360", "0002_rename_competiton_match_competition"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="matchday_date",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="match",
            name="matchday_time",
            field=models.CharField(default="", max_length=10),
        ),
    ]
