from django.contrib import admin

from .models import Player, Season, Match, Rating

# Register your models here.
admin.site.register(Player)
admin.site.register(Season)
admin.site.register(Match)
admin.site.register(Rating)
