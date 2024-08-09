from django.db.models import QuerySet
from django.urls import reverse
from htpy import html, body, h1, table, tr, td, thead, tbody, th, Node, a, hr

from southshorett.models import Season, Rating


def base_page(content: Node) -> Node:
    return html[body[content]]


def index(request, current_season: Season, ratings_players: QuerySet[Rating]) -> Node:
    content = (
        h1[f"Season {current_season.name.title()} Ratings:"],
        table[
            thead[tr[th["Player"], th["Rating"]]],
            tbody[(tr[td[r.player.name], td[str(r.elo)]] for r in ratings_players)],
        ],
        hr(),
        a(href=reverse("log_a_match"))["Log a Match"],
    )
    return base_page(content)


def log_a_match(request) -> Node:
    return base_page("log a match")
