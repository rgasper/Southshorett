from django.http import HttpResponse
from django_hv.http import hv_repond
from .models import Season

from southshorett.components.app import index as app_index
from southshorett.components.web import index as web_index


def index(request):
    current_season = Season.get_current()
    ratings_players = current_season.ratings.select_related("player")

    if request.hv:
        return hv_repond(
            HttpResponse(
                app_index(
                    request,
                    current_season=current_season,
                    ratings_players=ratings_players,
                )
            )
        )
    else:
        return HttpResponse(
            web_index(
                request, current_season=current_season, ratings_players=ratings_players
            )
        )
