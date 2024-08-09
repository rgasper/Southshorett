from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("log_a_match", views.log_a_match, name="log_a_match")
]
