import requests
import json

url = "http://127.0.0.1:8000/"
save_data = "myapp/save_data/"
event_list = "myapp/event_list/"
csrf_token = "myapp/csrf_token"

session = requests.Session()
session.get(url + csrf_token)
csrftoken = session.cookies["csrftoken"]

headers = {
    'Authorization': "Bearer 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",
    'X-CSRFToken': csrftoken,
    'Content-Type': 'application/json'
}


json_data = {"name": "Akira", "text": "Hi"}

data = json.dumps(json_data)

response = session.post(url + save_data, json=data, headers=headers)

print(response)