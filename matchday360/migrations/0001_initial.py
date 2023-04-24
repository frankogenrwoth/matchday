# Generated by Django 4.2 on 2023-04-23 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competition",
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
                ("competition_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Match",
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
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("team_name", models.CharField(max_length=100)),
                ("date_created", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Matchday",
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
                ("match_overview", models.TextField()),
                ("match_prediction", models.TextField()),
                ("home_team_news", models.TextField()),
                ("away_team_news", models.TextField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matchday360.match",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="match",
            name="away_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="The_away_team",
                to="matchday360.team",
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="competiton",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="matchday360.competition",
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="home_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="The_home_team",
                to="matchday360.team",
            ),
        ),
    ]