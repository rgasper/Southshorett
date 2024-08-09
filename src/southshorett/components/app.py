from django.db.models import QuerySet
from django.urls import reverse
from htpy_hv import hxml, list_
from htpy import Node, body, screen, style, styles, text, item

from southshorett.models import Season, Rating


def base_page(content: Node) -> Node:
    return hxml[screen[content]]


def index(request, current_season: Season, ratings_players: QuerySet[Rating]) -> Node:
    content = (
        styles[style(id="h1", fontSize=48, margin=48)],
        body[
            text(style="h1")[f"Season {current_season.name.title()} Ratings:"],
            list_[
                (
                    item(key=str(r))[text[r.player.name], text[str(r.elo)]]
                    for r in ratings_players
                )
            ],
            text(href=reverse("log_a_match"))["log a match"],
        ],
    )
    return base_page(content)


def log_a_match(request) -> Node:
    return base_page(text("log a match"))
