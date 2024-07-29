from django.test import TestCase, Client


class IndexTest(TestCase):

    def setUp(self):
        self.web_client = Client()
        self.app_client = Client(headers={"X-Hyperview-Version":"test"})

    def test_index_from_web(self):
        response = self.web_client.get("")
        assert response.status_code == 200
        assert response.content == b"Hello, world. You're at the southshorett index."
        assert response.headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_index_from_app(self):
        response = self.app_client.get("")
        assert response.status_code == 200
        assert response.content == b"Hello, world. You're at the southshorett index."
        assert response.headers["Content-Type"] == "application/vnd.hyperview+xml"
