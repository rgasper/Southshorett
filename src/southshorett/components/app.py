from django.db.models import QuerySet
from htpy_hv import hxml, list_
from htpy import Node, body, screen, style, styles, text, item

from southshorett.models import Season, Rating


def index(request, current_season: Season, ratings_players: QuerySet[Rating]) -> Node:
    content = hxml[
        screen[
            styles[style(id="h1", fontSize=48, margin=48)],
            body[
                text(style="h1")[f"Season {current_season.name.title()} Ratings:"],
                list_[
                    (
                        item(key=str(r))[text[r.player.name], text[str(r.elo)]]
                        for r in ratings_players
                    )
                ],
            ],
        ]
    ]
    return content
