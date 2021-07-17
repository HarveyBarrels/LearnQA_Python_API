import pytest
import requests

my_url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
user_agent_params = [
        (
            {
                'user_agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                'platform': 'Mobile',
                'browser': 'No',
                'device': 'Android'
            }
        ),
        (
            {
                'user_agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
                'platform': 'Mobile',
                'browser': 'Chrome',
                'device': 'iOS'
            }
        ),

        (
            {
                'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'platform': 'Googlebot',
                'browser': 'Unknown',
                'device': 'Unknown'
            }
        ),
        (
            {
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
                'platform': 'Web',
                'browser': 'Chrome',
                'device': 'No'
            }
        ),
        (
            {
                'user_agent': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'platform': 'Mobile',
                'browser': 'No',
                'device': 'iPhone'
            }
        )
    ]
class TestUserAgent:
    @pytest.mark.parametrize('data', user_agent_params)
    def test_my_user_agent(self, data):
        my_user_agent = data['user_agent']
        expected_platform = data['platform']
        expected_browser = data['browser']
        expected_device = data['device']

        response = requests.get(my_url, headers = {"User-Agent": my_user_agent})
        my_answer = response.json()
        # print(my_answer)
        actual_platform = my_answer["platform"]
        actual_browser = my_answer["browser"]
        actual_device = my_answer["device"]

        assert actual_platform == expected_platform, f"Platform is invalid, expected {expected_platform}, got: {actual_platform}"
        assert actual_browser == expected_browser, f"Browser is invalid, expected {expected_browser}, got: {actual_browser}"
        assert actual_device == expected_device, f"Device is invalid, expected {expected_device}, got: {actual_device}"
