from django.db import models


# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.team_name


class Competition(models.Model):
    competition_name = models.CharField(max_length=100)

    def __str__(self):
        return self.competition_name


class Match(models.Model):
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="The_home_team"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="The_away_team"
    )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    matchday_date = models.CharField(max_length=10, default="")
    matchday_time = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.competition.competition_name} -> {self.home_team.team_name} vs {self.away_team.team_name}"

    def get_match_title(self):
        return f"{self.home_team.team_name} vs {self.away_team.team_name}"


class Matchday(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    match_overview = models.TextField()
    match_prediction = models.TextField()
    home_team_news = models.TextField()
    away_team_news = models.TextField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"matchday {self.match}"

    def get_absolute_url(self):
        unclean_title = self.match.get_match_title()
        unclean_title = unclean_title.replace(" ", "-")
        title = unclean_title.strip() + f"-{self.id}"
        return f"/matches/{title}/"
