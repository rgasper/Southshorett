from django.db.models import QuerySet
from htpy import html, body, h1, table, tr, td, thead, tbody, th, Node

from southshorett.models import Season, Rating


def index(request, current_season: Season, ratings_players: QuerySet[Rating]) -> Node:
    content = html[
        body[
            h1[f"Season {current_season.name.title()} Ratings:"],
            table[
                thead[tr[th["Player"], th["Rating"]]],
                tbody[(tr[td[r.player.name], td[str(r.elo)]] for r in ratings_players)],
            ],
        ]
    ]
    return content
