from django.http import HttpResponse
from django_hv.http import hv_repond
from htpy import html, body, h1, table, tr, td, thead, tbody, th
from htpy_hv import hxml, text, screen, list_hv, item, style, styles

from .models import Player, Season, Rating


def index(request):
    current_season = Season.get_current()
    ratings_players = current_season.ratings.select_related("player")
    # table_columns = ["Player", "Rating"]
    # table_data = [(r.player.name, r.elo) for r in ratings_players]

    def app(request):
        content = hxml[
            screen[
                styles[style(id="h1", fontSize=48, margin=48)],
                body[
                    text(style="h1")[f"Season {current_season.name.title()} Ratings:"],
                    list_hv[
                        (
                            item(key=str(r))[text[r.player.name], text[str(r.elo)]]
                            for r in ratings_players
                        )
                    ],
                ],
            ]
        ]
        return hv_repond(HttpResponse(content))

    def web(request):
        content = html[
            body[
                h1[f"Season {current_season.name.title()} Ratings:"],
                table[
                    thead[tr[th["Player"], th["Rating"]]],
                    tbody[(tr[td[r.player.name], td[str(r.elo)]] for r in ratings_players)],
                ],
            ]
        ]
        return HttpResponse(content)

    if request.hv:
        return app(request)
    else:
        return web(request)
