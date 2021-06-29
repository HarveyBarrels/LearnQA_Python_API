import requests
from json.decoder import JSONDecodeError
import time

my_url = "https://playground.learnqa.ru/ajax/api/longtime_job"
start_job = requests.get(my_url)

try:
    parsed_start_job = start_job.json()
    my_token = parsed_start_job["token"]
    delay = parsed_start_job["seconds"]

    fast_req_response = requests.get(my_url, params={"token": my_token})
    parsed_fast_req_response = fast_req_response.json()
    if parsed_fast_req_response["status"] == "Job is NOT ready":
        print("Fast request status is correct")
    else:
        print("Fast request status is incorrect")

    time.sleep(delay)
    delayed_req_response = requests.get(my_url, params={"token": my_token})
    parsed_delayed_req_response = delayed_req_response.json()
    if "result" in parsed_delayed_req_response and parsed_delayed_req_response["status"] == "Job is ready":
        print("Result is:", parsed_delayed_req_response["result"], "\n", parsed_delayed_req_response["status"])
    else:
        print("Something went wrong")
except JSONDecodeError:
    print("Response is not a JSON")
