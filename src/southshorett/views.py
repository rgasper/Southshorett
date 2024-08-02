from django.http import HttpResponse
from django_hv.http import hv_repond
from htpy import html, body, div, h1, table, tr, td, thead, tbody, th
from htpy_hv import hxml, text, screen

from .models import Player, Season, Rating


def index(request):
    message = "Hello, world. You're at the southshorett index."

    current_season = Season.get_current()
    breakpoint()

    def web(request):
        content = hxml[screen[body[text[message]]]]
        hv_repond(HttpResponse(content))

    def app(request):
        content = html[
            body[
                h1[message],
                table[
                    thead[tr[th["Player"], th["rating"]]],
                    # tbody[
                    #     tr[td[],td[]],
                    # ]
                ],
            ]
        ]
        return HttpResponse(content)

    if request.hv:
        return app(request)
    else:
        return web(request)
