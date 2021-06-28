import requests

my_url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response = requests.get(my_url)
print("Request with no params:", response.text)

response = requests.head(my_url, params={"method": "HEAD"})
print("Request with method HEAD:", response.text)

response = requests.get(my_url, params={"method": "GET"})
print("Request with method = GET:", response.text)

methods = ["GET", "POST", "PUT", "DELETE"]
for my_method in methods:
    response = requests.get(my_url, params={"method": my_method})
    print(f"GET Request with 'method' = '{my_method}'", response.text)

    response = requests.post(my_url, data={"method": my_method})
    print(f"POST Request with 'method' = '{my_method}'", response.text)

    response = requests.put(my_url, data={"method": my_method})
    print(f"PUT Request with 'method' = '{my_method}'", response.text)

    response = requests.delete(my_url, data={"method": my_method})
    print(f"DELETE Request with 'method' = '{my_method}'", response.text)
