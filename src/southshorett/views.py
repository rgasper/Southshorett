from django.http import HttpResponse
from django_hv.http import hv_repond


def index(request):
    response = HttpResponse("Hello, world. You're at the southshorett index.")

    if request.hv:
        return hv_repond(response)
    return response
