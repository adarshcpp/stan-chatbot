import requests
r = requests.post("http://127.0.0.1:8000/chat",
                  json={"user_id":"u123","message":"I feel very sad today"})
print(r.json())

r = requests.post("http://127.0.0.1:8000/chat",
                  json={"user_id":"u123","message":"I'm so happy right now!"})
print(r.json())
