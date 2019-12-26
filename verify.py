import requests, json

url = ["http://localhost/auth", "http://localhost/test"]
data = {"user_id": "17fi088", "password": "fuckingpassword"}
data = json.dumps(data)
headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}

authreq = requests.post(url[0], data, headers=headers)
print(authreq.text)
userreq = requests.get(url[1])
print(userreq.text)
