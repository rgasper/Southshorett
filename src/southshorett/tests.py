from django.test import TestCase, Client
from .models import Season
from datetime import datetime, timedelta


class IndexTests(TestCase):
    def setUp(self):
        self.web_client = Client()
        self.app_client = Client(headers={"X-Hyperview-Version": "test"})

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
        s1 = Season(name='test', start=datetime.now()-timedelta(days=1), end=datetime.now()+timedelta(days=2))
        s1.save()
        s2 = Season.get_current()
        assert s2 == s1        

