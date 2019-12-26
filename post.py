import requests, json
headers = {'Content-Type': 'application/json'}
data = {"user_id": "17fi088", "password": "fuckingpassword"}
data = json.dumps(data)
print("Sending: " + data)
r = requests.post("http://localhost/auth", data=data, headers=headers)
print(r.text, r.status_code)
