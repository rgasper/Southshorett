from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Season, Player, Match, Rating
from datetime import datetime, timedelta


class RenderTests(TestCase):
    fixtures = ["demo"]

    @classmethod
    def setUpTestData(cls):
        cls.web_client = Client()
        cls.app_client = Client(headers={"X-Hyperview-Version": "test"})

    def test_index_from_web(self):
        response = self.web_client.get("")
        assert response.status_code == 200, response.status_code
        content = str(response.content, encoding="utf-8")
        assert content.startswith("<!doctype html>"), content[:20]
        assert Season.get_current().name.title() in content
        assert "tbody" in content
        assert (
            response.headers["Content-Type"] == "text/html; charset=utf-8"
        ), response.headers["Content-Type"]

    def test_index_from_app(self):
        response = self.app_client.get("")
        assert response.status_code == 200, response.status_code
        content = str(response.content, encoding="utf-8")
        assert content.startswith(
            '<doc xmlns="https://hyperview.org/hyperview">'
        ), content[:20]
        assert Season.get_current().name.title() in content
        assert (
            response.headers["Content-Type"] == "application/vnd.hyperview+xml"
        ), response.headers["Content-Type"]


class ModelsTests(TestCase):
    def test_Season_get_current(self):
        s1 = Season(
            name="test",
            start=datetime.now() - timedelta(days=1),
            end=datetime.now() + timedelta(days=2),
        )
        s1.save()
        s2 = Season.get_current()
        assert s2 == s1
