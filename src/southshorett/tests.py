from django.test import TestCase, Client


class IndexTest(TestCase):
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
            == b"<!DOCTYPE hxml><xml><view><text>Hello, world. You&#39;re at the southshorett index.</text></view></xml>"  # noqa: E501
        ), response.content
        assert (
            response.headers["Content-Type"] == "application/vnd.hyperview+xml"
        ), response.headers["Content-Type"]
