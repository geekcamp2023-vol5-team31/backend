import requests
import json

url = "http://127.0.0.1:8000/"
save_data = "myapp/save_data/"
event_list = "myapp/event_list/"

r = requests.get(url)
csrf_token = r.cookies["csrftoken"]

headers = {
    'Authorization': "Bearer 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",
    'X-CSRFToken': csrf_token,
}


json_data = {"name": "Akira", "text": "Hi"}

data = json.dumps(json_data)

response = requests.post(url + save_data, data=data, headers=headers)

print(response)