from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Season, Player, Match, Rating
from datetime import datetime, timedelta

def current_season_factory() -> Season:
    return Season(name='test', start=datetime.now()-timedelta(days=1), end=datetime.now()+timedelta(days=2))
    

class RenderTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.web_client = Client()
        cls.app_client = Client(headers={"X-Hyperview-Version": "test"})

        season = current_season_factory()
        season.save()

        user_one = User(username="test_one",password="test_one")
        user_one.save()
        user_two = User(username="test_two",password="test_two")
        user_two.save()

        player_one = Player(name="one", user=user_one)
        player_one.save()
        player_two = Player(name="two", user=user_two)
        player_two.save()

        match = Match(season=season, winner=player_one, loser=player_two, when=datetime.now())
        match.save()

        rating_one = Rating(season=season, player=player_one, elo=1100)
        rating_one.save()
        rating_two = Rating(season=season, player=player_two, elo=900)
        rating_two.save()

    def test_index_from_web(self):
        response = self.web_client.get("")
        assert response.status_code == 200, response.status_code
        assert (
            response.content
            == b"<!doctype html><html><body><div>Hello, world. You&#39;re at the southshorett index.</div></body></html>"  # noqa: E501
        ), response.content
        assert (
            response.headers["Content-Type"] == "text/html; charset=utf-8"
        ), response.headers["Content-Type"]

    def test_index_from_app(self):
        response = self.app_client.get("")
        assert response.status_code == 200, response.status_code
        assert (
            response.content
            == b'<doc xmlns="https://hyperview.org/hyperview"><screen><body><text>Hello, world. You&#39;re at the southshorett index.</text></body></screen></doc>'  # noqa: E501
        ), response.content
        assert (
            response.headers["Content-Type"] == "application/vnd.hyperview+xml"
        ), response.headers["Content-Type"]


class ModelsTests(TestCase):

    def test_Season_get_current(self):
        s1 =current_season_factory()
        s1.save()
        s2 = Season.get_current()
        assert s2 == s1        

