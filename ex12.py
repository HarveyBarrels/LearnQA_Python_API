import pytest
import requests

link = "https://playground.learnqa.ru/api/homework_header"
header_keys = ["Date", "Content-Type", "Content-Length", "Connection", "Keep-Alive", "Server", "x-secret-homework-header", "Cache-Control", "Expires"]

class TestSomeHeaders:
    def test_some_headers(self):
        response = requests.get(link)
        my_header = dict(response.headers)
        for key in header_keys:
            assert key in my_header, f"Key '{key}' is not found"


