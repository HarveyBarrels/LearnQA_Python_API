import pytest
import requests

link = "https://playground.learnqa.ru/api/homework_cookie"

class TestSomeCookie:
    def test_some_cookie(self):
        response = requests.get(link)
        my_cookie = dict(response.cookies)
        print(my_cookie)

        assert "HomeWork" in my_cookie, f"Expected cookie 'HomeWork', got:{my_cookie}"
        assert my_cookie["HomeWork"] == "hw_value", f"Expected cookie value is 'hw_value', got: {my_cookie['HomeWork']}"

