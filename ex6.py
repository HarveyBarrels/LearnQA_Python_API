import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects = True)
print("Number of redirects is", len(response.history))
print("Final URL is", response.url)
