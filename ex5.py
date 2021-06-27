import json


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj = json.loads(json_text)
key = "message"
if key in obj["messages"][0] or key in obj["messages"][1]:
    print(obj["messages"][1]["message"])
else:
    print(f"{key} is not in json")