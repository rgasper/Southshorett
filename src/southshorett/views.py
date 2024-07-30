from django.http import HttpResponse
from django_hv.http import hv_repond

from htpy import html, body, div
from htpy_hv import hxml, view, text


def index(request):
    message = "Hello, world. You're at the southshorett index."
    if request.hv:
        return hv_repond(
            HttpResponse(
                hxml[view[text[message]]]
            )
        )
    return HttpResponse(html[body[div[message]]])
