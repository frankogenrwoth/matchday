from django.contrib import admin
from matchday360.models import Competition, Match, Matchday, Team

# Register your models here.
admin.site.register(Competition)
admin.site.register(Matchday)
admin.site.register(Match)
admin.site.register(Team)
