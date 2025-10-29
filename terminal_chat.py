import requests

BASE_URL = "http://127.0.0.1:8000/chat"
USER_ID = "u123"

print("🤖 STAN Chatbot (type 'exit' to quit)\n")

while True:
    msg = input("You: ")
    if msg.lower() in ["exit", "quit"]:
        print("Bot: Bye! Have a great day 👋")
        break
    r = requests.post(BASE_URL, json={"user_id": USER_ID, "message": msg})
    if r.status_code == 200:
        print("Bot:", r.json().get("bot_reply", ""))
    else:
        print("Bot: (error communicating with server)")
