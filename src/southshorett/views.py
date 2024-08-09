from django.http import HttpResponse
from django_hv.http import hv_repond
from .models import Season

# index
from southshorett.components.app import index as app_index
from southshorett.components.web import index as web_index

# log a match
from southshorett.components.app import log_a_match as app_log_a_match
from southshorett.components.web import log_a_match as web_log_a_match


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


def log_a_match(request):
    if request.hv:
        return hv_repond(HttpResponse(app_log_a_match(request)))
    else:
        return HttpResponse(web_log_a_match(request))
